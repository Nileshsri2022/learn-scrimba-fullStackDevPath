# Module 08: Responsive Design

## Completion status

**Not covered by the transcript. This is the largest verified skills gap in the path.**

The module's entire subject matter is absent. Verified across the full transcript:

| Search term | Matches |
|---|---|
| "media quer(y / ies)" | **0** |
| "breakpoint" | 0 |
| "viewport" (as the meta tag) | 0 — the only "viewport" (44:24) is scrolling prose in the Next.js course |
| "minmax" / "grid template" | 0 |
| "relative unit" / "em unit" | 0 |
| "max-width" (as a CSS lesson) | 0 |
| "product page" | 0 |
| "responsive" | 3 passing mentions, 0 lessons — the lead list "looks pretty much like what we have and it's also responsive" (10:54), and two asides in the Next.js course (44:31, 45:41) |

Not one responsive layout, media query, or CSS grid track is written anywhere in 47.5 hours of
teaching. The CSS that exists (Modules 02, and the CSS inside the React/Next.js projects) is
fixed-width or flexbox-only, and the flexbox that is taught never wraps except once, in React
(38:36: `flex-wrap: wrap` for language chips).

This matters downstream: Module 14's dashboard refactor ends with three media-query lessons that
also cannot be written from this transcript, and every portfolio project a student ships from
this path will otherwise be desktop-only.

## Why the gap is easy to miss

Two things in the transcript *look* like responsive design if you skim:

1. **The Window Tracker project in React (37:27–37:36).** It reads `window.innerWidth` into
   state, and even listens for the window **resize event**:

   > "We can listen for a dedicated resize event on the window itself and then add some state to
   > our window tracker and update that state with the window.innerWidth every time the window
   > resize event triggers."

   But it is a lesson about `useEffect` and event listeners — a number on screen that updates
   live. No layout changes when the number changes. It is *measurement*, not *responsiveness*.

2. **`background-size: cover` (04:09) and flexbox (Module 02).** Both make pages *feel* fluid,
   and `cover` genuinely helps images scale. Neither adapts layout to a breakpoint.

Neither substitutes for the module.

## What the transcript does contain that's adjacent

- **`rem` (28:33).** The React course computes a font size: "16, we can get the REM size" — one
  sentence, inside a styling fix, not a unit system.
- **`flex-wrap: wrap` (38:36).** "We need to make sure that it can wrap" — for Assembly Endgame's
  language chips. The nearest thing to adaptive layout in the video.
- **`background-size: cover` (04:09).** Making a div-sized image behave responsively.
- **Percentages as width** — used implicitly (e.g. React's "the width should be 100%. But we will
  also set a max[-width]" at 39:24), never as a lesson on relative units.
- **Device thinking** — the course is otherwise honest that it builds desktop-first: the birthday
  site and space exploration site are styled at one fixed width; the hometown homepage solo
  project has no responsive requirement.

## Where to get the missing material

The module has three sections, and each maps to a self-study plan:

**Section 01 — Responsive Layouts** (30 items). Relative units (`%`, `em`, `rem`), controlling
image width, `max-width`, line-height, media queries, breakpoints, mobile-first navigation,
narrow- and wide-screen challenges, the viewport meta tag, and a flexbox image grid. *The
irreducible core:* a media query in CSS:

```css
/* desktop-first: override for small screens */
@media (max-width: 600px) {
  .container {
    flex-direction: column;
  }
}
```

and the viewport meta tag without which phones pretend to be desktops:

```html
<meta name="viewport" content="width=device-width, initial-scale=1" />
```

**Section 02 — Build a Product Page** (20 items). A single product page styled at three widths:
typography, uppercase, a wide-screen breakpoint, viewport-sized (`vh`) intro container, full
background image, form inputs, focus states, reordered flex items (`order`), and `box-sizing`
across the page.

**Section 03 — CSS Grid** (17 items). The mobile layout first, `span` for tablets, grid lines for
laptops, `grid-template-areas` with DevTools visualisation, `minmax`, header and footer rows.
The only mention of CSS grid in the entire transcript is a *course listing used as an object
example* in Module 03 ("the CSS grid course, actually the very first course we launched" —
09:51), which proves the course exists and confirms this video does not include it.

## Small practice task

Do Section 01's arc on a page you already own — the hometown homepage from Module 02 is ideal:

1. **Audit.** Open it in a narrow window (~400px). List everything that breaks: horizontal
   scrolling, squashed text, buttons off-screen. That list is your work queue.
2. **Relative units.** Convert fixed pixel widths to `max-width` + percentages; convert at least
   one font size to `rem` (with the 16px root default in mind) and one spacing to `em`.
3. **Images.** `img { max-width: 100%; height: auto; }` — verify no image ever causes horizontal
   scroll again.
4. **One breakpoint.** Write a single `@media (max-width: 600px)` block that stacks your
   multi-column flex layouts into columns and enlarges tap targets.
5. **The meta tag.** Add the viewport meta tag and re-test on a real phone. Without it, step 4
   does nothing on mobile — verify that claim yourself; it is the most commonly forgotten line
   in front-end development.
6. **Second breakpoint.** Add a wide-screen (`min-width: 1200px`) rule that caps content width
   and centres it.

Keep the before/after screenshots. They are the portfolio evidence for a skill this transcript
never taught you.

## Readiness check for Module 09

Module 09 (APIs) needs no CSS. Before moving on, be honest about your position:

- You can build a fixed-width, flexbox page (Module 02), and you can now — if you did the task
  above — write a media query and explain the viewport meta tag.
- You have **never** written: `em`/`rem` systems, grid tracks, `grid-template-areas`, `minmax`,
  flex `order`, or a mobile-first navigation. Those remain gaps.
- Module 14's dashboard refactor and any real portfolio piece will expose this module's absence;
  plan to fill it from a dedicated responsive-design source before job applications.

## Exact syllabus order

1. **Responsive Layouts** *(no transcript coverage)*
   1. 03. Aside- Relative units and percentages
   2. 04. Create flexible containers with percentage units
   3. 05. Controlling the width of images
   4. 06. Set width constraints with max-width — Exercises 1–2
   5. 07. Aside- The em unit
   6. 08. Set font sizes with em
   7. 09. Aside- Margin and padding with em
   8. 10. Set margin and padding with em — Exercises 1–2
   9. 13. Change font sizes to rem
   10. 14. Text line height
   11. 16. Aside- Media queries
   12. 17. Add media queries to your site — Exercises 1–3
   13. 21. Add a new breakpoint
   14. 22. Adapt the buttons for smaller screens
   15. 23. Adjust font size for smaller screens
   16. 24. Create a mobile-first navigation
   17. 25. Challenge- Narrow screens
   18. 26. Challenge- Wider screens
   19. 28. The viewport meta tag
   20. 29. Aside- Create a flexbox image grid
   21. 30. Wrap the featured items with flexbox
2. **Build a Product Page** *(no transcript coverage)*
   1. 02. Style the intro container
   2. 03. Style main content
   3. 04. Style the text — Exercises 1–3
   4. 06. Uppercase text
   5. 07. Add a breakpoint for wider screens
   6. 09. Viewport sized intro container — Exercises 1–2
   7. 10. Adjust content for wider screens — Exercises 1–2
   8. 11. Apply a full background image
   9. 12. Style the form inputs
   10. 13. Style the focus state
   11. 14. Style the submit button
   12. 16. Aside- Reordering flex items
   13. 17. Adjust visual order of the intro text
   14. 20. Apply box-sizing to the page
3. **CSS Grid** *(no transcript coverage)*
   1. 05. The Mobile Layout
   2. 07. Aside- Span
   3. 08. Tablet view with span
   4. 10. Aside- grid lines
   5. 11. Laptop view with grid lines — Exercises 1–2
   6. 12. Aside- grid template areas and Dev Tools
   7. 13. Convert to grid template areas
   8. 16. Use minmax
   9. 17. The header and footer — Exercises 1–2
