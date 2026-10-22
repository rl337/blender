---
name: data-driven-tests
description: >-
  Prefer declarative fixture matrices over near-duplicate test functions. Use
  when adding tests, expanding coverage, parametrizing cases, converting tests
  to data-driven form, or when the user mentions fixtures, case matrices, or
  test proliferation.
---

# Data-driven tests

Prefer **one interpreter + many fixtures** over N test functions that rebuild
the same arrange/act/assert with slight input tweaks.

## When to apply

**Do** when several tests share setup and differ mainly by inputs/expects; when
covering a decision matrix; when new coverage would be another near-clone.

**Skip** when the check is a unique structural/DI/import smoke test, or when a
fixture DSL would be longer than one focused unit test.

## Layout

```text
tests/
  fixtures/<domain>/           # one case file per scenario; id == stem preferred
  support/<domain>_cases.py    # load, build doubles, assert_expect (or equiv.)
  test_<domain>.py             # parametrize over iter_cases(); tiny structural tests aside
```

Name the **domain** at the leaf (see `unambiguous-names` rule) — not `cases` / `matrix`.

## Case shape (minimum)

| Field | Role |
|-------|------|
| `id` | Stable case id (default: filename stem) |
| `description` | Why this case exists |
| inputs… | Domain arrange data |
| `expect` | Outcomes the interpreter understands |

Prefer scripted modes (`succeed`, `fail_n_then_succeed`, `raise`) over embedding
code in fixtures. Put branching in the interpreter once.

## Interpreter rules

1. Call the **public** API; assert on results/events/payloads.
2. One `assert_expect(...)` with clear `case {id}: …` messages.
3. No `if case.id == …` forks in the test module — extend the schema instead.
4. Assert matrix size / unique ids so empty dirs fail loudly.

## Coverage bar (default)

For each functional change: cover success paths touched by the change; cover
identified edge cases aggressively; leave the suite green via project
`run_checks` / CI (see `validation-gates` rule).
