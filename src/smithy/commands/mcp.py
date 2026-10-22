"""``smithy mcp-serve`` — run generator MCP on SmithyConfig."""

from __future__ import annotations

from pyiv.command import CLICommand

from mechaharness.mcp_graph_driver import GeneratorMcpServer

from smithy.di import SmithyConfig, build_generator


class McpServeCommand(CLICommand):
    @classmethod
    def get_name(cls) -> str:
        return "mcp-serve"

    @classmethod
    def get_description(cls) -> str:
        return "Run MechaHarness generator MCP (stdio) with SmithyConfig"

    def run(self) -> None:
        # Long-running: GeneratorMcpServer blocks until stdin closes.
        generator = build_generator(SmithyConfig())
        GeneratorMcpServer(generator).serve_forever()
        self._exit_code = 0
