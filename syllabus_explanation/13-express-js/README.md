# Module 13: Express.js

## Completion status

**Not covered by the transcript. Express.js is never installed, imported, or used anywhere in
the 47.5 hours — and the omission is deliberate, stated, and twice explained.**

This is not a silent gap. The Node course (Module 11) that occupies the corresponding place in
the video addresses it head-on at 21:24:

> "Why is it good to learn NodeJS? Because **the elephant in the room here is that Express.js
> exists.** It's a very popular framework which wraps Node.js. Why not learn that instead? Well,
> when you understand how Node.js works at its core, you become a more versatile developer and
> that makes learning frameworks easier. And it's always good to be framework independent…
> After all, Express is not the only node framework out there. There's Nest.js and Fastify to
> name but two. Imagine as a front-end equivalent, imagine knowing jQuery without knowing
> JavaScript."

And again, at 22:23, immediately after hand-parsing query parameters with the `URL` constructor
— "It's overly complex with horrible verbose code":

> "Well, the good news is that the Express framework abstracts this away and makes it really,
> [simple]."

Verified absences across the whole transcript:

| Search term | Matches |
|---|---|
| `npm install express` / "require express" / `import express` | 0 |
| `app.get` / `app.listen` / `app.use` (Express's API surface) | 0 |
| "express-session" / "middleware" | 0 |
| "bcrypt" / "hash the password" / "jsonwebtoken" / "JWT" | 0 |
| "cart" (as a shopping cart) | passing uses only — "ability to add items to your cart" (31:07) and "abandon my cart" (37:35) are UI talk inside other courses |
| register/login routes, users table, seed table | 0 |

## What the transcript teaches instead — the bridge table

The crucial fact for a learner using this transcript: **Modules 11 and 13 are the same two
projects, built twice — once with plain Node (in the video), once with Express (in the challenge
files).** The lesson names are near-identical. Every skill in Sections 01 and 02 below *was*
taught, just without the framework:

| Module 13 lesson (Express) | Taught in the transcript as (Module 11) | Time |
|---|---|---|
| 01. Setting Things Up | `npm init`, package.json, `npm start` | 21:30 |
| 02. A Basic Server | `http.createServer`, `res.end`, `server.listen` | 21:33 |
| 04. Serving Data | mock DB + `JSON.stringify` + `Content-Type` | 21:54 |
| 06. Filtering by Query Params | `new URL(…)`, `searchParams.get()`, filtering | 22:21 |
| 07–09. Path Parameters 1 & 2 | `/api/country/:value` handled by hand from `req.url` | 22:00–22:21 |
| 11. Modularise The Code | handlers moved into modules; grouped imports | 22:06, 23:15 |
| 12. Route Not Found | manual 404 status + message | 22:00 |
| 02-03. Serve the Frontend Files | `public/`, fs `readFile`, per-extension Content-Type | 23:15–23:42 |
| 02-04. Setting up the Routes | route-handler patterns and refactors | 23:15–23:30 |
| 02-06. Setting up the Database | JSON file read through fs (the "mock database" is replaced by a file) | 23:45–24:00 |
| 02-09. seedTable.js | no direct equivalent — the sightings data ships pre-seeded | — |
| 02-11–13. Populate the Dropdown / Getting All Products / Wire Up the Dropdown | the frontend fetches the API it is served from; dropdown wired in vanilla JS | 22:45–23:00 |
| 02-14. Add Search Functionality | query-parameter filtering on the server + frontend fetch | 22:21–22:42 |

**The mechanical translation** the video never shows but the above implies:

```js
// Node, as taught (Module 11)          // Express, as the challenge files expect
const server = http.createServer(cb)     const app = express()
server.listen(8000)                     app.listen(8000)
if (req.url === "/api") { … }           app.get("/api", (req, res) => { … })
res.statusCode = 404                    res.status(404)
res.setHeader("Content-Type", …)        res.type(…) / res.json(…)
url.searchParams.get("x")               req.query.x
"/api/country/" + name from req.url     req.params.country
```

Learning Express after Module 11 is mostly learning that translation table — which is exactly
the "you become a more versatile developer" argument the instructor makes at 21:24.

## Section 03 — Authentication *(absent, and explicitly deferred)*

The third section (users table, register route, validation, hashing, `express-session`, login,
logout, cart tables and routes) has no transcript segment anywhere. The only thing the
transcript says about the topic is a warning, when the Node course lists stretch goals:

> "You could try handling post requests. We haven't talked about that at all. We are going to
> talk about it in future projects. But you could allow a user to upload some data to our API.
> If you do do that, I suggest that for now you just ignore authentication, because that is a
> pretty big topic." (22:42)

The neighbouring coverage that *does* exist, for context:

- **POST bodies** are handled thoroughly (parseJSONBody, buffering streams, sanitize-html) —
  Module 11, 24:03–24:33.
- **Passwords are never hashed** anywhere in the path; `localStorage` (Module 03) is the only
  persistence a username ever sees, and the HTML/CSS course even notes passwords "are always
  masked" as a UI behaviour (00:27).
- **Sessions** appear only as Scrimba's own login flow being described ("you can authenticate
  with Gmail, LinkedIn or…" — 21:17, in the AI course) — never implemented.
- The **cart** concept appears only as UI commentary inside other courses (31:07, 37:35).

## Where to get the missing material

**Sections 01–02:** you already have the skills from Module 11's transcript — what you are
missing is the Express API surface itself (`express()`, routing methods, `req.params`/
`req.query`, `res.json`, `express.static`, `express.Router`). A focused plan:

1. `npm install express`, create the app, `app.listen` — map each line to Module 11's
   `createServer` version.
2. Rebuild Wild Horizons (Module 11's project) with `app.get("/api")`,
   `app.get("/api/country/:country")`, and `req.query` — you have the data and the tests.
3. Serve the spooky-site frontend with `express.static("public")` instead of the fs loop.
4. Re-add POST with `app.use(express.json())` replacing your `parseJSONBody` — keep
   `sanitize-html`.

**Section 03 (authentication):** genuinely new territory with no transcript support at all.
Its lesson names give the build order, and it is a well-trodden tutorial sequence: users table
(extend Module 12's `CREATE TABLE` gap), register route, validation, **hash passwords with
bcrypt** (never store what Module 03 stored in localStorage), `express-session`, login/logout,
then the cart tables and routes. Treat it as the most security-sensitive part of the entire
path, and the part where following a current, dedicated source matters most.

## Small practice task

Prove the bridge table to yourself:

1. Take your Module 11 practice API (campus events) — or rebuild it from that README's task.
2. Install Express and port it: every `if (req.url === …)` becomes a route; every manual
   `searchParams` read becomes `req.query`; every path-parameter parse becomes `req.params`.
3. Keep both versions side by side for one afternoon. Every time Express does something in one
   line, find the Node code it replaced and write a comment naming it (e.g. `// this was my
   parseJSONBody`).
4. Add one route you *haven't* built before — `app.delete("/api/:id")` — first in Node, then in
   Express. Notice which version taught you more.
5. Do not attempt Section 03's auth flow without a current guide; instead, write the SQL for a
   `users` table (id, username, password_hash, created_at) and explain out loud why the column
   is called `password_hash` and not `password`.

## Readiness check for Module 14

Module 14 (UI design) is also a transcript gap, so there is nothing here that it depends on.
Before moving on, be able to:

- Write the Node server and the Express server for the same three-endpoint API from memory.
- Say what `express.json()` middleware replaces, and what `express.static` replaces.
- Explain why `req.params` is trusted only after validation, given what Module 11 taught about
  sanitizing user input.
- State clearly that this path's transcript never covered authentication, sessions, or password
  hashing — and that these must be learned elsewhere before building anything real.

## Exact syllabus order

1. **Build an Express API** *(no transcript coverage — Node equivalents at 21:24–22:42, see the
   bridge table)*
   1. 01. Setting Things Up — Exercises 1–2
   2. 02. A Basic Server
   3. 04. Serving Data
   4. 06. Filtering by Query Params
   5. 07. Aside- Path Parameters
   6. 08. Add Path Parameters 1
   7. 09. Path Parameters 2
   8. 11. Modularise The Code
   9. 12. Route Not Found
2. **Build a Fullstack Express App** *(no transcript coverage — Node equivalents at 22:43–24:54)*
   1. 03. Serve the Frontend Files
   2. 04. Setting up the Routes
   3. 06. Setting up the Database
   4. 09. seedTable.js
   5. 11. Populate the Dropdown
   6. 12. Getting All Products
   7. 13. Wire Up the Dropdown
   8. 14. Add Search Functionality
3. **Authentication** *(no transcript coverage anywhere in the path)*
   1. 02. Create a users table
   2. 03. The _register Route
   3. 05. Validate the User
   4. 06. Add user to DB
   5. 09. Hash the password
   6. 11. Add express-session
   7. 12. Display a User_s Name
   8. 13. Login
   9. 14. Add Logout Functionality
   10. 16. Adding to cart_table
   11. 17. The Cart Count
   12. 18. Cart Page Challenge 1
   13. 19. Cart Page Challenge 2
   14. 20. Cart Page Challenge 3
   15. 22. Projecting Cart Routes
