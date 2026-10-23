# Contributing

Phase 0 is a skeleton. Contributions that add a feature from a later phase should land in that phase's shape, not as a shortcut through it.

## Before you open a change

- Read [module boundaries](03-architecture/module-boundaries.md) if the change adds an import.
- Read [commenting](08-code-quality/commenting.md) if the change adds a public function.
- Update the document that describes the behaviour you changed. An outline page can stay an outline. A page that states a fact has to stay true. [ADR-0005](03-architecture/adr/0005-documentation.md) is the reason.

## Checks

From the repository root:

```powershell
uv run --directory backend ruff check src tests
uv run --directory backend ruff format --check src tests
uv run --directory backend mypy
uv run --directory backend lint-imports
uv run --directory backend pytest
uv run --directory backend mkdocs build --strict --config-file ../mkdocs.yml
pnpm --dir frontend lint
pnpm --dir frontend typecheck
pnpm --dir frontend format:check
pnpm --dir frontend build
```

CI runs the same list. A red check is fixed in a new commit, not by skipping the hook.

## Commits

Use a short imperative message that says why the change exists. `git log` is the style guide once there is history. Do not commit `.env`, key files, or the `site/` build.

## Decisions

A change that picks a direction the next person would otherwise have to guess at gets a new ADR under `docs/03-architecture/adr/`. Do not rewrite an accepted record to say something else. Supersede it.
