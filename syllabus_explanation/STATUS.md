# Explanation Status Audit

Audit date: 29 September 2026 — **final pass, all 20 modules written.**
Sources checked:
- `fullstack_developer_syllabus.txt` (20 modules, 85 sections, 1391 items)
- `[SubtitleTools.com] Become a Fullstack Developer from Scratch ... .en.txt` (221,189 lines,
  runtime 47:29:18)

## Verdict in one line

**All 20 module READMEs are now written and transcript-based.** Each one states its own
coverage honestly up front: six modules are full-coverage, seven are partial, and seven are
verified gaps (one of which — Testing — has nothing at all).

A written module is not the same as a fully covered one. The compilation video simply does
not contain courses for every syllabus module, and the READMEs say so rather than inventing
content. Summary:

| Module | Transcript coverage |
|---|---|
| 01. Introduction | Covered (00:00–00:55) |
| 02. HTML and CSS Fundamentals | Covered (00:05–05:30) |
| 03. JavaScript Fundamentals | Covered (05:30–14:02) |
| 04. Tools of the Trade | Sections 01 and 03 covered; Section 02 absent (the instructor says on tape it was unrecorded) |
| 05. Accessible Development | No dedicated course; 5 of 23 topics covered as asides elsewhere |
| 06. Essential CSS | **Nothing.** Verified gap — the compilation skips the course |
| 07. Essential JavaScript | Section 04 covered (15:14–18:27); Sections 01–03 absent |
| 08. Responsive Design | **Nothing.** "media quer(y/ies)" = 0 matches across the whole transcript |
| 09. APIs and Async JavaScript | Fundamentals covered (18:27–19:42); projects absent |
| 10. AI Engineering | Section 01 covered in full; Sections 03 (RAG) and 05 (Agents) absent |
| 11. Node.js | Covered (21:21–24:54, Tom Chant) |
| 12. Databases | SQL basics covered (24:54–26:33, Greger); GROUP BY/HAVING + all of Section 03 absent |
| 13. Express.js | **Nothing.** Verified gap — documented with a Node-bridge table (the Express code the syllabus expects is taught as raw Node) |
| 14. User Interface Design | **Nothing.** Zero matches for every design term searched |
| 15. React.js Fundamentals | Sections 01/03/04/05/07 covered (26:31–40:14, Bob Ziroll); **Tenzies capstone promised and claimed but absent** |
| 16. Testing | **Nothing.** Zero matches for every testing term searched |
| 17. Advanced React.js | **Nothing.** Biggest working-developer gap: context, custom hooks, performance, React Router, Supabase, auth — the Learn React outro advertises the course this compilation never includes |
| 18. TypeScript | Covered (40:14–43:08: Bob Ziroll + Rachel Johnson); the Typed Tenzies solo project has no lessons by design |
| 19. Next.js | Covered (43:08:56–47:29:18, Bob Ziroll, PrintForge + Cat Facts); ends at the search feature exactly where the syllabus ends |
| 20. Launching Your Career | **Nothing.** The video ends at 47:29:18 before any career module |

## Definitive transcript map

| Transcript time | Course | Syllabus module(s) |
|---|---|---|
| 00:00–00:55 | Path introduction | 01 |
| 00:05–05:30 | HTML & CSS (Per) | 02 |
| 02:03–02:1x | Accessibility asides (Per) | 05 |
| 05:30–14:02 | JavaScript (Per, + Treasure, + Tom Chant AI aside) | 03, 07 (S04 only), 09 (part) |
| 14:02–15:14 | Tooling: VS Code, terminal, Git/GitHub | 04 |
| 15:14–18:27 | "Make JS stick" section | 07 |
| 18:27–19:42 | Fetch & async | 09 |
| 19:42–21:21 | AI engineering | 10 |
| 21:21–24:54 | Node.js (Tom Chant) | 11, 13 (as raw Node) |
| 24:54–26:33 | SQL (Greger) | 12 |
| 26:31–40:14 | React (Bob Ziroll) | 15, 05 (ARIA live aside) |
| 40:14–43:08 | TypeScript (Bob Ziroll, Rachel Johnson) | 18 |
| 43:08–47:29 | Next.js (Bob Ziroll) | 19 |
| — | *(nothing)* | 06, 08, 13, 14, 16, 17, 20 |

## Per-module table

| Module | Title | Status | ~Words | Coverage |
|---|---|---|---|---|
| 01 | Introduction | **Written** | 1,136 | Full |
| 02 | HTML and CSS Fundamentals | **Written** | 5,159 | Full |
| 03 | JavaScript Fundamentals | **Written** | 4,570 | Full |
| 04 | Tools of the Trade | **Written** | 4,969 | Partial (S02 absent, on tape) |
| 05 | Accessible Development | **Written** | 3,471 | Asides only (5/23 topics) |
| 06 | Essential CSS | **Written** | 1,375 | **Gap** |
| 07 | Essential JavaScript | **Written** | 2,995 | Partial (S04 only) |
| 08 | Responsive Design | **Written** | 1,321 | **Gap** |
| 09 | APIs and Async JavaScript | **Written** | 3,232 | Partial |
| 10 | AI Engineering | **Written** | 4,764 | Partial (S01 only) |
| 11 | Node.js | **Written** | 2,749 | Full |
| 12 | Databases | **Written** | 2,435 | Partial |
| 13 | Express.js | **Written** | 1,513 | **Gap** (Node bridge table) |
| 14 | User Interface Design | **Written** | 1,336 | **Gap** |
| 15 | React.js Fundamentals | **Written** | 7,189 | Mostly full; Tenzies absent |
| 16 | Testing | **Written** | 1,063 | **Gap** (zero items) |
| 17 | Advanced React.js | **Written** | 2,270 | **Gap** |
| 18 | TypeScript | **Written** | 3,900 | Full (solo project = spec only) |
| 19 | Next.js | **Written** | 4,032 | Full |
| 20 | Launching Your Career | **Written** | 1,769 | **Gap** |

## Verification method

1. Every placeholder README was identified by its `## Ordered syllabus` heading and 100%
   verbatim-copied outline (see the previous audit; 19 of 20 files started that way).
2. Each module was then written against the transcript with time-ranged searches
   (`.index/rsearch.py START END "regex"`) plus full `awk` region reads — never truncated
   search output, which once produced a false "ORDER BY is absent" reading.
3. **Absence claims require zero-match searches across the entire transcript**, plus an
   examination of near-misses (e.g. " NavLink" hits are Module 19's own component name;
   "agile/scrum" hits are "Scrimba" mistranscriptions; "vitest" is `npm create vite@latest`
   misheard).
4. **Presence claims require a located timestamp**, and quotes are checked verbatim against
   the transcript before being committed.
5. Promise-vs-delivery discrepancies are documented rather than smoothed over — e.g. the
   React outro claims "we built two back-to-back games" (40:12:03) but Tenzies was never
   built in this recording.

## Findings recorded along the way

1. **Seven modules have no course in this compilation at all**: 06 (Essential CSS), 08
   (Responsive Design), 13 (Express), 14 (UI Design), 16 (Testing), 17 (Advanced React), and
   20 (Career). Each README documents the verification and the nearest substitutes.
2. **Module 04's missing Section 02 is confirmed on tape** — the instructor says it went
   unrecorded. Numbering gaps elsewhere (Module 04 lesson 05, Module 15 Section 02, Module 17
   Section 03, Module 20 Sections 01–03) were each checked individually rather than assumed.
3. **Tenzies is the one promise the video breaks**: promised at 26:32:42, claimed complete at
   40:12:03, absent everywhere. Module 18's "Typed Tenzies" solo project therefore has no
   untyped foundation in this recording — both READMEs say so.
4. **The Next.js course was released iteratively** and this recording stops where its second
   section stops (search feature). The instructor points to future database work (46:57:13)
   that never arrives. The syllabus also stops there, so this is a boundary, not a gap.
5. **The career material that does exist** is an aside: Module 03's LinkedIn/recruiter story
   of Justin (08:31–08:32), Module 09's promises-as-job-interview analogy (18:59), and one
   interview tip in the Next.js course (47:09:08). Module 20's README catalogs all three.
6. **Speech-to-text pitfalls**: "vitest" for `vite@latest`, "Scrumba/Scruma" for Scrimba,
   "Nex.js" for Next.js, "ARYA" for ARIA, spaced-out identifiers ("use state" for `useState`,
   "form data" for `FormData`). Identifiers must be searched in spoken form.
7. **The syllabus's own oddities**: Module 07 is entirely Section 04 of the JS course's
   syllabus; Module 09's projects live in the AI module; Module 13's content is inside
   Module 11's region as raw Node. The READMEs bridge these with tables.

## Suggested next steps

None for writing — all 20 modules are done. If this repo is extended later:

- The honest way to fill the six empty modules is external material (Scrimba's actual
  Essential CSS, Responsive Design, Express, Testing, Advanced React, and Career Essentials
  courses), each README already lists what to look for.
- A learner following only this transcript should read modules 06, 08, 13, 14, 15, 16, 17,
  and 20 as gap maps, not lessons.
