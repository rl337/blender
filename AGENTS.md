# Agent guide

This repository is the **Smithy Blender foundry**: typed Blender asset/scene work
orchestrated by MechaHarness, entered via the **`smithy` pyiv CLI**, with frontier
guidance through the **generator MCP** and local ``openai_local`` inference.

Inspiration catalog (living): `inspiration/`. Architecture sketch:
`inspiration/agentic-blender-execution-architecture.md`.

## Before you change anything

1. Read this file and `.cursor/rules/` (always-apply rules first; DI-first is on).
2. Check `docs/requirements/` for constraints.
3. Prefer `smithy` CLI / generator MCP for orchestration; Blender MCP for live scene I/O.

## Entry points

| Surface | How |
|---------|-----|
| CLI | `smithy` → `smithy.cli:cli` (pyiv `CommandRunner` + `SmithyConfig`) |
| Generator MCP | `smithy-generator` / `python -m smithy.mcp_server` (stdio) |
| Live Blender | `.cursor/mcp.json` → `mcp-for-blender` |
| Package | `src/smithy/` |

## Where things live

| Kind | Location |
|------|----------|
| Always-on guidance | `.cursor/rules/*.mdc` |
| Repeatable workflows | `.cursor/skills/<name>/SKILL.md` |
| Requirements | `docs/requirements/` |
| Architecture notes | `docs/architecture/` |
| Inspiration (non-binding) | `inspiration/` |
| Foundry package | `src/smithy/` |
| Agentic recipes | `src/smithy/recipes/` |
| Legacy trees (reference) | `automata/`, `main/`, `Untitled/` (N14E — process only; not first builds) |
| Secrets / local env | `.env/` only |

## Skills

| Skill | Use when |
|-------|----------|
| `project-docs` | Writing or syncing `docs/` + README |
| `write-requirements` | Normative MUST/SHOULD under `docs/requirements/` |
| `docker-dev-workflow` | Reproducible CLI/tests via Docker |
| `data-driven-tests` | Fixture matrices instead of clone tests |
| `user-stories` | Acceptance stories tied to validation |
| `di-config-ownership` | Settings/provider knobs (pyiv DI) |

## Orchestration model

- **MechaHarness** owns graphs, soft points, checkpoints, repair, and local inference.
- **Cursor** guides via generator MCP (`generator_start` / `generator_resume`) when a recipe yields `advice_requested`.
- **Local openai_local** does token-heavy work (configure `MECHA_*` in MCP `env`).
- First recipe: `smithy.prop_scaffold` — greenfield prop brief; **no Untitled/N14E assets**.

## Do not

- Commit `.env/` secrets (except tracked `.env/README.md`).
- Import `Untitled/` newsroom assets into first curated builds.
- Bypass `SmithyConfig` with ad-hoc global registries (see `di-first`).
- Treat inspiration docs as implementation commitments without requirements updates.
