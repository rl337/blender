"""Repository path helpers (no DI)."""

from __future__ import annotations

from pathlib import Path


def repo_root() -> Path:
    """Return the blender repository root (parent of ``src/``)."""
    return Path(__file__).resolve().parents[2]


def default_generator_store() -> Path:
    return repo_root() / ".mechaharness" / "generator-runs.json"


def default_workspace() -> Path:
    return repo_root()
