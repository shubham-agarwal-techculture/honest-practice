# ADR-0005: One documentation tree, three readers

- Status: Accepted
- Date: 2026-10-23

## Context

The docs have to serve three readers: someone in the repository, someone browsing a site, and the learner inside the app. Three copies would disagree within a month. The docs also have to stay long enough to be the reference for the system, which makes drift expensive.

## Decision

- Markdown under `docs/` is the only source.
- MkDocs Material builds the browsable site from that tree. `mkdocs build --strict` is part of CI, so a broken link or a file missing from the nav fails the build.
- Phase 8 renders the same files in the app. It does not keep a second set.
- Reference pages that can be generated (Python API, environment names, database schema, HTTP API) are generated from code in later phases. Phase 0 starts that habit for environment variables: `environment_variable_names()` is the list, `docs/10-reference/environment.md` must mention each name, and a test checks.

Pages that describe unbuilt behaviour are outlines. They name the phase that fills them. They do not describe the feature as if it already runs.

## Consequences

- A behaviour change updates the page in the same change. The contributing guide says so.
- The app and the site can differ in chrome (navigation, fonts) and must not differ in words.
- Strict mode means a new page is not done until it is in `mkdocs.yml`.
- Outlines are allowed to be short. Inventing the future in detail, before the code, is how this tree goes stale.
