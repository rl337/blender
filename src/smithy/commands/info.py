"""``smithy info`` — workspace / host summary."""

from __future__ import annotations

from pyiv.command import CLICommand

from smithy import __version__
from smithy.di import RepoRoot, WorkspaceRoot
from smithy.paths import default_generator_store


class InfoCommand(CLICommand):
    @classmethod
    def get_name(cls) -> str:
        return "info"

    @classmethod
    def get_description(cls) -> str:
        return "Show smithy version, workspace, and generator store paths"

    def run(self) -> None:
        root = "(unset)"
        workspace = "(unset)"
        if self.injector is not None:
            root = str(self.injector.inject(RepoRoot).path)
            workspace = str(self.injector.inject(WorkspaceRoot).path)
        print(f"smithy {__version__}")
        print(f"repo_root: {root}")
        print(f"workspace: {workspace}")
        print(f"generator_store: {default_generator_store()}")
        print("orchestrator: MechaHarness DurableGraphGenerator")
        print("inference: openai_local via MECHA_* env (MCP preferred)")
        print("entrypoints: smithy (CLI), smithy-generator (MCP stdio)")
        self._exit_code = 0
