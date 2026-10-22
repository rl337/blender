"""Offline smoke tests for smithy host + prop scaffold recipe."""

from __future__ import annotations

from pathlib import Path

from mechaharness.durable_graph_generator import ScriptedDriver
from mechaharness.harness.pass_through import PassThroughHarness
from mechaharness.inference.mock import MockInferenceStrategy

from smithy.di import SmithyConfig, build_generator
from smithy.recipes.prop_scaffold import PropScaffoldTemplate


class _TestConfig(SmithyConfig):
    def get_inference_class(self):  # type: ignore[override]
        return MockInferenceStrategy

    def get_harness_class(self):  # type: ignore[override]
        return PassThroughHarness


def test_prop_scaffold_in_catalog(tmp_path: Path) -> None:
    store = tmp_path / "runs.json"
    gen = build_generator(_TestConfig(generator_store=store))
    ids = {r.recipe_id for r in gen.list_recipes()}
    assert PropScaffoldTemplate.name in ids


def test_prop_scaffold_scripted_guidance(tmp_path: Path) -> None:
    store = tmp_path / "runs.json"
    gen = build_generator(_TestConfig(generator_store=store))
    driver = ScriptedDriver(gen)
    yields = driver.run(
        PropScaffoldTemplate.name,
        {
            "prop_kind": "desk_lamp",
            "prop_brief": "simple measurable lamp",
            "target_height_m": 0.45,
        },
        responses=[{"request_id": "", "choice_id": "primitive_blockout"}],
        expected_kinds=["advice_requested", "completed"],
        controller_id="test",
    )
    assert yields[-1].kind == "completed"


def test_cli_info_exits_zero() -> None:
    from smithy.cli import main

    assert main(["info"]) == 0
