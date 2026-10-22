"""CLI entrypoint: pyiv CommandRunner + SmithyConfig injector."""

from __future__ import annotations

import sys
from typing import List, Optional

from pyiv.command import CommandRunner

from smithy.commands import ROOT_COMMANDS
from smithy.di import SmithyConfig, build_injector


def main(argv: Optional[List[str]] = None) -> int:
    """Dispatch ``smithy <command>`` via pyiv CommandRunner."""
    config = SmithyConfig()
    runner = CommandRunner(config=config)
    parser = runner.create_parser(
        prog="smithy",
        description="Blender asset foundry (MechaHarness + local inference)",
        commands=ROOT_COMMANDS,
    )
    args = parser.parse_args(argv if argv is not None else sys.argv[1:])
    command_class = ROOT_COMMANDS.get(args.command)
    if command_class is None:
        parser.error(f"Unknown command: {args.command}")
        return 2

    injector = build_injector(config)
    command = command_class(args, injector=injector)
    return command.execute()


def cli() -> None:
    """Console-script entry used by ``[project.scripts] smithy``."""
    raise SystemExit(main())


if __name__ == "__main__":
    cli()
