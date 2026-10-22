# Smithy foundry (initial)

Normative constraints for the Blender asset foundry under `src/smithy/`.

## MUST

- Expose all operator entry points through the **`smithy` pyiv CLI** (`SmithyConfig` + `CommandRunner`).
- Orchestrate long-running / judgment-bearing work with **MechaHarness** `DurableGraphGenerator` (not ad-hoc bpy scripts as the default API).
- Drive frontier guidance through the **generator MCP** (`smithy-generator` / `smithy mcp-serve`) using `generator_start` / `generator_resume`.
- Prefer **local `openai_local`** inference (via `MECHA_*` env) for token-heavy work; Codex/frontier only for guidance soft points unless escalated.
- Keep **candidates** distinct from **curated** publish; never auto-publish on model confidence alone.
- First builds **MUST NOT** import or republish `Untitled/` N14E newsroom assets.

## SHOULD

- Register new Agentic Recipes under `src/smithy/recipes/` and expose them via `SmithyConfig.graph_template_classes`.
- Freeze acceptance criteria (soft point / checklist) before construct; re-run the same gate after repair.
- Inventory legacy trees (`automata/`, `main/`, `Untitled/`) with `smithy legacy` before relocating code.
- Keep Git for recipes/manifests/source; use LFS/object storage when binary size warrants.

## First recipe acceptance (`smithy.prop_scaffold`)

- Recipe id `smithy.prop_scaffold` is listed by `smithy recipes` / `generator_list_recipes`.
- A scripted offline run can complete `advice_requested` → `completed` with choice `primitive_blockout` or `parametric_detail`.
- Inputs accept at least `prop_kind` and `prop_brief`; acceptance forbids N14E asset reuse.
