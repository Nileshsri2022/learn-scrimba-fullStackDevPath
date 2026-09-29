# Module 17: Advanced React.js

## Completion status

**Not covered by the transcript. This is the biggest working-developer gap in the path: 116
lessons across five sections (Reusability, Performance, Routing, Persistence, Authentication),
and none of them appear anywhere in the video.**

The module corresponds to Scrimba's **Advanced React** course — and the *Learn React* course
that IS in the video ends by advertising it:

> "…I'd first like to put in a plug for my advanced React course here on Scribba. The
> advanced React course is the natural progression from where we left off at the end of this
> course. In that course, we dive deep into reusability in React and learn a bunch of new ways
> that we can turn our reusable components into even more reusable components. We learn how to
> build single page applications using the React router library. And we learn all about
> performance in React and how we can improve the performance of our React apps."
> (40:12:35–40:13:01)

That plug names three of the five syllabus sections — Reusability, Routing (React Router), and
Performance — and then the recording moves straight to TypeScript (40:14:23). The Advanced
React course itself was never included in this compilation.

The Learn React course even points at this module's content and explicitly declines to teach
it: "tools like context which is built [into React]… we do dive into context and we learn how
we can use context to avoid having to [pass props through every level]" (34:50:23–34:50:46)…
"if you do have state that is truly global across your entire application, that's usually the
time to start looking at one of those alternative solutions that I mentioned like **context,
redux or zustand**" (34:54:00–34:54:11).

## The verification

Zero-match searches across the entire transcript (74,868 lines):

| Search term | Matches | Note |
|---|---|---|
| "createContext" / "create context" | 0 | |
| "useContext" / "use context" | 1 | the Module 15 deferral quote itself (34:50:46) |
| "compound component" | 0 | |
| "render prop" | 3 | all false positives: "render properly" ×2 (02:32:43, 11:23:50), "render props.re[cipe]" (36:12:48) |
| "custom hook" | 0 | |
| "useMemo" / "use memo" | 0 | |
| "useCallback" / "use callback" | 0 | |
| "React.memo" | 0 | |
| "StrictMode" / "strict mode" | 0 | |
| "Suspense" / "code splitting" | 0 | all 12 "lazy" hits are the English word ("since I'm lazy") |
| "React Router" / "react router" | 6 | all references, no teaching — see below |
| "VanLife" / "van life" | 0 | the Routing section's project |
| "useParams" / "use params" | 0 | |
| "useLocation" / "use location" | 0 | |
| "Outlet" | 0 | |
| "NavLink" | 3 | false positive — see below |
| "Supabase" / "supabase" | 0 | the Persistence and Authentication backend |
| "JWT" / "json web token" | 0 | |
| "protected route" | 0 | |

### The near-misses, examined

- **"React Router" (6 matches, none taught).** Four are the Learn React outro plugging the
  library (40:12:55–40:13:22, including "React Router is about to release version 7"). One is
  the Next.js course contrasting full-page refreshes with "clientside routing with something
  like React Router in React" (47:01:01–47:01:05). The most interesting one is Bob recalling
  the course this module is based on, mid-forms-lesson: "when I was recording a course about
  React Router, I included a whole lesson that I called [hot take:] forms in React are bad"
  (32:59:49–32:59:56) — proof the React Router course exists, and proof this video doesn't
  contain it.
- **"NavLink" (3 matches, 45:43:55–45:44:06).** The Next.js course names its own PrintForge
  active-link component `NavLink` (with a `NavLinkProps` TypeScript type). That's a local
  component name in Module 19's content — not React Router's `<NavLink>`. The *concept*
  (active link styling) genuinely is taught there (45:33–45:52, with `usePathname`), which
  softens — but does not fill — this module's Routing section.
- **"lazy" (12 matches).** Ten are instructors saying "since I'm lazy" while copy-pasting. One
  is Next.js image lazy-loading (44:24:34, Module 19). One is real and noted below.

### What IS in the transcript, honestly

Two genuine pieces of Advanced-React-adjacent material do exist — both inside the *Learn
React* course (Module 15):

1. **Lazy state initialization** (39:56:10–39:56:52), in Assembly Endgame: "when you're
   initializing state by calling a function like this, technically every time we cause a
   rerender in our app, React will rerun this function… it doesn't hurt us to use lazy state
   initialization… by simply wrapping this in a callback function. This way on the very first
   render React will call this function… but on subsequent rerenders it's just going to simply
   ignore this function." This is a real performance technique — the Performance section's
   `useMemo`/`useCallback` family in miniature.
2. **Lifting state up and passing state/setters as props** (34:20–34:54), including the honest
   caveat that it doesn't scale ("that's generally not a good idea… pass it down as many
   levels as I need to" — 34:53:51) — which is precisely the problem Context (Section 01,
   lessons 26–31) exists to solve.

And several *concepts* from the Routing section are taught in their Next.js form in Module 19:
file-based routes and nested routes (43:24, 43:52), dynamic `[id]` params (44:56 — the
framework parallel of `useParams`), layout routes/outlets (44:00 — the parallel of `<Outlet>`),
search-params-driven filtering (47:04 — the parallel of VanLife's filter lessons), and active
link styling (45:43). A learner who completed Module 19 has the *ideas* but has never touched
the `react-router` package.

## What this module would teach

From its lesson titles, in order:

1. **Reusability** — building a `Button` with children, size props, and variants; the
   overloaded `Avatar` mega-challenge; compound components (`Toggle.Button`, `Toggle.On`,
   `Toggle.Off`); the `React.Children` API and its shortcomings; `createContext` + provider +
   `useContext`; state + context (theme switcher, menu); render props; custom hooks
   (`useEffectOnUpdate`, an eight-part `useToggle` build); `refs`.
2. **Performance** — rendering phases; StrictMode's double renders and side-effect re-runs;
   code splitting with `lazy` and `Suspense`; `useMemo`; `React.memo` and referential
   equality; `useCallback`.
3. **Routing** — React Router SPAs: `BrowserRouter`, `Route`/`path`/`element`, the **VanLife**
   project, `useParams`, layout routes, nested host routes, `NavLink` active styling,
   `<Outlet>` context, search-param filtering, `useLocation`, 404 pages.
4. **Persistence** — Supabase project setup, `supabase-js` queries, aggregate queries, storing
   data in state, realtime subscriptions, inserts.
5. **Authentication** — auth session state, JWTs, sign-in/sign-up components and functions,
   `Navigate`, protected routes, sign-out redirects, database triggers, profile fetching.

## Where the path leaves you, and how to fill it

A learner following only this transcript ends Module 16 with:

- Strong prop-drilling skills and lifting state up (Module 15), but no Context, no compound
  components, no custom hooks.
- One real performance technique (lazy state initialization), but no memoization tools.
- Next.js's file-based routing and its concepts, but zero `react-router` experience — notable
  because the outro markets React Router v7 as *about to release*, and many employers' legacy
  codebases still use it.
- No backend persistence or auth wiring at all: Supabase never appears, and even the Express
  auth section of Module 13 is absent from the video (see that module's README). The closest
  available building blocks are Module 11's raw Node servers and Module 12's SQL.

Sensible substitute work, using only what the transcript does provide:

1. Rebuild Module 15's sound pads as a **compound component** (`Pads.Button`, `Pads.On`) and
   then again with **Context** — you'll feel exactly the prop-drilling pain the first version
   causes.
2. Extract a `useToggle` custom hook from Module 15's toggling-state practice (32:3x) and
   reuse it in three components.
3. Take the README of React Router's current docs (v7) and re-implement Module 19's
   PrintForge routes in a Vite SPA instead of Next.js — the concepts map almost one-to-one.
4. For persistence/auth, the honest answer is external material: this path's transcript
   contains none of it.

## Small practice task (using only transcript-covered skills)

1. Build a `Card` component with `children` and a `size` prop; compose a dashboard of cards
   without repeating markup.
2. Lift shared state (a "dark mode" boolean) to an App-level provider and pass it down —
   notice the prop chain, and write a comment where Context would cut it.
3. Use lazy state initialization wherever a component calls a function in `useState(...)`.
4. In a Next.js app (Module 19 skills), add a `/items/[id]` route and a `?query=` filter —
   then write down, for each feature, what its `react-router` counterpart would be
   (`useParams`, `useSearchParams`, `useLocation`).

## Readiness check for Module 18

Module 18 (TypeScript) IS fully covered and follows immediately. Before starting it, be able
to:

- Explain why lifting state up stops scaling, and what problem Context solves (even though
  you haven't used Context yet).
- Explain what lazy state initialization buys you.
- Pass functions as props (the sound-pads pattern) — Section 02 of Module 18 formalizes this
  as "function props" in TypeScript.

## Exact syllabus order

*(No transcript coverage for any section. Note the syllabus numbering skips Section 03,
jumping from Performance to Routing — as with Module 15's missing Section 02, that is a
property of the challenge files, not a transcript gap.)*

1. **01. Reusability**
   1. 02. Button - props review challenge
   2. 05. Challenge - Button w_ Children
   3. 06. Button - More Complex React Children
   4. 07. Challenge - add onClick event listener
   5. 10. Button - size prop — Exercises 1–2
   6. 11. Button - fix className issue
   7. 12. Challenge - Button w_ Variants
   8. 13. Mega Challenge - Overloaded Avatar Component
   9. 17. Compound Components in React - Part 1
   10. 18. Compound Components Quiz
   11. 19. Compound Components in React - Part 2
   12. 20. Compound Components in React - Part 3
   13. 23. The React.Children API — Exercises 1–2
   14. 24. React.Children shortcomings — Exercises 1–2
   15. 26. createContext() & Context Provider
   16. 27. useContext() — Exercises 1–2
   17. 28. Add context to the Menu component — Exercises 1–2
   18. 29. State + Context — Exercises 1–4
   19. 30. Theme switcher final touches
   20. 31. Menu component final touches
   21. 35. Toggle - setup — Exercises 1–2
   22. 37. Toggle Context
   23. 38. Toggle.Button
   24. 39. Toggle.On & Toggle.Off — Exercises 1–2
   25. 40. Remove Star component
   26. 41. Use Toggle with Menu component
   27. 42. Composing new components with Toggle
   28. 43. onToggle event listener — Exercises 1–2
   29. 44. Menu onClose event
   30. 47. Fix onToggle bug using refs
   31. 50. Render Props Part 2
   32. 51. Renders Props Part 3 — Exercises 1–2
   33. 54. Toggle.Display — Exercises 1–2
   34. 56. Custom Hooks - useEffectOnUpdate — Exercises 1–5
   35. 57. Custom Hooks - useToggle
   36. 58. Custom Hooks - useToggle part 2
   37. 59. Custom Hooks - useToggle part 3
   38. 60. Custom Hooks - useToggle part 4
   39. 61. Custom Hooks - useToggle part 5
   40. 62. Custom Hooks - useToggle part 6
   41. 63. Custom Hooks - useToggle part 7
   42. 64. Custom Hooks - useToggle part 8
2. **02. Performance**
   1. 04. Rendering Phases Quiz
   2. 06. StrictMode - double renders components
   3. 07. StrictMode - rerunning side effects
   4. 09. Code Splitting, lazy, Suspense - Part 2
   5. 11. useMemo() practice
   6. 12. React.memo() - reducing rerenders
   7. 13. React.memo() practice
   8. 15. useMemo(), React.memo(), and referential equality
   9. 16. useMemo() practice
   10. 17. useCallback()
   11. 18. useCallback() practice — Exercises 1–3
3. **04. Routing**
   1. 05. BrowserRouter & Routes challenge
   2. 06. Route, path, & element — Exercises 1–2
   3. 09. VanLife project bootstrapping
   4. 11. Challenge- Vans Page - Part 1
   5. 12. Challenge- Vans Page - Part 2
   6. 14. Route Params - part 2
   7. 16. Route Params part 3.1 - useParams() & challenge — Exercises 1–2
   8. 17. Route Params part 3.2 - useParams() challenge
   9. 18. Route Params Quiz
   10. 20. Fixing the Navbar with a Layout Route
   11. 21. Fixing the Navbar with a Layout Route part 2
   12. 22. Bootstrap the Host pages
   13. 23. Nesting the _host routes
   14. 24. Creating the Host Layout — Exercises 1–2
   15. 27. To nest or not to nest_
   16. 28. Nested Routes Quiz
   17. 29. Add Footer
   18. 30. NavLink
   19. 31. Active Link Styling with NavLink
   20. 32. Active Link Styling with NavLink - part 2
   21. 33. Adding Host Vans Routes
   22. 34. Optional Side Quest - Building out the Host Vans List and Detail Pages
   23. 35. Building out the Host Van Detail page
   24. 37. Back to all vans
   25. 38. Add _host_vans_id Nested Routes
   26. 39. Add the Final Navbar
   27. 40. Outlet Context
   28. 43. Challenge- Set up search params in VanLife — Exercises 1–2
   29. 44. Filter the array w_ the search param
   30. 45. Challenge- Filter the vans in VanLife
   31. 46. Using Links to add seach params
   32. 47. Challenge- Filter the vans with Links
   33. 49. Challenge- Filter the vans with a setter function
   34. 53. Challenge- Conditional rendering practice — Exercises 1–2
   35. 54. Fix remaining absolute paths
   36. 57. useLocation
   37. 58. Challenge- conditionally render the back button text
   38. 59. 404 Page
4. **05. Persistence**
   1. 01. Supabase project setup
   2. 02. Query the database using supabase-js
   3. 03. Query with aggregate function
   4. 04. Storing the data in state
   5. 06. Realtime subscription
   6. 08. Insert new data
5. **06. Authentication**
   1. 01. Router setup
   2. 03. Auth Session state - part 1
   3. 06. JWTs (authenticated)
   4. 08. Sign in component - part 1
   5. 11. Sign in auth function - part 2
   6. 12. Navigate & Link — Exercises 1–2
   7. 13. Sign out
   8. 14. Navigate after sign out
   9. 17. Home redirect
   10. 18. Protected Route
   11. 19. Sign up
   12. 23. Sign up expansion
   13. 24. Trigger
   14. 27. Refactor deals table - part 3
   15. 28. Fetch all profiles - part 1
   16. 30. Update new deal form - part 1 — Exercises 1–2
   17. 31. Update new deal form - part 2
   18. 33. Update fetchMetrics - part 2
   19. 34. Account type in Header
