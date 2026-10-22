"""Smithy MechaHarness host Config — local inference + durable generator.

Only this module (and thin CLI / MCP entrypoints) should import pyiv /
mechaharness DI surfaces for production wiring. Domain types stay
injector-agnostic when practical.
"""

from __future__ import annotations

import os
from dataclasses import dataclass
from pathlib import Path

from mechaharness.config import Settings
from mechaharness.core.access import GraphEscalate, GraphExecute
from mechaharness.di import SettingsConfig, apply_backend_defaults, get_injector
from mechaharness.durable_graph_generator import (
    DurableGraphGenerator,
    FileGeneratorRunStore,
    GeneratorRunStore,
)
from mechaharness.graph_templates.catalog import default_graph_template_classes
from mechaharness.graph_templates.guided_coding import GuidedCodingTemplate
from mechaharness.harness.base import AbstractHarness
from mechaharness.harness.pass_through import PassThroughHarness
from pyiv import Stage
from pyiv.files import Filesystem, RealFilesystem
from pyiv.injector import Injector

from smithy.paths import default_generator_store, default_workspace, repo_root
from smithy.recipes import SMITHY_GRAPH_TEMPLATES


@dataclass(frozen=True)
class RepoRoot:
    """Injectable repository root path."""

    path: Path


@dataclass(frozen=True)
class WorkspaceRoot:
    """Injectable workspace root (tools / relative paths)."""

    path: Path


def _settings_for_smithy() -> Settings:
    """Load Settings from process env (MCP ``env`` primary) + optional cwd ``.env``."""
    raw = Settings()
    if raw.base_url and not os.environ.get("MECHA_INFERENCE_BACKEND"):
        if raw.inference_backend in {"openai"}:
            raw = raw.model_copy(update={"inference_backend": "openai_local"})
    return apply_backend_defaults(raw)


class SmithyConfig(SettingsConfig):
    """Host Config for the Blender foundry.

    Prefer ``openai_local`` via MCP / env. Registers default MechaHarness
    recipes plus Smithy foundry recipes. Drive long runs through
    :class:`~mechaharness.durable_graph_generator.DurableGraphGenerator`
    (CLI or ``smithy-generator`` MCP).
    """

    def __init__(
        self,
        settings: Settings | None = None,
        *,
        workspace: Path | str | None = None,
        generator_store: Path | str | None = None,
        filesystem: Filesystem | None = None,
    ) -> None:
        self._workspace = Path(workspace) if workspace else _env_workspace()
        self._generator_store = (
            Path(generator_store) if generator_store else _env_generator_store()
        )
        self._filesystem_override = filesystem
        resolved = settings if settings is not None else _settings_for_smithy()
        if not os.environ.get("MECHA_HARNESS_FAMILY"):
            # Foundry recipes start PassThrough-friendly; tool_loop when coding.
            resolved = resolved.model_copy(
                update={"harness_family": resolved.harness_family or "pass_through"}
            )
        super().__init__(settings=resolved)

    def get_filesystem(self) -> type[Filesystem] | Filesystem:
        if self._filesystem_override is not None:
            return self._filesystem_override
        return RealFilesystem

    def get_grants(self) -> list[object]:
        return [GraphExecute, GraphEscalate]

    def get_harness_class(self) -> type[AbstractHarness]:
        try:
            return super().get_harness_class()
        except KeyError:
            return PassThroughHarness

    def graph_template_classes(self) -> dict[str, type]:
        classes = dict(default_graph_template_classes())
        classes[GuidedCodingTemplate.name] = GuidedCodingTemplate
        classes.update(SMITHY_GRAPH_TEMPLATES)
        return classes

    def get_generator_run_store(self) -> GeneratorRunStore:
        path = self._generator_store
        path.parent.mkdir(parents=True, exist_ok=True)
        return FileGeneratorRunStore(path)

    def configure(self) -> None:
        super().configure()
        self.register_instance(RepoRoot, RepoRoot(repo_root()))
        self.register_instance(WorkspaceRoot, WorkspaceRoot(self._workspace))


def _env_workspace() -> Path:
    raw = os.environ.get("MECHA_WORKSPACE")
    return Path(raw) if raw else default_workspace()


def _env_generator_store() -> Path:
    raw = os.environ.get("MECHA_GENERATOR_STORE")
    return Path(raw) if raw else default_generator_store()


def build_injector(
    config: SmithyConfig | None = None,
    *,
    stage: Stage = Stage.DEVELOPMENT,
) -> Injector:
    """Build a pyiv injector from :class:`SmithyConfig`."""
    return get_injector(config or SmithyConfig(), stage=stage)


def build_generator(config: SmithyConfig | None = None) -> DurableGraphGenerator:
    """Inject a :class:`DurableGraphGenerator` for CLI / MCP."""
    return build_injector(config).inject(DurableGraphGenerator)


__all__ = [
    "RepoRoot",
    "SmithyConfig",
    "WorkspaceRoot",
    "build_generator",
    "build_injector",
]
