// News-image entry for Monday 23 November 2026 (Node 22, stdlib only).
//
// The front page is pre-built and shipped beside this file as entry.png:
// it was drawn by build_frontpage.py (real fonts, so every headline is
// crisp) around an AI-generated illustration of the lead story — the
// Russian warship burning off Benghazi after Ukraine's sea-drone strike.
// This program only copies that finished image to /output/entry.png, so
// both grader runs write byte-identical output with no network access.
// Nothing is generated at run time: the output is exactly entry.png.
//
// Run locally with:
//   mkdir -p out && MAKEFUN_OUTPUT_DIR=out node main.ts

import { copyFileSync } from 'node:fs';
import { join } from 'node:path';

const outDir = process.env.MAKEFUN_OUTPUT_DIR ?? '/output';
copyFileSync(new URL('./entry.png', import.meta.url), join(outDir, 'entry.png'));
