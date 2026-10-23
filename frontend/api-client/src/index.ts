/**
 * Types for the Honest Practice HTTP API.
 *
 * Phase 6 replaces this file with output from `openapi-typescript`. Until then
 * the only contract the UI needs is `GET /health`, and this type is checked
 * against the live response by the health line on the home page.
 */

/** `ok` means every enabled check passed. `degraded` means the process is up and a check failed. */
export type HealthStatus = "ok" | "degraded";

/** Body of `GET /health`. HTTP 503 uses the same shape as HTTP 200. */
export interface HealthResponse {
  status: HealthStatus;
  service: string;
  version: string;
  checks: Record<string, string>;
}
