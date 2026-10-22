# `.env/` — local secrets and environment (not committed)

Everything in this directory is **gitignored** and **dockerignored**, except this README.

## What belongs here

Put all materials that must never be checked in:

- Credentials and passwords
- Authorization tokens, API keys, OAuth client secrets
- Identifiers that are environment- or account-specific (private keys, device IDs, etc.)
- TLS certs/keys, connection strings, cloud config with secrets
- Any other local environment overlays

Examples (create as needed; none are tracked):

```text
.env/
  local.env           # KEY=value pairs for local runs
  config.json         # runtime config instantiated from a tracked *.example
  credentials.json    # service account or app credentials
  certs/              # private keys and certs
  data/               # durable local data (SQLite, caches) — bind-mount into Docker
```

## What does not belong here

- Public examples and placeholder docs (keep those tracked, outside or as this README)
- Application source code
- Requirements that are safe to share (`docs/requirements/`)

## Docker

Do not `COPY` or `ADD` this directory in a Dockerfile. Inject secrets at runtime. `.dockerignore` excludes `.env/` by default.
