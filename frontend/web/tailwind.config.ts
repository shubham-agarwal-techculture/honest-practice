import type { Config } from "tailwindcss";

const config: Config = {
  content: ["./app/**/*.{ts,tsx}"],
  theme: {
    extend: {
      colors: {
        paper: "var(--hp-paper)",
        raised: "var(--hp-raised)",
        ink: "var(--hp-ink)",
        graphite: "var(--hp-graphite)",
        rule: "var(--hp-rule)",
        prussian: "var(--hp-prussian)",
        oxide: "var(--hp-oxide)",
        moss: "var(--hp-moss)",
      },
      fontFamily: {
        display: "var(--hp-display)",
        sans: "var(--hp-sans)",
        mono: "var(--hp-mono)",
      },
    },
  },
  plugins: [],
};

export default config;
