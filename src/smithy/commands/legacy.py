"""``smithy legacy`` — inventory pre-smithy trees (automata / main / Untitled)."""

from __future__ import annotations

import argparse
from pathlib import Path

from pyiv.command import CLICommand

from smithy.di import RepoRoot


class LegacyCommand(CLICommand):
    @classmethod
    def get_name(cls) -> str:
        return "legacy"

    @classmethod
    def get_description(cls) -> str:
        return "List legacy trees (automata, main, Untitled) — not used by first recipes"

    @classmethod
    def add_args(cls, parser: argparse.ArgumentParser) -> None:
        parser.add_argument(
            "--path",
            choices=("automata", "main", "Untitled", "all"),
            default="all",
            help="Which legacy tree to summarize",
        )

    def run(self) -> None:
        if self.injector is None:
            raise RuntimeError("LegacyCommand requires an injector")
        root: Path = self.injector.inject(RepoRoot).path
        targets = (
            ["automata", "main", "Untitled"]
            if self.args.path == "all"
            else [self.args.path]
        )
        for name in targets:
            path = root / name
            if not path.exists():
                print(f"{name}: missing")
                continue
            entries = sorted(p.name for p in path.iterdir() if not p.name.startswith("."))
            preview = ", ".join(entries[:12])
            more = "" if len(entries) <= 12 else f" (+{len(entries) - 12} more)"
            print(f"{name}/ ({len(entries)} entries): {preview}{more}")
        print(
            "note: first foundry builds use smithy.prop_scaffold only — "
            "do not import Untitled/N14E assets"
        )
        self._exit_code = 0
