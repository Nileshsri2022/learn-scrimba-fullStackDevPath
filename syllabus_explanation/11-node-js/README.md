# Module 11: Node.js

## Completion status

**Complete for the supplied source files.** Both syllabus sections are covered by one continuous
course (21:21–24:54) taught by **Tom Chant** ("I've been working at Scrimba since 2021"), built
around two projects that match the challenge files:

1. **The Wild Horizons API** — a REST-ish travel-destinations API built with Node's core `http`
   module (Section 01).
2. **A paranormal-sightings site** — a full-stack app that serves its own frontend, accepts POSTs,
   sanitizes input, wires in an event emitter, and ends with a server-sent-events news feed
   (Section 02).

One framing decision by the instructor shapes the whole module and explains why Module 13 looks
the way it does — he teaches **Node without any framework, on purpose** (see the quote at
21:24 in "How the sources relate" below, and Module 13's README for the consequences).

## How the sources relate

The course opens with why Node exists at all:

> "JavaScript works in the browser because browsers have JavaScript engines like Chrome's V8…
> that all changed with Node.js. The V8 engine from Chrome is bundled in with Node. And it's that
> which enables us to run JavaScript outside the browser… NodeJS is not a language. It is an
> environment in which we can write JavaScript."

Prerequisites are stated honestly: "I'm assuming a solid foundation in JavaScript… map, reduce,
and filter and you've made a fetch request and worked with async or await… It doesn't matter if
you don't know any frameworks like React."

And the Express question is answered before it's asked:

> "Why is it good to learn NodeJS? Because the elephant in the room here is that Express.js
> exists. It's a very popular framework which wraps Node.js. Why not learn that instead? Well,
> when you understand how Node.js works at its core, you become a more versatile developer and
> that makes learning frameworks easier… there's Nest.js and Fastify to name but two. Imagine as
> a front-end equivalent, imagine knowing jQuery without knowing JavaScript."

### Transcript map

| Transcript time | Content | Syllabus section |
|---|---|---|
| 21:21–21:30 | Why Node; the two projects; requirements | — |
| 21:30–21:33 | `npm init`, package.json, `npm start` | 01, lesson 02 |
| 21:33–21:45 | `http.createServer`, ports, `listen`; recreate-the-server challenge | 01, lesson 04 |
| 21:45–21:54 | Routing by URL and method; the request object | 01, lesson 07 |
| 21:54–22:00 | The mock database; serving `JSON.stringify`-ed data | 01, lessons 09–10 |
| 22:00–22:21 | 404s, path parameters, refactoring into modules | 01, lessons 11–14 |
| 22:21–22:42 | Query parameters and filtering; status codes; stretch goals | 01, lessons 16–17 |
| 22:43–23:15 | Full-stack app: setup, `__dirname`/`import.meta`, serving files | 02, lessons 02–11 |
| 23:15–24:00 | Route-handler patterns; CommonJS vs ES modules; content types | 02, lessons 03–13 |
| 24:00–24:42 | POST handling, `parseJSONBody`, `sanitize-html`, event emitter | 02, lessons 14–22 |
| 24:42–24:54 | Server-sent events (live temperature, then the ghost news feed) | 02, lesson 24 |

---

## Section 01 — Build a Node API (21:24–22:43)

### The project: Wild Horizons (21:24)

> "It's a one-stop shop for fun facts about some of the world's most intriguing travel
> destinations… the dragon blood trees of Socotra or… the doorway to hell in Turkmenistan."

The data model is described field by field: each destination has `name`, `location`, `country`,
`continent`, a boolean `isOpenToPublic`, a `details` array, "and of course each one has a uid, a
unique identifier." Three access patterns are promised up front, and they are exactly the
syllabus's three lessons:

- `/api` — the whole dataset;
- `/api/country/India`, `/api/continent/Asia` — **path parameters**;
- `?country=Turkey&isOpenToPublic=true` — **query parameters** "for more complex filtering."

The topic list is explicit: "We are going to get to know Node's core HTTP module. We'll be
creating a server, sending status codes like 200, 400, and 404. We'll be setting headers,
handling requests and responses, filtering data, and extracting query params."

### The package.json file (21:30)

`npm init` ("init stands for initialize") launches the interactive utility that writes
package.json for you — name (`wild-horizons`), version, description, entry point
(`server.js`), license. Two lessons inside the lesson:

- "Package.json is just a JSON file. So we could create a new file… and manually type one by
  hand. But luckily Node gives us a tool."
- The **start script**: "This automates the task of actually running the app" — instead of
  `node server.js`, you run `npm start`, and anyone opening the project can find the entry point
  without searching: "we shouldn't have to search around for the entry point to our app. We
  should list it in package.json."

### A basic server, then recreate it (21:33–21:45)

The first server, taught method by method:

```js
import http from "http"

const server = http.createServer((req, res) => {
  res.end("Hello from the server")
})

server.listen(8000, () => console.log("Server running on port 8000"))
```

- `createServer` takes a callback that runs for **every** request, receiving the `req` and `res`
  objects — "it's these request and response objects that give us access to the request and
  response cycle."
- `res.end` "sends data over HTTP and then ends the response."
- `listen(8000, callback)` binds the port; the callback fires when the server connects.
- Testing uses Scrimba's **network tool** with the full URL — `http://localhost:8000`.

The challenge is to **rebuild it from scratch** ("I have maliciously deleted it"), with
`hint.md` prompts that "are pretty much pseudo code" — the course's recurring
read-the-pseudocode-then-write-it teaching style.

### Routing and the req object (21:45–21:54)

Routing before frameworks means reading `req` yourself:

- `req.url` — the path (and query string) the client asked for;
- `req.method` — "the request object has got a method property which will give us that info."

The first router is an `if`/`else` chain over URL and method — deliberately low-level, because
Express's `app.get()` is later revealed to be sugar over exactly this.

### The mock database, and serving data (21:54–22:00)

A candid design note:

> "In the real world, you would likely be holding the data for your API either in a database or…
> as JSON data within the app. That presented me with two issues. Firstly, we're not ready to go
> down the database rabbit hole yet. And secondly, if we store raw JSON, then we have to use
> Node's file system module to read it."

The compromise is a **mock database**: the data lives in `data.js` as a plain array, behind an
`async` function in `db.js` — "that just adds a little more realism so you can get into the
async mindset, because accessing a database is an async process."

Serving it teaches the module's most important single fact: "even though our data is stored here
as a regular JavaScript array of objects, we are still serving it as a JSON string. Remember, the
HTTP protocol demands we send a string, not an array of objects. So, using JSON.stringify is
definitely the way to go." The challenge plants the classic async bug on purpose: the empty
object you get back is fixed by `await`ing the mock-DB function (21:57).

Content-Type arrives next (23:36 in the second project, but the principle is stated here):
without `res.setHeader("Content-Type", "application/json")`, clients receive a string they may
not treat as JSON.

### Route not found, path parameters, modularising (22:00–22:21)

- Unknown routes get a **404 status** and a message — "we do not want any further code to
  [run]" once a route has matched.
- Path parameters are extracted by splitting or matching the URL: `/api/country/:value` → look
  up every destination whose `country` matches the value (the "biscuits on the price list" of
  this module: `/api/country/Nowhere` returns an empty array, which motivates the *gentler error
  handling* stretch goal at 22:42).
- **Modularise the code**: routing logic moves out of `server.js` into handler modules, imported
  with ES module syntax. The instructor's rule: "more important than clever, complex, but
  shorter code" — readable refactors beat golfed ones.

### Query parameters and filtering (22:21–22:42)

Query strings are parsed with the **`URL` constructor** ("the constructor needs the base URL as
well"), giving `url.searchParams` and its `.get()`/`.has()` methods. The filter challenge
combines them: match `continent`, then keep only destinations where `isOpenToPublic` is true —
and note the type lesson: query values are **strings**, so `"true"` must be compared or
converted deliberately (22:36).

Section 01 closes with stretch goals that read like a syllabus for the next section: gentler
error handling, "you could try handling post requests. We haven't talked about that at all…
I suggest that for now you just ignore authentication because that is a pretty big topic," and a
keyword search of the `details` property.

---

## Section 02 — Build a Fullstack Node App (22:43–24:54)

### The project: paranormal sightings (22:43)

> "We're going to expand on what we learned in the previous project as we build from the other
> side, a site where users can share paranormal sightings."

Now the server is on both sides: it serves the frontend files *and* processes data.

### Getting the path to resources, and `__dirname` (22:51–23:15)

Serving `index.html` needs its **file path on disk**, and relative paths break depending on
where the process runs — "worse still there won't be an error. We're just going to get some
unexpected [result]." The fix:

- `import.meta.url` — "let's see what we can find out about it with import.meta" — the current
  module's URL in ES modules;
- converted to a directory path with the **`URL` module** (`fileURLToPath`) plus `pathname` —
  the modern replacement for CommonJS's `__dirname`, and the reason for the aside on
  "the difference between Common JavaScript and ES modules" (23:27).

### Serving the frontend (23:15–23:42)

A `public/` folder holds the frontend; every non-API request is mapped to a file inside it:

- read the file with the **fs module** (`fs.readFile`);
- set the right `Content-Type` per extension — the debugging story is that "everything is
  working apart from the CSS" until the header says `text/css`;
- serve `index.html` for `/`, and the mini browser finally shows the real site.

### Route-handler patterns and modularisation (23:15–23:30)

The refactor pass names its patterns: separate files for handlers, grouped imports ("we don't
need three import statements"), small functions with one job, and no clever one-liners — the
same engineering values Module 04's Git section teaches for collaboration, applied to code.

### Wiring up the API, JSON data, and POST (23:45–24:33)

- The sightings data lives in a JSON file read through fs — the promise from 21:54 ("we will
  definitely be covering [the file system module] in a later project") kept.
- **Adding POST** (24:03): the explainer separates concerns — collect the raw body, parse it,
  validate it, store it, respond:
  - `parseJSONBody` (24:30): request bodies arrive as **streams**; the handler buffers chunks
    together and `JSON.parse`s the result;
  - the response for a created resource: "received your post request. We've got your new
    resource. Here's your status [code]";
  - **`sanitizeInput`** (24:21): user-submitted HTML is dangerous, so the app installs a real
    npm package — "it's npm install sanitize[-html]" — the first third-party dependency of the
    path, and a natural callback to Module 04's package-management talk.

### Add an event emitter (24:33–24:42)

Node's `EventEmitter` decouples "something happened" from "who cares":

```js
import EventEmitter from "events"
const emitter = new EventEmitter()
emitter.emit("sighting-added", newSighting)
```

"This is where we're actually going to emit the event" — and listeners elsewhere react, the
observer pattern in its native Node habitat.

### Server-sent events challenge (24:42–24:54)

The finale, taught in two steps. First a toy: a live temperature endpoint —

```js
res.statusCode = 200
res.setHeader("Content-Type", "text/event-stream")
res.setHeader("Cache-Control", "no-cache")
res.setHeader("Connection", "keep-alive")

setInterval(() => {
  res.write(`data: ${JSON.stringify({ event: "temp-updated", temp })}\n\n`)
}, 2000)
```

with each header explained ("that is the key header… we do not want any caching of the data…
we do not want this connection to close") and the message format drilled: start with `data:`,
JSON-stringify the payload, "and the next thing I'm going to do is really important… backslash
n, backslash n" — the double newline that "will signal the end of the message block." The
frontend consumes it with the browser's `EventSource` API and an `addEventListener` for the
named event.

Then the real challenge: the site's "beta" news feed streams ghost-story headlines
(`stories.js`, a random headline every 3 seconds) from `/api/news` — the same headers, the same
`res.write` format, this time written by the student.

## Mapping to the syllabus activities

All 36 syllabus lessons for Sections 01–02 appear above. Notes:

- **01.02 "The package.json file"** — covered at 21:30 (numbering offset: the transcript covers
  it before the server, same as the syllabus).
- **01.07 "Routing and the req object"** — covered at 21:45–21:54 plus the refactor at 23:15.
- **02.06–02.11** (path to resource, serve index.html, serve the frontend) — covered at
  22:51–23:42.
- **02.22 "Add an Event Emitter"** and **02.24 "Server-Sent Events Challenge"** — covered at
  24:33–24:54.
- Transcript-only extras: the stretch-goal list at 22:42 (gentler errors, keyword search, "sell
  your API"), and the iterative-launch note ("if you're an early adopter of this course, you
  might be aware that we're launching the projects iteratively").
- The course never uses Express — that is a **curated decision**, not an omission, and it is the
  single most important fact for reading [Module 13](../13-express-js/README.md).

## What this module teaches

1. Node is the V8 engine unbundled from the browser — an environment, not a language.
2. `npm init`, package.json, and `npm start` as the project's front door.
3. `http.createServer`, the `req`/`res` objects, ports and `listen`.
4. Routing by hand: `req.url`, `req.method`, if/else routing, 404s with proper status codes.
5. HTTP bodies are strings: `JSON.stringify` out, buffer-and-`JSON.parse` in.
6. `Content-Type` headers per response, including `text/css` for served files and
   `text/event-stream` for streams.
7. Path parameters vs query parameters, and parsing queries with the `URL` constructor and
   `searchParams`.
8. Mock databases that keep the async mindset honest.
9. `import.meta.url` and the `URL` module vs CommonJS `__dirname`; ES modules vs CommonJS.
10. Serving a frontend from `public/` with the fs module.
11. Validating and sanitizing user input (`sanitize-html` from npm) before storing it.
12. `EventEmitter` for decoupled, event-driven code.
13. Server-sent events end-to-end: headers, `data:` framing, double newline, `EventSource` on
    the client.

## Small practice task

Build a "campus events API" with Node only (no Express):

1. `npm init` a project with a `start` script; data in `events.js` behind an `async` function.
2. `GET /api` returns every event (stringified, with `Content-Type: application/json`);
   `GET /api/city/<city>` filters by path parameter; `GET /api?free=true` filters by query
   parameter (remember: the query value is a string).
3. Unknown routes return a 404 status and a helpful message.
4. Move all handlers into a separate module; keep `server.js` small.
5. Serve a `public/index.html` that lists events — read the file with fs, and fix the CSS
   `Content-Type` yourself when the styles "don't work."
6. Add `POST /api` with a `parseJSONBody` helper that buffers the stream; sanitize the
   `description` field with `sanitize-html`; emit an `event-added` event and log it from a
   listener.
7. Stretch: stream a "countdown to the next event" with server-sent events — `text/event-stream`,
   `Cache-Control: no-cache`, `data: {...}\n\n` every second, consumed with `EventSource`.

## Readiness check for Module 12

Module 12 (databases) replaces the mock database with SQL. Before moving on, be able to explain:

- What `createServer`'s callback receives, and when it runs.
- Why the API returns a string even though the data is an array of objects.
- The difference between a path parameter and a query parameter, with one URL containing both.
- Why `npm start` works when `node server.js` also works, and which one a stranger to your repo
  should use.
- Why `import.meta.url` is needed before serving files.
- What unsanitized user input in a rendered page can do.
- What the `\n\n` does in a server-sent event.

## Exact syllabus order

1. **Build a Node API**
   1. 02. The package.json file
   2. 04. Recreate the server
   3. 07. Routing and the req object — Exercises 1–2
   4. 09. Serve stringified JSON
   5. 10. Adding Content-Type — Exercises 1–2
   6. 11. Route Not Found
   7. 12. Add Path Parameters
   8. 13. Modularise the Code 1
   9. 14. Modularise the Code 2 — Exercises 1–2
   10. 16. Get the Query Parameters — Exercises 1–2
   11. 17. Filter by Query Parameters
2. **Build a Fullstack Node App**
   1. 02. Setting up the project — Exercises 1–2
   2. 06. Get Path to Resource
   3. 08. Serve index.html
   4. 11. serve the frontend — Exercises 1–2
   5. 12. Getting the JSON Data
   6. 13. Wire up the API
   7. 14. Explainer- Adding POST
   8. 16. parseJSONBody
   9. 17. Handling POST Part 1
   10. 18. Handling POST part 2
   11. 20. sanitizeInput
   12. 22. Add an Event Emitter
   13. 24. Server-Sent Events Challenge
