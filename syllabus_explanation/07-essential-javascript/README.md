# Module 07: Essential JavaScript

## Completion status

**Partially covered. Section 04 (Mini Projects) is well covered — roughly 15:14–18:27. Sections
01–03 (Cookie Consent, Meme App, X Clone) are not in the transcript at all.**

Verified findings:

| Syllabus section | Transcript coverage |
|---|---|
| 01. Build a Cookie Consent | **Absent.** "cookie" appears only in Module 02's cookie *widget* (01:05–01:09), which is a CSS styling exercise, not this app. |
| 02. Build a Meme App | **Absent here.** A meme generator *is* built at 36:20–36:51, but as a React project — see [Module 15](../15-react-js-fundamentals/README.md). |
| 03. Build a X Clone (Twimba) | **Absent.** "Twimba" and "tweet feed" builds: zero matches. |
| 04. Mini Projects | **Covered**, with named gaps listed below. |

Within Section 04, almost every named lesson has a segment: object destructuring, `.map()`,
`.join()`, `.map()` vs `.forEach()`, the dangers of `innerHTML`, function expressions, arrow
functions (incl. inline), import/export, `.reduce()` (incl. with objects), the super challenge,
the ternary operator, the rest parameter, switch statements, `Date()`, constructor functions and
debugging errors. **Not covered, even in Section 04:** spread syntax as its own topic (only the
rest parameter's `...`), short-circuiting with `||`/`&&` (zero matches in the region), the
Twimba ternary refactor (no Twimba exists), and constructor-functions-to-**classes** (classes are
named as future material — "we'll also see classes and generators" (16:16) — but never taught).

## How the sources relate

The transcript segment is a single continuous course (15:14–18:27) that announces its own
syllabus at the start:

> "We will be looking at the turnary operator, the switch statement, object destructuring, set
> timeout, set interval, two asynchronous methods. There we'll look in detail at the event loop.
> And we'll talk about scope, which will lead us into hoisting. Next up, we'll have import and
> export. We'll look at the date constructor and the error constructor, our first two built-in
> constructors, and then we'll look at a JavaScript oddity, pre-increment, the big int data type,
> and we'll finish off on numeric separators. And… we'll finish up with a super challenge."

### Transcript map

| Transcript time | Content | Syllabus lessons (Section 04) |
|---|---|---|
| 15:14–15:27 | Ternary operator; switch statements | 27, 37 |
| 15:27–15:36 | Objects recap; object destructuring | 03 |
| 15:36–15:51 | `setTimeout`/`setInterval`; call stack; the event loop | (supporting) |
| 15:51–15:59 | `import`/`export` (named) | 16 |
| 15:59–16:18 | `Date()` and `Error()` constructors; constructor functions; BigInt; numeric separators; scope & hoisting | 38, 42, 45 |
| 16:18–16:51 | Super challenge #1: the stock ticker | 23 |
| 16:51–17:45 | *Second pass* of the same material with extra depth (see note below) | — |
| 17:45–18:03 | Function expressions; arrow functions; `.map()` and `.reduce()` | 12, 14, 05, 19–21 |
| 18:03–18:18 | Rest parameter; `.join()`; first-class functions | 30, 07 |
| 18:18–18:27 | Super challenge #2: property-for-sale cards | 23 |

**Note — the video runs part of this course twice.** Near-identical passages appear twice, about
74 minutes apart: "you're welcome to go back and check my code if you absolutely need to" at
15:38:55 and again at 16:53:24; "in this course. So, let's start off with one of JavaScript's
inbuilt constructors" at 16:00:00 and 17:14:29; the stock ticker at 16:18 and 17:33. The second
pass (16:51–17:45) is not wasted — it carries the fuller scope/hoisting discussion (the
`trafficInfo` example at 17:30) and a `string.repeat` challenge — but listeners should expect
déjà vu, not new syllabus items.

---

## Section 01 — Build a Cookie Consent *(absent)*

The skills this section would teach do appear elsewhere, scattered:

- **`setTimeout`** — taught at 15:36–15:51, including the rule that the delay is in
  milliseconds ("which is going to count the 5,000 milliseconds") and how the timer interacts
  with the stack.
- **`element.style`** — `innerText`/`innerHTML` are used everywhere from Module 03; the `.style`
  property specifically is not demonstrated.
- **Forms and validation attributes** — not in this segment; the transcript's real forms teaching
  happens in the React course (controlled inputs, `name` attributes, checkboxes — 31:39–33:45,
  documented in Module 15).
- **`classList` add/remove/toggle** — `classList` never appears; class swapping in the transcript
  is done through template strings and `clsx` in React (38:54).

## Section 02 — Build a Meme App *(absent)*

The meme generator that exists in the transcript is the React version at 36:20–36:51: a form
with top/bottom text inputs, an image fetched from an API, `useEffect` and state. The vanilla-JS
version (`for…of` loops, radio inputs, `.includes()`, `.filter()`, `getElementsByClassName`,
`querySelector`) has no segment. The generic techniques are all taught elsewhere: `for…of` does
not appear, but `for` loops (Module 03) and `.filter()` thinking (Module 09's callbacks section)
do.

## Section 03 — Build a X Clone *(absent)*

No tweet feed, likes, retweets or replies are built anywhere in the transcript. The one relevant
transfer: the X/Twitter UI is name-checked in Module 02's flexbox tour ("Let's just have a look
at Twitter for example… the tweet options" — 02:12) as a flexbox example.

---

## Section 04 — Mini Projects (15:14–18:27) — covered

### The ternary operator (15:15)

> "We're not replacing the if else, but the turnary operator can be really useful in some
> situations."

Syntax, read exactly as the lesson reads it: a condition that returns truthy/falsy, then `?`,
then the expression that runs when truthy, then `:`, then the expression for falsy. The running
example is one of "those obnoxious health apps": `exerciseTimeInMinutes < 30 ? "You need to try
harder" : "You're doing good"`. A later lesson (16:36) gives the professional caveat: "as
turnaries become more complex, they become harder to read. So, it's best to [keep them short]."

### Switch statements (15:27, 16:42)

A restaurant-menu example: each `case` matches a menu item string; `break` stops the fall-through
("otherwise it's going to run right across the page"); `default` is the fallback — "and the
default doesn't have to be at the end of the switch statement." The challenge ("we don't have
biscuits on our price list") checks that unmatched items hit `default`.

### Object destructuring (15:31)

> "Object destructuring enables us to [pull properties out into variables]… if there were 50
> properties in here that we wanted to use, that would take forever."

```js
const { name, chips } = player
```

The default-value form and renaming are drilled; a later aside (16:27) calls destructuring "a
concise way of" achieving what dot notation does verbosely.

### `setTimeout`, the call stack, and the event loop (15:36–15:51, repeated 16:51–17:06)

The most conceptual part of the module:

- JavaScript is single-threaded — it runs "one [piece of] code at a time in its single thread."
- The **stack** runs the current work; timer callbacks wait in a **task queue**.
- The **event loop**'s "job is to keep an eye on the task queue and the stack. And when the stack
  is [empty]" the queued callback finally runs.
- Consequence, stated plainly: long synchronous work makes timers "significantly delayed. And
  that by the way is a good thing. It's what we want" — the language stays responsive by
  deferring, not by parallelism.
- `setTimeout` extras: passing extra arguments to the callback, and `clearTimeout` (16:51).

### `import` and `export` (15:51)

Named exports and imports between files — "every export needs to have a [matching import]" —
previewing the module structure Node (Module 11) and React (Module 15) rely on.

### `Date()`, `Error()`, and constructor functions (15:59–16:18)

- The copyright-page problem: "web devs don't spend the 31st of December updating all of these
  manually."
- `const dateSnapshot = new Date()` — "we use the new keyword and we summon the date
  constructor… the uppercase first letter is crucial. The inbuilt constructors always have an
  uppercase first letter."
- A constructor is "a type of function"; `new Date()` says "give us a new instance of the date
  object."
- The `Error` constructor produces objects with messages and stack traces that make "debugging a
  whole lot easier."
- **BigInt** ("big int is short for big integer… append an `n`") and **numeric separators**
  (`1_000_000`) are quick practical asides for unreadable large numbers.
- **Scope and hoisting** (16:06–16:16): function declarations are hoisted and usable before
  their definition; `const`/`let` are hoisted but "only usable after initialization" (the
  temporal dead zone, shown not named); `var` "is a little bit more forgiving. We get undefined
  rather than an error. But that doesn't matter because you're not going to use var anyway."

### Super challenge #1 — the stock ticker (16:18)

A "fake stock API" module exports `getStockData`; the challenge renders a ticker with
`renderStockTicker(stocks)` — including "a price direction icon. We should also give it some
[alt] text" (a rare accessibility beat in a data-rendering lesson). SVG icons are imported
"individually three times or we could [import them] via the data array" — a taste of mapping
over assets.

### Function expressions and arrow functions (17:45–18:03)

- "Recognize that what you're looking at here is a function. We've got no [name]" — the same
  `function` keyword, now stored in a variable.
- The arrow refactor, step by step: "get rid of this function keyword… now we're only returning
  one line," so the braces and `return` can go ("we want that to [stay implicit]").
- The speed-camera challenge ("the driver's actual speed, in this case 40") drills single- vs
  multi-line arrows.

### `.map()`, `.reduce()`, `.join()` (17:53–18:18)

- `map`: "we've got a map method set up here… remember map [returns a new array]" — and the
  explicit comparison with `forEach` (18:04): one transforms, one iterates.
- `reduce`: "back, we studied the reduce method… pass the reduce method a function" —
  accumulator, current value, initial value; then `reduce` over an **array of objects**
  (staff/desk counts) and "it's worth taking time to get the reduce [method's stages] right."
- `join`: "let's join our array of template strings. And the separator is just going to be…" —
  glue for the HTML-string rendering pattern this module keeps returning to.
- The **dangers of `innerHTML`** appear as the recurring cleanup: rebuilding an element by
  setting "the inner HTML to an empty string" before re-rendering (16:25, repeated 17:40), with
  the string-concatenation pitfalls shown rather than lectured.

### The rest parameter, and first-class functions (18:03–18:18)

> "Well, the rest parameter is coming to the rescue."

`function greetUser(...args)` gathers "the ones that were not explicitly matched to a parameter"
into a real array. Functions as "first class citizens" (18:13) — passing functions to functions
— is the concept the whole module has been using with `map`/`reduce`.

### Super challenge #2 — property for sale (18:18–18:27)

The closing integration test, quoted from the challenge text: each card needs "an image, a
property location, a price, a comment… and the total property size in square meters. And each
object has an array with the size… of the individual rooms" — so the totals need `reduce`; if no
array is passed, a placeholder property object is rendered instead (default parameters +
destructuring). The solution imports the data, maps it to template strings, joins, and renders —
the module's whole toolkit in one function.

## Mapping to the syllabus activities

- **Sections 01–03**: no transcript segments — see the per-section notes above for where each
  *technique* is actually taught (setTimeout here; forms in Module 15; `.filter()` callbacks in
  Module 09).
- **Section 04 lesson numbers skip** (03 → 05 → 07…): challenge-file numbering, not missing
  video.
- **32. Spread Syntax**: only the rest parameter's `...` is taught (18:03); spread into arrays /
  objects is not.
- **34/36. Short-circuiting**: absent — `||`/`&&` are taught as logical operators in Module 03
  (09:36–09:51), but the value-returning short-circuit behaviour is never covered.
- **44. Constructor Functions to Classes**: constructor functions are taught; classes are
  explicitly deferred ("we'll also see classes and generators" — 16:16).
- **28. Twimba Ternary Refactor**: no Twimba exists; ternary refactoring is practised on the
  health-app and menu examples instead.

## What this module teaches (from the parts that exist)

1. Ternaries as compact conditionals — with a readability limit.
2. Switch statements, `break`, and `default` anywhere.
3. Destructuring objects into variables.
4. Asynchrony's machinery: stack, task queue, event loop, and why timers fire late.
5. `setTimeout`/`setInterval`, extra callback arguments, clearing timers.
6. `import`/`export` between files.
7. Built-in constructors (`Date`, `Error`), `new`, and instances.
8. BigInt and numeric separators for huge numbers.
9. Scope and hoisting: declarations vs initialisation, and why `var` misbehaves.
10. Function expressions, arrow functions, implicit returns.
11. `map` vs `forEach`, `reduce` (including over objects), `join`.
12. Rest parameters and functions as first-class values.
13. Integration: data in, template strings out, one render function.

## Small practice task

Rebuild super challenge #2 without looking, then extend it:

1. An array of at least four course objects: `{ title, instructor, hours, topics: [...] }`.
2. One function `renderCourses(courses)` that maps each course to a template string (title,
   instructor, hours, and a joined list of topics) and sets them into a `<ul>` via `innerHTML` —
   clearing the existing HTML first.
3. A destructured default parameter: `renderCourses(courses = placeholderCourses)` so an empty
   call renders a placeholder card.
4. One function `totalHours(courses)` implemented with `reduce`.
5. Use a ternary to append " (long course)" when `hours > 20`.
6. Split your code into two files with a named `import`/`export`.

Then write down, from memory, the order in which a `setTimeout` callback, a `console.log`, and
another `setTimeout` actually execute — and verify it.

## Readiness check for Module 08

Nothing in Module 08 depends on this module (it is a CSS module with no transcript coverage).
Before moving on, be able to explain:

- What the event loop is waiting for before your timer callback runs.
- Why `new Date()` needs `new` and a capital letter.
- The difference between `map` and `forEach`, and what `reduce`'s accumulator does.
- When a ternary is the wrong choice.
- What `const { a, b } = obj` does.

Carry forward honestly: **short-circuiting, spread syntax, classes, and all of Sections 01–03
(modal/dialog work, radio inputs, `classList`, feed rendering) are gaps** — the React module
will re-teach forms and class toggling in its own idiom, but not these vanilla-JS patterns.

## Exact syllabus order

1. **Build a Cookie Consent** *(no transcript coverage)*
   1. 01. Position the modal
   2. 02. Aside- setTimeout *(technique taught at 15:36, outside this project)*
   3. 03. Set the timer
   4. 04. Aside- element.style
   5. 05. Make the modal reappear
   6. 06. Close the modal
   7. 07. Aside- Forms
   8. 08. Add a form 1
   9. 10. Aside- Forms - challenge
   10. 11. Aside- Validation Attributes — Exercises 1–2
   11. 12. Submit the form
   12. 14. preventDefault Challenge
   13. 16. Add modal message
   14. 17. Add modal messages 2 — Exercises 1–3
   15. 18. Add modal messages 3
   16. 20. Form Data 1
   17. 21. Aside- FormDate methods
   18. 22. Form Data 2
   19. 23. Aside- Disabling elements
   20. 24. Disable the close button
   21. 25. There is no choice 1
   22. 27. Aside- Classlist Toggle Challenge
   23. 28. There is no choice 2
2. **Build a Meme App** *(no transcript coverage; a React meme generator exists at 36:20)*
   1. 03. Aside-for of
   2. 04. Use a for of
   3. 05. Nest the for of — Exercises 1–3
   4. 06. Render out the emotions 1
   5. 07. Render out emotions 2
   6. 09. Import the data
   7. 10. Aside- Radio Imputs
   8. 11. Render the radios inputs
   9. 12. Aside- .includes()
   10. 13. remove duplicates
   11. 15. Get the id of the clicked option
   12. 17. Aside- classist add_remove
   13. 18. Add colour to the selected emotion — Exercises 1–2
   14. 19. Aside- getElementsByClassName
   15. 20. Remove the highlight class
   16. 21. Aside- querySelector and why it_s useful
   17. 22. Connect the button
   18. 23. Has an emotion been chosen_
   19. 24. Aside- checkbox
   20. 25. isGif
   21. 26. Aside- filter() — Exercises 1–2
   22. 27. Aside - filter() 2
   23. 28. Find matches with .filter()
   24. 29. Animated GIFs Only
   25. 31. If there_s only one cat..._ — Exercises 1–2
   26. 32. If there_s more than one cat..._
   27. 33. renderCat()
   28. 34. Close the modal
3. **Build a X Clone** *(no transcript coverage)*
   1. 02. Import the data
   2. 04. Aside- TextArea — Exercises 1–3
   3. 06. Tweet Boilerplate Challenge
   4. 07. Aside- forEach()
   5. 08. Use forEach to build the html
   6. 09. Render the tweets to the feed
   7. 10. Aside- CDN Font Awesome
   8. 11. Add some awesome icons — Exercises 1–2
   9. 14. Aside- Data Attr JS and Challenge
   10. 16. Like a tweet part 2- data attributes
   11. 17. Like a tweet part 3- eventListener
   12. 18. Like a tweet part 4- handleLikeClick()
   13. 19. Like a tweet part 5- find the tweet object
   14. 22. Unlike a tweet
   15. 23. Flip a boolean
   16. 24. Retweet a tweet
   17. 25. Aside- Conditionally render CSS class
   18. 26. Color the icons — Exercises 1–2
   19. 27. Replies 1- get uuids of tweets with replies
   20. 28. Replies 2- HTML string for replies and to add to parent div
   21. 29. Replies 3- toggle hidden
   22. 30. Refactor the tweet btn — Exercises 1–2
   23. 32. Build the new Tweet object
   24. 33. Render a new tweet
   25. 34. UX fixes — Exercises 1–2
4. **Mini Projects** *(covered, 15:14–18:27)*
   1. 03. Object Destructuring Challenge
   2. 05. The .map() Method Challenge
   3. 07. The .join() Method Challenge
   4. 08. .map() vs .forEach()
   5. 10. The dangers of innerHTML
   6. 12. Beyond Function Declarations 2- Function Expression Challenge
   7. 14. Aside- Arrow functions challenge — Exercises 1–2
   8. 15. Aside- inline arrow function challenge
   9. 16. Import Export (named)
   10. 19. Aside .reduce() challenge
   11. 20. The .reduce() Method with Objects
   12. 21. The .reduce() Method with Objects Challenge
   13. 23. Super Challenge Set-up
   14. 27. Ternary Operator Challenge — Exercises 1–2
   15. 28. Twimba Ternary Refactor *(no Twimba; refactoring practised on other examples)*
   16. 30. The Rest Parameter Challenge
   17. 32. Spread Syntax (...) Challenge *(only the rest parameter is taught)*
   18. 34. Short-circuiting with OR (III) Challenge *(not covered)*
   19. 36. Short-circuiting with AND (&&) Challenge *(not covered)*
   20. 37. Switch Statements (new)
   21. 38. Constructors- Date()
   22. 42. Constructor Function Challenge
   23. 44. Constructor Functions to Classes Challenge *(classes deferred)*
   24. 45. Debugging- Errors — Exercises 1–2
