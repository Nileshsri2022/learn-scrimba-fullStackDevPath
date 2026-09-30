# Module 11: Node.js

## Completion status

**Both sections are covered by the transcript.** Node.js begins at roughly **21:19** with an
animated intro, and the two projects run through to about **24:45**.

- **Section 01 — Build a Node API:** fully covered. The project is the **Wild Horizons API**, a
  REST API of unusual travel destinations, built with the core `http` module.
- **Section 02 — Build a Fullstack Node App:** fully covered. The project is **"From the Other
  Side"** (also called Retro Tech / the paranormal-sightings app), which serves a real front end,
  handles `POST` uploads, sanitises input, and finishes with **event emitters** and **server-sent
  events**.

The teacher for this whole module is **Tom Chant** ("My name is Tom Chant. I've been working at
Scrimba since 2021"). A few activity numbers in the syllabus skip (e.g. Section 01 jumps 02 → 04 →
07); those are recap/challenge scrims, and their content is folded into the lessons below.

---

## Why Node.js exists (the intro)

Back in the day, front-end code ran in the browser with JavaScript while backend logic used PHP,
Ruby or Java — developers had to juggle multiple languages. Then:

> "In 2009, Ryan Dahl had an idea and Node.js was born. A way to break JavaScript free from the
> browser."

The single most important framing in the whole module:

> "Node.js is not a language. It is an environment in which we can write JavaScript."

JavaScript runs in the browser because browsers ship a JavaScript engine (Chrome's **V8**). Node
bundles that same V8 engine so JavaScript can run **outside** the browser. There is no browser, so
**no DOM** — logging `document` in Node throws an error.

### Why learn raw Node before Express?

> "The elephant in the room here is that Express.js exists... Why not learn that instead? Well, when
> you understand how Node.js works at its core, you become a more versatile developer."

Express is a framework that *wraps* Node; Nest.js and Fastify are alternatives. The analogy: learning
Express without Node is "like knowing jQuery without knowing JavaScript."

---

## Section 01 — Build a Node API (Wild Horizons)

### The data and the endpoints

Each destination is an object: `name`, `location`, `country`, `continent`, a boolean
`isOpenToThePublic`, a `details` array (fun fact + description), and a `uid` (unique identifier).

There are three ways a client can reach the data:

| Request | Meaning |
|---|---|
| `/api` | the entire data set |
| `/api/country/India` or `/api/continent/Asia` | filter by a **path parameter** |
| `/api?country=Turkey&isOpenToThePublic=true` | filter with **query parameters** |

### Lesson 02 — The `package.json` file

> "At the heart of every Node.js project, we have got the package.json file... it acts as the
> project's blueprint."

It holds metadata (name, version, author, description), manages **dependencies**, and defines a
**start script**. You don't hand-write it — you generate it:

```bash
npm init          # "init stands for initialize"; asks a series of questions
```

Accept a default by hitting **Enter** (a blank default is fine). The generated file already sets
`server.js` as the entry point, which lets you replace `node server.js` with:

```bash
npm start
```

### Lesson 04 — Recreate the server

Run a file directly with `node server.js`; a bare `console.log("hello node")` prints in the terminal.
Node also gives you the **REPL** (Read-Evaluate-Print Loop) — type `node`, then live JavaScript — but
"the novelty does actually wear off after a few seconds. We don't want to be writing JavaScript in
the terminal. We want to create servers." Exit the REPL / stop anything running with **Ctrl-C**.

To create a server you need Node's core `http` module. Import it with the `node:` prefix (best
practice — it tells Node this is a core module, not one of your own files, which speeds up lookups):

```js
import http from "node:http"

const server = http.createServer((req, res) => {
  res.end("Hello from the server")
})

const PORT = 8000
server.listen(PORT, () => {
  console.log(`Server running on port ${PORT}`)
})
```

Two setup gotchas the transcript hits:

1. ES-module imports require `"type": "module"` in `package.json` (the course avoids the old
   `require` / CommonJS style).
2. `createServer` takes a **callback with two parameters** — the request (`req`) and response
   (`res`) objects. These "give us access to the request and response cycle."

`res.end(data)` **sends data over HTTP and ends the response**. Its cousin `res.write()` writes a
chunk *without* ending — use it to stream several chunks, but you must still call `res.end()` so the
browser knows the response is finished.

### The request/response cycle

> "The client makes an HTTP request to the server. The server does some processing and sends an HTTP
> response back to the client."

The **request** carries the method (`GET`, `POST`…), the path/URL, and extra data (path params,
query strings). The **response** carries the data, a **content type**, a **status code** (200 OK,
404 not found), and a status message.

### Lesson 07 — Routing and the `req` object

`req.url` holds the path after the base URL; `req.method` holds the verb (compare against
**uppercase** `"GET"`). Basic routing is just JavaScript:

```js
if (req.url === "/api" && req.method === "GET") {
  // serve the data
}
```

### Lesson 09 — Serve stringified JSON

HTTP is a text protocol: **all data must be sent as strings**. Convert with `JSON.stringify()`:

```js
import { getData } from "./database/db.js"   // async, mimics a real DB

const destinations = await getData()          // so the callback must be async
res.end(JSON.stringify(destinations))
```

The data lives in `data.js` as a plain array of objects, but `db.js` wraps it in an **async**
function "as if we were making a request to a database... to get you into the async mindset."
Forgetting `await` (and marking the callback `async`) is the bug Tom deliberately triggers.

### Lesson 10 — Adding Content-Type (and the status code)

Set the response's MIME type and status code explicitly (Node silently sends a 200, but that's bad
practice):

```js
res.setHeader("Content-Type", "application/json")   // watch the casing
res.statusCode = 200                                // a property, NOT a method
```

Common content/MIME types: `application/json`, `text/html`, `text/css`,
`application/javascript`, plus every image/audio/video format.

### Lesson 11 — Route Not Found

The happy path isn't enough. Add an `else` for unknown routes, returning a 404:

```js
res.setHeader("Content-Type", "application/json")
res.statusCode = 404
res.end(JSON.stringify({
  error: "Not Found",
  message: "The requested route does not exist"
}))
```

### Lesson 12 — Add Path Parameters

`/api/continent/Asia` filters by continent. Use `String.prototype.startsWith`, then grab the last
URL segment with `split("/").pop()`:

```js
else if (req.url.startsWith("/api/continent") && req.method === "GET") {
  const continent = req.url.split("/").pop()
  const filteredData = destinations.filter(
    dest => dest.continent.toLowerCase() === continent.toLowerCase()
  )
  // ...stringify and send filteredData
}
```

`.toLowerCase()` on both sides guards against inconsistent casing.

### Lessons 13–14 — Modularise the Code (DRY)

The route bodies repeat, so the filtering is abstracted into `utils/getDataByPathParams.js`. The
lesson's principle: "clean, easy-to-read code... is more important than clever, complex but shorter
code."

```js
export const getDataByPathParams = (data, locationType, locationName) =>
  data.filter(dest => dest[locationType].toLowerCase() === locationName.toLowerCase())
```

Bracket notation (`dest[locationType]`) lets the same function handle `country` **and** `continent`.

### Lessons 16–17 — Query Parameters (and filtering by them)

A query string — `/api?country=Turkey&isOpenToThePublic=true` — reads like an instruction: "bring
me data where country is Turkey." Getting them into a usable object is verbose in raw Node (Express
hides all of this):

```js
const urlObject = new URL(req.url, `http://${req.headers.host}`)
const queryObject = Object.fromEntries(urlObject.searchParams)
```

- `URL` is a **constructor**, so `new`. It needs the relative URL **and** a base URL — hence
  `req.headers.host` (which holds `localhost:8000`). Hardcoding the base would break on deploy.
- `urlObject.searchParams` isn't a plain object, so `Object.fromEntries()` converts it into
  `{ country: "Turkey", isOpenToThePublic: "true" }`.

### CORS (the deploy-time headers)

When the front end and server share protocol + domain + port, you do nothing. When they differ (or
you want a public API), set **Cross-Origin Resource Sharing** headers where you build the response:

```js
res.setHeader("Access-Control-Allow-Origin", "*")     // any origin
res.setHeader("Access-Control-Allow-Methods", "GET")  // only the methods you use
```

"Working here in Scrimba it's not going to make any difference. But if you were to deploy this out
there on the internet, you need to add these two lines."

---

## Section 02 — Build a Fullstack Node App ("From the Other Side")

A site for uploading paranormal sightings. Kept deliberately simple because "you're pretty unlikely
to be building a full stack project with a vanilla Node backend in the real world." Three tasks:
serve the static assets, provide data via an API, and accept new sightings via `POST`. New modules
studied: **`fs`** (file system) and **`path`**.

### Lesson 02 — Setting up the project

Same as Section 01: `npm init`, then set `"type": "module"`. Serve the first HTML page with
`Content-Type: text/html` and status `200`.

### Lessons 06–08 — Get path to resource / serve index.html

You can't hardcode file paths — they differ per operating system. The solution must be **agnostic**
(doesn't care which OS runs it).

- `import.meta` is an object with metadata about the current module. `import.meta.dirname` gives the
  directory of `server.js`. (Old CommonJS exposes this as the global `__dirname`; the course mimics
  the name: `const __dirname = import.meta.dirname`.)
- `process.cwd()` is the **current working directory** — the folder you launched Node from.
- The `path` module joins segments into one OS-safe string:

```js
import path from "node:path"
const pathToResource = path.join(__dirname, "public", "index.html")
```

**Absolute vs relative paths** (an important distinction the module labours):

| Path type | Built from | Behaviour |
|---|---|---|
| Absolute | `path.join(__dirname, ...)` | independent of the CWD — "rock-solid," used for serving HTML |
| Relative | `path.join("public", ...)` | relative to the **current working directory**, not the file — more flexible, used in shared utilities |

### Lesson 11 — Serve the front end

`serveStatic.js` reads and serves everything in `public/` using the async `fs` module. Detect a
missing file by its error code and serve the 404 page:

```js
import fs from "node:fs/promises"

try {
  const content = await fs.readFile(filePath)
  // ...send with the right content type
} catch (error) {
  if (error.code === "ENOENT") {                 // Error NO ENTity = file not found
    const content = await fs.readFile(path.join(__dirname, "public", "404.html"))
    res.statusCode = 404
    res.setHeader("Content-Type", "text/html")
    res.end(content)
  } else {
    res.statusCode = 500
    res.setHeader("Content-Type", "text/html")
    res.end("<h1>Server error</h1>")
  }
}
```

> **`res.writeHead` aside:** `res.writeHead(200, { "Content-Type": "text/html" })` sets the status
> code and headers in one line, but it **sends the headers immediately** — so `setHeader` calls
> *after* it are ignored, and any header it sets overrules an earlier `setHeader`. Know both; the
> project sticks with `setHeader` + `statusCode` for flexibility.

### Lessons 12–13 — Getting the JSON data / wire up the API

`utils/getData.js` reads `data.json` fresh each time (so writes are picked up), parses it, and
returns an empty array on error:

```js
export const getData = async () => {
  try {
    const data = await fs.readFile(path.join("data", "data.json"), "utf-8")
    return JSON.parse(data)
  } catch (error) {
    console.error(error)
    return []                 // callers expect an array
  }
}
```

Why parse it here just to `stringify` it when serving? **Future-proofing** — `POST` handling needs
to manipulate the data as a JavaScript array, and "you can't manipulate the JSON string directly."

The route check nests the method inside the path, because both GET and POST hit `/api`:

```js
if (!req.url.startsWith("/api")) {
  await serveStatic(__dirname, req, res)
  return
} else if (req.url === "/api") {
  if (req.method === "GET") handleGet(req, res)
  if (req.method === "POST") handlePost(req, res)
}
```

### Lessons 14–18 — Adding POST / parseJSONBody / handling POST

A `POST` body arrives as a **stream of chunks**, so you collect them, then parse. The upload form on
the front end sends the sighting; the server reassembles the body, parses it to an object, adds it to
the data, and writes the file back.

### Lesson 20 — sanitizeInput

Never trust uploaded content — it can contain malicious markup/scripts:

```js
const sanitizedBody = sanitizeInput(parsedBody)
```

In Tom's test, a `<button onclick=...>Click me</button>` is neutralised (the text survives, the
button doesn't), while a benign `<b>` tag is allowed through — a small allow-list sanitiser guarding
against injection.

### Lesson 22 — Add an Event Emitter

> "You might have heard it said that Node has got event-driven architecture... code is designed to
> react to events as they occur."

The `EventEmitter` class comes from the `events` module. You **emit** a named event and **register**
listeners with `on`:

```js
import EventEmitter from "node:events"

export const sightingEvents = new EventEmitter()
sightingEvents.on("sightingAdded", createAlert)   // register the listener
```

Then, wherever a sighting is added:

```js
import { sightingEvents } from "./events/sightingEvents.js"
sightingEvents.emit("sightingAdded", sanitizedBody)   // name + data for the listener
```

`emit` takes the event name plus any arguments the listener needs; `on` takes the event name plus the
listener function. The power is decoupling: "you can emit an event in one part of your app and listen
for it in another," and one event can trigger **multiple** listeners.

### Lesson 24 — Server-Sent Events Challenge

SSE let the server push a **one-way** stream of data to the client with no page reload — good for
news tickers, stock prices, sports scores, live monitoring. (Not for chat or two-way comms.) The
client requests once; the server holds the connection open and keeps writing.

```js
// route: /temp/live
res.statusCode = 200
res.setHeader("Content-Type", "text/event-stream")   // the key header
res.setHeader("Cache-Control", "no-cache")           // never cache a live stream
res.setHeader("Connection", "keep-alive")            // don't close the connection

setInterval(() => {
  const temperature = getTemp()
  res.write(`data: ${JSON.stringify({ event: "tempUpdated", temp: temperature })}\n\n`)
}, 2000)
```

Two non-negotiables: end each message with `\n\n` ("required by the server-sent events protocol...
it signals the end of a complete message block"), and use `res.write` **not** `res.end` — ending
would close the connection you're trying to keep open. The browser side listens with the
`EventSource` API.

---

## Mapping to the syllabus activities

| Syllabus activity | Where in the explanation |
|---|---|
| 01.02 The package.json file | *Lesson 02* — `npm init`, start script |
| 01.04 Recreate the server | *Lesson 04* — `http.createServer`, `listen` |
| 01.07 Routing and the req object | *Lesson 07* — `req.url`, `req.method` |
| 01.09 Serve stringified JSON | *Lesson 09* — `JSON.stringify`, async data |
| 01.10 Adding Content-Type | *Lesson 10* — `setHeader`, `statusCode` |
| 01.11 Route Not Found | *Lesson 11* — 404 object |
| 01.12 Add Path Parameters | *Lesson 12* — `startsWith`, `split().pop()` |
| 01.13–14 Modularise the Code | *Lessons 13–14* — `getDataByPathParams` |
| 01.16–17 Query Parameters / filter | *Lessons 16–17* — `URL`, `Object.fromEntries` |
| 02.02 Setting up the project | *Lesson 02* (Section 02) |
| 02.06 Get Path to Resource | *Lessons 06–08* — `import.meta.dirname`, `path.join` |
| 02.08 Serve index.html | *Lessons 06–08* |
| 02.11 serve the frontend | *Lesson 11* — `serveStatic`, `fs`, 404/500 |
| 02.12 Getting the JSON Data | *Lesson 12* — `getData`, parse vs stringify |
| 02.13 Wire up the API | *Lesson 13* — nested method routing |
| 02.14–18 Adding/handling POST | *Lessons 14–18* — chunked body, parse |
| 02.20 sanitizeInput | *Lesson 20* — injection guard |
| 02.22 Add an Event Emitter | *Lesson 22* — `EventEmitter`, emit/on |
| 02.24 Server-Sent Events | *Lesson 24* — `text/event-stream`, `\n\n` |

Everything the syllabus lists is present in the transcript. The `PRACTICE: Exercise` items are the
in-scrim challenges (recreate the server, filter by path params, complete the `URL`/`queryObject`
lines, etc.), described inline above.

## What this module teaches

- Node is an **environment** for running JavaScript outside the browser (V8, no DOM).
- Building an HTTP server from the core `http` module: `createServer`, `listen`, `req`/`res`.
- The request/response cycle: methods, URLs, status codes, headers, content types.
- Routing by hand with `req.url`/`req.method`, path params, and query params (`URL` +
  `Object.fromEntries`).
- The `fs` and `path` modules; absolute vs relative paths and why the CWD matters.
- Serving a real front end, handling `POST` uploads, and sanitising input.
- Node's event-driven side: `EventEmitter` and server-sent events.

## Practice task

Extend the Wild Horizons API from Section 01:

1. Add a `/api/country/:name` route alongside the continent route, reusing `getDataByPathParams`.
2. Support the query string `/api?continent=Asia&isOpenToThePublic=true`, filtering on **both**
   params (remember the query values arrive as strings — `"true"`, not `true`).
3. Return a friendly message (not an empty array) when a valid param matches no data.
4. Set a correct `Content-Type` and status code on **every** response, including the 404.

## Readiness check for the next module

Before moving to **Databases**, you should be able to:

- explain why Node needs `JSON.stringify` before sending data over HTTP;
- build an OS-safe file path with `path.join` and know when to use an absolute vs relative one;
- route a request by inspecting `req.url` and `req.method`;
- read and write a file with the async `fs` module and handle an `ENOENT` error.

The mock database (`db.js` returning an async function) foreshadows the next module: real relational
databases and SQL, which replace the `data.js` array entirely.

---

## Ordered syllabus

MODULE 11. Node.js
========================================================================
Learning focus: Server-side JavaScript with Node, API construction, and a full-stack Node application.
  SECTION / UNIT: 01. Build a Node API
    LESSON / ACTIVITY: 02. The package.json file
    LESSON / ACTIVITY: 04. Recreate the server
    LESSON / ACTIVITY: 07. Routing and the req object
      PRACTICE: Exercise 1
      PRACTICE: Exercise 2
    LESSON / ACTIVITY: 09. Serve stringified JSON
    LESSON / ACTIVITY: 10. Adding Content-Type
      PRACTICE: Exercise 1
      PRACTICE: Exercise 2
    LESSON / ACTIVITY: 11. Route Not Found
    LESSON / ACTIVITY: 12. Add Path Parameters
    LESSON / ACTIVITY: 13. Modularise the Code 1
    LESSON / ACTIVITY: 14. Modularise the Code 2
      PRACTICE: Exercise 1
      PRACTICE: Exercise 2
    LESSON / ACTIVITY: 16. Get the Query Parameters
      PRACTICE: Exercise 1
      PRACTICE: Exercise 2
    LESSON / ACTIVITY: 17. Filter by Query Parameters
  SECTION / UNIT: 02. Build a Fullstack Node App
    LESSON / ACTIVITY: 02. Setting up the project
      PRACTICE: Exercise 1
      PRACTICE: Exercise 2
    LESSON / ACTIVITY: 06. Get Path to Resource
    LESSON / ACTIVITY: 08. Serve index.html
    LESSON / ACTIVITY: 11. serve the frontend
      PRACTICE: Exercise 1
      PRACTICE: Exercise 2
    LESSON / ACTIVITY: 12. Getting the JSON Data
    LESSON / ACTIVITY: 13. Wire up the API
    LESSON / ACTIVITY: 14. Explainer- Adding POST
    LESSON / ACTIVITY: 16. parseJSONBody
    LESSON / ACTIVITY: 17. Handling POST Part 1
    LESSON / ACTIVITY: 18. Handling POST part 2
    LESSON / ACTIVITY: 20. sanitizeInput
    LESSON / ACTIVITY: 22. Add an Event Emitter
    LESSON / ACTIVITY: 24. Server-Sent Events Challenge

========================================================================
