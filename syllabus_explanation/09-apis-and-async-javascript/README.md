# Module 09: APIs and Async JavaScript

## Completion status

**Partially covered — the fundamentals sections are well covered (18:27–19:42); the big build
projects are not.**

| Syllabus section | Transcript coverage |
|---|---|
| 01. Intro to APIs (15 items) | **Mostly covered** — what an API is, clients/servers, requests/responses, first fetch, the Dog API practice. BoredBot as a named project: the *Bored API* is used (18:57, transcribed "board API"), but the BoredBot app build is not walked through. |
| 02. URLs and REST (22 items) | **Partially covered** — URLs, base URL + endpoints, JSON, GET/POST talk, query strings by example. BlogSpace: absent. REST design, nested resources, OpenWeatherMap: absent. |
| 04. Async JavaScript (27 items) | **Well covered** — callbacks, promises, `.then()` chaining, the promise constructor, `try…catch`, `async`/`await`, `Promise.all`. The War card game: absent. |
| 06. Capstone Project (24 items) | **Absent** — no Unsplash, geolocation, weather, crypto dashboard or extension build. |

The segment is a complete "working with APIs" course in miniature — about 75 minutes with an
explicit syllabus, two teachers, and a recap — but it stops at fundamentals. The named projects
(BlogSpace, War, the dashboard capstone) are not in this video.

## How the sources relate

The section announces itself at 18:27:42:

> "In this section, we're going to enter the world of asynchronous JavaScript and use it to
> access data from elsewhere on the internet… APIs are the link between the front end and the
> data on the back end."

And its own topic list:

> "You have not one but two teachers. We're going to start with Scribber's Bob Zerroll taking
> you through some of the fundamentals. With Bob, we'll take an overview of what an API actually
> is. We'll look at clients and servers and requests and responses. We'll also take an overview
> of JSON… we'll talk more about the URLs we use to access APIs. And then we'll get into
> fetching data and… two ways JavaScript gives us of fetching data. We'll learn how to handle
> errors when working asynchronously."

Bob Ziroll teaches the theory and first fetches (18:29–18:57); a second instructor takes the
async deep-dive (18:57–19:42). The closing recap (19:42) names exactly what was taught — a
useful coverage contract:

> "…the fetch API with chained then methods and then the more modern way using the async and
> await keywords. We looked at handling errors with try catch and checking the response object
> for the okay property. And we finished up taking a deep dive into promises and the promise
> constructor."

### Transcript map

| Transcript time | Content | Syllabus section |
|---|---|---|
| 18:27–18:36 | What is an API; clients & servers; requests & responses | 01 |
| 18:36–18:50 | Quiz; URLs, base URL + endpoints; JSON and JSON Lint | 01–02 |
| 18:50–18:57 | Dog API in the browser; first `fetch` + `.then()` chains | 01, 06 (lesson 06) |
| 18:57–19:00 | Bored API fetch practice | 01, 08–09 |
| 19:00–19:12 | Promises: three states; rejection; `try…catch`; `response.ok` | 04, 10–14 |
| 19:12–19:24 | The promise constructor; resolve/reject | 04, 10 |
| 19:24–19:42 | Async/await; `Promise.all`; section recap | 04, 25–26, 28 |

---

## Section 01 — Intro to APIs (18:29–18:57)

### What is an API (18:29)

> "The stuffy definition… is the application programming interface. However, this is just
> another one of those programming [terms]…"

The working definition is built from the student's own experience: until now, "you've probably
stored any data you used for your projects in arrays and objects right there in your codebase on
your local machine. Real world, the data we use in apps… is stored on a server somewhere in the
cloud. APIs enable us to get our hands on that data. They are the bridge we use to access it,
create it, read it, update it, and delete it" — CRUD named two modules before SQL makes it
formal. And the career framing: "Learning to work with APIs takes you in the direction of
becoming a full stack developer."

### Clients & servers (18:30–18:33)

The client/server diagram is walked through with the request→response cycle, and the lesson
narrows scope honestly: "when you hear me [say] API [in this] module, I'm mostly talking about
this kind of API where there's a server and a" client talking HTTP — the broad meaning of the
term (any programmed interface) is acknowledged but set aside.

### Requests & responses (18:36–18:42)

A quiz checks the cycle before any code: what does the client send, what comes back, and what
happens "if the client device isn't authorized to receive the resource" — status codes previewed
by behaviour (401/404-style failures) rather than by number. DevTools appears: "you'll actually
see a list of all the requests that are being made" in the network tab.

### JSON (18:42–18:50)

The data format arrives via a practical trick — paste an API URL into a normal browser and read
what comes back:

> "We have what looks like an object holding a bunch of other objects. And often times the data
> we get back from an API looks something like this. And this is actually JSON data."

- JSON formatter browser plugins are recommended for readability.
- **JSON is not a JavaScript object** — "before we can use this in an app, we will need to
  convert it."
- JSON Lint is used to validate hand-typed JSON ("I'm typing out my own JSON for something, and
  I just want to make sure [it's valid]").

### First fetch (18:50–18:57)

The Dog API is introduced through its docs — "when working with APIs, you'll need the docs to
figure out what data you can get from which endpoints" — with a base URL and two endpoints
(all dogs / one random dog). A Scrimba proxy URL is used so the course can't break if the API
changes, itself a small lesson in production thinking.

The first request, in the older style, taught line by line:

```js
fetch("https://apis.scrimba.com/dog.ceo/api/breeds/image/random")
  .then(response => response.json())
  .then(data => console.log(data))
```

- `fetch` takes the **full URL** — base URL plus endpoint.
- `.then` "will pick up what we get back from fetch and make it available to us in a parameter
  in a callback function. And by convention, we call this parameter response."
- `response.json()` "takes the JSON data we've got stored in the response and converts it to a
  JavaScript object" — and "APIs don't always give you JSON data… you just have to read the
  docs."
- The chain "is moving along a chain and you can read it like you're giving a set of
  instructions to be followed in order" — fetch, convert, use.
- The result is then rendered into the DOM (a random dog image), reusing Module 03's
  `getElementById` + template-string skills.

### Bored API practice (18:57)

"We're back with the board API" — the Bored API, whose GET endpoint returns a random activity.
The fetch-and-log pattern is practised once more; this is the segment that corresponds to the
syllabus's *Fetch idea from Bored API* lesson. The full BoredBot app (HTML/CSS/a11y builds) is
not in the transcript.

## Section 02 — URLs and REST (partially covered)

What the transcript teaches of this section is woven into the segments above:

- **Base URL + endpoint structure** (18:50) — "This is the base URL right here. And there are
  two possible endpoints."
- **Reading API docs** (18:52) — endpoints, data shapes, authentication requirements.
- **HTTP methods** — GET is used throughout; POST is discussed conceptually in Module 11
  (21:51–24:18) where a Node server actually handles request methods, and `fetch` options
  (method/body/headers) appear in the React course's POST lesson (35:4x). The syllabus's
  dedicated *Requests - Methods / Body / Headers* lessons have no standalone segment here.
- **Query strings** — used by example (the stock predictor's API key and prompt parameters in
  Module 10; the Node course's `?topic=` filtering at 21:48) but never as a named lesson.
- **REST design, nested resources, URL parameters** — genuinely absent as teaching; URL
  *parameters* reappear as **path parameters** in Module 11 (22:00–22:40), which is the closest
  the video comes.

**BlogSpace** (lessons 05–16: GET posts, render, new-post form, POST to server, reset form) has
no transcript segment — the nearest equivalent builds are the React course's Star Wars API
project (37:15) and the meme generator's API fetch (36:39), both documented in Module 15.

## Section 04 — Async JavaScript (19:00–19:42)

### Promises and their three states (19:00)

The state model is taught with a job-interview analogy that the lesson takes seriously enough to
test twice:

> "If you said the resolved state would be that we got the job, you'd be wrong. The promise was
> *we'll let you know within a week*, not that we'll let you have a positive answer… they might
> get in touch within a week to say you've got the job or it might be to say thanks but no
> thanks. Both of those are fulfilled or resolved promises."

- **Pending** — "the promise hasn't been completed yet. It's still in process"; exactly the
  window while a fetch waits for its response.
- **Fulfilled/resolved** — "the promise was completed as promised. But… that doesn't necessarily
  mean you got what you wanted." (A 404 response still *fulfills* the fetch promise — the reason
  `response.ok` must be checked.)
- **Rejected** — "they did not get back to you within a week. So the promise was not completed
  as promised" — network failure, not a bad answer.

### `.then()` chains and method chaining (19:02)

The chaining lesson makes the pipe explicit: each `.then` receives the previous step's output as
its parameter, which is why the order fetch → `response.json()` → use-the-data can't be
shuffled. (The syllabus's *Context- method chaining* aside is this passage.)

### `try…catch` and `response.ok` (19:06)

Error handling gets both layers the recap promises:

```js
try {
  const response = await fetch(url)
  if (!response.ok) {
    throw new Error("Failed to fetch")
  }
  const data = await response.json()
} catch (err) {
  console.error(err)
}
```

- `try` wraps the risky code; `catch` receives whatever was thrown.
- `response.ok` distinguishes "the server answered, but badly" from "the request never
  completed" — the job-interview payoff from 19:00.
- A fulfilled-but-empty response is handled as its own case: "the promise fulfills, but we're
  not getting a suggestion."

### The promise constructor (19:21–19:30)

The deepest cut in the section — creating promises by hand:

```js
const myPromise = new Promise((resolve, reject) => {
  // ...eventually:
  resolve("Operation successful")
  // or: reject("Operation failed")
})
```

> "I didn't have to call this promise. I could call it whatever I [want]… it returns
> 'operation successful' if it resolves and 'operation failed' if it [rejects]."

`resolve`/`reject` are functions the executor calls later — the same machinery `fetch` uses
internally. (The syllabus's War-card-game exercises would have drilled this; a
process-file/notify-user mini-project (19:30–19:36) drills it instead.)

### `async`/`await` (19:33)

The modern syntax, positioned exactly as the recap positions it — "the fetch API with chained
then methods and then the more modern way using the async and await keywords":

```js
async function getData() {
  const response = await fetch(url)
  const data = await response.json()
}
```

`await` pauses the function, not the page — connecting back to the event-loop teaching of
Module 07 (15:45).

### `Promise.all` (19:36)

> "[We can] pass in as many [promises] as we want. And we attempt to resolve them [all]."

An array of promises (built by mapping over an array of URLs) resolves together — with the
warning that one rejection rejects the whole batch.

## Section 06 — Capstone Project *(absent)*

No Unsplash photo fetch, author info, crypto prices, time, weather, geolocation, or
`getCurrentLocation`-as-a-promise thought experiment exists anywhere in the transcript
("geolocation", "unsplash", "weather" all return zero or irrelevant matches). The nearest
equivalents, for practice purposes:

- Unsplash-style image API + rendering → the Dog API fetch-and-render at 18:55.
- Multiple APIs composed into one dashboard → the React AI recipe generator (35:45–36:20,
  Module 15) and the Next.js Print Forge data fetching (44:44+, Module 19).
- A promise-based geolocation wrapper → the promise constructor lesson at 19:21 is the exact
  pattern you would need to write.

## Mapping to the syllabus activities

- **01.15 "BoredBot - Improve A11y"** and the BoredBot builds — no segments; only the Bored API
  fetch itself (18:57).
- **02.17–19 REST / REST API design / nested resources** — not taught; REST is only name-dropped
  as a term by other modules' instructors ("This is a REST API" — 21:22, in Node).
- **02.20–22 parameters, query strings, OpenWeatherMap** — query strings are used but never
  taught as a lesson; OpenWeatherMap is absent.
- **04.15–27 War** — absent; its promise drills are replaced by the constructor and
  process-file examples.
- **04.28 "A quick look at Async_Await"** — more than a quick look here: a full lesson with
  `try…catch`.
- **06 Capstone** — absent, with the nearest equivalents listed above.

## What this module teaches (from the parts that exist)

1. What an API is, in the client/server sense, and why APIs are the front-end/back-end bridge.
2. The request/response cycle, and where to watch it (browser, DevTools).
3. JSON: what it looks like, how to read it in the browser, how to validate it, and that it
   must be converted before use.
4. `fetch` + `.then()` chains, and `response.json()`.
5. The three promise states — and that *fulfilled* ≠ *successful*.
6. `async`/`await` as the modern form of the same chain.
7. `try…catch`, `throw`, and checking `response.ok`.
8. Creating promises with `new Promise` and `resolve`/`reject`.
9. `Promise.all` for parallel requests.

## Small practice task

Build a one-file "activity finder" — the BoredBot that the transcript never builds:

1. Fetch a random activity from the Bored API and render its `activity`, `type` and
   `participants` into a styled card.
2. Add a button that re-fetches; disable it while a request is pending (the pending state, made
   visible).
3. Implement it twice: once with `.then()` chains only, once with `async`/`await` +
   `try…catch`. Keep both in the file, one commented, and note which you found clearer.
4. Check `response.ok` and render an error message with a retry button when the API misbehaves
   (test it by temporarily fetching a 404 URL).
5. Wrap `Math.random()`-based coin flip in `new Promise` that resolves "heads"/"tails" after a
   1-second `setTimeout`, and await it — the promise constructor, used for real.
6. Stretch: fetch **three** activities up front with `Promise.all` and let the user pick one.

## Readiness check for Module 10

Module 10 (AI engineering) uses this module immediately — an API key in a URL, a fetch, and a
rendered response. Before moving on, be able to explain:

- What is pending, fulfilled and rejected, and why a 404 is *fulfilled*.
- What `response.json()` does and why it returns a promise.
- Why `.then()` order cannot be shuffled.
- What `await` actually waits for, and what it does *not* block.
- When `Promise.all` is the wrong tool.

Carry forward honestly: **REST design, HTTP methods as a lesson, headers, query strings as a
lesson, and every named project (BlogSpace, War, the capstone) are gaps** — Module 11 (Node)
will re-cover methods and routing from the server's side.

## Exact syllabus order

1. **Intro to APIs**
   1. 01. What is an API_
   2. 02. Clients & Servers
   3. 03. Requests & Responses
   4. 06. First fetch
   5. 08. Dog API Fetch and DOM Practice
   6. 09. Fetch idea from Bored API *(Bored API fetch only)*
   7. 11. BoredBot - HTML *(no transcript coverage)*
   8. 12. BoredBot - CSS *(no transcript coverage)*
   9. 13. BoredBot - JavaScript *(no transcript coverage)*
   10. 14. BoredBot - Extra Styling *(no transcript coverage)*
   11. 15. BoredBot - Improve A11y *(no transcript coverage)*
2. **URLs and REST**
   1. 02. HTTP Requests *(covered conceptually across 18:36–18:42 and Module 11)* — Exercises 1–2
   2. 03. Requests - URLs and Endpoints
   3. 04. Requests - Methods — Exercises 1–2 *(methods taught from the server side in Module 11)*
   4. 05. BlogSpace - GET first 5 blog posts *(no transcript coverage)*
   5. 06. BlogSpace - Display blogs on page *(no transcript coverage)*
   6. 07. BlogSpace - Add styling *(no transcript coverage)*
   7. 08. BlogSpace - New post form *(no transcript coverage)*
   8. 09. BlogSpace - Add style to form *(no transcript coverage)*
   9. 10. BlogSpace - Form submit event listener *(no transcript coverage)*
   10. 11. Requests - Body — Exercises 1–3 *(not taught as a lesson)*
   11. 12. Requests - Headers *(not taught as a lesson)*
   12. 13. BlogSpace - Send new post to server *(no transcript coverage)*
   13. 14. BlogSpace - Add new post to list of posts *(no transcript coverage)*
   14. 15. BlogSpace - Posts Refactor — Exercises 1–2 *(no transcript coverage)*
   15. 16. BlogSpace - Reset form *(no transcript coverage)*
   16. 17. REST *(named only, not taught)*
   17. 18. REST API Design *(no transcript coverage)*
   18. 19. Nested Resources — Exercises 1–2 *(no transcript coverage)*
   19. 20. URL - Parameteres - JSON Placeholder API *(path parameters covered in Module 11)*
   20. 21. Query Strings *(used by example in Modules 10–11, never as a lesson)*
   21. 22. Query String Practice - OpenWeatherMap API — Exercises 1–2 *(no transcript coverage)*
3. **Async JavaScript**
   1. 02. Callbacks Setup Challenge *(callback thinking taught in Modules 03/07)*
   2. 04. Separate event listener callback
   3. 05. Callbacks - revisting setTimeout — Exercises 1–3 *(setTimeout taught at 15:36)*
   4. 06. Callbacks - revisiting array.filter — Exercises 1–2
   5. 07. Callbacks - make own filerArray function
   6. 08. Callbacks - put our custom filterArray function to use
   7. 09. Thought experiment- what if _fetch_ used callbacks_
   8. 10. Promises — Exercises 1–3
   9. 11. Context- method chaining — Exercises 1–2
   10. 12. Promises - .then() chaining
   11. 13. Promises - .then()
   12. 14. Promises - passing basic values in the chain — Exercises 1–2
   13. 15. War - save deckid for later use *(no transcript coverage)*
   14. 16. War - draw 2 cards from our deck — Exercises 1–2 *(no transcript coverage)*
   15. 17. War - Display our card images *(no transcript coverage)*
   16. 18. War - Styling part 1 *(no transcript coverage)*
   17. 19. War - Styling part 2 *(no transcript coverage)*
   18. 20. War - Refactor card image placement *(no transcript coverage)*
   19. 21. War - Determine the winning card part 1 — Exercises 1–2 *(no transcript coverage)*
   20. 22. War - Determine winning card part 2 — Exercises 1–2 *(no transcript coverage)*
   21. 23. War - display remaining cards when drawing *(no transcript coverage)*
   22. 24. War - Display remaining cards on new deck *(no transcript coverage)*
   23. 25. War - Disable the draw button when we get to 0 cards remaining *(no transcript coverage)*
   24. 26. War - Keep score *(no transcript coverage)*
   25. 27. War - Display the final winner *(no transcript coverage)*
   26. 28. A quick look at Async_Await *(full lesson at 19:33)*
4. **Capstone Project** *(no transcript coverage)*
   1. 03. Get photo from Unsplash
   2. 04. Add Author Info
   3. 06. Set up flexbox
   4. 07. Promises review
   5. 09. Promise rejection practice
   6. 10. Crypto - Add cryptocurrency data
   7. 11. Crypto - Get Dogecoin data
   8. 12. Crypto - Display name and icon
   9. 13. Crypto - get prices
   10. 14. Time - Add current time with JavaScript
   11. 15. Time - Display time on page
   12. 16. Weather - start
   13. 17. Thought experiment - getCurrentLocation as a promise-based API_
   14. 18. Weather - Get user_s current weather
   15. 19. Weather - Add icon
   16. 20. Weather - Add temp and city
   17. 21. Weather - CSS
   18. 22. Chrome extension time
   19. 23. Update - using await — Exercises 1–2
   20. 24. Update - try...catch
