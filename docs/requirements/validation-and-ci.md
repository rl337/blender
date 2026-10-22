# Validation and CI

## Motivation

Agents and humans need one obvious way to prove a change is safe before push/merge.

## Requirements

### VAL-01: Local entrypoint

Projects MUST provide a documented root command (prefer `./run_checks.sh`) that
runs automated tests and static checks intended for CI parity.

### VAL-02: PR validation

Projects MUST have at least one CI workflow on pull requests that runs a
relevant subset of that entrypoint (SHOULD run the full set when feasible).

### VAL-03: Artifacts location

Generated reports and coverage output MUST land under `build/` (or another
single gitignored artifact root documented in `AGENTS.md`).

### VAL-04: No committed secrets for checks

Test and CI configuration MUST NOT require secrets committed to the repo.
Local secrets live under `.env/`; CI uses the host’s secret store.

## Acceptance anchors

1. A new contributor can find and run the local entrypoint from `README.md` or `AGENTS.md`.
2. Opening a PR without green checks is treated as incomplete work.
3. `build/` is gitignored and not relied upon as source.
