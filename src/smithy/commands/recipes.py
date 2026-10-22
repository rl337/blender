"""``smithy recipes`` — list DurableGraphGenerator catalog ids."""

from __future__ import annotations

from pyiv.command import CLICommand

from mechaharness.durable_graph_generator import DurableGraphGenerator


class RecipesCommand(CLICommand):
    @classmethod
    def get_name(cls) -> str:
        return "recipes"

    @classmethod
    def get_description(cls) -> str:
        return "List MechaHarness / Smithy Agentic Recipes available to generator"

    def run(self) -> None:
        if self.injector is None:
            raise RuntimeError("RecipesCommand requires an injector")
        gen = self.injector.inject(DurableGraphGenerator)
        recipes = gen.list_recipes()
        for recipe in recipes:
            soft = ",".join(recipe.soft_points) if recipe.soft_points else "-"
            ver = recipe.version or "-"
            print(f"{recipe.recipe_id}\tv{ver}\tsoft=[{soft}]")
        print(f"# {len(recipes)} recipes")
        self._exit_code = 0
