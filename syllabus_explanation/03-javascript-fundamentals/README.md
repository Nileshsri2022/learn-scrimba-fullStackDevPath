# Module 03: JavaScript Fundamentals

## Completion status

**Complete for the supplied source files.** All four syllabus sections have contiguous, thorough
transcript coverage (05:30–14:02 — about 8.5 hours, the longest single course in the video). The
transcript also contains three things the challenge-file syllabus does not list:

1. A **GitHub Desktop / GitHub Pages interlude** by Treasure after the basketball scoreboard
   (07:07–07:20).
2. A **password generator solo project** (10:38–10:41) and a **unit converter solo project**
   (13:59–14:02) — both named in the course intro, neither has a folder in this module.
3. An **AI-and-the-learner aside** by Tom (10:03–10:12) on using ChatGPT without letting it
   replace the practice that makes the learning stick.

The module's instructor is **Per Harald Borgen** throughout (the subway-counter story at 05:30 is
his), with Treasure and Tom dropping in for the asides above.

## How the sources relate

The transcript is one continuous "learn JavaScript" course; the syllabus is its challenge-file
skeleton. Section numbers in the syllabus skip (no Section 03, no Section 05) because those
sections have no challenge folders — not because content is missing.

### Transcript map

| Transcript time | Content | Syllabus section |
|---|---|---|
| 05:30–07:03 | Passenger counter app + first challenges | 01 |
| 07:03–07:07 | Basketball scoreboard solo project | 02 |
| 07:07–07:20 | Treasure: publish the project (GitHub Desktop, GitHub Pages) | — (extra) |
| 07:20–10:02 | Blackjack game | 04 |
| 10:02–10:12 | Methods on objects + Tom's AI aside | 04 (tail) + extra |
| 10:12–10:38 | JavaScript challenges (set 1) | 04, lesson 56 |
| 10:38–10:41 | Password generator solo project | — (extra) |
| 10:41–13:27 | Chrome extension (leads tracker) + challenges (set 3) | 06 |
| 13:27–14:02 | More challenges + unit converter solo project | 06, lesson 56 |

---

## Section 01 — Build a Counter App (05:30–07:03)

### Why a passenger counter (05:30)

> "When I was 19… my full-time job was to count people who entered the subway… I would bring up my
> pen and paper and note down the number six… it would have been so much better if I had a little
> people counter app on my Nokia phone."

The frame for the whole section: a real (if unglamorous) problem, solved one language feature at a
time.

### Your first JavaScript variable (05:36)

```js
let count = 0
```

- `count` is a variable — "a tiny piece of data" given a name.
- `let` creates it; the value can be replaced later.
- The `<script>` tag is added to the HTML `body`, and `console.log()` prints to the console so
  you can *see* what the program knows.

### Basic mathematical operations (05:42)

`+`, `-`, `*`, `/` on numbers; the result can be stored in another variable
(`let lapsCompleted = 4` etc.). "JavaScript starts reading at the top and works its way
downwards" — order of statements matters.

### Reassigning and incrementing (05:45)

```js
lapsCompleted = lapsCompleted + 1
```

Reading it exactly as the lesson does: take the old value, add one, put it back. The shorthand
(`+=`) arrives later, in the counter itself (06:30), as a deliberate "here's a tidier version of
something you've already written."

### Adding a button and your first function (05:48–06:03)

HTML button first, then the function that will run when it is clicked:

```js
function increment() {
  count += 1
  console.log(count)
}
```

Two vocabulary points that recur all module:

- **Declaring** a function (writing it) does not run it; **invoking/calling** it does. "If we run
  the code now… nothing happens of course because we also have to call the function."
- Wiring the button uses an inline `onclick` handler first (`onclick="increment()"`) — the same
  job is later redone properly with `addEventListener` in the Chrome extension section, and the
  course says so explicitly when it happens (10:57).

The teaching method is stated out loud at 06:01: "It's much better than me writing everything…
you are going to" turn pseudo-code into real code yourself — and "verify that it works [after]
every single step so that… you will have a better understanding of where [the bug] happened."

### Display the count with `innerText` (06:06)

The DOM makes its first appearance — "It's short for **d**ocument **o**bject **m**odel":

```js
let countEl = document.getElementById("count-el")
countEl.innerText = count
```

- the browser exposes the page as objects; `document` is one of them;
- `getElementById` grabs the element whose `id` matches the string;
- `innerText`/`textContent` write into it — the program can now *change the page*, not just log.

A small honesty note at 06:07: `console.log` and `document.getElementById` are "hooked onto
so-called objects… methods on objects. But don't worry about that" — the full explanation is
deferred to 10:02.

### The save button, and strings (06:12–06:24)

A second button saves the current count and resets it to zero (06:42: "you need to do here count
equals zero as well"). Strings are introduced as the second data type — "strings are used all over
the place in software" — with quotes as delimiters, and then the classic trap:

> "Okay, let's run this. The result is 410. That is weird because perhaps you expected 14. No, as
> I said, **the string always wins**."

When `+` sees a string and a number, the number is coerced to a string and the two are
concatenated. The drill that follows predicts four `console.log`s before running them
(`4 + 5 → 9`, `"2" + "4" → "24"`, `"5" + 1 → 51`, `100 + "100" → "100100"`).

### Rendering messages, concatenation (06:27–06:36)

The welcome-El paragraph gets a greeting built by concatenation: `"Welcome back, " + name + " 👋"`.
`+=` is reused for the count. The save feature renders the previous entries into a second element
— the counter app is now a real (tiny) application, and the section's challenges
(*Variables practice*, *Concatenate two strings in a function*, *Incrementing and decrementing*,
*Strings and numbers*, *Rendering an error message*, *Calculator challenge*, *Arithmetic Operator
Precedence*) drill exactly these mechanics — the calculator challenge is where operator precedence
(`*` before `+`) is discovered.

### The DOM recap (06:45)

> "So we interacted with the DOM at several places… up here where we [grabbed elements]"

The recap names the loop that defines front-end JavaScript: state in variables → events change the
state → the DOM is re-rendered from the state.

---

## Section 02 — Solo Project — Basketball Scoreboard (07:03–07:07)

> "Okay, it is time to remove the training wheels and have you build your very own project from
> scratch… this basketball scorecard."

- **Requirements:** six buttons (three per team) that add 1, 2 or 3 points to the right counter,
  following a supplied Figma design. "You are to build this from scratch — or I write that in
  quotes because I've given you a little bit of a skeleton."
- **Stretch goals** come with an honest warning: "in this JavaScript module, I haven't really
  taught you the concepts you need… a new game button [that] sets both of these scores to zero…
  highlight which team is leading… more counters… even a countdown timer. Though, this is really
  complex. It's far beyond the scope of the JavaScript I've been teaching you so far."
- **Figma workflow:** duplicate the shared file ("that's how Figma works. It's a multiplayer
  app"), follow the linked 10-minute Figma tutorial if lost, use the help section for hints.
- The skeleton leaves the JavaScript "a completely blank file" on purpose.

The mapping trick students need (adding to `num1El`/`num2El`, converting numbers to strings when
rendering) is exactly the counter app's pattern — the project tests transfer, not new knowledge.

### Treasure's interlude — put it on the web (07:07–07:20)

> "Hello students. My name is Treasure… congratulations on completing yet another solo project…
> now we have to get this project up on the web to share with the world."

The lesson: the drag-and-drop upload to GitHub "is a perfectly fine way" for one-off projects, but
real development uses **version control, a tool to keep changes updated on GitHub**. Enter
**GitHub Desktop** — "a tool made by GitHub that offers a really nice [GUI]" — and GitHub Pages:

1. Sign in to GitHub Desktop, create a repository ("remember that a repository is basically a
   folder" — echoing Bob's Module-02 aside).
2. Write a commit message, **commit to main**, then **publish**.
3. In the repo settings, enable GitHub Pages, wait for the deployment, and visit the live URL.

This segment is the bridge between the "upload files" workflow and Module 04's full Git course.

---

## Section 04 — Build a Blackjack Game (07:20–10:38)

> "Hey, and welcome to building blackjack… this section, of course, is to make you feel as cool
> as I did in 2016."

### Cards, sum, and the first `if…else` (07:21–07:30)

```js
let firstCard = 10
let secondCard = 4
let sum = firstCard + secondCard
```

Then the first conditional:

```js
if (sum < 21) {
  console.log("Do you want to draw a new card?")
} else if (sum === 21) {
  console.log("Wohoo! You've got Blackjack!")
} else {
  console.log("You're out of the game!")
}
```

The lesson is careful about `=` vs `===`: "here we are saying that we want the sum to *become*
first card plus second card. But here we're *asking* — is the sum strictly equal to 21… just use
three equal marks when you write [comparisons]." (`==` vs `===` is promised "later" and delivered
at 07:33 with the `100 === "100"` example — same value, different types, so not strictly equal.)

### Booleans and the `isAlive` flag (07:39–07:51)

A boolean ("yes or no… is there a data type in JavaScript that you think might be" right for
that) tracks game state: `let isAlive = true`, flipped to `false` when the player busts, along
with `let hasBlackJack = false`. Practice drills comparisons (`<=`, `>=`) before the state is
used.

### The `message` variable, styling, and the start button (07:51–08:24)

`let message = ""` is assigned inside the branches and rendered to a paragraph — the same
render-from-state pattern as the counter. A stylesheet is linked ("CSS is short for cascading
stylesheets" — revision from Module 02), the message/sum/cards elements are grabbed by id, and
`startGame()` becomes the single entry point that renders all three.

### `newCard()`, and renaming `startGame` (08:21–08:30)

A second button draws a card, adds it to the sum, and re-renders. The refactor lesson renames the
start function to `startGame()` and introduces the render-everything helper — "this way of [only
rendering from one function]… it still works" — a first taste of single-source-of-truth design.

### Aside — arrays (08:25–08:45)

> "Actually to use what's called an array… arrays are ordered lists of [values]… you're most
> likely going to use arrays as a data structure [for rendering] stuff."

- Syntax: `let cards = [firstCard, secondCard]`.
- **Zero-based indexing** is drilled hard (08:33): "in real life you start counting at one. But
  in arrays you start [at zero]" — including the trap that `array[array.length]` is out of range
  because "the length of an array is always one larger than" the last index.
- Mixed data types are allowed; `push`/`pop` add and remove from the end
  (*push, pop, unshift, shift* practice covers the front-of-array pair too).

### Aside — loops (08:51–09:06)

```js
for (let i = 0; i < cards.length; i++) {
  console.log(cards[i])
}
```

The three-part header is read out loud: start at zero ("because zero is where we want to start"),
keep going while the condition holds, increment after each pass. The payoff: "you can't simply
hardcode out all of the console [logs]" — loops plus arrays render any number of cards, e.g. a
`cardsEl.textContent = cards[0] + " " + cards[1]` looped into one string.

### Aside — returning values (09:06)

Functions that *return* instead of log: `return` hands a value back to the caller and exits
immediately. The dice example turns this into `getRandomCard()` next.

### Aside — `Math.random()`, `Math.floor()`, and dice (09:15–09:33)

- `Math.random()` generates a number "between 0.0000… and 0.999…".
- Scaling and flooring: `Math.floor(Math.random() * 6) + 1` for a die — the +1 exists because
  flooring throws away the fraction and six itself is barely reachable without it.
- The full dice function is assembled piece by piece, then reused as `getRandomCard()` (with the
  blackjack rule that 11 → 11, but the course keeps it simple).

### Logical operators (09:36–09:51)

`&&` ("what does that do? Well, it allows you to check if… this condition [is] true **or** this
one" — actually *both*, and the challenge at 09:45 fixes that misconception) and `||` for either.
The rule taught: `newCard()` may only fire `if (isAlive === true && hasBlackJack === false)`.

### Aside — objects (09:51–10:02)

> "One way to think of objects is that they give you the ability to store data in depth."

The course object example (title, lessons, creator — "the CSS grid course, actually the very
first course we launched") is translated into JavaScript:

```js
let course = {
  title: "Learn CSS Grid for free",
  numOfLessons: 15,
  creator: "Per Harald Borgen",
  length: 63,
  level: 2,
  isFree: true
}
```

Player data follows (`let player = { name: "Per", chips: 145 }`), accessed and reassigned via dot
notation. The section closes the loop it opened at 06:07 — **methods are functions attached to
objects** (10:02), which is "the exact same thing we're doing… when we're saying document dot
getElementById… Math is an object and random is a function on that object… even our good old
friend console.log."

### Tom's aside — AI and the coding student (10:03–10:12)

> "AI tools like chat GPT have taken the world by storm… AI is here to stay and it does have
> implications… for you as a learner."

Tom pastes a Scrimba challenge into ChatGPT, gets a correct answer, and then makes the module's
most quotable pedagogical point: copying the answer feels like progress but skips the retrieval
practice that builds "muscle memory." The advice is to use AI as an *explainer* — "paste the
error, ask what it means" — not as a substitute for typing the code, and to keep building the
things "you're going to feel like you've become somewhat of a genius" for building yourself. (The
full treatment of AI tools lives in Module 10.)

### JavaScript challenges (10:12–10:38)

The practice set named in the syllabus (*Objects and functions*, *if else*, *Loops and arrays*,
*push, pop, unshift, shift*, *Logical operators*, *Rock papers scissors*, *EmojiFighter*,
*Sorting fruits*) runs here: a discount calculator ("6 to 17 gives a child discount. 18 to 26
gives a student discount"), loop-and-array rendering, the four array methods, a random duel, and
a sort. Then the **password generator** solo project (10:38): "It has only one piece of
interactivity… the user can [click a button to] generate two random passwords" — a stretch of the
dice logic into strings, with `.toFixed` and `Number()` debugging appearing in its wake.

---

## Section 06 — Build a Chrome Extension (10:41–13:59)

> "Welcome to this section where we are going to build a Chrome extension, which is just so
> freaking cool… This is an example called Honey… it was acquired by PayPal for $4 billion."

The pitch (10:41–10:48) tours Honey, Grammarly, and Momentum to establish what extensions are;
then the actual project is introduced as "actually a pretty useful tool for sales
representatives" — a **lead tracker** that saves URLs.

### Button, input, and `onclick` vs `addEventListener` (10:48–11:03)

The UI (input + two buttons: save input, delete all) is styled first — including a deliberate
`margin: 0` / `padding` review and the discovery that `box-sizing` decides whether "full width
includes the paddings as well" (10:51). The first wiring uses `onclick` from the counter app;
then (10:57):

> "I think it's about time that you learn both of these methods."

```js
inputBtn.addEventListener("click", function () {
  console.log("Button clicked from addEventListener()")
})
```

The refactor lesson deletes the `onclick` attribute — separation of HTML and JS is the stated
reason.

### `myLeads`, `let` vs `const`, and pushing (11:03–11:15)

- `let myLeads = []` plus `inputEl = document.getElementById("input-el")`.
- The rule of thumb (12:45, stated while refactoring): "if you can use const then use const
  because it enforces strictness throughout your codebase" — use `let` only when the variable is
  reassigned.
- `myLeads.push(inputEl.value)` — and `inputEl.value` is read at click time, which is why reading
  it earlier captures an empty string (a planted bug the challenge asks you to find).

### Rendering: `innerHTML`, `createElement`/`append`, and performance (11:15–11:42)

Three generations of the same feature:

1. A `for` loop + `ulEl.textContent += "<li>" + myLeads[i] + "</li>"` — **doesn't work**:
   `textContent` writes literal text, not markup. The fix is `innerHTML`, which parses the string
   as HTML.
2. Building `<a>` elements so each lead is a clickable link (target="_blank" for the tab).
3. `createElement` + `.append()` — "we've removed a ton of [string building]… this is simply
   replacing this here with" DOM nodes; the performance lesson explains why injecting nodes beats
   re-parsing strings, and both are kept in the toolbox.

All of it is wrapped in `renderLeads()` so the same code serves every render (11:36), and the
input is cleared after saving (11:39).

### `localStorage` (12:12–12:24)

The API is taught as key/value strings:

```js
localStorage.setItem("myLeads", JSON.stringify(myLeads))
const stored = JSON.parse(localStorage.getItem("myLeads"))
```

The round-trip is spelled out: "we have gone from string to array back to string again." The
refresh test — "refresh this page again, boom, our leads are gone. Or actually, they're not gone"
— is the moment persistence clicks. (Module 03's *save to localStorage* practice item is exactly
this.)

### Truthy and falsy (12:27–12:42)

> "So let's learn about truthy and falsy values."

`if (leadsFromLocalStorage)` works because an empty string/array-ish value is falsy — the course
uses it to decide whether to restore saved leads, and warns that "an empty array wouldn't do the
trick" for `JSON.parse(null)`-style edge cases. The *Guess the expression* practice is this
drill.

### The delete button (12:43–12:53)

Styled white-on-green ("we also seemingly lost the text, but that's not the case. It's just
white, so it blends in with the background"), then made real in a three-part challenge ending
with `localStorage.clear()` and a re-render.

### Function parameters (12:54–13:27)

```js
function greetUser(name) {
  welcomeEl.textContent = "Welcome back, " + name + " 👋"
}
greetUser("Per Harald Borgen")
```

The lesson's framing: the first version "is a really bad function because it can only render out
this string… it can only render out my name, which is pretty silly." **Parameters** are the
placeholders; **arguments** are the values passed in (13:06) — "from now on [I'll] call them
arguments" when invoking. Multiple parameters, numbers, and arrays all pass through, and
`renderLeads(leads)` is refactored to take the array as a parameter (13:12) instead of reading
the global.

### Template strings (13:00)

The final rendering upgrade replaces concatenation:

```js
ulEl.innerHTML += `<li><a target='_blank' href='${lead}'>${lead}</a></li>`
```

Backticks, `${}` interpolation, multi-line strings without `+` — "greeting and name which we need
to escape out from the string" becomes unnecessary. (The transcript teaches this just after
parameters, slightly out of the syllabus's listed order.)

### The tab button, and the second extension (13:18–13:27)

A "save tab" button uses the **Chrome tabs API** — `chrome.tabs.query({active: true,
currentWindow: true})` — which requires adding `"permissions": ["tabs"]` to `manifest.json`.
The instructor's note: "this is an API" — the first time the word is used for something students
*consume*, previewing Module 09. A second mini-extension exercise then reuses the pattern.

### JavaScript challenges, part 3 (13:27–13:59)

The named practice set (*let & const*, *Log out items in an array*, *save to localStorage*,
*addEventListener and object in array*, *Generate sentence*, *Render images*, *Rounding numbers*,
*Convert string to number*) — including a deliberate debugging lesson (13:49–13:59) where an
error message is Googled: "I'm actually omitting the total price from the error message because…
it definitely won't include that" — stripping your variable names before searching is itself the
skill. The **unit converter** solo project follows (13:59–14:02), closing the course with a
second deployment of the same variables/functions/render loop.

## Mapping to the syllabus activities

Every syllabus lesson for sections 01, 04 and 06 is covered above. Honest notes:

- **Section 03 and Section 05 do not exist** in the challenge files — no transcript gap.
- **02 Solo Project — Basketball Scoreboard** is one folder with no lessons; the transcript
  treats it as a requirements walkthrough (07:03–07:07) plus Treasure's publishing interlude.
- **01.03 "Write your first JavaScript variable"** and neighbours: transcript numbering and
  syllabus numbering don't align one-to-one; coverage is complete but sequenced by the course's
  own build order.
- The **password generator**, **unit converter**, Treasure's **GitHub Desktop** interlude, and
  Tom's **AI aside** are transcript-only extras with no challenge folder.
- *EmojiFighter*, *Rock papers scissors*, *Sorting fruits* are named in the syllabus; the
  transcript runs equivalents (random duels, discounts, sorts) without always using the same
  names.

## What this module teaches

1. Variables (`let`/`const`), numbers, strings, booleans — and coercion ("the string always
   wins").
2. Functions: declaration vs invocation, parameters vs arguments, `return`.
3. Conditionals: `if`/`else if`/`else`, `===` vs `=`, logical `&&`/`||`, truthy/falsy.
4. Loops: the three-part `for` header, looping over arrays by index.
5. Arrays: ordered, zero-indexed, `push`/`pop`/`unshift`/`shift`, `.length`.
6. Objects: key/value pairs, dot notation, methods as functions on objects.
7. The DOM: `getElementById`, `innerText`/`textContent`, `innerHTML` vs
   `createElement`/`append`.
8. Events: `onclick` attributes vs `addEventListener`.
9. Persistence: `localStorage` with `JSON.stringify`/`JSON.parse`.
10. Template strings with backticks and `${}`.
11. Browser power: Chrome extensions, `manifest.json`, the tabs API.
12. Process: verify after every step, read error messages, Google them without your variable
    names, and use AI to explain rather than to replace practice.

## Small practice task

Build a **reading-list tracker** (the leads tracker, re-specified):

1. An input and two buttons: *Add book* and *Clear list*, plus a `ul` for rendering.
2. `addEventListener` on both buttons (no inline `onclick`).
3. Store entries in an array; render each as an `<li>` containing a link — build the list items
   with `createElement`/`append` (not `innerHTML`).
4. Persist the array in `localStorage` via `JSON.stringify`, restore it on load with
   `JSON.parse`, and guard the restore with a truthy/falsy check.
5. Clearing must empty both the array and `localStorage`, then re-render.
6. Write one function `renderBooks(books)` that takes the array as a parameter and is the only
   place that touches the `ul`.

Before checking the result, predict what happens on refresh, on double-click, and on an empty
input — then verify all three.

## Readiness check for Module 04

You are ready to move on when you can explain:

- The difference between declaring and calling a function, and between a parameter and an
  argument.
- Why `===` and `=` are not interchangeable, and what `"2" + 4` evaluates to.
- What truthy and falsy mean, with one example each.
- Why `array[array.length]` is a bug.
- `textContent` vs `innerHTML`, and one reason to prefer `createElement`.
- What `JSON.stringify` is for, given that `localStorage` only stores strings.
- Why the same button wired with `onclick` and again with `addEventListener` fires twice.
- What a Chrome extension's `manifest.json` is for.

(Module 04 changes topic to the command line and Git — no JavaScript is required there — but
Treasure's GitHub Desktop interlude at 07:07 is the best bridge into it.)

## Exact syllabus order

1. **Build a Counter App**
   1. 03. Write your first JavaScript variable
   2. 04. Basic mathematical operations
   3. 05. Reassigning and incrementing
   4. 06. Adding a button
   5. 09. Write your first function
   6. 10. Write a function that logs the sum
   7. 11. Write a function that increments
   8. 12. Increment on clicks
   9. 15. Display the count with innerText
   10. 16. Create the save button
   11. 18. Write your first string variable — Exercises 1–2
   12. 19. Log a greeting to the console
   13. 20. Strings vs. Numbers
   14. 22. Render a welcome message
   15. 23. Improve the message with string concatenation
   16. 24. Use plus equal for count
   17. 25. Create the save feature
   18. 27. Set the count to 0
   19. 29. JavaScript challenges — Practices 01–07 (Variables practice … Arithmetic Operator
       Precedence)
2. **Solo Project — Basketball Scoreboard** *(requirements walkthrough + Treasure's GitHub
   Desktop / GitHub Pages interlude, 07:03–07:20)*
3. **Build a Blackjack Game**
   1. 01. Add the firstCard, secondCard, and sum
   2. 03. Your first if...else statement
   3. 04. if_else...if_else statement
   4. 05. The if...else statement for our game
   5. 08. Add the isAlive variable
   6. 09. Let_s practice boolean conditions
   7. 10. Add the message variable
   8. 11. Link to stylesheet
   9. 12. Add basic styling
   10. 13. Make the start button work
   11. 14. Display the message
   12. 15. Display the sum
   13. 16. Display the cards
   14. 17. New card button
   15. 18. Add to the sum when newCard is clicked
   16. 19. Rename the startGame function
   17. 21. Aside- Intro to arrays
   18. 22. Aside- Array indexes
   19. 23. Arrays with multiple data types
   20. 24. Array- Array.push() and .pop() — Exercises 1–2
   21. 25. Creating the cards array
   22. 26. Push a new card to the array
   23. 27. Aside- Loops
   24. 28. Write your first loop
   25. 30. Write your first array-based for loop
   26. 31. For loops, arrays, and DOM — Exercises 1–2
   27. 32. Use a loop to render cards
   28. 34. Aside- Returning values in functions
   29. 35. Use a function to set the card values
   30. 36. Aside- Math.random()
   31. 37. Math.random() _ 6
   32. 38. Flooring the number with Math.floor()
   33. 39. Using Math.random() and Math.floor() to create a dice
   34. 40. Completing our dice function — Exercises 1–2
   35. 41. Make getRandomCard() work
   36. 42. Complete getRandomNumber function
   37. 43. Assign values in the startGame function
   38. 46. Write your first logical operator
   39. 47. Aside- The OR operator (II)
   40. 48. Only trigger newCard() if you_re allowed to
   41. 51. Create your first object
   42. 52. Use an object to store player data
   43. 56. JavaScript challenges — Practices 01–08 (Objects and functions … Sorting fruits)
4. **Build a Chrome Extension**
   1. 01. Add button and input tag
   2. 02. Style the button and input tag
   3. 03. Make the input button work with onclick
   4. 05. Write your first addEvent Listener()
   5. 06. Your turn to refactor
   6. 07. Create the myLeads array and inputEI
   7. 08. When to use let and const
   8. 09. Push to the myLeads array
   9. 10. Push the value from the input field
   10. 11. Use a for loop to log out leads
   11. 12. Create the unordered list
   12. 13. Render the leads in the unordered list
   13. 15. Write your first innerHTML
   14. 16. More innerHTML practice
   15. 17. Render the _li_ elements with innerHTML
   16. 18. Use createElement() and append() instead of innerHTML
   17. 19. Improving the performance of our app
   18. 20. Create the render function
   19. 21. Clear the input field
   20. 23. Add the _a_ tag
   21. 25. Write your first template string
   22. 26. Make the template string even more dynamic
   23. 27. Template strings on multiple lines
   24. 28. Refactor the app to use a template string
   25. 30. Style the list
   26. 34. Your first localStorage
   27. 35. Storing arrays in localStorage
   28. 36. Save the leads to localStorage
   29. 37. Get the leads from localStorage
   30. 39. Guess the expression - truthy or falsy_
   31. 40. Checking localStorage before rendering
   32. 41. Style the delete button
   33. 42. Make the delete button work — Exercises 1–2
   34. 44. Write your first function parameter
   35. 45. Functions with multiple parameters — Exercises 1–2
   36. 46. Numbers as function parameters
   37. 47. Aside- Arguments vs Parameters
   38. 48. Arrays as parameters
   39. 49. Refactor renderLeads() to use a parameter
   40. 50. Create the tabBtn
   41. 51. Save the tab url
   42. 56. JavaScript challenges - part 3 — Practices 01–08 (let & const … Convert string to
       number challenge)
