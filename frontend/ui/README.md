# @honest-practice/ui

Design tokens for the web app and, from Phase 7, the component library.

`src/tokens.ts` and `src/tokens.css` currently repeat the same palette. The
CSS file is what pages import. The TypeScript file is what other packages
import when they need a value in code. Phase 7 generates one from the other
and adds the component set (masthead, specimen plate, marginalia, and the rest).
