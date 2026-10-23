# Start here

Honest Practice is one repository: a Python backend, a Next.js frontend, and this documentation tree.

The backend is the package `honest_practice`. The frontend is the pnpm workspace under `frontend/`. Docker Compose in `deploy/` runs Postgres, the API, the worker, and the web app together.

If you are new, read the [quickstart](quickstart.md), then the [reading map](reading-map.md). If you are about to change a boundary between packages, read [module boundaries](../03-architecture/module-boundaries.md) before you write the import.
