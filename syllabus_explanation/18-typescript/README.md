# Module 18: TypeScript

## Completion status

**Fully covered — two back-to-back course segments between 40:14:23 and 43:08:50.** Bob Ziroll
teaches the fundamentals (Section 01, 40:15:19–42:17:22, built around a console **pizza
restaurant app**), then Rachel Johnson takes over for TypeScript-in-React (Section 02,
42:17:26–43:08:50, converting **Assembly Endgame** from the React course to TypeScript). The
only thing not present is Section 03 (the *Typed Tenzies* solo project), which is a
specification-only solo project with no lessons — and which this transcript never mentions at
all.

The module intro sets the promise and keeps it:

> "Hi there and welcome to this module where you are going to learn Typescript, the
> supererset of JavaScript that add[s] constraints to your code and thereby helps you write
> software with fewer bugs… you'll learn about basic literal and custom types, optional
> properties, unions, type narrowing, utility types, and also how to use TypeScript with
> React… end[ing] up adding TypeScript to the assembly game you worked with earlier in this
> path. Now, your teachers are the beloved Bob Z[i]roll, who will take you through the first
> part before Rachel Johnson, another amazing Scribba teacher, takes over."
> (40:14:23–40:15:10)

## How the sources relate

| Transcript time | Segment | Syllabus section |
|---|---|---|
| 40:14:23–40:15:15 | Module intro (curriculum + teachers) | — |
| 40:15:19–40:22:24 | Why TypeScript: three reasons, analogies, limits | — / 01 |
| 40:22:24–40:31:40 | Pizza restaurant app written in plain JavaScript first | 01 (01) |
| 40:31:40–40:35:30 | Move the code to TS; first red squigglies; const/let fixes | 01 (02) |
| 40:35:30–40:39:26 | `selectedPizza` guards; where inference stops helping | 01 (02) |
| 40:39:26–40:44:35 | "Obligatory" types basics: inference, annotations, arrays, functions | 01 (04–05) |
| 40:44:35–41:01:44 | Custom types: Person, Pizza (nested), Order; typing arrays; orderQueue | 01 (06–12) |
| 41:05:39–41:22:10 | Literal types & unions (order status) | 01 (15) |
| 41:22:10–41:37:31 | Type narrowing; void; getPizzaDetail return type | 01 (17–21) |
| 41:09:47–41:40:04 | Automatic ids for menu items | 01 (22) |
| 41:41:00–42:00:14 | Utility types: Partial (then why it's not enough) | 01 (23) |
| 41:52:31–42:00:14 | Omit; fixing TS warnings with Omit | 01 (24–25) |
| 42:00:14–42:17:22 | Generics: placeholders, generic functions in the restaurant, explicit calls | 01 (26–28) |
| 42:17:26–42:18:41 | Rachel's handoff + roadmap | 02 |
| 42:19:53–42:31:28 | Assembly Endgame (TS variant); refresher: languages, utils functions | 02 (02–04) |
| 42:31:28–42:40:09 | Typing `useState`, derived values, arrow functions, App.tsx functions | 02 (05–07) |
| 42:40:13–42:47:08 | Component tour; `JSX.Element`; `React.FC`; `JSX.Element \| null` | 02 (10) |
| 42:47:08–42:56:20 | Component props: inline, then custom types | 02 (11–12, 14) |
| 42:56:20–43:04:46 | LanguageChips (element within element); WordLetters challenge; function props | 02 (15–17) |
| 43:04:46–43:07:33 | Final challenge: fully type the Keyboard | 02 (18) |
| 43:07:37–43:08:50 | Recap + Rachel's sign-off | — |
| — | *Typed Tenzies solo project — no lessons, no transcript mention* | 03 |

Note on lesson 13 (*The AriaLiveStatus Component Challenge*) and 16 (*The WordLetters
Component Challenge*): the components themselves are typed in the transcript's component tour
and challenges (42:41:40 "Arya Live status… status updates designed for just screen readers";
the WordLetters work at 42:59:27–43:02:53); the syllabus simply splits them into named
challenge lessons.

---

## Section 01 — TypeScript Fundamentals (Bob Ziroll)

### Why learn TypeScript at all (40:15:19–40:19:30)

Three reasons, stated as such:

1. **Confidence** — "TypeScript's ability to check your code during compile time or using
   modern IDEs essentially in real time as you're typing your code dramatically reduces the
   number of app crashing runtime errors that would normally only be caught after your app is
   running and possibly even deployed live to production" (40:15:46–40:16:02).
2. **Productivity** — "in JavaScript, you'll get some autocomplete, but… as you're using
   TypeScript, autocomplete turns up to a completely different level," plus "refactoring
   capabilities, immediate error checking" (40:16:32–40:16:48).
3. **Employability** — "learning Typescript is oftentimes considered table stakes by many
   companies, even if it's not explicitly listed in their job descriptions… knowing even a
   little bit of TypeScript can really set you apart from other junior developer candidates"
   (40:17:12–40:17:24).

And the meta-promise: "TypeScript can be a catalyst that helps train your brain to think like
a senior developer" (40:17:57–40:18:05).

Two analogies for what the errors mean:

- **The Kent C. Dodds line**, quoting a friend: "Typescript is not going to be making your
  life terrible. It's simply going to be showing you how terrible your life already is"
  (40:18:50–40:18:57) — the errors "are not there to bug you or be annoying. They're really
  there to protect you against some of the loosey goosey typing that happens in vanilla
  JavaScript" (40:18:59–40:19:08).
- **Blueprints and the stud guard** (40:19:11–40:20:36): planning a house before building it,
  and the 16-gauge steel plate that stops a too-long screw from hitting a water, electrical,
  or gas line: "A little bit of extra work, planning ahead, just like using TypeScript, can
  save you big headaches in the future."

Honest limits, stated up front (40:20:39–40:21:04): "TypeScript does not solve every
programming problem… The main focus of TypeScript is on fixing possible runtime errors…
it won't protect you against certain things like logical errors."

### The Pizza app, in JavaScript first (40:21:51–40:31:40)

The pedagogical trick is stated openly: "I really wanted to demonstrate the improvements that
your code will receive by using TypeScript instead of JavaScript just by itself… we're going
to start by writing it in regular JavaScript" (40:21:51–40:22:19). The app is "just going to
be console-based, so we won't be worrying about HTML" (40:22:12).

- A `menu` array of pizzas with names and prices (40:22:24–40:22:47), `cashInRegister`
  starting at $100, and an `orderQueue` initialized as an empty array (40:22:50–40:23:13).
- Simple challenges add functions like `addNewPizza`, `placeOrder`, and `completeOrder` over
  the next several minutes.

### Move the code to TS (40:31:40–40:39:26)

- Locally you'd "change my JavaScript file to a .ts file extension and set TypeScript up as a
  dependency" (40:31:55–40:32:03); in Scrimba the code is copied into a new `index.ts`
  instead — with the promise "we'll talk a little bit more about setting up TypeScript in a
  local environment" later.
- The immediate payoff: "We get a bunch of red squigglies. Of course, JavaScript was
  perfectly happy to let us write the code that we had before, but out of the box, TypeScript
  is able to warn us ahead of time of any potential errors that we might have" (40:32:24–40:32:38).
- A study habit is mandated: "anytime you see these red squigglies, I want you to actively
  move your mouse, hover over the word… and see the IntelliSense pop-up" (40:32:40–40:32:48).
- First catches, before any TS-specific code is written: `cashInRegister` and `nextOrderId`
  declared `const` but reassigned — "you cannot assign to cash and register because it is a
  constant" — fixed with `let` (40:33:15–40:34:02).
- The framing lesson of the whole section: "TypeScript is showing us the problems in our
  code. Nothing about using TypeScript here is introducing new bugs. It's just showing me
  where the bugs already existed… instead of having to wait till it crashes for our users"
  (40:34:17–40:34:32).
- **Guard clauses**: `menu.find(...)` can return `undefined`, so `selectedPizza` needs an
  early return — "if there is no selected pizza, then first [log that] the current pizza name
  that you're trying to search for does not exist in the menu" (40:36:32–40:37:55).
- And the limit that motivates the rest: passing a *string* id to `completeOrder(number)` goes
  unnoticed because nothing is typed yet — "TypeScript is no longer willing to help us without
  defining specific types in [our code]" (40:38:55–40:39:19).

### The "obligatory" basics lesson (40:39:26–40:44:35)

- "TypeScript is a supererset of JavaScript, any JavaScript code that we have will be
  legitimate Typescript code" (40:39:46–40:39:50).
- **Inference**: "TypeScript is very smart and it's able to infer what data type is being
  used" — hover `name` and it's already `string` (40:39:59–40:40:20).
- **Annotations**: `let myName: string`; then `myName = 5` produces "the type of five is not
  assignable to the type of string" (40:40:40–40:40:50) — with the note that explicit
  annotations are mostly for when inference can't help (e.g. a variable initialized later).
- Typing `orderId`-style variables, arrays, and function parameters follows, feeding straight
  into custom types.

### Custom types: Person → Pizza → Order (40:44:35–41:01:44)

- Why: "there are going to be times when the basic built-in types… aren't going to be
  enough" — type aliases are "handy for creating custom types around [the shapes our data
  actually takes]" (40:45:25).
- A `Person` type first (40:46:12–40:47:56), then **nested object types** (40:48:25): a
  `Person` with an `Address` inside it.
- **The `Pizza` type** (40:49:58–40:52:54): the menu items become `Pizza[]`, functions take
  `pizza: Pizza` parameters — and TS immediately flags `NoSuchPizzaError` style mistakes:
  "[property] does not exist in type pizza" (40:51:03). The `meta` property is redesigned
  from a string "but instead by a nested [object]" (40:52:54).
- **Optional properties** (40:55:09–40:58:47): the `?` marker — a pizza's `description` can
  be optional; "you can just leave it nested inside of [the parent type]" (40:57:40).
- **The `Order` type** (41:00:44–41:01:21): an order contains a pizza "which makes sense
  because it's a nested object inside there," plus a status and an id.
- **Typing arrays** and **`orderQueue`** (41:01:37): `Order[]` — the empty array that was
  `any[]` becomes a real queue of orders.

### Literal types and unions (41:05:39–41:22:10)

- **Literal types** (41:11:51): instead of "a generic string which would allow that
  [anything]… instead it's a literal type, an actual [specific value]" — `type PizzaStatus =
  "ordered" | "completed"`-style thinking.
- **Unions**: "the concept of using literal types is much [more powerful when] combined" —
  telling "TypeScript that an order type is allowed [only certain values]" (41:13:21–41:16:39).
- The payoff is lived, not just told: a typo'd status immediately gets flagged because it
  "isn't just a generic string" anymore (41:18:22).

### Type narrowing, void, and return types (41:22:10–41:37:31)

- **Type narrowing** via a challenge first (41:22:18), then the concept: "a concept called
  type narrowing where, when [you check what a value is], TypeScript [follows along]" — the
  `selectedPizza !== undefined` guard from earlier is the running example (41:26:43–41:27:03).
- **`void`** (41:29:27–41:30:41): "There's another return type that isn't [something you
  choose]… the inferred return type is called void" — functions that return nothing.
- **`getPizzaDetail`'s return type** (41:31:03–41:35:12): it "is either going to be an order
  type or [undefined]" — `Pizza | undefined` — plus `unknown` name-dropped for values whose
  type genuinely isn't known (41:34:12).

### Automatic ids (41:09:47–41:40:04)

`nextPizzaId++` replaces hand-written ids in the menu items — and TS catches the hoisting bug
for free: "the block scoped variable next pizza ID is used before its declaration" (41:39:01),
so the global declarations move to the top. The goal is stated as the bridge to Partial:
"my goal is to get us to a point where we can submit a partial pizza object without the ID
and have the function handle adding the ID for us" (41:38:24–41:38:31).

### Utility types: Partial, then Omit (41:41:00–42:00:14)

- The **motivation is built by hand first**: an `updateUser` function wants "every property
  from user… optional" — so the manual copy-paste-everything-with-`?` version is written out
  (41:45:15–41:45:48), then the complaint: "this was a lot of busy work. Imagine if we had a
  type that had 15 properties" (41:45:55–41:46:02).
- **Utility types defined** (41:46:12–41:46:29): "types that like a function… can take other
  types in as a parameter and they will return a new type… built directly into TypeScript…
  to perform some commonly needed modifications to existing types" — using "generic syntax
  which uses angle brackets."
- **`Partial<User>`** solves the update case — but then its limits are shown honestly:
  "partial's not really going to work for us [here] because all of the properties are
  optional" and the return value must be a full `User` (41:52:31–41:52:49).
- **`Omit<User, "id">`** (41:52:59–41:54:15): "it takes in a type just like partial, but it
  also takes… a second parameter… the property names that we want to omit from this type.
  It's going to return a brand new type with the properties that we specified removed" —
  used inline for one-off cases, with a pointer to the official TS docs. (Plus a Scrimba
  quirk worth a smile: "the omit utility type is currently omitted by Scribba" — the runtime
  needed a workaround, 41:54:12.)
- **Fixing TS warnings with Omit** completes the arc: `addNewPizza` finally accepts a pizza
  *without* an id (41:56–42:00).

### Generics (42:00:14–42:17:22)

- "Generics in [their essence are]… a [placeholder for a type in] your function. And a
  generic is a [type parameter]… generics use this bracket syntax" (42:00:24–42:00:56).
- A from-scratch `addToArray` example: "instead of [being more] generic than just using
  numbers, we can use that placeholder type" (42:07:09–42:07:12) — the same function now
  works for any type, type-safely.
- **Generic functions in the pizza restaurant** (42:06:07+): `getListItem<T>`-style helpers
  are written for menu/queue lookups.
- **Explicitly typing generic function calls**: `getListItem<Order>(...)` when inference
  can't decide (42:08:31–42:08:56).
- Bob's sign-off (42:17:10–42:17:22): subscribe to the newsletter for course updates, "I've
  been your teacher, Bob Z[i]roll… good luck and happy coding."

## Section 02 — TypeScript in React (Rachel Johnson)

### Handoff and plan (42:17:26–42:19:53)

> "…welcome to the next section of the Learn Typescript course where we're going to put
> TypeScript and React together. My name is Rachel and I'll be taking you through this
> React-specific section… We're going to be working with a very familiar project from the
> Learn React course called Assembly Endgame… it's a hangman style game where with every
> incorrect letter [guess], a programming language gets snapped out of existence until only
> assembly remains… we're not going to be spending a lot of time tweaking or extending the
> game itself… What we are going to do is reworking this project with TypeScript."
> (42:17:26–42:18:16)

Roadmap (42:18:16–42:18:41): refresher → typing `useState` and functional components →
component props "using both inline types and custom types and even importing prop types from
other [files]" → function props, "challenges at you every [step]."

### The refresher (42:19:53–42:31:28)

- The Assembly Endgame **TypeScript variant** is loaded (42:19:53–42:21:01: "is upload the
  original assembly endgame [project]").
- **Hover-to-infer challenge** (42:22:48–42:23:21): hover the `words` variable and read the
  inferred type.
- **`languages.js` → `languages.ts`** (42:23:34–42:25:25): define a `Language` type, "and now
  to type languages, we just have to refer to the type" — "that was your quick refresher."
- **`utils.ts`** (42:25:45–42:29:23): type `getRandomIndex`'s return, the `randomIndex`
  variable, and `getFarewellText`'s `language` parameter ("saying goodbye to that language"
  — the farewell-message function from the React course, now typed).

### Typing `useState`, derived values, and App.tsx functions (42:31:28–42:40:09)

- **`useState` needs the generic argument when inference can't help** (42:32:11–42:33:17):
  `guessedLetters` initialized with `[]` "is typed as an array… of any… guessed letters
  should actually be an array of strings. So, it's best to explicitly type our states… we
  actually need to pass the generic type argument into use state itself using these angled
  brackets. Remember generics from the end of the first section… we can simply pass string
  as the generic argument" — and hovering the `useState` import shows "the generic in
  action."
- **Derived values and arrow functions** (42:34:52–42:37:02): Assembly Endgame's derived
  constants and its callback arrows get typed in a challenge.
- **App.tsx functions** (42:37:13–42:39:55): "fully type the add [guessed letter]" function —
  "previous letters is a string [array]" — every function in App.tsx ends up typed.

### `JSX.Element`, `React.FC`, and null (42:40:13–42:47:08)

- A tour of the app's components first (42:41:01–42:42:45): game status, language chips,
  word letters, "Arya Live status… status updates designed for just screen readers,"
  keyboard, new game button.
- **`JSX.Element`** (42:43:30–42:43:51): `import type { JSX } from "react"` and type the
  return value — "some React programmers do this and some don't… since we are learning about
  TypeScript right now, we will keep doing this… just to form that type scripting habit."
- **`React.FC`** (42:44:09–42:44:46): "you might also see components defined and typed like
  this… React.fc… It automatically types the return value as a JSX element which is great.
  But the slight downside is that it does include children in props by default even if it's
  not used. That last point… is why TypeScript users are now defining components with JSX
  element instead."
- **`JSX.Element | null`** (42:45:19–42:46:43): components that conditionally render "will
  return either a JSX element or it will return a null" — the union covers both.

### Component props: inline, custom, imported (42:47:08–42:56:20)

- Inline typing first on the **GameStatus** component (42:47:08–42:50:00): "five component
  props this time… we typed them all in line."
- Then the cleaner way (42:50:11–42:50:43): "we're going to use what we [learned about
  custom] type and call it game status props" — a named type "contains the props and their
  types."
- **Imported types** (42:55:42): `import type { Language }` so types "keep things modular and
  clean" — the syllabus's *Component Props and Imported Types*.

### Elements within elements, WordLetters, function props (42:56:20–43:04:46)

- **LanguageChips / LanguageChip** (42:56:20–42:58:45): a chip "contains a background color
  string and a [text color]" — a component rendering another component, each with its own
  prop types.
- **The WordLetters challenge** (42:59:27–43:02:53): type `WordLettersProps`, the
  `shouldRevealLetter` logic, `letterClassName`, and the derived `isGameOver` value.
- **Function props** (43:03:16–43:04:03): "which is a function prop that returns [something]…
  this is how you type a function prop" — the pattern for callbacks passed to children
  (Assembly Endgame's keyboard keys call back up to App).

### The final challenge (43:04:46–43:07:33)

> "Welcome to your final challenge. In this [challenge]… Fully type the [Keyboard component]"
> (43:04:46–43:05:12) — variables inside the component, the `.map` callback, and the
  keyboard's own props — ending with "the assembly endgame project has been typed. Well
> done." (43:07:30)

### Rachel's recap (43:07:37–43:08:50)

> "We've taken our beloved assembly endgame app from Learn React and leveled it up with
> TypeScript. Functionally, the app still works the exact same way, but now it's fully typed,
> which means better readability, fewer bugs, and a smoother developer experience. Same app,
> but stronger and just a little bit fancier… We started with a refresher on vanilla
> TypeScript. Then we looked at how to type use state properly depending on what we're
> storing… typing React components using the imported JSX element type… component props, both
> the inline way and the cleaner approach using custom prop types… imported types… and
> finally… typing function props, which is super common in React when you're passing
> callbacks around. Same app, new superpowers, less guesswork, fewer bugs, and way more
> peace of mind."

## Section 03 — Solo project: Typed Tenzies *(no lesson content)*

The syllabus lists this section as a title with no lessons — solo projects on Scrimba are
specification-only ("We give you the specifications for the project, a design file to follow,
and then leave it up to you to build the project from scratch" — the React course's own
description at 26:33:14). The transcript never mentions Tenzies in this module.

Two honest notes for a learner following only this video:

1. Nothing in Section 03 is "missing" from the transcript — there was never teaching content
   to include.
2. But the project itself assumes you built the **untyped Tenzies in Module 15 — which this
   compilation also lacks** (see Module 15's README). The practical workaround: Assembly
   Endgame, typed end-to-end in Section 02, exercises every skill Typed Tenzies asks for
   (`useState` generics, component prop types, function props, derived values). Building
   Tenzies from its Module 15 lesson list *and then* typing it with Section 02's patterns is
   a legitimate substitute path.

## What this module teaches

1. Why TypeScript: confidence (compile-time errors), productivity (autocomplete/refactoring),
   employability ("table stakes").
2. What types can't fix: logical errors.
3. Reading red squigglies and IntelliSense hover pop-ups as a habit.
4. Inference vs explicit annotations, and when each is needed.
5. Custom types (type aliases) for objects, with nested and optional properties.
6. Typing arrays of custom types (`Order[]`, `Pizza[]`).
7. Literal types and unions to constrain values (order statuses).
8. Type narrowing with guard clauses and early returns.
9. Return types, including `void`, unions with `undefined`, and `unknown`.
10. Built-in utility types `Partial` and `Omit` — and reading their docs.
11. Generics: writing and explicitly calling generic functions.
12. Typing React: `useState<string[]>`-style generics, derived values, arrow functions.
13. Component return types: `JSX.Element`, `JSX.Element | null`, and why `React.FC` fell out
    of favor.
14. Props: inline types, custom `XProps` types, and imported types.
15. Function props (callbacks) — "super common in React."

## Small practice task

Rebuild a slice of the pizza restaurant yourself, then React-ify it:

1. Plain JS: `menu` (5+ items), `cashInRegister`, `orderQueue`, and
   `addNewPizza` / `placeOrder` / `completeOrder` functions.
2. Rename to `.ts`: fix every red squiggly with `let`/`const`, guards for `find(...)`, and no
   `any` left standing.
3. Add `type Pizza` (with a nested `meta` object and an optional `description`),
   `type Order`, and `type OrderStatus = "ordered" | "completed"`; type the queue as
   `Order[]`.
4. Give `getPizzaDetail` an explicit `Pizza | undefined` return type; make one function
   return `void` on purpose.
5. Replace hand-written ids with `nextPizzaId++`; make `addNewPizza` accept
   `Omit<Pizza, "id">`.
6. Write a generic `getListItem<T>(items: T[], id: number): T | undefined` and call it both
   inferred and explicitly.
7. Then port any small React app from Module 15 to TS: type every `useState`, every
   component's props (one inline, the rest as custom/imported types), one `JSX.Element |
   null` component, and at least one function prop.

## Readiness check for Module 19

Module 19 (Next.js) follows immediately — its course starts at 43:08:56. Before moving on,
be able to:

- Explain the difference between inference and annotation, and why `useState([])` needs an
  explicit generic.
- Write a custom type with a nested object and an optional property, from memory.
- Convert a union-typed status field and narrow it with a guard clause.
- Choose between `Partial`, `Omit`, and a hand-written type — and say why.
- Type a component that renders conditionally (`JSX.Element | null`) and one that takes a
  callback prop.

## Exact syllabus order

1. **TypeScript Fundamentals**
   1. 01. Intro to Pizza app (1) — Exercises 1–3
   2. 02. Move code to TS
   3. 04. Obligatory types basics lesson
   4. 05. Add type to orderId
   5. 06. Defining Custom Types
   6. 07. Adding a Pizza type — Exercises 1–2
   7. 08. Nested object types (5)
   8. 10. Adding an Order type
   9. 11. Typing arrays
   10. 12. Type orderQueue — Exercises 1–3
   11. 15. Update order status to use literal type unions
   12. 17. Type Narrowing — Exercises 1–2
   13. 19. Void return type
   14. 21. Add return type to getPizzaDetail — Exercises 1–2
   15. 22. Add automatic ids to menu items — Exercises 1–2
   16. 23. Utility Types & Partial
   17. 24. Omit Utility Type
   18. 25. Fix TS warnings with Omit
   19. 26. Generics — Exercises 1–2
   20. 27. Generic functions in the pizza restaurant
   21. 28. Explicitly type generic function calls
2. **TypeScript in React**
   1. 02. TS Refresher - Basic & Custom Types — Exercises 1–2
   2. 03. TS Refresher - Functions — Exercises 1–2
   3. 04. TS Refresher - A new getRandomIndex() function
   4. 05. Typing useState()
   5. 06. Typing Derived Values and Arrow Functions
   6. 07. Typing App.tsx functions — Exercises 1–2
   7. 10. JSX Element or null
   8. 11. Typing Component Props
   9. 12. Custom Component Prop Types
   10. 13. The AriaLiveStatus Component Challenge
   11. 14. Component Props and Imported Types — Exercises 1–2
   12. 15. Element within an Element — Exercises 1–2
   13. 16. The WordLetters Component Challenge
   14. 17. Typing Function Props
   15. 18. The Final Challenge
3. **Solo project - Typed Tenzies** *(specification-only; no lessons, and no mention anywhere
   in the transcript — see the note above)*
