# Api keys

!!! note

    Outline. Phase 10 for the threat model, Phase 12 for deployment secrets writes this page. Nothing described here is implemented unless another page says it is.

## This page will answer

- `CURSOR_API_KEY` is read by settings and by the SDK.
- It is never logged. See `Settings.for_log`.
- Where the key is created in the Cursor dashboard.
- The database URL is treated the same way.
