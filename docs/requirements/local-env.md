# Local environment layout

## Motivation

Credentials and machine-local state scatter easily. A single `.env/` root keeps
git and Docker images clean.

## Requirements

### ENV-01: Secrets root

All credentials, authorizations, identifiers, and other non-shareable materials
MUST live under `.env/` (see `.cursor/rules/env-secrets.mdc`).

### ENV-02: Optional local data

When a project needs durable local data (SQLite, caches, media), it SHOULD use
`.env/data/` (or another path under `.env/`) and bind-mount that path into
containers rather than writing into the tracked tree.

### ENV-03: Tracked examples

Committed templates (e.g. `config.example.json`, `.env.example`) MUST use
placeholders only and MUST NOT include live secrets.

### ENV-04: Docker

Dockerfiles MUST NOT `COPY` or `ADD` `.env/`. Runtime injection or mounts only.

## Acceptance anchors

1. `.gitignore` / `.dockerignore` exclude `.env/` contents except the tracked README.
2. Fresh clones run without a developer’s private `.env/` (tests use memory/temp fixtures).
