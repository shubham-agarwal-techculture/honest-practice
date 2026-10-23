# Frontend

pnpm workspace for the Honest Practice interface.

| Package      | Role                                                                   |
| ------------ | ---------------------------------------------------------------------- |
| `web`        | Next.js application. Phase 0 is a single page that reports API health. |
| `ui`         | Design tokens. Components arrive in Phase 7.                           |
| `api-client` | Hand-written health type today. Generated from OpenAPI in Phase 6.     |

```powershell
pnpm install
pnpm dev
pnpm lint
pnpm typecheck
pnpm format:check
```

Run the commands from this directory. The dev server listens on port 3000 and
expects the API at `http://localhost:8000` unless `NEXT_PUBLIC_API_URL` is set.
