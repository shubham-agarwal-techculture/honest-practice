/**
 * Colour and type tokens for Honest Practice.
 *
 * CSS custom properties in `tokens.css` are what the browser uses. This module
 * exists for code that needs the same values in TypeScript. Phase 7 replaces
 * the pair with one generated source. Until then, change a value in both files.
 */

/** Ink, paper, and the two subject accents. */
export const color = {
  paper: "#F5F1E8",
  raised: "#ECE5D6",
  ink: "#22201C",
  graphite: "#5E5A52",
  rule: "#D9D0BE",
  prussian: "#1F4E79",
  oxide: "#9A4330",
  moss: "#4F6F52",
} as const;

/** Fonts loaded by the web app. The docs site loads the same families. */
export const font = {
  display: "Newsreader",
  sans: "IBM Plex Sans",
  mono: "IBM Plex Mono",
} as const;
