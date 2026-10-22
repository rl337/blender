"""Smithy MechaHarness graph templates (Agentic Recipes)."""

from __future__ import annotations

from smithy.recipes.prop_scaffold import PropScaffoldTemplate

SMITHY_GRAPH_TEMPLATES = {
    PropScaffoldTemplate.name: PropScaffoldTemplate,
}

__all__ = ["PropScaffoldTemplate", "SMITHY_GRAPH_TEMPLATES"]
