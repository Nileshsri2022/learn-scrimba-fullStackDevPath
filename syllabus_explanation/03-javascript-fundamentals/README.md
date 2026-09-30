# Module 03: JavaScript Fundamentals

## Completion status

**Covered by the transcript.** JavaScript is taught from a standing start, roughly **05:32 to
~12:50**, across three built projects plus one solo project.

- **Section 01 — Build a Counter App:** fully covered. A subway/people counter.
- **Section 02 — Solo Project: Basketball Scoreboard:** this is a **solo project** — the syllabus
  lists no lessons for it, and there is no walkthrough on tape. You apply Section 01's skills yourself.
- **Section 04 — Build a Blackjack Game:** fully covered. Conditionals, booleans, arrays.
- **Section 06 — Build a Chrome Extension:** fully covered. A "leads tracker" using arrays and
  `localStorage`.

The teacher is **Per Borgen** (Scrimba's CEO), with brief appearances from other Scrimba staff
("Gil"). Section/lesson numbers skip in places (Section 01 jumps 03 → 04 → … with recap scrims
between); the content of the skipped numbers is folded into the lessons below.

---

## Section 01 — Build a Counter App

### Getting JavaScript onto the page (lesson 03 setup)

You can write JS inside a `<script>` tag in the HTML, but that's "an amateurish way to do it." The
proper setup is an external file linked by `src`:

```html
<script src="index.js"></script>
```

The very first demonstration — grabbing an element and changing its text — is the DOM in miniature:

```js
document.getElementById("count-el").innerText = 5
```

> "Hey HTML document, I want to get an element and I want to get it by its ID... and then we can do
> `.innerText` set that equal to five."

### Lesson 03 — Your first variable

```js
let count = 0        // "let count be zero"
console.log(count)   // prints 0
```

`console.log` is "a tool that every single developer uses every single day," available in every
browser's dev tools (right-click → Inspect → Console). A key early gotcha — **you can't use a
variable before it's declared**:

```js
console.log(myAge)   // ReferenceError: Cannot access 'myAge' before initialization
let myAge = 35
```

"JavaScript starts reading at the top and works its way downwards."

### Lesson 04 — Basic mathematical operations

JavaScript is a calculator: `+ - * /`. Real code uses variables, not hardcoded numbers:

```js
let firstBatch = 5
let secondBatch = 7
count = firstBatch + secondBatch   // 12
```

### Lesson 05 — Reassigning and incrementing

A `let` variable can be reassigned; JS "uses the latest value it can find." To increment, put the
variable on both sides of `=`:

```js
count = count + 1   // take the current count, add one, store it back
```

(Later, lesson 24 introduces the shorthand `count += 1`.)

### Lesson 06 + 09–12 — Buttons and functions

The button calls a function via the `onclick` HTML attribute:

```html
<button onclick="increment()">INCREMENT</button>
```

```js
function increment() {
  console.log("button was clicked")
}
```

- `function` keyword + name + `()` + `{ }`. Code inside the curly brackets is the **body**, and runs
  every time the function is **called / invoked** (same thing).
- Declaring a function does nothing on its own — "we have taught JavaScript to countdown, but in
  order for it to actually do the counting, we have to say `countdown()`."
- Functions **remove repetition** (the race-car countdown example): extract repeated lines into one
  named command and call it whenever needed.

**Scope:** a function can read variables from the outer (**global**) scope, but a `let` declared
*inside* a function only exists inside it — `let` variables are **block-scoped**:

```js
function logLapTime() {
  let totalTime = lap1 + lap2 + lap3   // can read outer laps
  console.log(totalTime)
}
console.log(totalTime)   // ReferenceError: totalTime is not defined
```

Wiring it into the counter:

```js
let count = 0
function increment() {
  count = count + 1
  console.log(count)
}
```

### Lesson 15 — Display the count with innerText

Break the original one-liner into "get the element" then "modify the element," and store the element
in a **camelCase** variable (dashes aren't valid in JS names):

```js
let countEl = document.getElementById("count-el")
// ...inside increment():
countEl.innerText = count
```

`document.getElementById` returns a JavaScript **representation** (a model) of the element, which you
can then manipulate. Later the course switches `innerText` → **`textContent`** after checking MDN
(the Mozilla Developer Network) — `textContent` is the better default.

### Lessons 18–25 — Strings and the save feature

Your second data type is the **string**. Build messages with **concatenation** (`+`), remembering to
add spaces yourself:

```js
let fullName = firstName + " " + lastName   // space is its own string
```

Quote nesting matters: wrap a string containing an apostrophe in double quotes (`"you've"`) so JS
doesn't think the apostrophe ends the string.

The **save** feature resets the display — but you must reset **both** the DOM *and* the variable:

```js
function save() {
  countEl.textContent = 0
  count = 0          // WITHOUT this, the next click jumps back to the old count
}
```

> "JavaScript remembers what we've done previously unless we refresh the entire browser... You got to
> give JavaScript very specific instructions."

### A flagged best practice

A guest (Gil) notes that `onclick` in the HTML is intuitive but mixing structure and behaviour
"can lead to code that is harder to maintain." The recommended `addEventListener` approach comes
later (and is used in the Chrome extension project).

### Section recap (lessons 27–29)

Concepts locked in: the `<script src>` setup, `let` variables, the **number** and **string** data
types, math and incrementing, **functions** (declare vs invoke), and the **DOM** — "how to use
JavaScript to change the website" — via `getElementById`, `innerText`/`textContent`, and
`console.log`. Lesson 29 is a batch of quickfire challenges (variables, concatenation in a function,
incrementing/decrementing, strings vs numbers, an error message, a calculator, operator precedence).

---

## Section 02 — Solo Project: Basketball Scoreboard

No walkthrough exists — this is a **solo project**. Using only Section 01's skills (variables,
functions, `getElementById`/`textContent`, `+= `), you build a scoreboard where buttons add points to
a home and away score and a reset button zeroes both. It's the "active retrieval" checkpoint before
Blackjack.

---

## Section 04 — Build a Blackjack Game

### Lesson 01 — firstCard, secondCard, sum

```js
let firstCard = 6
let secondCard = 9
let sum = firstCard + secondCard
```

### Lessons 03–05 — if / else if / else

The game rules translate into a conditional. The `<` and `>` "alligator mouth" from school; the
`===` **strict equals** for comparison (distinct from the single `=` assignment):

```js
if (sum < 21) {
  console.log("Do you want to draw a new card?")
} else if (sum === 21) {
  console.log("You've got blackjack!")
} else {
  console.log("You're out of the game!")   // any other case must be > 21
}
```

The final branch can be a plain `else` — "if sum is not less than 21 and it's not exactly 21 either...
then it must be over 21. There's no other alternative in the entire universe."

`<=` (less than *or equal to*) is inclusive of the boundary; choose your number accordingly
(`age < 21` vs `age <= 20`).

### Lessons 08–09 — Booleans

The **boolean** data type (`true`/`false`) tracks game state:

```js
let isAlive = true
// ...inside the else (bust) block:
isAlive = false
```

And a crucial insight: **the expression inside `( )` is itself evaluated to a boolean**. `sum === 21`
becomes `21 === 21` → `true`, so that branch runs. Conditionals are just booleans under the hood.

### `===` vs `==`

Use **triple equals**. Double equals (`==`) is "less strict" — it converts types, so `100 == "100"`
is `true`. Triple equals does **not** convert: `100 === "100"` is `false`. "Ignore double equals...
This forces you to be a bit more mindful about how you are checking your conditionals."

### Lessons 10–19 — Rendering to the DOM

Same three-step pattern for the message, sum, and cards: add an `id` in the HTML, grab it into a
camelCase variable, set its `textContent`, keeping any static label text:

```js
let sumEl = document.getElementById("sum-el")
sumEl.textContent = "Sum: " + sum
```

> **`querySelector` aside:** `document.querySelector("#sum-el")` selects by **CSS selector** — `#`
> for an id, `.` for a class, or a bare tag name for an element. It's more powerful/dynamic than
> `getElementById`, but the course sticks with `getElementById` "to avoid the added complexity."

### Lessons 21–23 — Arrays

To hold "all the cards regardless of how many," use an **array** — an ordered list, written with
square brackets and **zero-indexed**:

```js
let cards = [firstCard, secondCard]
cards[0]   // firstCard  (index starts at 0)
cards[1]   // secondCard
```

The LinkedIn example grounds it: promotions, "people also viewed," featured posts, work experience —
all lists an app would store as arrays. Commas go **between** items, not after the last one.

### for loops (the render-all mechanism)

To display every card no matter how many, a **for loop** iterates the array — the tool that lets one
piece of code run once per item, replacing hardcoded `cards[0]`, `cards[1]`.

---

## Section 06 — Build a Chrome Extension

A **leads tracker**: save URLs of prospects while browsing.

### Loading the extension

Go to `chrome://extensions`, toggle **Developer mode** on, click **Load unpacked**, and pick the
`leadsTracker` folder. The extension now appears behind the puzzle-piece icon and works on any page.

### The critical flaw → arrays + push

Saved leads vanish when the popup closes ("every time we open up our Chrome extension, it's a full
refresh"). Leads are collected in an array and appended with **`push`**:

```js
let myLeads = []
myLeads.push(inputEl.value)
```

### `addEventListener`

The recommended event pattern (finally replacing `onclick`):

```js
saveBtn.addEventListener("click", function () {
  myLeads.push(inputEl.value)
  // ...render + persist
})
```

### localStorage — persistence across refreshes

Explored first in the browser's dev tools (Application → Local Storage): a per-domain, per-user
"kind of like a local database" of key/value pairs.

```js
localStorage.setItem("myLeads", "sample-lead.com")   // save
let leads = localStorage.getItem("myLeads")          // retrieve
localStorage.clear()                                 // wipe it
```

Data survives a page refresh — exactly the feature needed. **The catch: `localStorage` stores only
strings.** To persist the array you must serialise it, and parse it back:

```js
localStorage.setItem("myLeads", JSON.stringify(myLeads))       // array → string
let myLeads = JSON.parse(localStorage.getItem("myLeads"))      // string → array
```

### Rendering the list — innerHTML

The saved leads are rendered into a `<ul>` by building an HTML string and assigning it to
**`innerHTML`** (which parses HTML, unlike `textContent`), typically inside a `render` function driven
by a for loop over `myLeads`.

---

## Mapping to the syllabus activities

| Syllabus | Coverage |
|---|---|
| 01.03–05 variables, math, reassigning/incrementing | Covered |
| 01.06, 09–12 button + functions + increment on click | Covered — `onclick`, declare/invoke, scope |
| 01.15 display with innerText | Covered — `getElementById`, `innerText`→`textContent` |
| 01.16, 25, 27 save feature / set to 0 | Covered — reset DOM **and** variable |
| 01.18–24 strings, greeting, concatenation, `+=` | Covered |
| 01.29 JavaScript challenges | Covered (quickfire drills) |
| 02. Basketball Scoreboard | Solo project (no walkthrough) |
| 04.01–05 firstCard/sum, if…else | Covered — `<`, `>`, `<=`, `===` |
| 04.08–10 isAlive boolean, message | Covered — booleans, conditionals as booleans |
| 04.11–20 styling + DOM display | Covered — message/sum/cards, `querySelector` aside |
| 04.21–23 arrays, indexes, data types | Covered — zero-indexed lists |
| 06. Chrome extension | Covered — `push`, `addEventListener`, `localStorage`, `JSON.stringify/parse`, `innerHTML` |

The `PRACTICE: Exercise` items are the in-scrim challenges (dog-age calculator, `log 42`, lap-time
sum, lap counter, full-name concatenation, `greetLinda`, nightclub age check, king's birthday card,
true/false prediction drills, LinkedIn array, localStorage three-parter, etc.), described inline.

## What this module teaches

- Linking JS with `<script src>`, and `console.log` for verification/debugging.
- **Data types:** numbers, strings (concatenation, quote nesting), booleans.
- Variables with `let`: declaration, reassignment, incrementing (`count = count + 1`, `+=`), and why
  reference-before-declaration and block scope matter.
- **Functions:** declaring vs invoking, bodies, removing repetition, scope.
- **Conditionals:** `if`/`else if`/`else`, comparison operators, and `===` vs `==` (always use `===`).
- The **DOM:** `getElementById` (and `querySelector`), `textContent`/`innerText`, `innerHTML`, and
  event handling (`onclick` → `addEventListener`).
- **Arrays:** ordered, zero-indexed lists; `push`; iterating with a for loop.
- **Persistence:** `localStorage` (strings only) with `JSON.stringify`/`JSON.parse`.

## Practice task

Rebuild the leads tracker's core from memory:

1. `let myLeads = []` and an input + save button wired with `addEventListener`.
2. On click, `push` the input value, then persist with
   `localStorage.setItem("myLeads", JSON.stringify(myLeads))`.
3. On load, restore with `JSON.parse(localStorage.getItem("myLeads"))` (guard against `null`).
4. A `render(leads)` function that builds a `<ul>` string in a for loop and sets it via `innerHTML`.
5. A "delete all" button that clears the array, the DOM, and `localStorage`.

## Readiness check for the next module

Before moving on you should be able to:

- declare and reassign variables, and explain block scope and `===` vs `==`;
- write and invoke a function, and wire it to a click (both `onclick` and `addEventListener`);
- read from and write to the DOM by id, using `textContent` vs `innerHTML` appropriately;
- create an array, `push` to it, index it, and iterate it with a for loop;
- persist data with `localStorage` and serialise an array with `JSON.stringify`/`parse`.

These are the foundations Modules 07 (Essential JavaScript) and 09 (APIs & Async JavaScript) build on,
and the same DOM/array thinking underpins React in Module 15.

---

## Ordered syllabus

MODULE 03. JavaScript Fundamentals
========================================================================
Learning focus: JavaScript syntax, program logic, DOM manipulation, browser storage, and interactive projects.
  SECTION / UNIT: 01. Build a Counter App
    LESSON / ACTIVITY: 03. Write your first JavaScript variable
    LESSON / ACTIVITY: 04. Basic mathematical operations
    LESSON / ACTIVITY: 05. Reassigning and incrementing
    LESSON / ACTIVITY: 06. Adding a button
    LESSON / ACTIVITY: 09. Write your first function
    LESSON / ACTIVITY: 10. Write a function that logs the sum
    LESSON / ACTIVITY: 11. Write a function that increments
    LESSON / ACTIVITY: 12. Increment on clicks
    LESSON / ACTIVITY: 15. Display the count with innerText
    LESSON / ACTIVITY: 16. Create the save button
    LESSON / ACTIVITY: 18. Write your first string variable
      PRACTICE: Exercise 1
      PRACTICE: Exercise 2
    LESSON / ACTIVITY: 19. Log a greeting to the console
    LESSON / ACTIVITY: 20. Strings vs. Numbers
    LESSON / ACTIVITY: 22. Render a welcome message
    LESSON / ACTIVITY: 23. Improve the message with string concatenation
    LESSON / ACTIVITY: 24. Use plus equal for count
    LESSON / ACTIVITY: 25. Create the save feature
    LESSON / ACTIVITY: 27. Set the count to 0
    LESSON / ACTIVITY: 29. JavaScript challenges
      PRACTICE: 01. Variables practice
      PRACTICE: 02. Concatenate two strings in a function
      PRACTICE: 03. Incrementing and decrementing
      PRACTICE: 04. Strings and numbers
      PRACTICE: 05. Rendering an error message
      PRACTICE: 06. Calculator challenge
      PRACTICE: 07. Arithmetic Operator Precedence
  SECTION / UNIT: 02. Solo Project - Basketball Scoreboard
  SECTION / UNIT: 04. Build a Blackjack Game
    LESSON / ACTIVITY: 01. Add the firstCard. secondCard, and sum
    LESSON / ACTIVITY: 03. Your first if...else statement
    LESSON / ACTIVITY: 04. if_else...if_else statement
    LESSON / ACTIVITY: 05. The if...else statement for our game
    LESSON / ACTIVITY: 08. Add the isAlive variable
    LESSON / ACTIVITY: 09. Let_s practice boolean conditions
    LESSON / ACTIVITY: 10. Add the message variable
    LESSON / ACTIVITY: 11. Link to stylesheet
    LESSON / ACTIVITY: 12. Add basic styling
    LESSON / ACTIVITY: 13. Make the start button work
    LESSON / ACTIVITY: 14. Display the message
    LESSON / ACTIVITY: 15. Display the sum
    LESSON / ACTIVITY: 16. Display the cards
    LESSON / ACTIVITY: 17. New card button
    LESSON / ACTIVITY: 18. Add to the sum when newCard is clicked
    LESSON / ACTIVITY: 19. Rename the startGame function
    LESSON / ACTIVITY: 21. Aside- Intro to arrays
    LESSON / ACTIVITY: 22. Aside- Array indexes
    LESSON / ACTIVITY: 23. Arrays with multiple data types
    LESSON / ACTIVITY: 24. Array- Array.push() and .pop()
      PRACTICE: Exercise 1
      PRACTICE: Exercise 2
    LESSON / ACTIVITY: 25. Creating the cards array
    LESSON / ACTIVITY: 26. Push a new card to the array
    LESSON / ACTIVITY: 27. Aside- Loops
    LESSON / ACTIVITY: 28. Write your first loop
    LESSON / ACTIVITY: 30. Write your first array-based for loop
    LESSON / ACTIVITY: 31. For loops, arrays, and DOM
      PRACTICE: Exercise 1
      PRACTICE: Exercise 2
    LESSON / ACTIVITY: 32. Use a loop to render cards
    LESSON / ACTIVITY: 34. Aside- Returning values in functions
    LESSON / ACTIVITY: 35. Use a function to set the card values
    LESSON / ACTIVITY: 36. Aside- Math.random()
    LESSON / ACTIVITY: 37. Math.random() _ 6
    LESSON / ACTIVITY: 38. Flooring the number with Math.floor()
    LESSON / ACTIVITY: 39. Using Math.random() and Math.floor() to createa dice
    LESSON / ACTIVITY: 40. Completing our dice function
      PRACTICE: Exercise 1
      PRACTICE: Exercise 2
    LESSON / ACTIVITY: 41. Make getRandomCard() work
    LESSON / ACTIVITY: 42. Complete getRandomNumber function
    LESSON / ACTIVITY: 43. Assign values in the startGame function
    LESSON / ACTIVITY: 46. Write your first logical operator
    LESSON / ACTIVITY: 47. Aside- The OR operator (II)
    LESSON / ACTIVITY: 48. Only trigger newCard() if you_re allowed to
    LESSON / ACTIVITY: 51. Create your first object
    LESSON / ACTIVITY: 52. Use an object to store player data
    LESSON / ACTIVITY: 56. JavaScript challenges
      PRACTICE: 01. Objects and functions
      PRACTICE: 02. if else
      PRACTICE: 03. Loops and arrays
      PRACTICE: 04. push, pop, unshift, shift challenge
      PRACTICE: 05. Logical operators
      PRACTICE: 06. Rock papers scissors
      PRACTICE: 07. EmojiFighter
      PRACTICE: 08. Sorting fruits
  SECTION / UNIT: 06. Build a Chrome Extension
    LESSON / ACTIVITY: 01. Add button and input tag
    LESSON / ACTIVITY: 02. Style the button and input tag
    LESSON / ACTIVITY: 03. Make the input button work with onclick
    LESSON / ACTIVITY: 05. Write your first addEvent Listener()
    LESSON / ACTIVITY: 06. Your turn to refactor
    LESSON / ACTIVITY: 07. Create the myLeads array and inputEI
    LESSON / ACTIVITY: 08. When to use let and const
    LESSON / ACTIVITY: 09. Push to the myLeads array
    LESSON / ACTIVITY: 10. Push the value from the input field
    LESSON / ACTIVITY: 11. Use a for loop to log out leads
    LESSON / ACTIVITY: 12. Create the unordered list
    LESSON / ACTIVITY: 13. Render the leads in the unordered list
    LESSON / ACTIVITY: 15. Write your first innerHTML
    LESSON / ACTIVITY: 16. More innerHTML practice
    LESSON / ACTIVITY: 17. Render the _li_ elements with innerHTML
    LESSON / ACTIVITY: 18. Use createElement() and append() instead of innerHTML
    LESSON / ACTIVITY: 19. Improving the performance of our app
    LESSON / ACTIVITY: 20. Create the render function
    LESSON / ACTIVITY: 21. Clear the input field
    LESSON / ACTIVITY: 23. Add the _a_ tag
    LESSON / ACTIVITY: 25. Write your first template string
    LESSON / ACTIVITY: 26. Make the template string even more dynamic
    LESSON / ACTIVITY: 27. Template strings on multiple lines
    LESSON / ACTIVITY: 28. Refactor the app to use a template string
    LESSON / ACTIVITY: 30. Style the list
    LESSON / ACTIVITY: 34. Your first localStorage
    LESSON / ACTIVITY: 35. Storing arrays in localStorage
    LESSON / ACTIVITY: 36. Save the leads to localStorage
    LESSON / ACTIVITY: 37. Get the leads from localStorage
    LESSON / ACTIVITY: 39. Guess the expression - truthy ir falsy_
    LESSON / ACTIVITY: 40. Checking localStorage before rendering
    LESSON / ACTIVITY: 41. Style the delete button
    LESSON / ACTIVITY: 42. Make the delete button work
      PRACTICE: Exercise 1
      PRACTICE: Exercise 2
    LESSON / ACTIVITY: 44. Write your first function parameter
    LESSON / ACTIVITY: 45. Functions with multiple parameters
      PRACTICE: Exercise 1
      PRACTICE: Exercise 2
    LESSON / ACTIVITY: 46. Numbers as function parameters
    LESSON / ACTIVITY: 47. Aside- Arguements vs Parameters
    LESSON / ACTIVITY: 48. Arrays as parameters
    LESSON / ACTIVITY: 49. Refactor renderLeads() to use a parameter
    LESSON / ACTIVITY: 50. Create the tabBtn
    LESSON / ACTIVITY: 51. Save the tab url
    LESSON / ACTIVITY: 56. JavaScript challenges - part 3
      PRACTICE: 01. let & const
      PRACTICE: 02. Log out items in an array
      PRACTICE: 03. save to localStorage
      PRACTICE: 04. addEventListener and object in array
      PRACTICE: 05. Generate sentence
      PRACTICE: 06. Render images
      PRACTICE: 07. Rounding numbers
      PRACTICE: 08. Convert string to number challenge

========================================================================
