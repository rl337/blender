# blender (Smithy foundry)

Blender models, scenes, and **agentic foundry** tooling for rl337 projects.

**CLI:** `smithy` (pyiv commands)  
**Orchestrator:** MechaHarness `DurableGraphGenerator`  
**Guidance:** generator MCP (`smithy-generator`) + local `openai_local` inference  
**Inspiration:** [`inspiration/`](inspiration/) · [PR #1](https://github.com/rl337/blender/pull/1)

## Quick start

```bash
# From repo root — use an env that already has mechaharness + pyiv (or install editable)
export PYTHONPATH="src:/Users/richard/dev/mechaharness/src:/Users/richard/dev/pyiv"
pip install -e .   # optional once deps resolve

smithy info
smithy recipes
smithy generator start --recipe-id smithy.prop_scaffold \
  --input prop_kind=desk_lamp --input prop_brief='simple measurable lamp'
```

Generator MCP (Cursor): see `.cursor/mcp.json` → `mechaharness-generator` runs
`python -m smithy.mcp_server` with `MECHA_*` local-inference env.

## Layout

| Path | Purpose |
|------|---------|
| `src/smithy/` | Foundry package — Config, recipes, pyiv CLI, MCP entry |
| `inspiration/` | Living tool/architecture catalog (not binding) |
| `docs/requirements/` | Normative constraints |
| `automata/`, `main/` | Legacy procedural experiments (`smithy legacy`) |
| `Untitled/` | N14E newsroom archive — **process inspiration only** for v0 |

## First recipe

`smithy.prop_scaffold` — freeze a greenfield prop brief, yield for frontier
construction guidance, stub construct. No N14E geometry.

## Agent meta

See `AGENTS.md`. Bootstrap defaults from [rl337/project-template](https://github.com/rl337/project-template).
