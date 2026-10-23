import { HealthStatus } from "./health-status";

/** Phase 0 home page. Later phases replace the empty desk with today's edition. */
export default function HomePage() {
  return (
    <main className="mx-auto flex min-h-screen max-w-3xl flex-col px-6 py-16">
      <p className="font-mono text-xs tracking-[0.22em] text-prussian">HONEST PRACTICE</p>
      <h1
        className="mt-6 text-5xl font-medium text-ink"
        style={{ fontFamily: "var(--font-display), var(--hp-display)" }}
      >
        The desk is clear.
      </h1>
      <p className="mt-6 max-w-xl text-lg leading-relaxed text-graphite">
        Daily editions of five DSA patterns and five system design patterns will be published here.
        This install is the skeleton: the API, the worker, and this page.
      </p>
      <div className="mt-10 border-t border-rule pt-4">
        <HealthStatus />
      </div>
      <p className="mt-auto pt-16 font-mono text-xs text-graphite">Edition 000 · Phase 0</p>
    </main>
  );
}
