# Module 06: Essential CSS

## Completion status

**Not covered by the transcript. No explanation can be written from this source for the three
site builds.**

This is a verified finding. The module's three projects and their signature techniques return
**zero matches** across the transcript:

| Search term | Matches |
|---|---|
| "NFT" | 0 |
| "coworking" / "co-working" | 0 |
| "portfolio" (as a build project) | only Module 02's personal website (00:34–01:04) and a student's portfolio shown in passing (08:29) |
| "compound selector" | 0 |
| "z-index" | 0 |
| "inline-block" | 0 |
| "position: absolute" / "absolute position" | 0 |
| "CSS organisation" / "content container" | 0 |

The transcript jumps from the end of Module 03's JavaScript course (14:02, command line) straight
into more JavaScript at 15:14. There is no second dedicated CSS course anywhere in the 47.5 hours.

The instructor even flags the missing material himself. Teaching the birthday-site hover effect
(05:11), he explains why an `id` rule beats a `class` rule — "because of something called
**specificity**… I don't want to get more into specificity. We're going to learn more about that
later in the front end developer career path." That "later" course is this module, and it is not
in the video.

## What the transcript does contain that serves this module

The techniques this module formalises are scattered across earlier modules as one-off moves.
Collecting them is the honest way to prepare.

### 1. Specificity — the one-minute version (05:11)

> "The more specific a CSS selector is, the higher it will be prioritized… this ID selector is a
> more specific selector than the class, because… only one element can have an ID whereas
> multiple elements can share the same class. So IDs are more specific than classes."

What is missing: compound selectors, the specificity calculation (inline > id > class > element),
and how `!important` interacts with it. Module 06's *Aside- Compound selectors and specificity*
is exactly that missing lesson.

### 2. Grouping selectors (05:21)

The birthday-site recap teaches the comma: "the grouping selector… allowed us to make our CSS
syntax much more compact as we could target all of these HTML tags instead of having to recreate
this text shadow rule again and again." Module 06's *Grouping Selectors* lesson extends this into
deliberate CSS architecture; the transcript only shows the trick.

### 3. Utility classes and modifiers (03:51, 04:16)

The business card and space exploration sites both build a class that "only has one job and that
is setting a single CSS property" (the border-bottom "underline class"). This is precisely the
*main class + modifier class* pattern Module 06's Section 01 finishes with (lesson 26–27,
refactoring the buttons) — but only the utility half is demonstrated, not the
`.btn` + `.btn--secondary` composition.

### 4. Hover and active states (04:54)

`:hover` is taught once, swapping a background image on the birthday GIFts. `:active` — which
Module 06's *Aside- Hover and active states* pairs with it — is never mentioned in the transcript.

### 5. Line-height (01:59)

The Google clone fixes button height "here and use line height instead." Module 06's
*Line-height debug* lesson (spacing diagnosis) is not present.

### 6. Semantic sectioning + footer (Module 02, throughout)

`header`, `main`, `section`, `footer` — Module 06 Section 01's opening lesson — are used from the
personal website (00:50) onward, but never named as a lesson. The closest explicit statement is
the React course's "we're going to use a semantic HTML header element" (31:12).

### 7. Full-width backgrounds and content containers (01:42, 02:45)

The Google clone builds a full-width colored footer behind centered content — the exact visual
problem of Module 06's *Aside- background full width* and *Content Container* lessons. The
transcript solves it once, ad hoc; the module would systematise it.

## Where to get the missing material

**Section 01 — Build an NFT Site** (27 lessons). Semantic sectioning, margins' strange behaviour
(margin collapse), hover/active, full-width backgrounds, content containers, CSS organisation,
grouping and compound selectors, specificity, line-height debugging, inline-block, main + modifier
classes, button/link styling. *In the transcript: only the fragments listed above.*

**Section 02 — Build a Portfolio** (10 "CSS Fundamentals" challenges). A design arrives as a
Figma comp; layout, Google fonts, typography, "fancier" details, breathing room, colour, buttons
and headings are produced challenge-by-challenge. *The transcript's closest analogue is Module
02's hometown homepage solo project (05:21–05:30), which uses the same workflow but a simpler
brief.*

**Section 03 — Build a Coworking Space Site** (11 lessons). `margin: auto` on flexbox children,
`position: relative` + `absolute`, a chatbox overlay, and the `z-index` challenge. *Zero
transcript coverage — no positioned element is built anywhere in the video.*

## Small practice task

Without the videos, Section 01's structure is still known from its lesson names, so rebuild its
skeleton using only techniques the transcript *did* teach:

1. Semantic shell: `header` (dark), `main`, two `section`s, `footer` — each full-width, with an
   inner content container capped at ~800px and centred (margin auto).
2. A card grid inside one section (flexbox from Module 02), each card with image, heading, text,
   and a link styled as a button.
3. Two buttons that share one `.btn` class but differ by a modifier class (e.g. `.btn-primary`).
4. One grouping-selector rule and at least two utility classes (single job each).
5. `:hover` states on the buttons and cards.

Then — as the part the transcript cannot teach you — add a `position: absolute` "New" badge on
the first card, offset from its top-left corner, and give it a `z-index` above the card image.
Test that it survives browser zoom and narrow windows.

## Readiness check for Module 07

No transcript content to be examined on. Before the JavaScript module, confirm you can:

- Explain why an `id` rule overrides a `class` rule, and predict which of two competing rules
  wins without running the code.
- Write one rule that styles four different elements at once (grouping).
- Compose a base class and a modifier class instead of copy-pasting a button style.
- Build a full-width colour band with centred content inside it.

And carry forward honestly: **compound selectors, z-index, positioning, and organised CSS
architecture are gaps from this module** that Module 08 (responsive design) and Module 14 (UI
design) would otherwise have built on.

## Exact syllabus order

1. **Build an NFT Site** *(no transcript coverage)*
   1. 01. Semantic HTML - Header, Main, Section, Footer
   2. 02. Set up the CSS basics
   3. 03. Aside- Margins - strange behaviour
   4. 04. Header
   5. 05. The first section - image
   6. 06. The first section - text
   7. 07. Aside- Hover and active states
   8. 08. The first section - links
   9. 09. Aside- background full width — Exercises 1–2
   10. 10. Content Container
   11. 11. CSS organisation
   12. 12. The second section colors
   13. 13. The second section imgs
   14. 14. Style the Footer
   15. 15. Grouping Selectors
   16. 18. Aside- Compound selectors
   17. 19. Aside- Compound selectors and specificity
   18. 20. Line-height debug — Exercises 1–2
   19. 22. Aside- Buttons_Links
   20. 23. Style the buttons individually new
   21. 24. Aside- Inline-block
   22. 25. space out the buttons
   23. 26. Aside- A main class and a modifier class
   24. 27. Refactor the buttons
2. **Build a Portfolio** *(no transcript coverage)*
   1. 01. CSS Fundamentals- Challenge #1 - Setting up the layout
   2. 03. CSS Fundamentals- Challenge #2 - Google fonts
   3. 05. CSS Fundamentals- Challenge #3 - Setting up the typography
   4. 07. CSS Fundamentals- Challenge #4 - Making things a little more fancy
   5. 09. CSS Fundamentals- Challenge #5 - Breathing Room
   6. 11. CSS Fundamentals- Challenge #6 - Playing with colors
   7. 13. CSS Fundamentals- Challenge #7 - The finer details
   8. 15. CSS Fundamentals- Challenge #8 - Creating buttons
   9. 17. CSS Fundamentals- Challenge #9 - Fancier headings
   10. 19. CSS Fundamentals- Challenge #10 - Working with what you have
3. **Build a Coworking Space Site** *(no transcript coverage)*
   1. 01. Build the foundations
   2. 02. Aside- margin- auto on flexbox children — Exercises 1–3
   3. 03. Position the menu icon
   4. 04. Aside- Position- relative & absolute — Exercises 1–2
   5. 05. Add the image banner
   6. 06. Add buttons — Exercises 1–2
   7. 07. Stop the vertical stretch on the button
   8. 09. Add the chatbox — Exercises 1–2
   9. 11. z-index challenge
