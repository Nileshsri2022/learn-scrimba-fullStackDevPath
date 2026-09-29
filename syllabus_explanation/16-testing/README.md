# Module 16: Testing

## Completion status

**Not covered by the transcript. This is the largest single gap in the course material.**

The repository lists five sections for this module and **no** nested lessons — it is the only module
in the syllabus with zero lesson-level entries. The transcript matches: there is no testing course
in it at all.

## The verification

Every one of these searches returns **zero matches** across all 221,189 transcript lines:

| Search term | Matches |
|---|---|
| "jest" | 0 |
| "testing library" | 0 |
| "unit test" | 0 |
| "first test" | 0 |
| "test driven" / "test-driven" / "TDD" | 0 |
| "assertion" / "assert " | 0 |
| "describe(" | 0 |
| "npm test" | 0 |

### The one near-miss, and why it is a false positive

Searching for "vitest" returns exactly one hit, at 27:14 in the React module:

> "Building your first project with Vite couldn't be easier. In your terminal, you're simply going
> to type **npm create vitest**. And this will jump you into kind of a wizard that helps you create
> your project."

This is the auto-transcription mishearing **`npm create vite@latest`** — the Vite scaffolding
command. The surrounding context confirms it: the wizard asks for a project name, a framework
(React), and a variant (JavaScript). Nothing to do with the Vitest test runner.

The word "mock" appears four times, none of them about testing: "just a mockup" (a UI reference), "a
kind of mock database" (hardcoded data in the Express module), and two references to mock data in
the Next.js module.

**Conclusion:** no test is written, run, or discussed anywhere in this transcript.

## What is missing

The five sections, with what each would cover:

**03. Write your first test** — installing and configuring a test runner, the `describe`/`it`/`test`
structure, `expect` and matchers, rendering a component in a test environment, and running the suite.

**04. Practice, practice, and practice** — repetition on the basics. The section title implies it is
mostly exercises, which means its value is almost entirely in the challenge files rather than in
video explanation.

**05. Test user interactions** — simulating clicks, typing and form submission, then asserting on
the resulting UI. Querying the DOM the way a user perceives it (by role, by label text) rather than
by implementation detail.

**07. Mock external services — Test** — replacing network calls so tests are fast and deterministic;
asserting on loading, success and error states without hitting a real API.

**09. Accessibility testing with a side of TDD** — automated accessibility assertions, plus
test-driven development: write the failing test first, then the code that makes it pass.

The numbering gaps (01, 02, 06, 08) indicate further material in the hosted course with no folder in
the source repository.

## Why this gap matters more than the others

Two reasons specific to this module.

**1. Nothing else in the course substitutes for it.** With the design module you can at least read
the CSS builds; with RAG you at least have the AI fundamentals. Here there is no partial coverage of
any kind — not one `expect` call in 47 hours.

**2. It is the gap most visible to employers.** Module 20 (Launching Your Career) assumes you can
discuss your process. "How do you test your code?" is a standard interview question, and the honest
answer after this transcript alone is "I haven't."

## The one genuinely relevant piece of context that is in the transcript

Section 09 pairs accessibility testing with TDD, and the transcript *does* teach the accessibility
techniques that would be asserted on — `aria-live` regions, `role="status"`, `aria-label`,
`aria-disabled`, and label/input association. These are documented in
[Module 05](../05-accessible-development/README.md).

That is useful because accessibility assertions are among the easiest first tests to write: they
check for attributes and roles that either exist in the markup or do not. If you self-study this
module, the accessibility work already done on the Assembly Endgame project in Module 15 is the
natural thing to write your first tests against.

## Small practice task

Self-directed, following the section order the syllabus implies. Use the React project you build in
Module 15 — testing is far easier to learn against code you already understand.

1. **Set up.** Add a test runner to the project (Vitest is the natural pairing with Vite, which the
   course already uses) plus a component testing library. Get one trivial test passing —
   `expect(1 + 1).toBe(2)` — before touching any components. Confirm `npm test` runs.
2. **First real test.** Render one component and assert that something expected is on screen. Then
   deliberately break the component and confirm the test **fails**. A test you have never seen fail
   is not yet a test.
3. **Practice.** Repeat step 2 for every component in the project. Resist adding new techniques;
   the point of the section title is repetition.
4. **User interactions.** For an interactive component, simulate a click or a keystroke and assert
   on what changed. Query elements by their accessible role or label text, not by CSS class.
5. **Mocking.** For any component that fetches data, replace the network call and write three tests:
   loading, success, and error. The error case is the one real apps skip and the one that matters.
6. **Accessibility + TDD.** Pick one accessibility improvement not yet made — say, an `aria-live`
   region on a status message. **Write the test first.** Watch it fail. Then add the attribute. Watch
   it pass. That cycle is the whole of TDD.

## Readiness check for Module 17

There is nothing from this module to be examined on. Before moving to Advanced React, just be
explicit with yourself about the position you are in:

- You have completed a full-stack path in which **no code was ever tested**.
- Module 17 will add complexity — context, reducers, custom hooks, performance work — that is
  materially harder to change safely without tests.
- If you intend to interview on the strength of this path, this module is the highest-value thing to
  self-study, and the practice task above is a reasonable syllabus for doing so.

## Exact syllabus order

1. 03. Write your first test *(no transcript coverage)*
2. 04. Practice, practice, and practice *(no transcript coverage)*
3. 05. Test user interactions *(no transcript coverage)*
4. 07. Mock external services — Test *(no transcript coverage)*
5. 09. Accessibility testing with a side of TDD *(no transcript coverage)*
