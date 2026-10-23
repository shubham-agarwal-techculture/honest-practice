# Threat model

!!! note

    Outline. Phase 10 for the threat model, Phase 12 for deployment secrets writes this page. Nothing described here is implemented unless another page says it is.

## This page will answer

- Fetched URLs as an SSRF risk, handled when manual URL fetch exists.
- An exposed port spending Cursor credit. Phase 12 requires authentication before a public deploy.
- Secrets in logs. The redaction list, and how a reviewer checks a new log line.
