# Explanation Status Audit

Audit date: 30 September 2026 (updated after writing modules 11, 12, 13; earlier passes did 01, 04, 05, 10, 14, 16)
Sources checked:
- `fullstack_developer_syllabus.txt` (20 modules, 85 sections, 1391 items)
- `[SubtitleTools.com] Become a Fullstack Developer from Scratch ... .en.txt` (221,189 lines, runtime 47:29:18)

## Verdict in one line

**Ten modules are written (01, 03, 04, 05, 10, 11, 12, 13, 14, 16). The remaining ten are still
placeholders** — their "Ordered syllabus" block is a verbatim copy of the matching block in
`fullstack_developer_syllabus.txt` with zero added explanation.

**Important correction:** Module 13 (Express.js) turned out to be a **documented gap**, not a
well-covered module. The earlier estimate that Express was "well covered, roughly 21:40–26:50" was
wrong — reading that region line by line shows it is Node.js (Module 11) followed by Databases
(Module 12), then React. Express is only *mentioned* three times, always to contrast with the raw
Node the course actually teaches. See `13-express-js/README.md` for the full verification.

A written module is not the same as a fully covered one. The transcript does not contain material
for every module, so each written file states its own coverage honestly up front:

| Module | Transcript coverage |
|---|---|
| 01. Introduction | Covered |
| 04. Tools of the Trade | Sections 01 and 03 covered; Section 02 absent (the instructor says on tape it was unrecorded) |
| 05. Accessible Development | No dedicated course; 5 of 23 topics covered as asides elsewhere |
| 10. AI Engineering | Section 01 covered in full; Sections 03 (RAG) and 05 (Agents) absent |
| 11. Node.js | Both sections covered in full (Wild Horizons API + "From the Other Side") |
| 12. Databases | Section 02 (SQL queries) covered in full; Section 03 (Creating/Joining tables) announced on tape but never delivered |
| 13. Express.js | **Nothing.** Express is only mentioned in passing; never taught. Documented gap |
| 14. User Interface Design | **Nothing.** Zero matches for every design term searched |
| 16. Testing | **Nothing.** Zero matches for every testing term searched |

## Verification method

1. Any README containing the heading `## Ordered syllabus` was treated as a candidate stub.
2. Every non-blank line after that heading was tested for verbatim presence in
   `fullstack_developer_syllabus.txt`.
3. Result: for all 19 stub files, **0 lines** were original text. 100% copied outline.
4. Module 01 has no `## Ordered syllabus` dump; it contains prose, code samples, a practice task
   and a readiness check, and its content matches transcript lines ~110–200
   ("I code, therefore I am", `index.html`, `h1` opening/closing tags).

## Per-module table

| Module | Title | Status | Own words | Syllabus items to cover (sections / lessons / practices) |
|---|---|---|---|---|
| 01 | Introduction | **Written** (transcript-based) | ~1139 | 2 / 6 / 2 |
| 02 | HTML and CSS Fundamentals | Placeholder — outline only | 0 | 5 / 67 / 17 |
| 03 | JavaScript Fundamentals | **Written** (4 sections, per-lesson) | ~3200 | 4 / 104 / 35 |
| 04 | Tools of the Trade | **Written** (per-lesson) | ~5072 | 3 / 11 / 7 |
| 05 | Accessible Development | **Written** (coverage map + 5 topics) | ~3534 | 20 / 6 / 0 |
| 06 | Essential CSS | Placeholder — outline only | 0 | 3 / 43 / 13 |
| 07 | Essential JavaScript | Placeholder — outline only | 0 | 4 / 100 / 31 |
| 08 | Responsive Design | Placeholder — outline only | 0 | 3 / 44 / 18 |
| 09 | APIs and Async JavaScript | Placeholder — outline only | 0 | 4 / 78 / 33 |
| 10 | AI Engineering | **Written** (per-lesson) | ~4863 | 3 / 14 / 0 |
| 11 | Node.js | **Written** (both sections, per-lesson) | ~2600 | 2 / 24 / 12 |
| 12 | Databases | **Written** (Section 02 full; Section 03 gap documented) | ~2400 | 2 / 27 / 42 |
| 13 | Express.js | **Written** (documented gap) | ~1400 | 3 / 32 / 2 |
| 14 | User Interface Design | **Written** (documented gap) | ~1353 | 3 / 13 / 0 |
| 15 | React.js Fundamentals | Placeholder — outline only | 0 | 6 / 121 / 61 |
| 16 | Testing | **Written** (documented gap) | ~1080 | 5 / 0 / 0 |
| 17 | Advanced React.js | Placeholder — outline only | 0 | 5 / 116 / 46 |
| 18 | TypeScript | Placeholder — outline only | 0 | 3 / 36 / 26 |
| 19 | Next.js | Placeholder — outline only | 0 | 2 / 26 / 12 |
| 20 | Launching Your Career | Placeholder — outline only | 0 | 5 / 50 / 31 |

The "own words" column counts words outside the copied outline and the two boilerplate lines
(`## Study path` + its one-sentence paragraph), which are identical in all 19 stub files.

## Where each module lives in the transcript

First mention timestamps, useful as anchors when writing the remaining modules:

| Topic | First transcript timestamp |
|---|---|
| HTML / first page | 00:01:30 |
| Accessibility | 02:03:48 |
| Node / Express region | 05:32:27 |
| Responsive design | 10:54:51 |
| Tailwind / Next.js region | 43:11:05 |
| End of transcript | 47:29:18 |

## What "complete" should mean for the remaining modules

Module 01 sets the quality bar. To match it, each module README needs:

1. A completion-status note stating how transcript coverage maps to syllabus activity names.
2. Step-by-step prose explanation drawn from the transcript, with code blocks.
3. A "Mapping to the syllabus activities" section, honestly flagging activities the transcript
   never names out loud.
4. A "What this module teaches" summary.
5. A small practice task.
6. A readiness check for the next module.
7. The exact syllabus order at the end.

Module 01 covers 8 syllabus items. Module 13 alone covers 37, and Module 15 covers 188, so the
larger modules will need to be written in several passes rather than one.

## Findings recorded while writing modules 04, 05, 10, 14 and 16

These are verified transcript facts that affect the remaining modules:

1. **Module 08 (Responsive Design) is at risk.** "media quer(y/ies)" returns **0 matches** in the
   entire transcript. Module 08 lists 44 lessons on responsive layouts. Check this before starting it.
2. **Testing is entirely absent.** The single "vitest" hit is the transcriber mishearing
   `npm create vite@latest`, not the Vitest test runner.
3. **RAG, embeddings and vector databases are entirely absent.** "embedding", "vector" and
   "supabase" all return 0 matches, so Module 10 Section 03 and probably parts of Module 12 are gaps.
4. **Syllabus numbering gaps sometimes mark content the transcript does have.** Module 04 Section 03
   jumps from lesson 04 to lesson 06; the transcript fills that slot with a full merge-conflict
   lesson. Worth checking other gaps the same way rather than assuming missing means absent.
5. **Accessibility is taught as asides scattered across other modules**, including inside React
   (labels at 33:04, ARIA live regions at 39:45). Topic order in the syllabus is not the order the
   transcript teaches in.

## Findings recorded while writing modules 11, 12 and 13

6. **Express.js (Module 13) is a gap, not a covered module.** This overturns the earlier estimate.
   `express()`, `app.get`, `app.use`, `app.listen`, `req.params`, `res.send`, `middleware`,
   `express-session`, `bcrypt`, `passport` and `jwt` all return **0 matches**. Express appears only
   as three passing mentions (21:24, 22:23, 40:13), each contrasting it with raw Node. Module 11
   (Node.js) is the honest substitute for its API section; authentication has no substitute anywhere.

7. **Databases (Module 12) Section 03 is a gap.** The project intro (25:16) *promises* staff and
   dealership tables and joins, but the closing recap (26:29) reviews only Section 02 and declares the
   course over. `create table`, `left join`, `right join`, `inner join`, `foreign key`, `drop table`
   all return **0 matches**. Section 02 (SELECT → DELETE) is fully covered.

8. **The backend teachers are new.** Node.js and its intro are taught by **Tom Chant**; Databases by
   **Greger** (his first Scrimba course). React onward is **Bob Ziroll**, with **Rachel Johnson**
   joining for part of TypeScript.

9. **The Node "mock database" note in the Testing module refers to Module 11, not Express.** The
   `db.js` async function that mimics a database lives in the Wild Horizons **Node** project.

## Suggested next steps

Remaining placeholders, in the order they are most worth writing:

- **15. React.js Fundamentals** — 188 syllabus items, ~13 hours of transcript (starts ~26:35, taught
  by Bob Ziroll). The single biggest remaining module; needs several passes.
- **07**, **09** — JavaScript (essentials & async), both well covered.
- **02**, **06** — HTML and CSS, well covered.
- **17. Advanced React**, **18. TypeScript** (Bob Ziroll then Rachel Johnson; TypeScript starts
  ~40:16), **19. Next.js** (~43:11 region), **20. Launching Your Career**.
- **08** — check coverage first; the media query finding above suggests it may be another gap.

**Done this pass (30 Sep):** 11 (Node.js), 12 (Databases), 13 (Express.js — turned out to be a gap), 03 (JavaScript Fundamentals).
