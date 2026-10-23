"use client";

import type { HealthResponse } from "@honest-practice/api-client";
import { useEffect, useState } from "react";

type Probe = "checking" | "ok" | "degraded" | "unreachable";

const COPY: Record<Probe, string> = {
  checking: "Checking the API",
  ok: "API ready",
  degraded: "API up, a check failed",
  unreachable: "API unreachable",
};

const TONE: Record<Probe, string> = {
  checking: "text-graphite",
  ok: "text-moss",
  degraded: "text-oxide",
  unreachable: "text-oxide",
};

/** Reads `GET /health` once and shows a one-line status in the page footer. */
export function HealthStatus() {
  const [probe, setProbe] = useState<Probe>("checking");

  useEffect(() => {
    const base = process.env.NEXT_PUBLIC_API_URL ?? "http://localhost:8000";
    const controller = new AbortController();

    fetch(`${base}/health`, { signal: controller.signal })
      .then(async (response) => {
        const body = (await response.json()) as HealthResponse;
        setProbe(body.status === "ok" ? "ok" : "degraded");
      })
      .catch((error: unknown) => {
        if (error instanceof DOMException && error.name === "AbortError") {
          return;
        }
        setProbe("unreachable");
      });

    return () => controller.abort();
  }, []);

  return (
    <p className={`font-mono text-xs tracking-wide ${TONE[probe]}`} role="status">
      {COPY[probe]}
    </p>
  );
}
