# Requirements style

## Motivation

Durable constraints should be citable and testable, not buried in chat history.

## Requirements

### REQ-01: Location

Normative product and integration constraints MUST live under `docs/requirements/`.

### REQ-02: Language

Requirement bodies SHOULD use RFC-style **MUST** / **SHOULD** / **MUST NOT**.

### REQ-03: Stable IDs

Discrete requirements SHOULD have stable IDs (`VAL-01`, `HOST-02`) for maps,
tests, and cross-links.

### REQ-04: Inspiration is not authority

Non-normative research belongs under `docs/inspiration/` (or similar) and MUST
NOT override `docs/requirements/` without an explicit revision of the
requirements doc.

### REQ-05: Secrets

Requirements docs MUST NOT contain live credentials, tokens, or private
identifiers. Describe shapes and point at `.env/` + examples instead.

### REQ-06: Skills stay current

When a requirement is added, removed, or materially changed, the change MUST
include creating or updating the relevant project skill(s) under
`.cursor/skills/` so agents can execute the constraint. See
`.cursor/rules/requirements-skills-sync.mdc`.

## Acceptance anchors

1. Agents read `docs/requirements/` before inventing product scope.
2. New constraints land as requirement edits (or explicit out-of-scope notes),
   not only as chat agreement.
3. New or changed MUST/SHOULD items that agents must uphold have a matching
   skill create/update in the same change set.
