---
name: project-docs
description: >-
  Create and maintain project documentation under docs/ and keep README short.
  Use when writing, updating, restructuring, or reviewing docs; syncing README;
  architecture notes; guides; reference pages; or docs/requirements/.
---

# Project docs

`docs/` is the source of truth. `README.md` stays a short entry surface.

## Layout (adapt names to the stack)

```text
docs/
  index.md           # TOC / home (optional but preferred)
  architecture/      # or architecture.md — design and boundaries
  guides/            # task-oriented how-tos
  reference/         # stable contracts (CLI, API, types)
  requirements/      # normative MUST/SHOULD
  adr/               # decision records (optional)

README.md            # pitch, install/quick start, links into docs/
AGENTS.md            # agent entry — link skills/rules, do not duplicate long guides
```

| Audience | Location |
|----------|----------|
| Maintainer agents | `.cursor/skills/`, `.cursor/rules/` |
| Humans + agents (product truth) | `docs/` |
| Downstream consumers (libraries) | optional `agent-skills/` kept in sync with public APIs |

## Workflow

```text
Docs task:
- [ ] 1. Audience + type (guide / reference / architecture / requirement / ADR)
- [ ] 2. Read current code + existing docs
- [ ] 3. Create or update the page (kebab-case filenames)
- [ ] 4. Update docs/index.md TOC if needed
- [ ] 5. Touch README only if the entry surface changed
- [ ] 6. Verify commands, paths, and env names against the repo
```

After public behavior changes: update `docs/reference/` (or requirements) first, then guides, then architecture if the design shifted. Do not invent APIs — read the code.

## Writing rules

- Lead with what the reader can do, then how.
- Use real module/CLI paths.
- No secrets in examples; point at `.env/` + tracked examples instead.
- Prefer relative links inside `docs/`.
