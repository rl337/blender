---
name: user-stories
description: >-
  Write acceptance-oriented user stories that tie behavior to personas,
  implementation touchpoints, and validation. Use when adding user-facing
  behavior, acceptance criteria, or when the user mentions user stories or
  persona narratives.
---

# User stories

User stories are **documentation and acceptance**. Prefer tracing library or
product behavior to a story — unit tests alone are not enough for user-facing
paths.

## Shape

Each story should capture:

| Field | Purpose |
|-------|---------|
| `id` | Stable slug (`fangore_compound_grants`) |
| `persona` | Who cares (operator, app developer, end user, …) |
| `title` | Short outcome |
| `narrative` | PM-facing prose — features, not module paths |
| `implementation` | Modules/surfaces that fulfill it |
| `validation` | How it is proven (tests, fixtures, manual) |

Store structured stories under something like `tests/fixtures/.../stories/` or
`docs/requirements/stories/` and generate a human guide if the project grows
enough copies that hand-editing diverges.

## Narrative rules

- Literal English for a non-technical reader.
- No CamelCase APIs, file paths, or CLI flags as the primary explanation.
- Cross-link other story ids; put URLs in footnotes, not the narrative body.

## Workflow

```text
Story task:
- [ ] 1. Name persona + story id
- [ ] 2. Write narrative (outcome + constraints)
- [ ] 3. Point implementation at real modules
- [ ] 4. Point validation at real tests/fixtures
- [ ] 5. Keep twin docs/fixtures in sync if the project generates a guide
```

Derived projects may add named personas and a generator (see MechaHarness) once
the suite needs it — do not invent personas until there is more than one story.
