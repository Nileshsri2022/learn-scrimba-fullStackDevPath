# Module 13: Express.js

## Completion status

**Not covered by the transcript.** Despite being the backend framework the whole path builds toward,
Express.js is **never taught** in the 47-hour recording. It is *mentioned* three times, always in
passing and always to contrast it with the raw Node.js the course actually teaches. All three
sections of this module — the Express API, the full-stack Express app, and authentication — are a
**gap**.

> **Correction to earlier notes.** A previous audit (`STATUS.md`) estimated Express was "well
> covered, roughly 21:40–26:50." That was wrong. Reading that region line by line shows it is
> **Module 11 (Node.js)** from ~21:19–24:45 and **Module 12 (Databases)** from ~24:45–26:35, running
> straight into **Module 15 (React)** at ~26:35. There is no Express project anywhere between them.

## The verification

Every Express-specific construct returns **zero matches** across all 221,189 transcript lines:

| Search term | Matches |
|---|---|
| `express()` / `const app` / `app = express` | 0 |
| `app.get` / `app.use` / `app.listen` | 0 |
| `req.params` | 0 |
| `res.send` | 0 |
| `router` (as Express routing) | 0 — the only `router` hits are **React** Router |
| `middleware` | 0 |
| `npm install express` / `npm i express` | 0 |
| `express-session` | 0 |
| `bcrypt` / `hash` (password) | 0 |
| `passport` / `jwt` | 0 |

The word `res.json` appears, but only in **fetch/React** contexts (`await res.json()` on the client),
never as Express's `res.json()` response method.

### The three mentions that do exist

All three are asides that name Express to explain why you're learning something *else*:

1. **21:24 (Node.js intro).** Justifying learning raw Node first:
   > "The elephant in the room here is that Express.js exists. It's a very popular framework which
   > wraps Node.js. Why not learn that instead? Well, when you understand how Node.js works at its
   > core, you become a more versatile developer... After all, Express is not the only Node framework
   > out there. There's Nest.js and Fastify to name but two."

2. **22:23 (Node.js, query parameters).** After the verbose vanilla-Node `URL` + `Object.fromEntries`
   dance:
   > "The good news is that the Express framework abstracts this away and makes it really, really
   > simple. But in vanilla Node, this is what we have to do."

3. **40:13 (React outro).** Listing next steps:
   > "If you are interested in backend, you could go the direct backend route by learning Node.js
   > **with or without Express**, all to help you build REST APIs that your front-end React apps can
   > consume."

That is the entire Express footprint of the course.

## What the syllabus lists (and what it would cover)

The repository defines three sections for this module, none of which is in the transcript:

**01. Build an Express API** — the Express version of the Wild Horizons / Node API from Module 11.
It would replace the hand-rolled `http.createServer` + `req.url`/`req.method` routing with:

```js
import express from "express"
const app = express()

app.get("/api", (req, res) => res.json(destinations))
app.get("/api/country/:country", (req, res) => { /* req.params.country */ })
app.get("/api", (req, res) => { /* req.query for ?key=value */ })

app.listen(8000, () => console.log("Server running on port 8000"))
```

The listed lessons — *Serving Data*, *Filtering by Query Params*, *Path Parameters 1 & 2*,
*Modularise the Code* (Express `Router`), *Route Not Found* (a catch-all `app.use`) — are exactly the
things Module 11 does the hard way in raw Node. Express replaces them with `req.params`, `req.query`,
`res.json`, `express.Router()`, and a fallthrough 404 handler.

**02. Build a Fullstack Express App** — serving a front end with `express.static`, wiring routes to a
database (the SQL from Module 12), seeding a table (`seedTable.js`), populating a dropdown, fetching
all products, and adding search. This is the integration point where Modules 11, 12 and 13 were meant
to meet.

**03. Authentication** — the most consequential gap: a users table, a `/register` route, input
validation, storing users, **password hashing**, `express-session` for sessions, login/logout,
displaying the logged-in user's name, and a cart (add to cart, cart count, cart-page challenges,
protecting cart routes). None of authentication, sessions, or hashing appears anywhere in the
transcript (`bcrypt`, `express-session`, `passport`, `jwt` all return 0).

## Why this gap matters

Express is the hinge of the whole full-stack path: it is where the Node skills (Module 11), the SQL
skills (Module 12), and the React front end (Module 15) are supposed to come together into a real
authenticated application. Its absence means:

- there is no transcript-sourced example of a **middleware pipeline**, the concept that most
  distinguishes Express from raw Node;
- there is **no authentication material at all** — a topic the Node module explicitly defers
  ("if you do do that, I suggest that for now you just ignore authentication because that is a pretty
  big topic"), promising it for "future projects" that this transcript never reaches;
- Module 20 (Launching Your Career) assumes you can talk about building secure backends, and the
  honest answer from this transcript alone is that you built one **without** a framework and never
  handled auth.

## The closest substitute you *do* have

**Module 11 (Node.js) is the honest stand-in for Section 01 of this module.** Everything the Express
API section would teach — routing, path parameters, query parameters, modularising routes, a
not-found handler, serving static files, handling `POST`, CORS — Module 11 teaches from first
principles using the core `http` module. Once you understand *why* those pieces exist (which is the
Node module's whole argument for teaching raw Node first), Express is mostly a thinner syntax over the
same ideas.

For the parts with **no** substitute anywhere in the course — Express middleware, `express-session`,
password hashing, and the full auth/cart flow — you will need an external Express tutorial. The
official Express guide (expressjs.com) and any reputable course covering `express-session` + `bcrypt`
password hashing will fill Section 03.

## Mapping to the syllabus activities

| Section / lessons | Coverage | Nearest source |
|---|---|---|
| 01. Build an Express API (Setting up → Route Not Found) | **GAP** | Module 11 §01 does the same in raw Node |
| 02. Build a Fullstack Express App (static → search) | **GAP** | Module 11 §02 (static/POST) + Module 12 (SQL) |
| 03. Authentication (register → cart routes) | **GAP** | none — external material required |

The numbering gaps in the syllabus (Section 01 skips 03, 05, 10; Section 03 skips lessons) mark
further hosted lessons with no folder in the source repository — but since the whole module is absent
from the transcript, those gaps are moot here.

## What this module *would* teach (summary)

- Express as a framework that wraps Node's `http` module, reducing boilerplate.
- Routing with `app.get`/`app.post`, `req.params` for path params, `req.query` for query strings.
- `res.json`/`res.send` responses and a catch-all 404.
- Modular routing with `express.Router()` and serving static assets with `express.static`.
- Middleware — the request-processing pipeline central to Express.
- Full-stack integration: Express routes backed by a SQL database, feeding a front end.
- Authentication: registration, validation, **password hashing**, sessions with `express-session`,
  login/logout, and protected routes; plus a shopping-cart feature.

## Practice task (using the substitute material)

You can't practise Express from the transcript, but you can practise the concepts it wraps:

1. Take the Wild Horizons raw-Node API from **Module 11** and re-implement one route
   (`/api/continent/:name`) — first note how much code `req.url.split("/").pop()` +
   `startsWith` requires, then look up how Express's `:name` path parameter replaces it.
2. Do the same for query-string filtering: compare Module 11's `new URL(...)` +
   `Object.fromEntries` block with Express's `req.query` one-liner.

This makes concrete the exact abstraction the two transcript mentions are pointing at.

## Readiness check for the next module

Because this module is a gap, the real readiness bar is the **Node.js** module's: you should be able
to route by hand, handle `POST`, serve static files, and write the SQL from **Databases**. If you
want genuine Express (especially authentication) before continuing, complete an external Express +
`express-session` + password-hashing tutorial and treat this file as the map of what to look for.

---

## Ordered syllabus

MODULE 13. Express.js
========================================================================
Learning focus: Express APIs, full-stack integration, authentication, authorization, and backend application practices.
  SECTION / UNIT: 01. Build an Express API
    LESSON / ACTIVITY: 01. Setting Things Up
      PRACTICE: Exercise 1
      PRACTICE: Exercise 2
    LESSON / ACTIVITY: 02. A Basic Server
    LESSON / ACTIVITY: 04. Serving Data
    LESSON / ACTIVITY: 06. Filtering by Query Params
    LESSON / ACTIVITY: 07. Aside- Path Parameters
    LESSON / ACTIVITY: 08. Add Path Parameters 1
    LESSON / ACTIVITY: 09. Path Parameters 2
    LESSON / ACTIVITY: 11. Modularise The Code
    LESSON / ACTIVITY: 12. Route Not Found
  SECTION / UNIT: 02. Build a Fullstack Express App
    LESSON / ACTIVITY: 03. Serve the Frontend Files
    LESSON / ACTIVITY: 04. Setting up the Routes
    LESSON / ACTIVITY: 06. Setting up the Database
    LESSON / ACTIVITY: 09. seedTable.js
    LESSON / ACTIVITY: 11. Populate the Dropdown
    LESSON / ACTIVITY: 12. Getting All Products
    LESSON / ACTIVITY: 13. Wire Up the Dropdown
    LESSON / ACTIVITY: 14. Add Search Functionality
  SECTION / UNIT: 03. Authentication
    LESSON / ACTIVITY: 02. Create a users table
    LESSON / ACTIVITY: 03. The _register Route
    LESSON / ACTIVITY: 05. Validate the User
    LESSON / ACTIVITY: 06. Add user to DB
    LESSON / ACTIVITY: 09. Hash the password
    LESSON / ACTIVITY: 11. Add express-session
    LESSON / ACTIVITY: 12. Display a User_s Name
    LESSON / ACTIVITY: 13. Login
    LESSON / ACTIVITY: 14. Add Logout Functionality
    LESSON / ACTIVITY: 16. Adding to cart_table
    LESSON / ACTIVITY: 17. The Cart Count
    LESSON / ACTIVITY: 18. Cart Page Challenge 1
    LESSON / ACTIVITY: 19. Cart Page Challenge 2
    LESSON / ACTIVITY: 20. Cart Page Challenge 3
    LESSON / ACTIVITY: 22. Projecting Cart Routes

========================================================================
