"""pyiv CLICommand tree for smithy.

Root commands are registered explicitly (no package auto-discovery).
"""

from __future__ import annotations

from typing import Dict, Type

from pyiv.command import Command

from smithy.commands.generator import GeneratorCommand
from smithy.commands.info import InfoCommand
from smithy.commands.legacy import LegacyCommand
from smithy.commands.mcp import McpServeCommand
from smithy.commands.recipes import RecipesCommand

ROOT_COMMANDS: Dict[str, Type[Command]] = {
    "info": InfoCommand,
    "recipes": RecipesCommand,
    "generator": GeneratorCommand,
    "mcp-serve": McpServeCommand,
    "legacy": LegacyCommand,
}

__all__ = [
    "ROOT_COMMANDS",
    "InfoCommand",
    "RecipesCommand",
    "GeneratorCommand",
    "McpServeCommand",
    "LegacyCommand",
]
