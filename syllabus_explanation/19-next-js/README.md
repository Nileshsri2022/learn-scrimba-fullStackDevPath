# Module 19: Next.js

## Completion status

**Fully covered — the video's final course, 43:08:56–47:29:18.** Bob Ziroll teaches Scrimba's
"Introduction to Next.js" (43:11:45: "My name is Bob Z[i]roll. I have been helping students
transition careers into web development for over 10 years now"), building one project —
**PrintForge, "a site for 3D printing enthusiasts to browse different 3D models that they can
print for themselves"** (43:09:50) — from scratch to a working search feature. The syllabus's
two sections map one-to-one onto the course's two sections, and the course outro (47:28:04)
recaps exactly the syllabus's lesson list.

One honest framing note: this course was **"released iteratively"** — "if you're jumping in
soon after the launch, you'll have access to the entire first section… As I continue to record
other sections, I'll be adding those sections onto this course until we finally reach the end"
(43:10:23–43:10:38) — and the instructor points forward to content this compilation never
reaches: "In a future section, we are going to be moving that data over to a real database"
(46:57:13). The transcript (and the syllabus) end at the search feature; API routes,
databases, and deployment are not taught here. The syllabus doesn't promise them either, so
this is a boundary, not a gap.

Prerequisites are stated explicitly (43:10:40–43:11:17): "a solid foundation in HTML, CSS,
JavaScript, and React," plus Tailwind CSS and TypeScript as used-but-not-required technologies
("TypeScript because of its nature as just an industry standard these days").

## How the sources relate

| Transcript time | Course segment | Syllabus section |
|---|---|---|
| 43:08:56–43:12:02 | Course intro: why Next.js, PrintForge, iterative release, prereqs, teacher | — |
| 43:12:08–43:20:00 | Manual install (next, react, react-dom), scripts, `npm run dev`, app folder, layout + page | 01 (02–03) |
| 43:20:00–43:26:00 | Home page contents; about-page challenge; **file-based routing** | 01 (03–04) |
| 43:29:18–43:36:30 | **PrintForge** intro; Tailwind; home page challenge | 01 (10) |
| 43:36:28–43:39:00 | **Scrimba's Runner**; first runner challenge | 01 (07) |
| 43:39:00–43:52:00 | About page challenge; metadata; fonts | 01 (11) |
| 43:52:00–44:00:00 | Hero image swap; **nested routes** (`/about/mission`) | 01 (12) |
| 44:00:06–44:12:45 | **Layouts** (children prop, shared UI, header/nav in root layout) | 01 (14–15) |
| 44:21:48–44:26:00 | **Optimizing images** (`next/image`) | 01 (17) |
| 44:26:00–44:31:25 | Models list page challenge | 01 (22) |
| 44:31:25–44:39:00 | **Link** (client-side navigation, prefetch); add links to navbar challenge | 01 (19) |
| 44:42:40–44:50:17 | **Server vs client components**; models page (`getAllModels`, await) | 01 (22) |
| 44:53:26–45:04:00 | **Dynamic routes** (`[id]`, params); model detail page | 01 (23–24) |
| 45:15:00–45:22:30 | Categories page + nav bar | 02 (02–03) |
| 45:33:00–46:14:00 | Active link styling; **use client**; client-boundary rules; `usePathname` | 02 (06–09) |
| 46:14:42–46:20:00 | Category pages (`getModels` with category filter) | 02 (10) |
| 46:20:01–46:43:00 | **Rendering strategies**: SSG, ISR, SSR; fetch caching options | 02 (14) |
| 46:43:00–46:58:00 | **Cat Facts** — SSG pt. 1, add fetch, dev-server output, structured play | 02 (14–16) |
| 46:57:26–47:13:56 | **Form submissions are navigation events**; searchParams; Cat Facts filter | 02 (17) |
| 47:13:58–47:20:00 | **PrintForge search bar** with native form | 02 (20) |
| 47:23:11–47:28:00 | **Next's `<Form>` component** + progressive enhancement | 02 (22) |
| 47:28:04–47:29:18 | Section recap + Discord plug; **end of transcript** | — |

---

## Section 01 — Build a Next.js App

### Creating an app the minimal way (43:12:08–43:20:00)

- The honest detour around the standard tool: "Usually when you're creating a new Nex.js app,
  you'll create it using create next app, a CLI tool that uses npx… It's actually the way I
  would recommend doing it. However, when you're first starting out… it can be a little bit
  intimidating… to see all of the files and all of the questions" (43:12:16–43:12:42). So the
  course follows the docs' **manual installation** page.
- Just three packages: "we need to install just three packages, next, react, and react DOM"
  (43:13:01) — `npm install next@latest react@latest react-dom@latest` (43:13:07).
- **package.json scripts** (43:13:31): what `scripts` does — "it allows me to use npm run and
  then the name of the script… `npm run dev`… runs next dev" (43:13:55–43:14:09).
- **The app folder** needs two files: `layout.jsx` "and then… page.jsx or .tsx if you're using
  TypeScript" (43:14:46–43:16:07).
- **Root layout** explained by contrast with Vite: client-side React projects "have an
  index.html HTML file… the HTML tag, the body tag, the head tag… maybe with the ID named root
  where your React components would render to. In [Next], [we] actually create a React
  component that is our root component here in this layout file that contains all the things"
  (43:15:24–43:15:59) — returning `<html>` and `<body>` tags.
- The `Page` component is "just a React component… it simply returns an H1" (43:16:14).
- A from-scratch challenge has the learner recreate the app folder, layout, and page
  themselves (43:18:40), with the quirk that `page.jsx` must be "exactly all lowercase
  page.jsx or .tsx" (43:24:20).

### Adding a page + file-based routing (43:21:21–43:26:00)

- The about-page challenge (43:21:41): new folder `about` with its own `page.jsx` — solved at
  43:23:20 ("new folder and I'll call my folder about… we'll do page.jsx… return an H1 that
  says this is the about page").
- The naming of the concept: "As we can see, Nex.js uses something called **file-based
  routing**. This means in order to create new pages [you create folders in] the app folder
  and make sure that those directories have a page.jsx file" (43:23:59–43:24:14).
- Routing defined: "a route is a URL path [that] maps to a page in your app. So in Nex.js, we
  create new routes or pages by creating folders with a file called page.jsx" (43:24:59–43:25:11).

### PrintForge, Tailwind, and the Runner (43:29:18–43:39:00)

- "The project for this course is called Print Forge, which is a site for 3D printing
  enthusiasts to browse different 3D models" (43:09:50) — one project built "feature for
  feature all the way until it is a fully-fledged, fully capable web application"
  (43:10:17–43:10:21).
- **Tailwind CSS** is used for styling; the learner is told familiarity "will [help]" but the
  course teaches what it needs — with a Scrimba quirk: the platform works "behind the scenes
  to downgrade Tailwind [v4]" (43:35:21).
- **Scrimba's Runner** (43:36:28–43:38:25): "we at [Scrimba have] a runner. And a runner is an
  automated [system that spins up the code of] a challenge for you to work on" — a modal pops
  the challenge's live app, "the runner actually spinning up the code on [the server]," and
  "depending on a number of different factors, the runner may take [a while]." A deliberate
  "super contrived challenge" (43:38:04) lets the learner see one run before real use.
- The **PrintForge home page** challenge follows, built against a Figma design, with hero
  image `hero-image-square.png` swapped in around 43:52.

### Nested routes and layouts (43:52:59–44:12:45)

- **Nested routes**: "want to create a nested route, I simply [create a folder inside another
  route's folder]" — the example is `/about/mission` (43:52:59–43:58:22), then generalized:
  "nested routes and nested layouts as deep [as you want]" (44:02:40).
- **Layouts** (44:00:06–44:12:45): a layout is shared UI that persists across navigations —
  "the navigation bar is the portion of the UI [that stays the same while] visiting [pages
  with] nested routes" (44:01:49).
- **The children prop is the whole mechanism**: a layout "takes in the children prop [to]
  render all the children of this layout… The children is where the page component is going
  to be placed. So Nex.js [takes the] page component and just put[s] them right here inside
  of the children" (44:05:21–44:05:48).
- The **header/nav is added to the root layout** so every page shares it (44:07:26–44:09:16),
  and a footer below the children (44:09:16) — the syllabus's *Add Header to PrintForge*
  challenge, designed against Figma (44:09:41).
- **Fonts** get the same treatment as everything else — built in, no external `<link>`: two
  `next/font` fonts, "one for all the headers" (44:12:30–44:14:08).

### Optimizing images (44:21:48–44:26:00)

> "What I wanted to cover is this idea of optimizing images. Nex.js has some pretty cool
> built-in ways to make images [better]… [they] allow you to avoid doing any of the [manual
> work]" (44:21:56–44:22:16)

- `import Image from "next/image"` — "an extension on top of [the native img element]"
  (44:22:41–44:22:43); drop-in replacement with `src` like any image.
- **`width` and `height` are required and mean the native pixel dimensions** (742×742 for the
  hero) — "The image component from Nex.js doesn't change the height or width of the image.
  What they expect you to provide here is the native height and width in pixels" (44:23:24–44:23:33),
  unlike `<img>`, where the attributes *set* the rendered size.
- What you get: automatic resizing, "converting the image file itself to a [modern format]
  that is designed specifically for images on the web" (44:24:19–44:24:30), **lazy loading**
  ("the image will only begin to load once that image is [near the viewport]" — 44:24:34, with
  the image-heavy-page scenario spelled out), and placeholder handling while images load
  (44:25:06).

### Link and client-side navigation (44:31:25–44:39:00)

- `import Link from "next/link"` and replace anchors (44:33:21–44:33:30).
- **Why**: "when you use the link component, it enables client-side [navigation]… [the
  browser doesn't request the] server in order to get the content for [the next page]"
  (44:33:52–44:34:03) — no full-page refresh (44:35:12).
- **Prefetching**: "whenever that link is in view on the web [page, the content is
  prefetched]… so when the user actually clicks that link, it [loads instantly]… although [you
  can turn that off with the] prefetch prop set to false" (44:34:10–44:34:40).
- The challenge: swap the navbar's `<div>`s for Links — Home, About, and a "3D models" link to
  `/3d-models` (44:36:07–44:38:09).

### Server vs client components (44:42:40–44:50:17)

The framing is candid: "This is not [an easy topic]… [it has everything] to do with how we
fetch data in Nex.js" (44:42:51).

- **Client components**: "code… is only ever run in the browser… React will first mount the
  component to the page and then initiate any fetch requests you have" (44:43:16–44:43:35) —
  so a slow API means the user lands on a page "but won't be looking at any of the data they
  were expecting to see" (44:43:46).
- **Server components**: "the code is run on the server… it can perform any data fetching
  before it [sends anything to the] client… we can simply await the data and then use [it]…
  our React component will include the data that we fetched" (44:44:22–44:45:09).
- The old pattern is shown for contrast: "in client-side React [I] would need [state] to hold
  the data… add a use effect to fetch the data… once the data comes back, I would rerender
  the component" (44:45:34–44:45:45) — the Module 15 way.
- **The models list page** (44:50:17–44:53): a `/3d-models` folder + page, calling
  `getAllModels()` — "get all models is an async [function]… We'll await it" — mapping the
  result with `key={model.id}` from `models.json`, importing a TypeScript `Model` type
  (44:51:58–44:52:35). A server component, no `useEffect` in sight.

### Dynamic routes and the model detail page (44:53:26–45:04:00)

- Introduced with a **blog posts** analogy: "in true list page fashion, it [links each item
  to] a detail page… either the ID of the blog post… [or] these days they'll have some kind of
  slug" (44:53:48–44:54:13).
- **The square-bracket folder**: "to create a dynamic route in Nex.js, you need to surround
  that folder name that you chose with square brackets. So if you chose ID… it should be
  square brackets [id]" (44:56:29–44:56:40) — nested inside `/posts`, with a `page` file.
- Why: "it very obviously wouldn't be [smart]… [to create a] folder for each one of our blog
  posts. By adding a folder called one, a folder [called two]… [that's] not super dynamic"
  (44:58:17–44:58:44).
- **The params prop**: "in order to get dynamic information about [the route, we] can use the
  params prop on our dynamic [page]" (44:58:52–44:59:00) — `const { id } = await params`
  (45:00:13), and the folder's name decides the key: "If I called this square brackets slug,
  then this params object would have [a] property called slug instead of ID" (45:02:30–45:02:35).
- **Model detail page**: the models page's cards become Links (45:03:15–45:03:41), and the
  detail page resolves the id to a single model.

## Section 02 — Rendering Strategies and More

### Categories page and nav bar (45:15:00–45:23:00)

- The categories live at `/3d-models/categories` (45:15:38), driven by `categories.json` /
  `categories.ts` (45:15:49, 45:16:34), with a dynamic `[category]` folder — `/categories/art`
  (45:20:00) — below it.
- The **categories nav bar** is "sort of a subnavigation bar… Because we have the full site
  navigation up here on the top" (45:22:36–45:22:39), designed against Figma.

### Active links, `use client`, and the client boundary (45:33:00–46:14:00)

- **Active link styling**: the Figma "shows these kind of active [states]" (45:33:14); a
  component compares the current URL to each link's href and conditionally applies the active
  class — extended to the main navbar too (45:39:42).
- **`use client`**: making a component interactive "can be done very simply with the use
  client directive… it designates [the file as a client component]" — placed at the top of
  the file (45:37:03–45:37:19). The term is unpacked: "that's called a directive in
  JavaScript" (45:47:54), with a pointer to the React docs and the note that "Nex.js has been
  using client components with use client for a bit longer than React" (45:48:34).
- **Components are server components by default** in the App Router (45:49:27), and
  interactivity is the trigger for opting out: components with "an onclick or an onsubmit…
  [need to be client components]" (46:08:36).
- **The client boundary rule, taught explicitly**: "components… automatically get turned into
  client components [if] they are imported and rendered by [a client component]" (46:01:31–46:02:23)
  — so the discipline is to keep client components leaf-small and "keep as much of our app
  rendering on [the server]" (46:08:44). The refactor pulls interactivity into a small child
  (46:05:29–46:07:32).
- **`usePathname` from `next/navigation`** powers the active-link check (46:12:16), and the
  categories navigation is extracted into its own component (46:10:10).

### Category pages (46:14:42–46:20:00)

`getModels` (renamed from `getAllModels`) now "optionally takes a parameter of an object which
could have a category property… if you provided a category… it will [filter] that category"
(46:15:17–46:15:38) — remembering that "in models.json, category is actually the slug of the
category" (46:15:40). The `[category]` page renders the filtered models grid instead of just
the category name (46:16:40–46:17:03).

### Rendering strategies (46:20:01–46:43:00)

> "…the rest of this section… has to do with different rendering strategies that [Next.js
> provides]" (46:20:01–46:20:16)

All three, by name and when each renders (46:24:46–46:26:57):

| Strategy | When it renders | Use case taught |
|---|---|---|
| **SSG** — static site generation | "rendered just one time at build [time]" | content that's the same for everyone (a blog post) |
| **ISR** — incremental static regeneration | "rendered once at [build time, but] parts of a page can be regenerated after [an interval]" | "information [that needs] to periodically update" |
| **SSR** — server-side rendering / dynamic | "rendered on every [request]" | data per-user or "speak[ing] to a database to get the most updated information" |

- All three render on the server — "same for all of these" (46:25:40).
- Choosing is practical: the blog example ("the same page for person A… [as] for person B"
  — 46:28:12) vs. fresh-data needs (46:29:32–46:32:10).
- **Fetch options drive the choice** (46:34:01–46:37:10): `next: { revalidate: N }` ("refetch
  the data… Refetching every 60 seconds" — 46:35:41) for ISR, and `cache: "no-store"` ("you
  pass a second parameter of cache no[-store]" — 46:35:50) for dynamic rendering — because
  "when you're doing a fetch request, Nex.js [extends] the native fetch function to include
  [these options]" (46:47:57–46:48:01).

### Cat Facts — SSG practice (46:37:10–46:58:00)

A deliberately separate practice project:

- **Part 1** (46:43:13): "use the fetch API or the fetch function to fetch a random [cat
  fact]" — in a server component, "make sure to await that fetch" (44:44:29→46:44:29).
- **Reading the dev server output** (46:37:47–46:42:08): the route table `next dev` prints,
  and the little circle icon "means that it was server [rendered]" (46:42:08).
- **Add fetch / caching variants**: the default caches ("fetched one time when the app is
  built" — 46:48:19); the `no-store` version refetches "each time because the fetch request
  is [not cached]" (46:50:43).
- **Structured play** (46:57:01–46:58:27): the endpoint switches to one returning "an array
  of the first 10 facts… And we are mapping over those and displaying them on the page" —
  then a **form challenge**: "add a form element below the H1… a single input element. Make
  sure to give it a type of text and to give it a name property, which you can set to
  something like search or query… If you'd like to practice your accessibility chops… put a
  label… Make sure that they're connected" (46:58:40–46:59:05).

### Form submissions are navigation events (47:00:40–47:13:56)

The section's best insight, discovered live:

- Submitting the search form "did a full page refresh… We see we have question mark search
  equals food. This is something that was automatically added to the URL by our browser"
  (47:00:56–47:01:23).
- **The input's `name` is the query-string key**: "The word search… came from the name of the
  input that we submitted with our form. If we change this to something like query… it says
  query equals food. So that name property is actually quite important" (47:01:53–47:02:16).
- **The insight**: "when you submit a form, it's actually performing a navigation event on
  your site… It's the same path but with the query string included and Nex.js, because of
  that navigation event, is going to re-evaluate the code that we have for the component of
  this page" (47:02:20–47:03:19).
- **Why it matters**: shareable URLs — "take this URL and share it with a friend… When they
  visit the URL, we're going to write our code in a way that it will automatically filter the
  results based on the search term that's up in the URL" (47:02:44–47:02:59).
- **`searchParams`**: page components "can optionally receive this search params property…
  the search params prop is a promise, you [must await it]" (47:04:18–47:04:26) —
  `await searchParams` yields `{ search: "food" }`, and the Cat Facts list is filtered with
  `.filter()` (47:08:43–47:11:21).
- Finishing touches, each taught: the **`sr-only`** class ("screen reader only… completely
  removed from what's actually visible… but still allows the item to exist in the DOM so
  screen readers can access it" — 47:12:30–47:12:53), `autocomplete="off"` (47:13:05), and
  `defaultValue` seeded from the query so shared URLs show their search (47:13:20–47:13:41).

### PrintForge search bar, native form first (47:13:58–47:20:00)

The three-part challenge: "add a form with an input here above the models grid… get access to
the query string that will come through search params… then I want you to filter down the
models that are being passed to models grid" (47:14:00–47:14:37) — with an optional
`ModelsPageProps` type "to satisfy TypeScript" (47:14:26). The result filters models "that
have a name or description with the word [searched]" — exactly the goal stated at 46:57:40.

### Next's `<Form>` component (47:23:11–47:28:00)

The upgrade from the native form: same markup, capital-F `<Form>`, and client-side navigation
without the full-page refresh — "just like that, immediately we got the filtered down list…
celebrate these little wins that we get with using this capital F form" (47:26:47–47:27:03).
And the concept it carries:

> "This form component uses something called **progressive enhancement**… if the user were
> ever to find themselves without access to JavaScript — either the JavaScript failed to load…
> maybe they have a really slow internet connection… or maybe even they have a browser
> extension or browser setting that has turned off JavaScript altogether — this capital F
> form will automatically downgrade itself to the native HTML form element and it will act
> exactly the way that it was before we made this upgrade." (47:27:06–47:27:41)

### The outro (47:28:04–47:29:18)

> "…we have covered adding the categories, navbar, and the pages to our Print Forge project.
> We've learned about use path name and… active link styling… We've learned a little bit more
> about client components and how we can turn any component into a client component with the
> use client directive that you place at the top of the file. Then we did a bit of a deep dive
> into rendering strategies… static rendering, dynamic rendering, and… incremental static
> regeneration. Boy, that is a mouthful. Then here at the end of this section, we started
> using forms, search params, and combined these together so that we could add a search
> feature to Printforge… Good luck and happy coding."

This is the **end of the entire transcript** — nothing follows for Module 20.

## What this module teaches

1. Creating a Next.js app manually (next, react, react-dom) and via create-next-app.
2. `npm run dev` / `next dev`, and reading the dev server's route table.
3. The app folder: `layout` + `page`, and the root layout as the `index.html` replacement.
4. File-based routing: folders become URL segments; `page.jsx` must be lowercase.
5. Nested routes (`/about/mission`) and nested layouts, as deep as needed.
6. Layouts and the `children` prop; shared header/nav/footer in the root layout.
7. `next/font` for fonts; `next/image` with required native width/height, lazy loading, and
   modern format conversion.
8. `next/link`: client-side navigation, prefetching, `prefetch={false}`.
9. Server vs client components: fetch-before-send vs mount-then-fetch; server by default.
10. Dynamic routes: `[id]` folders, the awaited `params` prop, folder-name-as-key.
11. `use client` directive and the client boundary (imported-by-client ⇒ client); keeping the
    client surface small.
12. `usePathname` for active link styling.
13. Rendering strategies — SSG, ISR, SSR — and how fetch options (`next.revalidate`,
    `cache: "no-store"`) select them.
14. Forms as navigation events; `name` → query-string key; `searchParams` (awaited) for
    reading it; shareable filtered URLs.
15. Accessibility carried through: labels, `sr-only`, and the `<Form>` component's progressive
    enhancement as the final lesson of the whole path.

## Small practice task

Build a mini "PrintForge" of your own for a domain you like (books, plants, bikes…):

1. Manual setup: install next/react/react-dom, add the dev script, create `app/layout.jsx`
   and `app/page.jsx` from scratch — no create-next-app.
2. Add an about page and a nested `about/team` route.
3. Put a shared header (three links) and footer in the root layout; use `next/image` for a
   hero image with its true pixel dimensions.
4. Create a `/items` server-component page that reads a local `items.json`, awaits the data,
   and maps cards with `Link` to `/items/[id]` detail pages.
5. Style the active nav link with a small `use client` + `usePathname` component — and keep
   everything else a server component.
6. Add a `[category]` route that filters items, then a search form: native `<form>` +
   `name="query"` input, await `searchParams`, filter by name/description, and seed the input
   with `defaultValue`. Finish by swapping to Next's `<Form>`.

## Readiness check for Module 20

Module 20 (Career Essentials) has **no transcript coverage** — the video ends with this
course's sign-off at 47:29:18. Before moving on, be able to:

- Explain what renders where: server vs client components, and what `use client` opts into.
- Create a page, a nested route, a dynamic route, and a layout — and say what `children` is.
- Pick a rendering strategy (SSG/ISR/SSR) for a given page and configure it via fetch options.
- Explain why a submitted form changes the URL and how the page reads that query.

## Exact syllabus order

1. **Build a Next.js App**
   1. 02. Challenge- create a new Next.js app from scratch
   2. 03. Adding a new page to our site
   3. 04. File-based routing in Next.js
   4. 07. Scrimba_s _Runner_
   5. 10. Challenge - PrintForge Home Page
   6. 11. Challenge - PrintForge About Page
   7. 12. Nested Routes — Exercises 1–2
   8. 14. Layouts part 2
   9. 15. Challenge - Add Header to PrintForge
   10. 17. Optimizing Images
   11. 19. Challenge - Add Links to Navbar
   12. 22. Challenge - Create the Models List Page
   13. 23. Dynamic Routes — Exercises 1–2
   14. 24. Model Detail Page
2. **Rendering Strategies and More**
   1. 02. Challenge- add categories page
   2. 03. Add categories Nav Bar — Exercises 1–2
   3. 06. More about client components
   4. 07. Challenge- Style Active Link
   5. 09. Challenge- Style Categories Link
   6. 10. Challenge- Category Pages
   7. 14. Cat Facts - SSG Pt. 1 — Exercises 1–2
   8. 15. Cat Facts - Add Fetch — Exercises 1–2
   9. 16. CatFacts- Structured Play
   10. 17. HTML Form Submissions are Navigation Events — Exercises 1–2
   11. 20. PrintForge - Search Bar using native form
   12. 22. PrintForge - Upgrade to Next_s Form Component
