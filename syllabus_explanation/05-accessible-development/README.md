# Module 05: Accessible Development

## Completion status

**Partially covered — and the gap is large enough that it has to be stated up front.**

The repository lists 23 sections for this module (text contrast, use of color, alternative text,
links, labels, radio buttons, semantic HTML, lists, text size, headings, ARIA, ARIA live regions,
skip navigation links, and a two-part final challenge). **The supplied transcript contains no
dedicated accessibility course.** There is no segment where a teacher says "welcome to the
accessible development module", and topics like *Use of color*, *Lists*, *Text-size*, *Headings*,
*Skip Navigation Link* and the *Final challenge* have no transcript material at all.

The React teacher confirms this directly while doing accessibility work later in the course:

> "Because this isn't a dedicated course to accessibility, I am just going to kind of explain the
> code that I'm writing as we go."

What the transcript *does* contain is **six accessibility segments scattered through other
modules**, taught as asides by four different teachers. Together they genuinely cover five of this
module's topics — contrast, alternative text, labels, ARIA, and ARIA live regions — and those five
are explained in full below, from the transcript. The rest is listed as a gap, not invented.

## Coverage map

| Syllabus section | Transcript coverage | Where it is taught |
|---|---|---|
| 02. Aside — Text contrast | **Covered** | 02:03:37, inside the Google clone CSS lesson (Module 02) |
| 03. Aside — Use of color | Not covered | — |
| 04. Text contrast (Exercises 1–2) | Concept covered, exercises absent | 02:03:37 |
| 05. Aside — Alternative text | **Covered in depth** | 02:31:41, business card project (Module 02) |
| 06. Aside — Links | Not covered | — |
| 07. Links and alternative text | Alt text only | 02:31:41 |
| 08. Aside — Labels | **Covered** | 33:04:35, React forms lesson (Module 15) |
| 09. Aside — Radio buttons (Ex. 1–2) | Mentioned only, not taught for accessibility | 33:32:04 |
| 10. Labels | **Covered** | 33:04:35 |
| 11. Semantic HTML | Touched on, never taught systematically | scattered |
| 12. Lists | Not covered | — |
| 13. Text-size | Not covered | — |
| 14. Headings | Not covered | — |
| 15. ARIA | **Covered** | 39:43:17, Assembly Endgame project (Module 15) |
| 16. ARIA live regions (Ex. 1–2) | **Covered in depth** | 39:45:54 |
| 19–21. Skip Navigation Link | Not covered | — |
| 22–23. Final challenge | Not covered | — |
| *(not in syllabus)* | **`lang` attribute** | 04:15:21, taught by Gil (Module 02/06 boundary) |

---

## Text contrast

Taught inside a CSS lesson on styling a Google homepage clone, not as an accessibility lesson — but
the reasoning is complete.

The instructor stops mid-project because of a problem with the real google.com design:

> "Notice how low the contrast is between the background color of the button and the background
> color of the entire website. It's hardly possible to see that there's any difference. And that's
> not good because it reduces the accessibility of the site and makes it hard for people who are
> visually impaired to use it."

### How to check contrast

1. Take the two colours involved — the **foreground** and the **background**.
2. Paste them into an online contrast checker (the lesson uses the one at `userway.org`).
3. Read off the **contrast ratio**.

### The worked example

Google's button background is the hex colour `#F8F9FA`, sitting on a white page background.

- Measured ratio: **1.05**
- Required minimum: **4.5 or more**
- Verdict in the lesson: "Google indeed fails miserably on this test. Complete failure."

The fix applied in the project is simply to use a visibly darker grey for the button background so
that the button reads as a button. The instructor notes the deliberate divergence: "even though the
real background color is this one right here, we are going to use this one right here."

### What to take from it

- Contrast is measured as a **ratio between two specific colours**, not judged by eye.
- **4.5:1** is the threshold used in this course for normal text.
- A very large, very famous site can fail it — so check your own work rather than copying.
- Low contrast is not only an aesthetic issue; it is what makes an interactive element fail to read
  as interactive.

**Syllabus note:** Section 04 lists two exercises for text contrast. They are not in the transcript.
Substitute practice: take any project you have built, run every foreground/background pair through a
contrast checker, and record the ratios before changing anything.

---

## Alternative text

The most thoroughly taught accessibility topic in the whole transcript. It appears in the business
card project, immediately after an image element is added.

> "This image element actually has a serious flaw because it lacks an important ingredient that all
> image tags should have, which is called the alt text or the alternative text."

### The syntax

```html
<img src="profile.png" alt="Per Harald Borgen smiling at the camera with a colorful background">
```

`alt` is an attribute on the `img` tag whose value is a description of the image. Adding it produces
**no visible change** in the browser — which is exactly why the lesson stops to justify it.

### Three reasons it matters

1. **Screen readers.** A person who is blind or visually impaired uses a screen reader, which "goes
   through the HTML and reads it out loud to the user." An `h3` is easy — it is text. An image has
   nothing to read unless you supply the `alt` text.
2. **Fallback rendering.** If the `src` is wrong — the example given is an accidental extra letter
   in the filename — the image will not render, and the `alt` text tells the user what was supposed
   to be there.
3. **Search ranking.** The `alt` text is metadata Google uses to understand the image, so it can
   bring search traffic. And "if your site is not accessible, it might be punished in the form of
   ranking lower."

### Three rules for writing it

1. **Do not start with "image of".** The screen reader already knows it is an image, because it is
   an `img` tag.
2. **Keep it under 125 characters.** "A lot of screen readers will cut off after this limit has been
   reached."
3. **Imagine describing the image to a person over the phone.** This is the trick the lesson offers
   for judging whether a description is good enough.

### The Muhammad Ali example

An iconic photo of Muhammad Ali standing over Sonny Liston, worked through three drafts:

| Draft | Verdict from the lesson |
|---|---|
| `alt="a boxing match"` | "A pretty poor way of describing it because there's so much more going on here." |
| `alt="two boxers in the ring, one lying down and the other standing up"` | "A good factual explanation, but we're not quite there yet" — it misses the moment. |
| `alt="Muhammad Ali in the boxing ring screaming at Sonny Liston after knocking him out"` | "That properly describes the intent of this image." |

The principle behind the progression: describe **what the image is there to convey**, not just what
objects are visible in it. "What the person who has decided to show this image on a website is
trying to convey."

### The challenge and its solution

Write alt text for the instructor's profile photo. The solution is built in three pieces, thinking
aloud:

- the subject — his name
- what he is doing — "smiling at the camera", judged important
- the setting — "the background is really playful and colorful", so "with a colorful background"

Closing note, which is a reasonable standard to hold yourself to:

> "If yours was a bit simpler or shorter, don't worry about it. The most important thing is that you
> add an alt text and do as best as you can. Plenty of developers never add this. So just by adding
> it, you are actually separating yourself from most other beginners."

### Reinforcement later in the course

The same idea returns during a DOM-manipulation lesson, where images are built as an HTML string
and injected in one go. After the performance point is made, the instructor adds:

> "The final thing we should add is an alt attribute because that is important for accessibility
> purposes so that people with, for example, screen readers can understand what the images contain."

The value used there is `employee in the company`. Worth noting: when images are generated by
JavaScript, the `alt` text has to be generated too — it is easy to lose it in a template string.

---

## The `lang` attribute

Taught by Gil as a short drop-in at the end of a section. It is **not** in this module's syllabus at
all, but it belongs here topically, so it is recorded rather than dropped.

```html
<html lang="en">
```

Three reasons given:

1. **Screen readers use it to decide which language to read the content in.** "This is essential for
   users who rely on assistive technologies" — the same text read with the wrong pronunciation rules
   is far harder to understand.
2. **Search engines use it** to understand the language of your content.
3. **It ensures consistency in language-specific features** like date formats and character sets.

The value is a standardised language code, usually two or three letters: `en` for English, `es` for
Spanish. "You can easily find the correct code for your language with a quick online search."

**Mixed-language pages:** set the primary language on the `<html>` tag, then put `lang` on the
individual elements that differ.

```html
<html lang="en">
  ...
  <h3 lang="es">Bienvenidos</h3>
```

> "Setting the language of your page might seem like a small step, but it does play a big role in
> accessibility and helps your website reach the right audience."

---

## Labels

Taught inside the React forms lesson, which makes it a *later* topic in the course than this module,
but the HTML reasoning is general.

### Why a placeholder is not a label

The lesson treats this as a habit to break, in unusually direct terms:

> "It can be tempting to say, well, I'm going to use the placeholder attribute to say this is going
> to be where the email goes. In fact, I think this is something you will very commonly see, but
> it's a habit that I'm going to try and weed out of you right now. A placeholder is **not** the
> correct tool to use as a label for your input."

The reason: **a screen reader will not read placeholder text**, so a user relying on one has no way
to know what the input is for.

What a placeholder *is* good for: an **example** of the expected input, like `joe@email.com`.

Related point made in the same lesson: always set the correct `type` on an input (`email`,
`password`, and so on). It affects keyboards on mobile, validation, and possibly password managers.

### Two correct ways to associate a label

**Option 1 — wrap the input inside the label.** No extra attributes needed; the association is
automatic.

```html
<label>
  Email
  <input type="email" placeholder="joe@email.com">
</label>
```

**Option 2 — keep them as siblings, and link them explicitly.**

```html
<label for="email">Email</label>
<input type="email" id="email">
```

The `for` attribute's value must be the **`id` of the input** it labels.

> **React caveat from the transcript:** in JSX you write `htmlFor` instead of `for`, because you are
> setting a property on a DOM element from JavaScript and the label element "doesn't have a `for`
> property, it has an `htmlFor` property."

### How to verify it worked

**Click the label text.** If the association is correct, the cursor jumps into the input. This is a
two-second check you can run on any form, and it is the test the lesson uses for both options.

The instructor's own preference is the sibling version with `htmlFor`, on the grounds that it is
easier to style — "honestly whichever way you choose is going to be completely fine."

**Challenge from the transcript:** add a second label and input for a password field, using the
correct `type` and "the other attributes that are necessary too" — meaning the `id`/`htmlFor` pair.

---

## ARIA

Taught while finishing the Assembly Endgame game in the React module. Three distinct techniques.

### 1. `aria-disabled`

The game disables its on-screen keyboard when the game ends. The visual `disabled` attribute is not
always enough:

> "There are some screen readers that will announce when a button is disabled, but some of them
> don't. And so we can add a dedicated `aria-disabled` property."

```jsx
<button
  disabled={isGameOver}
  aria-disabled={guessedLetters.includes(letter)}
>
```

Note the deliberate difference between the two values. `disabled` reflects whether the game is over;
`aria-disabled` is set per-letter, for letters already guessed. The reasoning is about the
tab-through experience: "when we're thinking about someone who is using the tab key to tab through
all of these letters, maybe a better user experience would be to disable the ones that have already
been chosen."

### 2. `aria-label`

When tabbing across the keyboard, a screen reader reads just the letter — "A", "B", "C". Adding a
label gives it context:

```jsx
<button aria-label={`Letter ${letter}`}>
```

Now it announces "Letter A", "Letter B". The instructor is honest that this one is a judgement call:
"I guess at that point it might just be a preference."

### 3. `aria-live` regions

This is the most important technique in the segment, and the one the syllabus gives its own section to.

**The problem:**

> "Screen readers are not just going to automatically announce things that get added to the DOM by
> React."

A status message that appears dynamically is invisible to assistive technology unless you mark the
region as live.

**The basic fix** — applied to the section wrapping the game status:

```jsx
<section
  className="game-status"
  aria-live="polite"
  role="status"
>
```

- **`aria-live="polite"`** — "polite just means that it's not going to interrupt the rest of
  whatever it's currently reading to announce changes to the section. It will queue it to the end of
  any changes that the screen reader is currently reading."
- **`role="status"`** — declares the section's role, giving "some additional accessibility benefits".

**The advanced fix — a visually hidden live region.** For the revealed word, a simple live region
would read out something awkward. So the lesson builds a section that exists *only* to be read
aloud:

```jsx
<section className="sr-only" aria-live="polite" role="status">
  <p>Current word: {currentWord.split("").join(" ")}</p>
  <p>You have {numGuessesLeft} attempts left.</p>
</section>
```

- **`sr-only`** stands for *screen reader only*. The CSS class "essentially is removing it from the
  visible area and doing everything it can to make sure it never shows up."
- Because the content is never seen, **you can write text specifically for listening** — full
  sentences like "Current word:" and a spaced-out word so letters are read individually, rather than
  reusing the visual markup.
- The number of remaining guesses is pulled from state rather than hard-coded, so the announcement
  stays correct.

**A maintenance note made in the lesson:** another developer could easily miss what `sr-only` means,
so add a comment describing the section as a combined visually-hidden ARIA live region for status
updates.

The summary given: "with just those few updates, maybe a dozen or two lines of code, we have now
made this app much, much more accessible for those using any kind of assistive technology" — with
the caveat that you still need to "go through and make sure that your contrast ratios are good
enough and everything like that."

### One more judgement call worth recording

While adding a decorative React logo to a page, the instructor chooses a CSS `background-image` over
an `<img>` element:

> "Because this isn't an element that is really a semantically important part of our markup... I
> don't need a screen reader to read that there's an image element here or have it be accessible via
> the keyboard."

**Decorative images belong in CSS; meaningful images belong in HTML with `alt` text.** That choice
is itself an accessibility decision.

---

## Gaps — what this module's syllabus covers that the transcript does not

These need a different source. Do not treat their absence as unimportant; several are core.

- **Use of color** — not relying on colour alone to convey meaning.
- **Links** — descriptive link text, and why "click here" fails out of context.
- **Radio buttons** — accessible grouping with `fieldset`/`legend`. Radio buttons appear in the React
  module, but only as form mechanics, not accessibility.
- **Semantic HTML** — `nav`, `main`, `header`, `footer`, `article` are used throughout the transcript
  but never taught as an accessibility topic in their own right.
- **Lists** — why list markup matters to screen reader navigation.
- **Text-size** — relative units and respecting user zoom/font settings.
- **Headings** — a logical `h1`–`h6` hierarchy with no skipped levels.
- **Skip navigation links** (three sections, including a two-part aside).
- **The final challenge** (two parts).

## What this module teaches — from the parts that exist

1. Contrast is a measurable ratio between two colours; **4.5:1** is the working minimum, and you
   check it with a tool rather than by eye.
2. Every meaningful `<img>` needs `alt` text; decorative images should be CSS backgrounds instead.
3. Good alt text conveys the image's **intent**, avoids "image of", and stays under 125 characters.
4. Alt text also buys you fallback rendering and search ranking — accessibility work is rarely
   *only* accessibility work.
5. Set `lang` on `<html>`, and on any element whose language differs.
6. A placeholder is not a label. Screen readers do not read placeholders.
7. Associate labels either by wrapping the input or with `for`/`htmlFor` + `id`, and verify by
   clicking the label text.
8. Content injected into the DOM dynamically is silent to screen readers unless it sits in an
   `aria-live` region.
9. `aria-live="polite"` queues announcements instead of interrupting; pair it with `role="status"`.
10. A visually hidden `sr-only` region lets you write text *for listening* rather than reusing
    visual markup.
11. Use `aria-label` and `aria-disabled` to give assistive technology information the visual design
    conveys some other way.

## Small practice task

Take any finished project of yours and make five passes over it, one per topic:

1. **Contrast.** List every foreground/background colour pair. Run each through a contrast checker.
   Write down the ratios. Fix anything below 4.5:1.
2. **Images.** For each image, decide: meaningful or decorative? Meaningful ones get an `<img>` with
   alt text written by the over-the-phone test. Decorative ones become CSS backgrounds.
3. **Language.** Add `lang` to `<html>`. If any content is in another language, tag those elements too.
4. **Forms.** Find every input. Remove any placeholder that is acting as a label, replace it with a
   real `<label>`, and click each label to confirm focus moves into its input.
5. **Dynamic content.** Find everything that appears or changes without a page reload — status
   messages, counters, error text, search results. Wrap each in `aria-live="polite"` with
   `role="status"`. For one of them, add a visually hidden `sr-only` version written specifically to
   be read aloud.

## Readiness check for Module 06

You are ready to continue when you can explain:

- What a contrast ratio is, what the minimum is, and how to measure one.
- Three reasons alt text matters, and three rules for writing it well.
- Why `alt="image of a dog"` is worse than `alt="a dog"`.
- How to decide whether an image belongs in HTML or in CSS.
- What `lang` does and where it goes.
- Why a placeholder cannot serve as a label, and two correct ways to associate one.
- Why `htmlFor` replaces `for` in JSX.
- Why a screen reader misses React-rendered updates, and what `aria-live="polite"` changes.
- What `sr-only` is for and why its text can differ from the visible text.
- **Which accessibility topics you still have not been taught** — the nine listed in the Gaps
  section above. Knowing what you are missing is part of the readiness check for this module.

## Exact syllabus order

1. 02. Aside — Text contrast *(covered)*
2. 03. Aside — Use of color *(gap)*
3. 04. Text contrast — Exercise 1, Exercise 2 *(concept covered, exercises absent)*
4. 05. Aside — Alternative text *(covered)*
5. 06. Aside — Links *(gap)*
6. 07. Links and alternative text *(partial)*
7. 08. Aside — Labels *(covered)*
8. 09. Aside — Radio buttons — Exercise 1, Exercise 2 *(gap)*
9. 10. Labels *(covered)*
10. 11. Semantic HTML *(partial)*
11. 12. Lists *(gap)*
12. 13. Text-size *(gap)*
13. 14. Headings *(gap)*
14. 15. ARIA *(covered)*
15. 16. ARIA live regions — Exercise 1, Exercise 2 *(covered)*
16. 19. Aside — Skip Navigation Link Part 1 *(gap)*
17. 20. Aside — Skip Navigation Link Part 2 *(gap)*
18. 21. Skip Navigation Link *(gap)*
19. 22. Final challenge part 1 *(gap)*
20. 23. Final challenge part 2 *(gap)*
