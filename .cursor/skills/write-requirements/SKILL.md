---
name: write-requirements
description: >-
  Author normative requirements under docs/requirements/ with stable IDs,
  MUST/SHOULD language, ownership, and acceptance anchors. Use when capturing
  durable product or integration constraints, requirement maps, or when the
  user mentions requirements docs.
---

# Write requirements

Requirements are **normative**, not chat notes or inspiration digests.

## File habits

- One theme per file under `docs/requirements/` (`host-integration.md`, `validation-and-ci.md`).
- Stable IDs (`HOST-01`, `VAL-02`) so maps and tests can cite them.
- Prefer **MUST** / **SHOULD** / **MUST NOT** over vague wishes.
- Separate **inspiration** (non-normative) from **requirements** (normative).

## Suggested sections

1. **Motivation** — why this constraint exists  
2. **Ownership** — who owns what (table)  
3. **Requirements** — ID’d MUST/SHOULD items  
4. **Acceptance anchors** — observable checks  
5. **Out of scope** — explicit non-goals  

## Map pattern (multi-source synthesis)

When folding inspiration or multi-system asks:

| ID | Theme | Owners | Phase |
|----|-------|--------|-------|
| … | … | modules / teams | … |

Link acceptance anchors back to IDs. Update the map when owners move.

## Skills sync (required)

After adding or changing requirements, follow
`.cursor/rules/requirements-skills-sync.mdc`:

```text
Requirements → skills:
- [ ] 1. Name the agent workflow the requirement implies
- [ ] 2. Create or update `.cursor/skills/<name>/SKILL.md` (triggers + checklist)
- [ ] 3. Cite requirement IDs from the skill; link the skill from the requirements doc
- [ ] 4. Update AGENTS.md if a skill was added/renamed
- [ ] 5. Drop or rewrite skills for retired requirements
```

## Do not

- Put secrets or live credentials in requirements.
- Treat legacy code as authority when it conflicts with written requirements — note the conflict and resolve deliberately.
- Duplicate long requirements into `README.md` or `AGENTS.md` — link instead.
- Ship a new MUST/SHOULD that agents must uphold without a matching skill update.
