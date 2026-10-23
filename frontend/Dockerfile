FROM node:22-alpine

# Pin the pnpm release. pnpm 12 refuses this lockfile under its default
# minimum-release-age policy, and the image must install the same pnpm the
# lockfile was produced with.
ENV COREPACK_ENABLE_DOWNLOAD_PROMPT=0
RUN corepack enable && corepack prepare pnpm@10.21.0 --activate

WORKDIR /app

# Install after the sources are copied. Copying the workspace on top of an
# earlier install deletes the per-package node_modules links pnpm creates.
COPY . .

RUN pnpm install --frozen-lockfile

ARG NEXT_PUBLIC_API_URL=http://localhost:8000
ENV NEXT_PUBLIC_API_URL=$NEXT_PUBLIC_API_URL

RUN pnpm --filter @honest-practice/web build

EXPOSE 3000

CMD ["pnpm", "--filter", "@honest-practice/web", "start"]
