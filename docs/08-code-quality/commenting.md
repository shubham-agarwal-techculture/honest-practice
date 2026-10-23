# Commenting

Comments and documents do different jobs. The document says what the system is for and how the pieces fit. The comment says what a reader of this function cannot see from the next ten lines.

## Python

Public modules, classes, and functions use Google-style docstrings. Ruff's `D` rules, with the Google convention, enforce that in CI.

A docstring includes:

- a summary line that says what the callable is for, not a restatement of its name
- `Args` when there is an argument worth explaining
- `Returns` when the return value is not obvious from the summary
- a note of errors the caller is expected to handle, when the function raises them

Do not add a docstring that repeats the signature in prose. Do not add a comment above a line that says what the line does.

```python
def check_database(database_url: str) -> str:
    """Run ``SELECT 1`` and report the outcome without raising.

    The returned string never includes the URL, because the URL contains
    the database password.

    Args:
        database_url: SQLAlchemy URL, including the driver.

    Returns:
        ``ok``, or ``error:`` plus the exception class name.
    """
```

An inline comment is for a constraint: a timeout, an ordering requirement, a workaround, a reason a value looks arbitrary. The health check sets a connect timeout because a down database must not hold the probe open. That is worth a comment. `status_code = 200` is not.

## TypeScript

Exported functions, types, and components get a TSDoc comment with the same standard: purpose, and anything the types do not say. `HealthResponse` documents that HTTP 503 uses the same body as HTTP 200, because the type system cannot say that.

## Module READMEs

Each backend subpackage has a `README.md` of a few lines: what it owns, what it must not import, and which phase fills it in. If the README and the import-linter contract disagree, the contract is the one CI believes, and the README is a bug.

## What not to write

- Comments that describe the change you just made ("added for phase 0"). Git history holds that.
- Commented-out code.
- Headers that banner a section of a file.
