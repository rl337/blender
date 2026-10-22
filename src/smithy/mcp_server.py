"""Stdio generator MCP server hosted on SmithyConfig.

Cursor (or another frontier client) drives durable MechaHarness recipes via
``generator_start`` / ``generator_resume`` while local ``openai_local``
inference does the token-heavy work. This entrypoint injects
:class:`~smithy.di.SmithyConfig` instead of MechaHarness
``project_coding``.
"""

from __future__ import annotations

import sys
from typing import List, Optional

from mechaharness.mcp_graph_driver import GeneratorMcpServer

from smithy.di import SmithyConfig, build_generator


def main(argv: Optional[List[str]] = None) -> int:
    """Run the generator MCP server on stdio (Smithy host)."""
    del argv
    generator = build_generator(SmithyConfig())
    GeneratorMcpServer(generator).serve_forever()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
