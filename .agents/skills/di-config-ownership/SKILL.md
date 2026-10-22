---
name: di-config-ownership
description: >-
  Keep shared Settings slim: service and provider knobs belong on owning
  injectables and Config hooks. Use when adding Settings fields, backends,
  providers, connections, from_env wiring, or when tempted to put URLs, OAuth,
  or service instances on Settings. For pyiv DI-first projects.
---

# DI config ownership

**Settings is not a provider bag.** Injectables that need configuration own it.

## When to apply

- Adding or changing `Settings` / `*Settings` fields
- Adding a backend, provider, reader/writer, or HTTP connection
- Tempted to put `*_base_url`, credentials, codec options, or service instances on Settings

## Checklist

1. **Name the owner injectable** — connection config, strategy/provider, nested config type — not Settings.
2. **Put knobs on that type** — constructor args and/or `from_env()` on that type.
3. **Expose via Config hook** — e.g. `get_*_connection()`, `get_*_provider()`, `get_*_class()`. Register in `configure()`.
4. **Env for operators** — document env on the owning type; do not mirror every env into Settings. Prefer files under `.env/` for local secrets (see `env-secrets` rule).
5. **Do not add to Settings** unless the knob is truly cross-cutting run surface — and prefer shrinking Settings over time.
6. **Never** store provider/strategy/service **instances** as Settings attributes.

## Anti-patterns

```python
# BAD
Settings.judge_base_url = ...
Settings.writer = AvroChunkWriter(...)

# GOOD
SimpleHttpConnectionConfig.from_env()  # or explicit ctor
class AppConfig(ProjectConfig):
    def get_writer_class(self):
        return AvroChunkWriter
```

Flavors of the same type use qualified bindings (`Named` / `Key` / `Matched`), not a second Settings map.

See `.cursor/rules/di-first.mdc`.
