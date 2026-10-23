# Module boundaries

The backend is one installable package, `honest_practice`, with subpackages that are not allowed to import each other freely. The rules live in `backend/pyproject.toml` under `[tool.importlinter]` and run in CI as `lint-imports`.

A rule that is only written down will be broken. A rule that fails the build will be discussed first.

## The packages

| Package | May import | Must not import |
| --- | --- | --- |
| `core` | The standard library and third-party libraries that do no I/O for us | Every other `honest_practice` subpackage |
| `agents`, `sources`, `memory`, `uniqueness`, `db` | `core`, and each other when a later phase needs it | `api`, `worker`, `cli` |
| `tasks` | `core` and the adapter packages | `api`. The worker calls `tasks`, not the other way around |
| `api` | `core`, adapter packages, `tasks` | `worker` |
| `worker` | `core`, adapter packages, `tasks` | `api` |
| `cli` | The same services the API uses, once they exist | `api` |

`config` and `logging` sit at the package root. Every process may import them. They are not a place to hide a database call.

## The three contracts

1. **Core stays free of I/O and adapters.** `honest_practice.core` cannot import `agents`, `sources`, `memory`, `uniqueness`, `tasks`, `db`, `api`, `worker`, or `cli`.
2. **Adapters do not depend on delivery.** `agents`, `sources`, `memory`, `uniqueness`, and `db` cannot import `api`, `worker`, or `cli`.
3. **API and worker are independent.** Neither imports the other. They share behaviour by calling a lower package.

## How to add a package

Add the directory, give it a module docstring that says what it owns and what it must not import, and add it to the contract that matches that sentence. If you cannot name the contract, the package boundary is not decided yet. Write the decision down before the code.

## Why this shape

[ADR-0002](adr/0002-package-boundaries.md) records the choice of one package plus a linter, instead of many separately versioned packages.
