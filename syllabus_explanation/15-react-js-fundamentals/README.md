# Module 15: React.js Fundamentals

## Completion status

**Sections 01, 03, 04, 05 and 07 are covered in depth — 26:31–40:14, the longest course in the
video (~13.5 hours). Section 06 (Capstone #1 — Tenzies) is a verified gap: it is promised in the
course intro, and the outro even claims it was built, but no Tenzies segment exists anywhere in
the transcript.**

The course is Scrimba's **Learn React**, taught end-to-end by **Bob Ziroll**, opening at 26:31:18
("React is arguably the most popular front-end library that exists out there today") and closing
at 40:14:18 ("My name is Bob Ziroll. It has been my absolute pleasure… congratulations on
completing this Learn React course"). It promises **six projects**:

> "…we are going to be building six projects together. I've designed the curriculum in a way that
> the projects will drive forward the curriculum… The very first project that we'll work together
> is a simple static page with some fun facts about React. In the next section, we'll be building
> another static page, but this time that iterates over data in an array… Then in section three,
> we are really going to dial it up. We're building an amazing project that I've called Chef
> Claude… The next project we work on will be in a section all dedicated to learning about side
> effects in React. And the project is a meme generator app. After the meme generator, we have
> two back-to-back capstone projects. The first one is a game of tenzies where you roll a series
> of 10 dice and hold the ones that you want to keep and keep rolling until all 10 dice are the
> same number. And lastly, the fate of the programming world lies in your hands as we play
> assembly endgame, where you guess a secret word and every letter that you get wrong erases one
> of the programming languages from the face of the earth." (26:31:48–26:33:02)

What the video actually contains: ReactFacts (static pages), Travel Journal (data-driven),
Chef Claude (state, forms, AI), Meme Generator (side effects), and Assembly Endgame (capstone).
**Tenzies is missing** — verified: "tenzies", "dice", "roll" and "hold" return no relevant
matches between 36:00 and 40:06, and the course outro's claim that "we built two back-to-back
games" (40:12:03) does not match the video's contents. The gap matters because Module 18's solo
project (Typed Tenzies) builds directly on the original.

Two honest framing notes:

- The course teaches **React 19**'s new form approach *and* the older controlled-component
  pattern ("forms were bad. They are so much better now in React 19 than they ever have been…
  React has shifted to using the native capabilities of form" — 33:00:13–33:00:43). Both
  generations are covered.
- The instructor is explicit about prerequisites: "Do I really need to learn JavaScript before I
  learn React?… my personal unhesitating emphatic answer is yes." (27:03)

## How the sources relate

| Transcript time | Course segment | Syllabus section |
|---|---|---|
| 26:31–26:39 | Course intro; philosophy ("the easy way is the hard way"); six projects; solo projects/Pro | — |
| 26:39–27:06 | "Think in React"; JS-first; when *not* to use React; `createElement` → JSX | — / 01 |
| 26:41–26:50 | First React code (`createRoot`) + from-scratch challenges | 01 |
| 26:50–26:54 | Local setup: Vite, Node/npm checks, NVM | 01 (09) |
| 27:10–27:23 | Why React: composable (David/Lego) & declarative (restaurant, PB&J) | 01 (07–08) |
| 27:26–27:41 | Housekeeping (.jsx, static images, one-parent rule, fragments); ReactFacts markup; pop quiz | 01 (09–11) |
| 27:42–28:02 | Custom components; PascalCase; parent/child | 01 (12–16) |
| 28:02–28:17 | Styling with classes; organizing components (files, exports, components folder) | 01 (17–18) |
| 28:17–28:49 | **Project: ReactFacts** — mental outline, setup, navbar, main content, background image | 01 (19–24) |
| 28:49–31:06 | **Project: Travel Journal** — props (contact book, jokes), `.map()`, keys | 03 |
| 31:09–36:18 | **Project: Chef Claude** — events, state, complex state, forms, conditional rendering, sound pads, AI recipe | 04 |
| 36:18–37:55 | **Project: Meme Generator** + side effects, `useEffect`, Star Wars, cleanup, scrollIntoView | 05 |
| — | **Tenzies** — promised, not present | 06 *(gap)* |
| 38:06–40:06 | **Capstone: Assembly Endgame** | 07 |
| 40:07–40:14 | Recap, what-to-learn-next, sign-off | — |

---

## Section 01 — Static Pages

### Course philosophy, first (26:31–26:39)

- "the easy way is the hard way" (26:34:35) — doing the challenges yourself is the only way the
  skills stick. It recurs at the first challenge: "you really will just be shorting your own
  education and your own practice if you decide to take the easy way out" (26:47:57).
- "learn how to think in React" (26:39:10).
- Solo projects and Scrimba Pro are pitched at 26:33:04–26:33:28 ("We give you the
  specifications for the project, a design file to follow, and then leave it up to you to build
  the project from scratch").

### First React code (26:41–26:50)

- `import { createRoot } from "react-dom/client"`, then `createRoot(...)` with
  `document.getElementById("root")` — or `querySelector("#root")` as an alternative (26:46) —
  and `.render(...)`; chained vs two lines, and the `ReactDOM.createRoot` import style (26:47).
- Two from-scratch challenges: rewrite the first lines of React code (26:45:30), then set up an
  app rendering an unordered list of "why you're excited to be learning React" (26:47:33) —
  with the library-vs-framework aside ("it's a super popular JavaScript framework, or I guess
  you could say library. There's a little bit of contention about that" — 26:49:12).

### Local setup with Vite (26:50–26:54)

> "…let's go back and talk a little bit more about how we can set React up locally, especially
> for those of you that are not following along in Scribba." (26:50:20)

- "**We're going to be using the recommended build tool called Vit. And yes, it is pronounced
  VIT. That's French for quick or fast.**" (26:51:36)
- "In order to use vit on your machine, you need to have node and npm installed already on your
  machine" (26:51:57) — checked with `node -v` / `npm -v`; "If it gives you any kind of version
  that's 18 and above, then you're golden" (26:52:10).
- Installing/updating Node via **NVM / nvm-windows** (26:52:44–26:53:39), `nvm install --lts`
  (26:53:46).
- Scrimba learners are told to keep working in the Scrimba interface for now so tooling doesn't
  distract from "the syntax and the philosophy behind React" (26:50:55–26:51:10).

### Why React — and when not to use it (27:03–27:05)

- **JS-first prerequisite**: "Do I really need to learn JavaScript before I learn React?…
  my personal unhesitating emphatic answer is yes." (27:03)
- **When not to use it** (27:03:41–27:05:19): a simple static landing page may not need a
  library; frameworks are big codebases "pulled down to the user's machine"; there's a learning
  curve, constant version upgrades ("you may find yourself spending a fair amount of time doing
  maintenance to your application"), and possible incompatibility with an existing codebase —
  "In the decisions you make in all of web development, you'll find that there's always
  trade-offs" (27:05:12).

### `createElement` and JSX (27:05–27:10)

Before JSX, the old way, so JSX is never magic:

- `React.createElement(type, props, children)` — "The first parameter is what type of element
  you want to create… The second parameter is something that's called props… The third
  parameter is what children we want our H1 to have" (27:06:00–27:06:25).
- What it returns: "create element returns an object… it's just a regular JavaScript object. It
  needs to be structured in this way so that React can understand what it is. Remember this
  because it will be key for us down the road when we start talking about JSX" (27:07:15–27:07:36).
- "JSX is simply what we call syntactic sugar on top of the create element call" (27:09:52) —
  demonstrated by console-logging a JSX element and getting the same object (still true "in
  version 19", 27:07:47).

### Composable (27:10–27:17)

- **Statue of David vs Lego** (27:11:19–27:12:01): a carved 14-foot marble block "can't be
  reused or repurposed in any way", while Lego bricks "can be reused and repurposed in a lot of
  different ways… some of which are pretty complex like replicating the statue of David."
- **Bootstrap navbar example** (27:12:51–27:14:34): 30+ lines of nav HTML copied into every
  page, vs a `<MyAwesomeNavbar />` custom component — "if I want to make a change, I can make
  that change in one place and it will reflect everywhere."
- First hands-on custom component: a `MainContent` challenge (27:15:34), with the `className`
  aside: "I am using class name instead of just class. That's not a mistake. It's something
  that we do have to do in React" (27:15:13).

### Declarative (27:18–27:23)

- "Declarative simply means that we can lean on the library of React to handle all of the
  manual, tedious tasks that we otherwise would have to worry about ourselves" (27:18:06);
  imperative is the computer saying "I need you to describe to me every single step along the
  way on how to do something" (27:18:41).
- The challenge: recreate the JSX `<h1>` with vanilla `document.createElement`, `.textContent`,
  and `appendChild` — "this is imperative coding… we've had to manually tell it every single
  step of the way" (27:21:01–27:21:03).
- **Restaurant analogy** (27:21:55): directing the host "down the hallway by 50 steps and then
  turn right" vs simply "We would like a table for four."
- **Peanut-butter-and-jelly analogy** in the quiz (27:39:45) — imperative instructions taken
  literally "usually ends up as a big mess."

### Housekeeping (27:26–27:31) — syllabus lesson 09

- `.jsx` file extension required when a file contains JSX (27:26:31).
- **Static images**: `src="react-logo.png"` relative to the file works in Scrimba, but local
  Vite projects may need "an absolute path from your project root" like `/src/assets/…`
  (27:27:44–27:28:44); "there is a better way to deal with static images in React, but we're
  not quite yet set up to learn about that" (27:28:46) — delivered in the next section.
- **One parent element**: "JSX expressions must have one parent element" (27:29:33), explained
  via createElement's inability to return two things — the fix being a wrapper, or a
  **fragment**: `<>…</>` is "under the hood… just creating a fragment, which essentially allows
  us to bypass that issue about rendering multiple sibling React elements together" (27:57:16–27:57:40).

### ReactFacts markup + pop quiz (27:32–27:41)

- The markup challenge builds the ReactFacts page: logo image (`react-logo.png`, `width="40px"`
  because "we haven't officially learned about how to tie class names into our JSX" — 27:33:18),
  `<main>` as the single parent ("I usually tend to do [a div] as a last resort… a main because
  that feels a little bit more semantically correct" — 27:34:25), and alt text (27:35:15).
- The five-question **pop quiz** (27:36–27:41): where `createRoot` puts the rendered elements
  (inside `#root`); what `console.log(<h1>…</h1>)` prints ("an object… just a plain JavaScript
  object" — 27:38:01); the sibling-elements error; declarative vs imperative (PB&J); and
  composable ("small pieces that we can put together to make something larger" — 27:41:32).

### Custom components, parent/child (27:42–28:02)

- Components are functions: "we use the concept of a function to give us the power of
  reusability… that's exactly what we do when we're creating custom components" (27:43:00–27:43:24).
- **PascalCase is required**: "with custom components in React, we have to use something called
  Pascal case… The only difference [from camelCase] is we need to start with a capital letter
  as well" (27:45:01–27:45:13). Rendering uses angle brackets, not a function call.
- Self-closing slash required for component instances (27:17:14).
- **Parent/child hierarchy** via the header/main-content/footer refactor challenge
  (27:57:48–28:02): "what we call parent components and child components… grandchild components
  and grandparent components" (28:02:23–28:02:29) — "similar to that statue of David made out
  of Lego bricks" (28:02:37).
- Honest scope note: "this is pretty clear that it's prematurely optimizing to create these
  three separate components" for a tiny page (28:01:25) — but the habit matters at scale.

### Styling with classes (28:02–28:11)

- The `<nav>`/pricing-about-contact challenge (28:03:11) starts it: "It's beautiful. Done. Ship
  it. No, let's learn about some styling" (28:03:59).
- CSS still lives in a stylesheet linked from the HTML file — "just like in regular vanilla
  HTML and CSS, we can just add any classes that we want to our JSX" (28:04:30).
- **`className`** instead of `class`, "with a capital N" (28:04:48) — because inside a
  JavaScript file "the word class is a [reserved word]" (28:04:54–28:05:07); the vanilla DOM
  property is `className` too (`ul.className = …`, 28:05:30).

### Organizing components (28:11–28:17)

- "these components are [all in our] index.jsx file. Especially as these components were to get
  larger and larger" (28:11:58–28:12:05) — so each component moves to its own file.
- **`export default`** the component (28:13:31–28:13:43), then `import Header from
  "./components/Header"` — no curly braces for default exports, with a mini-review of
  default vs named imports (28:14:01–28:14:47).
- `.js` vs `.jsx` extensions are a team convention: "most important to [pick a convention for
  your] project and just to stay consistent" (28:15:19).
- A dedicated **`components/` folder** (28:16:01–28:16:13): "as the project gets larger and
  larger, you'll [want] to organize things so that it's not too overwhelming."

### Project: ReactFacts (28:17–28:49)

- **Mental outline first** (28:17:20): "When I'm starting out on a new project, [I] try to
  solidify a mental model of how [it's structured]" — then "With this quick mental outline of
  the project behind us, let's jump into a series of challenges" (28:21:01).
- **Setup** scaffolds a components folder with `Navbar.jsx` and `Main.jsx` stubs (28:21:16–28:22:18).
- **Navbar & styling** against the **Figma design** (28:26:38–28:29): "make sure you reference
  the Figma design" (28:27:46) — header with the logo image and "React Facts" text, with the
  image imported as a module.
- **Main content section** (28:33–28:42), including styling by class and font properties.
- **Background image** (28:42:55–28:47): added as a CSS background, with `background-repeat`,
  `background-position` (which "is actually a combination of two different properties…
  background position X and background position Y" — 28:45:06) and the `background` shorthand
  (28:46:40).
- Section sign-off at 28:49:19 — "of finishing section one of the React [course]" — plus a
  reminder that local learners can now run their own Vite projects.

---

## Section 03 — Data-Driven React (28:49–31:06)

### Section intro + Travel Journal header (28:49–29:24)

> "…in our previous project, everything [was hard-coded]… The project we'll be building in this
> section is going to be a travel journal." (28:50:27–28:50:33)

The plan is stated up front: "we are going to be learning [about] reusability and datadriven
React [through] props. Then, with an understanding of how props works, we will create components
from an array of data" (28:51:36–28:51:44). The data lives in `data.js` (28:50:51). The first
challenge is the journal's header ("my travel journal" H1, 28:52:13–28:56:06).

### Props, taught in five deliberate steps (29:25–29:44)

The syllabus's "Props Part 1–5" is exactly how the transcript teaches it, via a **contact
book** of cards:

1. **The concept** — "the way that we pass data into a React component is going to look very,
   very similar to how we do it in HTML… it's called a property or more commonly a **prop**.
   And because it's custom, I can create a prop that's called whatever I [want]" (29:30:20–29:30:25).
2. **What to pass** — "whatever information we need to pass in so that the contact component
   can finish its job… Remember the goal is to take out any hard-coded data" (29:30:50):
   the image, name, phone, and email of each contact (29:31:01–29:31:06).
3. **Passing data** — attributes on the component instance, one per line when there are many
   (29:34:47).
4. **Receiving props** — the props object as the function's parameter, read as `props.img`,
   `props.name`, etc. (29:34:12).
5. **Destructuring props** — "it can be kind of nice to destructure some [props]" with curly
   braces in the parameter list (29:49:24–29:49:34).

### JS inside JSX + the jokes drill (29:44–30:02)

- An aside shows embedding JavaScript expressions in JSX with curly braces (29:41:50–29:43:04).
- The **jokes** challenge (29:54:11–30:02:49): a `Joke` component with `setup` and `punchline`
  props rendered four/five times, with the data sourced from a `jokes.md` file.
- **Conditional rendering gets a first, informal taste** here — a one-liner joke with no setup:
  "With conditional rendering, I can tell React that I only [want to render something when a
  condition holds]" (30:00:30), previewing Section 04's formal treatment.

### Non-string props (30:04–30:08)

- Numeric props: `upvotes` — `props.upvotes + 1` demonstrates that a prop arrives as real data
  (30:05:40).
- **Boolean props**: `isPun` — "we'll say this is a pun. It's… true as a pun. Again, not a
  string, but the actual boolean value of true" (30:06:17–30:06:20).
- **Arrays and objects as props**: "if we wanted to pass in maybe an array… that new array
  might be an array of objects" (30:07:15–30:07:38) — e.g. a `comments` array consumed with
  `.map()` inside the child.

### `.map()`, rendering arrays, and keys (30:18–30:41)

- **`.map()` review** (30:18:37–30:25:49): map takes a callback, returns "an array that will be
  the exact same length as the original array" (30:20:17) — drilled with squares and
  first-letters challenges.
- **"React knows how to render arrays"** (30:26:03) — an array of strings (Ninja Turtles,
  30:26:25) renders; but plain objects don't: "objects are not valid as a React child"
  (30:27:36) — except the special objects JSX creates.
- **The key warning appears live**: "there is a little warning that says each child in a list
  should have a unique key prop. We're going to cover that a bit later, so don't be too
  concerned about that now" (30:30:12). (The payoff arrives in the sound pads challenge,
  34:52–34:58.)
- **Mapping components**: export an array of joke objects (30:31:48), import it, and
  `jokes.map(joke => <Joke … />)` — passing each object's fields down as props (30:32:30–30:33:25).
  You get to choose prop names even when the data's keys are fixed (30:35:50).
- **Map quiz** (30:37:39–30:41:16): what `.map()` returns; what it's used for in React ("take
  some kind of array of raw data, usually from [an API or database], and we turn it into JSX"
  — 30:38:35–30:38:50); and *why* mapping matters — new data "added to the data" renders
  automatically because "we are accessing that array [dynamically]" (30:40:00–30:40:26).

### Travel Journal finishes (30:41–31:06)

- The `data.js` file of journal-entry objects is introduced (30:41:39–30:41:46) and mapped to
  `<Entry />` components — the whole point of the section: change the data, and the page
  follows.

---

## Section 04 — React State (31:09–36:18)

### The Chef Claude project (31:09–31:28)

> "Your challenge is to start by building the header component… I've already included the
> chefclaw icon.png file. That's the little robot with the chef's hat." (31:09)

The project brief (from the course intro): "users can input a list of ingredients, send that
list of ingredients off to an artificial intelligence engine to then get a suggested recipe
based on the available ingredients" (26:32:20–26:32:30). Early in the section: "Claude is an
extremely capable text completion AI" (31:27:02).

- Header challenge (31:09–31:19), then mapping the ingredients list (31:19–31:24).

### Event listeners (31:28–31:45)

- `onClick` first (31:28:52), then `onMouseOver` (31:33:01) — React event props that receive
  functions, looked up in the React docs ("in that documentation, we can see that there is an
  event called on mouse over").
- `onChange` on an input, firing on every keystroke (31:54:44).

### `useState` and re-rendering (31:45–32:13)

The mental model before the syntax (31:50):

> "Once React has run this app function, it's only going to run it again if either the props
> that it's receiving change… or it will also rerender if internally it has a state value that
> changes. Now, a state value is different than just a random variable that you declare within
> the body of your function."

- `useState` introduced at 31:55:34; the state/setter pair and initial value.
- **Changing state** with the setter — **state practice** drills with `setCount` (32:07:22).
- **Updating state with a callback function** (32:13:33): `setCount(prev => prev + 1)` for
  correctness when new state depends on old.

### Complex state — arrays and objects (32:32–33:00)

- **Arrays**: `setIngredients(prev => [...prev, ingredient])` — the **spread operator**
  (32:36:59) and `setIngredients` (32:42:47) updating the Chef Claude ingredients list
  immutably; "React has a philosophical basis in functional programming" (32:36:49) flagged
  here and expanded in Section 05.
- **Ternary practice** inside a contacts/favorites challenge — `contact.isFavorite ? "Remove
  from favorites" : "Add to favorites"` inline in JSX, plus aria-labels for the star icon
  (32:50:18–32:50:59).
- **Objects** (32:51:21): "what we're actually here to learn… is how we can update our state
  when what's being saved in state is an object. We're going to see in the next lesson why that
  might not be as simple as we think" — spread-then-override, never mutate.

### Forms — twice (33:00–33:45)

The section opens with a verdict on history:

> "…after the last about 8 years of teaching React, I can confidently and happily say that now
> forms were bad. They are so much better now in React 19 than they ever have been… because
> React has shifted to using the native capabilities of form… React 19 has changed the game."
> (33:00:08–33:01:16)

- **HTML forms review first** (33:01:27–33:15): the `<form>` element; `input` as "kind of a
  crazy… overloaded" element — `type="text"` vs `type="radio"` (33:02:36); the **`name`
  attribute** as "how we're going to access the data that is input into this input box by the
  user" (33:03:01); `type="email"`; labels; submit buttons.
- **React 19 form actions**: the form's `action` prop pointing at a function, gathering fields
  with `Object.fromEntries(new FormData(form))` (33:43:02) — "much more closely aligned with
  how the native web platform handles forms."
- **Controlled components** as the still-useful older pattern (33:15:17): state + `onChange` per
  keystroke — the pattern the Meme Generator (Section 05) will use, since "there are instances
  where you may still want to do forms in the way that they used to be done in React" (36:19:44).
- Radio buttons (33:02) and checkboxes (33:21:29), including reading checked values from
  FormData.

### Conditional rendering (33:46–34:39)

- Formal `&&` treatment: how the operator actually works — "if [the left side is] truthy, then
  the double ampersand says just return whatever's on the right side. If this is falsy, then
  the whole [expression returns the falsy value]" (33:59:02–33:59:09).
- **The count-of-zero trap**, taught explicitly: an array's unread count "need[s] to know if
  the length is greater than zero. So, if the length [is 0]… the number zero, React will choose
  to display that zero instead of just [rendering nothing]" (34:00:56–34:04:12) — so write
  `unreadMessages.length > 0 && …` rather than `unreadMessages.length && …`.
- Ternaries for either/or (reusing the 32:50 favorites work); **toggling state** at 34:39:14
  (`setShown(prev => !prev)`-style flips).

### Passing data around React (34:20–34:54)

- **Passing state as props** and **setting state from child components**: the parent owns the
  state, the child receives both the value and a setter-calling callback.
- **Lifting state up** (34:51:43): "we need to lift that state up so that it [can be shared]" —
  don't put everything in the top-level App "and then pass it down as many levels as I need
  to… as a rule of thumb, that's generally not a good idea" (34:53:51–34:53:58).
- **Context name-dropped, explicitly deferred** — and it names the whole Module 17 space:
  "tools like context which is built [into React]… we do dive into context and we learn how we
  can use context to avoid having to [pass props through every level]" (34:50:23–34:50:46)…
  "if you do have state that is truly global across your entire application, that's usually
  the time to start looking at one of those alternative solutions that I mentioned like
  **context, redux or zustand**" (34:54:00–34:54:11).

### Sound pads challenge (34:54–35:45)

The section's integration challenge — a 2×4 grid of toggleable pads, "inspired by my Roadcaster
Pro, which is what I use for mixing the sound from my microphone. And it has these eight
buttons… they are just for doing sound effects" (34:54:41–34:54:52). `pads.js` holds "an array
of objects. They have an ID, a color, which we're going to use eventually, and an on value"
(34:55:30–34:55:39).

1. Initialize state with the pads array; map it to `<button>` elements in a 2×4 grid
   (34:55:18–34:56:25).
2. **Keys** — the warning met again and finally resolved: "each child in a list should have a
   unique key prop and that's because we're mapping over it. We need to make sure that we
   provide a key" (34:52–34:58), using each pad's `id`.
3. **Dynamic styles** (35:08:36) driven by state — styling "held"/on pads via their `color` and
   `on` properties.
4. **Local vs shared state** (lessons 48–50): first each pad toggles itself, then the state is
   lifted so the parent updates one item in the array immutably — "updating the item in
   [the] array" via `map` producing a new array with the toggled pad replaced.

### Chef Claude meets AI (35:45–36:18)

> "Now, because this isn't a course all [about AI]… [here's a] link here to a course here on
> Scribba called Intro to AI Engineering" (35:54:07–35:54:36) — the Module 10 cross-reference,
> a "90-minute course."

- **HuggingFace** as the model gateway: "HuggingFace, you can kind of think of it like the
  GitHub for AI models" (35:46:12).
- The recipe request is sent to **Claude**; the response is **markdown**, rendered into the
  recipe section (35:57:15), which is itself conditionally rendered only once a recipe exists.
- The finished recipe then gets the **`scrollIntoView()` UX treatment** — but that lands in
  Section 05 as its named `useEffect` practice (37:49), "to add a feature to our chef cloud app
  from the last section" (36:21:15).

---

## Section 05 — Side Effects (36:18–37:55)

### Section intro: the contract before the hook (36:18:50–36:21)

> "This entire section is all about how we can handle side effects in React. And in the years
> that I've been teaching React, I have found that understanding side effects in React can be
> one of the more tricky things that even seasoned React developers can experience. When React
> transitioned away from class components into functional components and started using hooks
> back in version 16.3, the way that the world thought about React kind of changed forever."
> (36:18:50–36:19:15)

- Roadmap: controlled components (the meme generator uses them), "a bit of a studious aside to
  talk about functional programming" (36:19:59), effects, and "a quick chance to apply the
  concepts that we learned in this section to add a feature to our chef cloud app from the last
  section" (36:21:15).
- **The philosophy**:

  > "React has a philosophical basis in functional programming. We touched on the concepts of
  > immutability in React and how our components shouldn't affect any outside systems from
  > themselves. However, the purpose of the side effect section is to learn how we can use an
  > escape hatch from that functional programming paradigm when we absolutely need to."
  > (36:20)

### The Meme Generator (36:21–37:05)

> "To help us guide our discussion about side effects, we are going to be following this meme
> generator project. And unlike the previous projects where I actually have us start it
> completely from scratch, we are going to be beginning this one from a starting point."
> (36:21:24–36:21:37)

- The finished app: "you have the option to click a button which will get a new random meme
  image from a list of popular meme images that comes from the meme API called **image flip**"
  (36:21:02–36:21:09).
- **Controlled components** for the two text inputs: "The user will simply type into the top
  text input box and that will on every keystroke update the text that displays on the image"
  (36:22:40–36:22:45) — "clicking the button doesn't submit any form anywhere. It just randomly
  gets a new meme image" (36:22:51).
- **Meme state** as an object: "should contain an object that has a top text, bottom text, and
  image properties" (36:24) — complex-state practice from Section 04, applied; updates via
  `setMeme(prev => …)` — "behind the scenes it's replacing the old version of state with the
  new version of state" (37:45).

### `useEffect`, the dependencies array, and the infinite loop (36:51–37:23)

- **Effect order, demonstrated**: render first, effect after — logging "rendered" then "effect
  ran" regardless of code order (36:57).
- **Dependencies array** (36:57:53): no array → runs on every render; `[]` → once on mount;
  values → re-run when they change (drilled with a counter/dark-mode-style demo).
- The **infinite-loop trap** met live before being taught — a fetch that sets state on every
  render: "make sure you don't get stuck in an infinite rendering loop like we did before"
  (37:13:14).
- **Fetching data in React**: memes fetched from the imgflip API on mount, a random one
  selected for the "Get random meme" button (37:16–37:23).

### The Star Wars API practice (37:06–37:16)

Fetch-on-mount with `useEffect` + `useState`, rendering character data — and a first gentle
look at REST endpoints: "the URL on the Star Wars API says /people/1. Well, this slash one is
the ID" (37:15:03–37:15:06). This is Module 09's fetch skill inside React's lifecycle.

### Cleanup (37:27–37:48)

> "It's really important that we clean up any of the side effects that we have created."

- Return a function from the effect; React calls it before unmount/re-run.
- The **window tracker**: `addEventListener("resize", watchWindowWidth)` in the effect, and
  `removeEventListener` with the *exact same named function* in the cleanup — "I have to pass
  it the exact same function that I used when I was setting it up."
- The generalisation: "if instead… we had created a websocket connection with a server then it
  would be important… to disconnect that websocket connection."

### `useEffect` practice — `scrollIntoView()` (37:49–37:55)

Back in Chef Claude: a `ref` on the recipe section and `scrollIntoView()` so the user is
scrolled to the AI-generated recipe the moment it arrives — the syllabus's final Section 05
lesson.

---

## Section 06 — Capstone #1 — Tenzies *(absent)*

Promised at 26:32:42 ("a game of tenzies where you roll a series of 10 dice and hold the ones
that you want to keep and keep rolling until all 10 dice are the same number") and referenced by
the outro ("We built two back-to-back games that were both really fun to build and legitimately
are fun to play" — 40:12:03), but **no Tenzies build exists in the transcript** — verified by
zero matches for tenzies/dice/roll/hold in the whole React region. The outro's own
section-by-section recap (40:07–40:12) names static pages, props/mapping, Chef Claude, forms,
conditional rendering, state management, the meme generator and side effects — and never
describes a dice game.

What Tenzies would teach (from its lesson list), and where else in the path each piece exists:

- Mapping an array of objects to components — Travel Journal (30:41) and sound pads (34:55).
- Random number generation — Module 03's `Math.random()` dice function (09:15–09:33).
- Conditional styling of "held" items — dynamic styles in the sound pads (35:08) and Assembly
  Endgame's keyboard (39:03).
- The `key` prop — 30:30 and 34:52–34:58.
- End-game win detection (all-equal check) and a new-game reset — Assembly Endgame's
  `isGameOver` and new-game button (39:09–40:06) are the closest equivalents.
- **Confetti** — a `<Confetti />` component appears in Assembly Endgame ("we do celebrate the
  win with the confetti component" — 40:06), which is the same library Tenzies uses.

Practical consequence: **Module 18's solo project is "Typed Tenzies"** — a learner following
only this transcript reaches it having never built the untyped original. Module 18's README
covers how its transcript segment compensates (it types Assembly Endgame instead).

## Section 07 — Capstone #2 — Assembly Endgame (38:06–40:06)

From the course intro: "the fate of the programming world lies in your hands as we play
assembly endgame, where you guess a secret word and every letter that you get wrong erases one
of the programming languages from the face of the earth" (26:32:52–26:33:02). The build, in the
syllabus's order, all present:

- **Planning first**: "the first one. What are the main containers of elements I need in this
  project?" (38:12) — the same mental-outline discipline as ReactFacts.
- **Header, status, languages list, word display, keyboard** — a component per region; the
  language chips laid out with flexbox and `flex-wrap: wrap` (38:36), styled from the Figma
  comp.
- **Guessed letters in state**; the keyboard reflects guesses with per-letter correct/incorrect
  classes — "it will gray it out with an overlay that's opacity of 70%" (39:03).
- **Wrong guess count** and **lost languages**: the chips gray out as languages are lost, and
  the **farewell messages** render — "it takes a language as a parameter. It has an array of
  farewell options" (39:30).
- **Derived state** for game-over — "what we should do is try to derive some state about
  whether the game is lost" (39:09) rather than storing it.
- **`clsx`** for conditional classes: "this CLSX package… [when you have conditional] class
  names and clsx gives you a chance to [combine them]" (38:46:06–38:46:34); `import clsx from
  "clsx"` (38:51:23) — used "in a couple different places" (38:50:35).
- **Random word choice** and the **new game button** that resets all state (39:57–40:06).
- **Accessibility, taught unprompted** — the syllabus's Module 05 connection made real:

  > "Keep accessibility in mind, specifically when you're choosing what [text to render]. What
  > we can do is add an ARYA live region to it and say that it is polite." (39:42–39:48)

  The status section becomes an `aria-live="polite"` region so screen readers announce correct
  and wrong guesses — the exact technique Module 05 documented as an aside.
- **Extra credit** ideas (40:06): display the remaining guesses count, "anti-confetti when the
  game is lost," a chess timer that causes a loss when time runs out — and the two things every
  Scrimba project ends with: deploy it, and post it in the Discord's **"Today I did"** channel
  (40:12:19).

## The outro (40:07–40:14) — and what it says about later modules

- Recap of every section: static pages; props and mapping with "reusability [dialed] to 11"
  (40:09:45); Chef Claude; "React 19 enables an entirely new approach to forms… much more
  closely aligned with how the native web platform handles forms" (40:10:32); conditional
  rendering; "a little bit of state management dabbling" (40:10:42) with the honest caveat
  that real state management "would probably require an entire course of its own"; side
  effects — "one of the more misunderstood aspects of React" (40:11:55); then "our capstone
  projects. We built two back-to-back games" (40:12:03) — the sentence that overstates the
  video's contents.
- **What to learn next (40:12:28–40:13:57)** — the direct evidence for Modules 17–20: an
  **advanced React course** (reusability deep-dive, performance), the **TypeScript course**
  ("add TypeScript to assembly endgame"), **React Router v7** "about to release," **Next.js
  and Remix**, **Node with or without Express**, and **deployment**.

## Mapping to the syllabus activities

- **Section 02 does not exist** in the challenge files (numbering runs 01 → 03) — no transcript
  gap.
- **Section 01** lessons 01–24: fully covered across 26:41–28:49. The transcript spends extra
  time on *why/why-not* React (27:03–27:05) that the syllabus compresses into lessons 07–08.
- **Section 03**: fully covered; the five-part props sequence is unmistakable in the transcript
  (29:25–29:49), including the syllabus's aside (JS inside JSX), quizzes, and the
  travel-journal finale.
- **Section 04**: fully covered, including the sound pads four-parter (34:54–35:45) and the
  Chef Claude AI integration (35:45–36:18). Lessons 51–57 (refactor to components, get recipe,
  format recipe) all present.
- **Section 05**: fully covered; *useEffect practice- scrollIntoView()* is the Chef Claude UX
  pass at 37:49.
- **Section 06 (Tenzies)**: **not covered** — see above.
- **Section 07**: fully covered, including lessons 18 (farewell messages), 19 (disable
  keyboard), 22–24 (random word, new game, missed letters) and the accessibility work.
- Transcript-only extras: the course intro/outro (solo projects, Discord, Pro) and the
  what-to-learn-next plug at 40:12–40:13 — which doubles as evidence for Modules 17 and 20.

## What this module teaches

1. Why React exists, when a library is overkill, and why JavaScript must come first.
2. Project setup with Vite (and Node/npm/NVM underneath it).
3. Mounting with `createRoot`; JSX as sugar over `createElement`; curly braces as JavaScript
   holes.
4. Components: functions returning markup, PascalCase, parent/child, one component per file,
   `export default`/imports, a `components/` folder.
5. Props: concept, passing, receiving, destructuring, non-string values (booleans, arrays,
   objects).
6. Data-driven rendering: `.map()` over arrays, "objects are not valid as a React child," and
   the `key` prop.
7. Events as props; `onChange` per keystroke.
8. `useState`: the state/setter pair, functional updates, immutability for arrays and objects.
9. Re-render triggers: prop changes and state changes — and only those.
10. Conditional rendering with `&&` (and its count-of-zero trap) and ternaries.
11. Forms twice over: React 19 actions with `FormData`/`Object.fromEntries`, then controlled
    components.
12. Lifting state up; passing state and setters as props; when to reach for
    context/Redux/Zustand instead.
13. Side effects: the functional-programming contract, `useEffect`, dependencies arrays,
    infinite loops, and cleanup with `removeEventListener`.
14. API consumption inside React (imgflip memes, Star Wars, Claude recipes via HuggingFace).
15. Shipping discipline: deploy, share, celebrate — and accessibility (`aria-live`) as a
    first-class concern.

## Small practice task

Build a "study deck" app that touches every section of this module:

1. **Static + data-driven**: a header component and an array of at least five term/definition
   cards rendered with `.map()` and proper `key`s; data imported from its own file.
2. **State**: a "reveal definition" toggle per card (ternary or `&&`), and a "known" counter.
3. **Complex state**: a "new card" form — first with a React 19 action and
   `Object.fromEntries(new FormData(…))`, then redone with controlled inputs; submit adds to
   the array immutably (`[…prev, card]`).
4. **Child-to-parent**: the card component calls a prop function to mark itself known; the
   parent owns the array and updates one item immutably (the sound-pads lesson).
5. **Side effect**: fetch a random term from a public API on mount (`useEffect` + `[]`), with a
   cleanup function that cancels the fetch or clears a timer; guard any `&&` that could render
   a zero.
6. **Accessibility**: add an `aria-live="polite"` status line announcing "known cards: N"
   (the Assembly Endgame lesson).
7. Deploy it and post the link — the course's own final instruction.

## Readiness check for Module 16

Module 16 (Testing) has no transcript coverage — nothing in this module was ever tested. Before
moving on, be able to explain:

- Why a component re-renders (two triggers), and why mutating a local variable doesn't count.
- Why state updates must be immutable, with the spread pattern for arrays and objects.
- What the dependencies array of `useEffect` controls, and what happens with no array, `[]`, and
  a value.
- What a `useEffect` cleanup function is for, with the event-listener example.
- Why mapped components need keys.
- How props flow down and how data flows back up (lifting state).

And carry forward honestly: **you have never written a test for any of this, and you have never
built Tenzies** — Module 16's README covers the first gap; Module 18's covers the second.

## Exact syllabus order

1. **Static Pages**
   1. 01. First React Code
   2. 02. First React Challenge
   3. 07. Why React_ It_s Composable
   4. 08. Why React_ It_s Declarative
   5. 09. Random housekeeping
   6. 10. ReactFacts Project - Markup
   7. 11. Pop quiz
   8. 12. Custom Components
   9. 13. Custom Components Challenge Part 2
   10. 14. Custom Components Quiz
   11. 16. Custom Components - Parent_Child Components — Exercises 1–2
   12. 17. Styling with Classes — Exercises 1–3
   13. 18. Organizing Components — Exercises 1–2
   14. 19. Make Mental Outline of Project
   15. 20. Initial Project Setup
   16. 21. ReactFacts Project - Navbar & Styling
   17. 22. ReactFacts Project - Main Content Section
   18. 24. ReactFacts Project - Add Background Image
2. **Data-Driven React**
   1. 02. Travel Journal - Header
   2. 03. Travel Journal - Entry Component
   3. 05. Props Part 1- Understanding the Concept — Exercises 1–2
   4. 07. Aside- JS inside JSX — Exercises 1–2
   5. 08. Props part 3- Create a contract component
   6. 09. Props part 4- Passing data into a component
   7. 10. Props part 5- Receiving props in a component
   8. 11. Prop quiz (Get it_)
   9. 12. Destructuring props
   10. 13. Props practice
   11. 14. Non-string props
   12. 16. Pass props to Entry component
   13. 17. Review - array .map() — Exercises 1–3
   14. 18. React can render arrays
   15. 19. Mapping components
   16. 20. Map quiz
   17. 21. Travel Journal- Map Entry components
   18. 23. Travel Journal- Pass object as props
3. **React State**
   1. 02. Chef Claude Header
   2. 05. Event Listeners — Exercises 1–2
   3. 06. Chef Claude- Map ingredients list — Exercises 1–3
   4. 09. useState
   5. 11. Changing state
   6. 12. State practice — Exercises 1–4
   7. 13. Updating state with a callback function
   8. 14. Changing state quiz
   9. 15. Ternary practice — Exercises 1–2
   10. 16. Toggling state
   11. 17. Complex state- Arrays — Exercises 1–3
   12. 18. Chef Claude- Refactor array state
   13. 19. Complex state- Objects
   14. 20. Comeplex state- updating state objects
   15. 22. Form basics
   16. 24. Form action
   17. 25. Chef Claude- Refactor form submission
   18. 27. Forms- radio
   19. 30. Forms- Object.fromEntries
   20. 32. Conditional rendering- &&
   21. 34. Conditional rendering practice- &&
   22. 36. Conditional rendering practice
   23. 37. Conditional rendering quiz
   24. 38. Chef Claude- conditional rendering challenge 1
   25. 39. Chef Claude- conditional rendering challenge 2
   26. 40. Chef Claude- Get recipe placeholder challenge
   27. 41. Passing state as props
   28. 42. Setting state from child components
   29. 43. Passing data around React
   30. 44. Sound pads challenge, part 1
   31. 45. Dynamic styles
   32. 46. Sound pads challenge, part 2
   33. 47. Sound pads challenge, part 3
   34. 48. Sound pads challenge part 4.1 - local state
   35. 49. Sound pads challenge part 4.2 - shared state
   36. 50. Sound pads challenge part 4.3 - updating the item in array
   37. 51. Chef Claude challenge- refactor to separate components
   38. 55. Challenge quiz- prep to get recipe from the AI chef
   39. 56. Challenge- Get recipe from the AI chef
   40. 57. Format recipe response
4. **Side Effects**
   1. 02. Meme Generator Starting Point
   2. 03. Meme Generator State
   3. 04. Meme Generator - Controlled Components - part 1
   4. 06. Meme Generator - Planing data fetch
   5. 08. Fetching data in React
   6. 11. useEffect() Dependencies array
   7. 13. useEffect quiz
   8. 14. useEffect practice
   9. 16. State and Effect practices
   10. 18. Meme Generator - Get random meme
   11. 20. useEffect practice- scrolllntoView()
5. **Capstone Project #1 - Tenzies** *(no transcript coverage — promised at 26:32 and claimed in
   the outro at 40:12, but absent from the video)*
   1. 02. Tenzies- Setup
   2. 03. Tenzies- Die component
   3. 04. Tenzies- Generate 10 random numbers
   4. 05. Tenzies- Map array to Die components
   5. 06. Tenzies- Roll dice button
   6. 07. Tenzies- Challenge dice to objects
   7. 08. Tenzies- Styling held dice
   8. 09. Tenzies- Hold dice - part 1
   9. 10. Tenzies- Hold dice - part 2
   10. 11. Tenzies- Hold dice - part 3
   11. 12. Tenzies- End game - part 1
   12. 13. Tenzies- End game part 2
   13. 14. Tenzies- End game - part 3
   14. 16. Tenzies- New game
   15. 18. Tenzies- Accessibility Improvements - part 2
6. **Capstone Project #2 - Assembly- Endgame**
   1. 02. Assembly Endgame - Project Planning
   2. 03. Assembly Endgame - Header Section
   3. 04. Assembly Endgame - Status Section
   4. 05. Assembly Endgame - Languages List
   5. 06. Assembly Endgame - Word Display
   6. 07. Assembly Endgame - Keyboard
   7. 08. Assembly Endgame - Save the guessed letters
   8. 09. Assembly Endgame - Keyboard letter styles for guesses
   9. 10. Assembly Endgame - Only display correctly guessed letters in word
   10. 11. Assembly Endgame - Wrong guess count
   11. 12. Assembly Endgame - Lost languages
   12. 13. Assembly Endgame - isGameOver
   13. 14. Assembly Endgame - Display won_lost status
   14. 18. Assembly Endgame - Farewell messages
   15. 19. Assembly Endgame - Disable keyboard when the game is over
   16. 22. Assembly Endgame - Choose random word
   17. 23. Assembly Endgame - New game button resets the game
   18. 24. Assembly Endgame - missed letters when lost
   19. 25. Assembly Endgame
