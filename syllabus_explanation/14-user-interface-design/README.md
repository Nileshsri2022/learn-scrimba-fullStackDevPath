# Module 14: User Interface Design

## Completion status

**Not covered by the transcript. No explanation can be written from this source.**

This is a verified finding, not an omission. The following searches return **zero matches** across
all 221,189 lines of the transcript:

| Search term | Matches |
|---|---|
| "UI design" / "user interface design" | 0 |
| "design principle" | 0 |
| "design challenge" | 0 |
| "metrics" | 0 |
| "visual hierarchy" | 0 |
| "visual weight" | 0 |
| "typography" | 0 |
| "proximity" / "alignment principle" | 0 |
| "media quer(y/ies)" | 0 |

The repository lists 16 activities across three sections for this module — five design challenges
plus a final challenge, a simple-layout build, and a six-lesson metrics-dashboard refactor. **None
of them has a transcript segment.** The word "dashboard" appears 13 times, but every occurrence
refers to something else: the Polygon API dashboard, the OpenAI dashboard, a Netlify dashboard, and
a project dashboard in an unrelated JavaScript exercise.

Writing explanations for these lessons would mean inventing them. This file records the gap instead
and points at the design material that genuinely *is* in the transcript, so the module is not a
total dead end.

## What the transcript does contain about design

Design is taught **inside the CSS modules**, as practical decisions made while building projects —
never as a design curriculum. Five threads are worth collecting.

### 1. Figma as the design source (05:23:34)

Before the first solo project, students are sent to **figma.com** to sign up.

> "Figma is the design tool in which you'll get the design for your project. It is the most popular
> design tool these days. It can kind of be seen as the GitHub equivalent for designers."

A separate ~10-minute Figma tutorial exists on YouTube, made by Bob specifically for Scrimba
students. The reason it is hosted off-platform is itself a small lesson: "learning a browser-based
tool like this is actually better to do via a regular video than via slides."

**The workflow implied throughout the course:** the design arrives as a Figma file, and your job is
to reproduce it in HTML and CSS. That is the professional loop this module would otherwise formalise.

### 2. Reading a design by decomposition (05:25 onwards)

The most transferable design-thinking passage in the transcript. Faced with a full page comp for the
"hometown homepage" solo project, the instructor breaks it into pieces the student has already built:

- hero with a background image + a section beneath → "pretty similar to what we did in the space
  exploration site"
- two headings with background colours → "that's what we did in the birthday gift card"
- the card at the bottom → "resembles our business card quite a lot"
- three equal columns → "that looks like a job for flexbox"
- and each of those three flex children is itself a container holding an image, a heading and a
  paragraph

**The method:** a design that looks impossible is a set of patterns you already know, arranged
together. Decompose before you write any CSS.

### 3. Colour palettes

Named explicitly as "a really important concept in web design... because colors really do make or
break a design."

The practical approach taught:

- Use a palette generator — **coolors.co** is linked from the project.
- The project supplies hex values for its palette in the CSS, and using them is a **requirement**.
- Choosing your own palette is a **stretch goal**, framed as what makes your build distinctive.

### 4. Typography choices

Two threads, both from the CSS modules:

- **Web-safe fonts** — fonts like Verdana that you can use "without worrying about whether or not
  it's installed on your users' computers, because most likely it is."
- **Google Fonts** — imported in the `<head>`, then applied with `font-family`. The instructor's own
  assessment of a project built without one: "the font here is a little bit boring", and adding a
  Google font "can really level up the design."

### 5. White space

Discussed repeatedly during the Google clone build (around 01:21–01:33), always as a diagnosis of a
concrete problem — "the lack of white space above our Google logo", "some breathing room", "we lost
all of our white space." The vocabulary of Section 03's *Fixing White Space* lesson is present; the
lesson itself is not.

**Also relevant:** the contrast checker material documented in
[Module 05](../05-accessible-development/README.md) is the closest the transcript comes to Section
03's *Fixing the Color & Contrast* lesson.

## Where to get the missing material

The three sections need a different source. What each would cover:

**Section 01 — UI Design Fundamentals** (5 design challenges + a final challenge). Core interface
design principles: hierarchy, contrast, alignment, proximity, repetition, and the use of scale and
weight to direct attention.

**Section 02 — Design a Simple Layout** (Challenge 1, Final Chapter Lesson). Composing a full layout
from those principles rather than from a supplied comp.

**Section 03 — Refactor a Metrics Dashboard** (6 lessons). The most concrete and the most missed —
taking an existing bad dashboard and fixing it in a fixed order:

1. Colour & contrast
2. Type & visual hierarchy
3. White space
4. Initial media queries
5. Tablet media queries
6. Desktop media query

That ordering is itself the lesson: colour, then type, then spacing, then responsiveness. It is
worth following even without the video, as a self-directed exercise.

**Note on media queries:** these appear in this module's syllabus *and* in Module 08 (Responsive
Design), and the transcript contains **no media query teaching at all**. If you reach this module
without having written one, that gap traces back to Module 08, not to this module.

## Small practice task

You can do Section 03's refactor without the videos, because its structure is known. Take a
dashboard-style page — one of your own, or a deliberately ugly template — and make exactly four
passes, changing nothing outside the pass you are on:

1. **Colour & contrast.** Reduce to one background, one surface, one text colour and one accent.
   Run every pair through a contrast checker; nothing below 4.5:1 survives.
2. **Type & hierarchy.** Pick at most two sizes for body text and three for headings. Make the most
   important number on the page unambiguously the largest thing on it. No two elements should have
   the same visual weight unless they have the same importance.
3. **White space.** Choose one spacing unit (8px works) and make every margin and padding a multiple
   of it. Group related items by putting *less* space between them than around them.
4. **Media queries.** Mobile layout first, then tablet, then desktop — in that order, each as a
   separate pass.

Screenshot the page after every pass. The before/after sequence teaches more than any single
finished result.

## Readiness check for Module 15

There is no transcript content to be examined on. Before moving to React, confirm only that you can:

- Take a design comp and decompose it into layout patterns you already know how to build.
- Apply a supplied colour palette from hex values, and generate your own with a tool.
- Import and apply a Google font, and explain when a web-safe font is the safer choice.
- Explain why white space around a group communicates that the group belongs together.

And be aware, going into Module 15, that **this module's design principles and all of its media
query material are gaps you are carrying forward.**

## Exact syllabus order

1. **UI Design Fundamentals** *(no transcript coverage)*
   1. 05. Design Challenge 1
   2. 08. Design Challenge 2
   3. 11. Design Challenge 3
   4. 13. Design Challenge 4
   5. 14. The Final Challenge
2. **Design a Simple Layout** *(no transcript coverage)*
   1. 04. Challenge 1
   2. 07. Final Chapter Lesson
3. **Refactor a Metrics Dashboard** *(no transcript coverage)*
   1. 02. Fixing the Color & Contrast
   2. 03. Fixing the Type & Visual Hierarchy
   3. 04. Fixing White Space
   4. 05. Initial Media Queries
   5. 06. Tablet Media Queries
   6. 07. Desktop Media Query
