---
name: docker-dev-workflow
description: >-
  Run project CLI, tests, and tooling inside Docker for reproducible
  environments. Use when adding dependencies, writing run scripts, debugging
  environment drift, or when the user mentions Docker, containers, or host vs
  container execution.
---

# Docker dev workflow

Prefer a **project container** (or Compose service) for CLI tools and test runs
so host language/tool versions do not drift.

## Defaults

1. If no Dockerfile exists and the user wants isolation, add a minimal one and a
   thin wrapper script (`run_checks.sh`, `scripts/docker.sh`, etc.).
2. Mount the project directory into the container; keep durable/local data under
   `.env/` on the host (see `env-secrets` rule) and bind-mount as needed.
3. Add runtime OS packages and language toolchains to the image — not ad-hoc on
   the developer laptop — when those tools are required to build or test.
4. Document the one command humans and agents should run (e.g. `./run_checks.sh`).

## Do not

- Assume host-installed toolchains when the project standardized on Docker.
- Commit image-local state or bind-mounted `.env/` contents.
- `COPY` `.env/` into images (see `.dockerignore`).

## When Docker is optional

Pure library work with a locked local toolchain may skip containers; still keep
`run_checks.sh` as the single entry for CI parity.
