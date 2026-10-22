"""Greenfield procedural prop scaffold — first foundry recipe.

Catalog id: ``smithy.prop_scaffold``. Frontier driver (Cursor via generator MCP)
answers ``external_guidance``; local MechaHarness / openai_local owns the
token-heavy work in later tiles. This first version only establishes the
guidance → plan → construct stub loop — no N14E assets.
"""

from __future__ import annotations

from mechaharness.graph import ExecutionGraph, GraphNode
from mechaharness.graph_templates.base import (
    GraphTemplate,
    GraphTemplateParams,
    SoftPoint,
)
from mechaharness.isolation.isolation_contract import TemplateIOContract


class PropScaffoldTemplate(GraphTemplate):
    """Specify a boring measurable prop, then yield for construction guidance.

    Example::

        >>> from mechaharness.graph_templates import GraphTemplateParams
        >>> from smithy.recipes.prop_scaffold import PropScaffoldTemplate
        >>> graph = PropScaffoldTemplate().instantiate(
        ...     GraphTemplateParams(goal="scaffold prop", inputs={"prop_kind": "lamp"})
        ... )
        >>> graph.template_name
        'smithy.prop_scaffold'
    """

    name = "smithy.prop_scaffold"
    version = "1"
    category = "agentic_recipe"
    summary = (
        "Greenfield procedural prop: freeze a typed brief, ask frontier for "
        "construction direction, then stub construct/validate nodes."
    )
    description = (
        "First Smithy foundry recipe. Soft point external_guidance lets the "
        "generator MCP client (Cursor) steer silhouette/scale/material intent "
        "while local inference will later run construct/validate. Does not "
        "touch Untitled/N14E assets."
    )
    soft_points = (
        SoftPoint(
            name="external_guidance",
            kind="guidance",
            description=(
                "How should we construct this greenfield prop "
                "(silhouette, real-world scale, material intent)?"
            ),
            required=True,
            default={
                "choices": [
                    {
                        "id": "primitive_blockout",
                        "label": "Primitive blockout — measurable bounds first",
                    },
                    {
                        "id": "parametric_detail",
                        "label": "Parametric detail — named parts + simple materials",
                    },
                ],
                "recommendation": "primitive_blockout",
                "requested_authority": "foundry_direction",
            },
        ),
        SoftPoint(
            name="acceptance",
            kind="policy",
            description="Acceptance criteria frozen before construct (scale, naming)",
            required=False,
            default={
                "must_have_bounds_m": True,
                "must_export_glb": False,
                "forbid_n14e_assets": True,
            },
        ),
    )
    io_contract = TemplateIOContract(
        inputs={
            "prop_kind": "string",
            "prop_brief": "string",
            "target_height_m": "number",
        },
        outputs={"candidate_ref": "string", "direction": "string"},
    )

    def build(self, params: GraphTemplateParams) -> ExecutionGraph:
        inputs = dict(params.inputs or {})
        prop_kind = str(inputs.get("prop_kind") or "prop")
        graph = ExecutionGraph(
            goal=params.goal or f"scaffold {prop_kind}",
            template_name=self.name,
            template_version=self.version,
        )
        graph.add_node(
            GraphNode(
                id="specify",
                kind="specify_prop",
                goal="Freeze typed prop brief and acceptance",
                payload={
                    "prop_kind": prop_kind,
                    "prop_brief": inputs.get("prop_brief", ""),
                    "target_height_m": inputs.get("target_height_m"),
                    "soft_points": ["acceptance", "external_guidance"],
                },
            )
        )
        graph.add_node(
            GraphNode(
                id="plan_construct",
                kind="plan_construct",
                goal="Apply frontier construction guidance",
                depends_on=["specify"],
                payload={"soft_points": ["external_guidance"]},
            )
        )
        graph.add_node(
            GraphNode(
                id="construct_stub",
                kind="construct_prop_stub",
                goal="Record construct plan (geometry work lands in a later recipe version)",
                depends_on=["plan_construct"],
                payload={"soft_points": ["acceptance"]},
            )
        )
        return graph
