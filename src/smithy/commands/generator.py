"""``smithy generator`` — CLI mirror of generator MCP ops."""

from __future__ import annotations

import argparse
import json
from typing import Any, Dict, List, Type

from mechaharness.durable_graph_generator import (
    DurableGraphGenerator,
    GuidanceResponse,
)
from pyiv.command import CLICommand, Command


def _print_yield(payload: Any) -> None:
    if hasattr(payload, "model_dump"):
        print(json.dumps(payload.model_dump(mode="json"), indent=2, sort_keys=True))
    else:
        print(json.dumps(payload, indent=2, sort_keys=True, default=str))


class GeneratorListCommand(CLICommand):
    @classmethod
    def get_name(cls) -> str:
        return "list"

    @classmethod
    def get_description(cls) -> str:
        return "List recipes (same as smithy recipes)"

    def run(self) -> None:
        assert self.injector is not None
        gen = self.injector.inject(DurableGraphGenerator)
        _print_yield({"recipes": [r.model_dump(mode="json") for r in gen.list_recipes()]})
        self._exit_code = 0


class GeneratorStartCommand(CLICommand):
    @classmethod
    def get_name(cls) -> str:
        return "start"

    @classmethod
    def get_description(cls) -> str:
        return "Start a durable generator run (may yield advice_requested)"

    @classmethod
    def add_args(cls, parser: argparse.ArgumentParser) -> None:
        parser.add_argument("--recipe-id", required=True)
        parser.add_argument("--run-id", default=None)
        parser.add_argument("--controller-id", default="smithy-cli")
        parser.add_argument(
            "--input",
            action="append",
            default=[],
            metavar="KEY=VALUE",
            help="Recipe input (repeatable). Values are strings.",
        )
        parser.add_argument(
            "--inputs-json",
            default=None,
            help="JSON object merged into inputs (overrides --input keys)",
        )

    def run(self) -> None:
        assert self.injector is not None
        inputs: Dict[str, Any] = {}
        for item in self.args.input:
            if "=" not in item:
                raise SystemExit(f"invalid --input {item!r}; expected KEY=VALUE")
            key, value = item.split("=", 1)
            inputs[key] = value
        if self.args.inputs_json:
            parsed = json.loads(self.args.inputs_json)
            if not isinstance(parsed, dict):
                raise SystemExit("--inputs-json must be an object")
            inputs.update(parsed)
        gen = self.injector.inject(DurableGraphGenerator)
        y = gen.start(
            self.args.recipe_id,
            inputs,
            run_id=self.args.run_id,
            controller_id=self.args.controller_id,
        )
        _print_yield(y)
        self._exit_code = 0


class GeneratorResumeCommand(CLICommand):
    @classmethod
    def get_name(cls) -> str:
        return "resume"

    @classmethod
    def get_description(cls) -> str:
        return "Resume a run (supply guidance when advice_requested)"

    @classmethod
    def add_args(cls, parser: argparse.ArgumentParser) -> None:
        parser.add_argument("--run-id", required=True)
        parser.add_argument("--expected-sequence", type=int, required=True)
        parser.add_argument("--request-id", default="")
        parser.add_argument("--choice-id", default=None)
        parser.add_argument("--text", default=None)
        parser.add_argument("--controller-id", default="smithy-cli")
        parser.add_argument("--idempotency-key", default=None)

    def run(self) -> None:
        assert self.injector is not None
        response = None
        if self.args.choice_id or self.args.text or self.args.request_id:
            response = GuidanceResponse(
                request_id=str(self.args.request_id or ""),
                choice_id=self.args.choice_id,
                text=self.args.text,
            )
        gen = self.injector.inject(DurableGraphGenerator)
        y = gen.resume(
            self.args.run_id,
            response,
            expected_sequence=self.args.expected_sequence,
            request_id=self.args.request_id or None,
            idempotency_key=self.args.idempotency_key,
            controller_id=self.args.controller_id,
        )
        _print_yield(y)
        self._exit_code = 0


class GeneratorInspectCommand(CLICommand):
    @classmethod
    def get_name(cls) -> str:
        return "inspect"

    @classmethod
    def get_description(cls) -> str:
        return "Inspect a durable generator run without advancing"

    @classmethod
    def add_args(cls, parser: argparse.ArgumentParser) -> None:
        parser.add_argument("--run-id", required=True)

    def run(self) -> None:
        assert self.injector is not None
        gen = self.injector.inject(DurableGraphGenerator)
        _print_yield(gen.inspect(self.args.run_id))
        self._exit_code = 0


class GeneratorCancelCommand(CLICommand):
    @classmethod
    def get_name(cls) -> str:
        return "cancel"

    @classmethod
    def get_description(cls) -> str:
        return "Cancel a durable generator run"

    @classmethod
    def add_args(cls, parser: argparse.ArgumentParser) -> None:
        parser.add_argument("--run-id", required=True)
        parser.add_argument("--controller-id", default="smithy-cli")
        parser.add_argument("--expected-sequence", type=int, default=None)

    def run(self) -> None:
        assert self.injector is not None
        gen = self.injector.inject(DurableGraphGenerator)
        y = gen.cancel(
            self.args.run_id,
            controller_id=self.args.controller_id,
            expected_sequence=self.args.expected_sequence,
        )
        _print_yield(y)
        self._exit_code = 0


class GeneratorCommand(Command):
    """Parent: ``smithy generator <list|start|resume|inspect|cancel>``."""

    @classmethod
    def get_name(cls) -> str:
        return "generator"

    @classmethod
    def get_description(cls) -> str:
        return "Drive DurableGraphGenerator (CLI mirror of generator MCP)"

    @classmethod
    def get_subcommands(cls) -> List[Type[Command]]:
        return [
            GeneratorListCommand,
            GeneratorStartCommand,
            GeneratorResumeCommand,
            GeneratorInspectCommand,
            GeneratorCancelCommand,
        ]

    def execute(self) -> int:
        name = getattr(self.args, "subcommand", None)
        for command_cls in type(self).get_subcommands():
            if command_cls.get_name() == name or name in command_cls.get_aliases():
                return command_cls(self.args, injector=self.injector).execute()
        return 2
