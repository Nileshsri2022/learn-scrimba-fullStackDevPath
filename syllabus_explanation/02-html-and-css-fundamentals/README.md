# Module 02: HTML and CSS Fundamentals

## Completion status

**Complete for the supplied source files.** All five syllabus sections have a matching, contiguous
transcript segment, in the same order the syllabus lists them. This is one of the best-covered
modules in the whole course: roughly 4.5 hours of teaching (00:05–05:30) covering 67 named lessons
and 17 practice items.

Two things the transcript contains that the challenge-file syllabus does not:

1. A **hometown homepage solo project** at the end of the course (05:22–05:30), complete with a
   Figma onboarding segment.
2. Two **Bob Ziroll asides** that preview later modules: relative file paths (02:24) and
   Git-vs-GitHub / version control (03:24) — the latter is effectively a trailer for Module 04.

One thing the syllabus names that belongs to Module 01's territory: the very first lesson
(*HTML tags*, the `I code, therefore I am` demonstration) is documented in
[Module 01](../01-introduction/README.md) and is not repeated here.

## How the sources relate

The whole module is taught as one continuous beginner course by the Scrimba CEO, **Per Harald
Borgen** (the auto-transcriber renders his name "Pear", "Pier" and "pair" — including a `per.jpeg`
image file transcribed as "the pier.jpeg"). Bob Ziroll steps in twice for asides. There are no
chapter markers, so the boundaries below were found by listening for each project's introduction.

### Transcript map

| Transcript time | Content | Syllabus section |
|---|---|---|
| 00:05–00:12 | First heading lesson (documented in Module 01) | 01, lesson 01 |
| 00:12–00:36 | Nesting, news article, images, buttons, inputs | 01 |
| 00:36–00:50 | Anchor tags, the Google build, document structure, lists | 01 |
| 00:50–01:04 | Personal website project + deploy | 01, lesson 13 |
| 01:04–02:21 | "Second section": CSS syntax, the Google homepage with CSS | 02 |
| 02:21–03:24 | "Second CSS section": business card build + Netlify deploy | 03 |
| 03:24–03:32 | Bob aside: Git vs GitHub, version control (Module 04 preview) | — |
| 03:32–04:17 | Space exploration site | 04 |
| 04:17–05:21 | Birthday gift site | 05 |
| 05:21–05:30 | Hometown homepage solo project + course outro | — (extra) |

---

## Section 01 — Intro to HTML (00:12–01:04)

### Nesting and the `div` (00:12)

After the first heading lesson, the instructor introduces "something called **nesting**, which is
the act of nesting HTML elements inside of other HTML elements." A `div` ("short for divider…
I would rather call this a container") is written around the article's elements, the closing tag
goes below all of them, and everything inside is indented:

- the `h1`, `img`, `h3` and `p` become **children** of the `div`;
- indentation is "for readability purposes" — it signals the parent/child relationship;
- a `div` is invisible and changes nothing visually, "however, it has now given us the ability to
  target the entire article just by targeting this div" — the reason nesting matters for CSS and
  JavaScript.

The lesson then visualises the document as a **family tree** of parents, children and siblings —
vocabulary that returns when CSS selectors and flexbox need "the direct children" of a container.

### Write a news article (00:14–00:19)

The practice project is a news article used as a running joke: *"Jeff Bezos to buy Man United and
rename it Bezos United."* Structurally it is a `title`, an `h1`, an `h3` sub-heading and a
paragraph. The important teaching point is that the same information can be marked up in many
ways, and the browser only knows what the tags tell it.

### The `img` tag (00:18)

An image is added by copying an image address from the web and pasting it into the `src`
attribute. Two facts are stressed:

- the attribute goes **inside the opening tag**;
- images need a source that resolves — otherwise you get the broken-image icon.

(Alt text arrives much later, in the business card project at 02:31, where it is taught as an
accessibility requirement, not decoration.)

### Buttons (00:23)

Buttons are introduced with typical honesty about what HTML alone can do:

> "Now, this button doesn't do [anything]… this button will just be there and pretend to [work]."

The `button` element has an opening and closing tag with text between them. Interactivity comes
later, with JavaScript.

### Input tags (00:25–00:30)

Inputs are self-closing (`<input>` needs no closing tag) and their `type` attribute changes their
behaviour. The demonstration is a sign-up form: text inputs for "their username or a password",
and the observation that in password fields "the characters are always masked." A `select` dropdown
appears in the personal website project (00:52) for choosing a favourite movie genre.

### Anchor tags, and the Google build (00:36–00:46)

The Google homepage is the section's main project. First anchors are taught in isolation:

```html
<a href="https://www.google.com">Google</a>
```

- `a` stands for **anchor**; `href` is the address.
- "If we now run this, you can see that it renders as a link. And when we click it" — the browser
  navigates away.

Then the Google homepage is rebuilt: the logo image, a search input, two buttons, and Google's
small print underneath the buttons — which turns out to be anchors in paragraphs, e.g. text about
Google's privacy policy linking to google.com. A link back to `index.html` from the cloned page
demonstrates relative vs absolute URLs in passing.

### Proper document structure (00:41–00:43)

The lesson formalises what Scrimba had been doing behind the scenes:

```html
<!DOCTYPE html>
<html>
  <head>
    <title>...</title>
  </head>
  <body>
    <!-- everything rendered -->
  </body>
</html>
```

- `<!DOCTYPE html>` tells the browser this is modern HTML.
- `head` holds metadata "about the page that isn't rendered", including the **title tag** that
  names the browser tab.
- `body` holds everything that is rendered.

### Lists (00:46–00:50)

A "tribute site" listing top travel destinations introduces lists: an `ol` (**ordered list**)
wraps the whole list, and each `li` (**list item**) is one entry. Unordered lists (`ul`) get the
same treatment with bullet points instead of numbers.

### Build a Personal Website (00:50–01:04)

The section's capstone: *"you are going to build a website about yourself and we're going to
personalize it as well plus deploy it to the world."* Required tags:

- an `img` (your own photo, added by drag-and-drop — the example file is Per's `per.jpeg`);
- an `h1` "with a title. Of course, you should write your own name, not my name";
- an `h2` "some fun facts about you", as a `ul` of `li`s;
- a `p` with a nested `a` to your LinkedIn profile;
- an `input` and a `button` — "we are just pretending that you have a newsletter."

Part two is personalization through pre-written JavaScript functions the student only invokes:
choosing a movie genre changes the font ("cowboy" makes it a western-movie font), choosing a fruit
changes the colours ("if it for example is banana… suddenly your page is banana colored"), plus
light/dark mode and sharp/soft/round edge styles. *"So, now you are a cowboy banana."* The
JavaScript itself is explicitly out of scope: "you're going to learn JavaScript later in the
front-end developer path anyway."

Finally the site is deployed so "anyone around the world can visit this website" — the first of
several deploys in this module. (The personalization parameters overlap with Module 01's
*Your First App* activities: choose a colour, set the font, set the border. Module 01's README
treats those as unlabelled; this project is where the transcript actually demonstrates them.)

---

## Section 02 — Intro to CSS (01:04–02:21)

> "Welcome to the second section of this course where you are going to graduate from HTML into the
> world of CSS… The main project of this section is actually the google.com homepage because this
> time around you are going to write the CSS as well."

### Write your first lines of CSS (01:05)

The first CSS file is already linked from the HTML, and the lesson reverse-engineers the link:

```html
<link rel="stylesheet" href="styles.css">
```

- `link` points at something external; `rel="stylesheet"` says "it is a sheet that contains
  styles"; `href` dictates where it lives — the same attribute known from anchor tags.

The first CSS challenge is to redesign a "please accept our cookies" widget by changing values in
a `body` rule, which is where the core syntax is taught:

```css
body {
  color: red;
}
```

- the **selector** (`body`) chooses which elements to style;
- curly braces open and close the rule;
- inside, a **property** (`color`) is followed by a colon, a **value** (`red`) is followed by a
  semicolon — "you have to have that notation, otherwise you'll break the example";
- `color` means **text colour**.

CSS comments (`/* … */`) are introduced as the place where challenge hints live.

### Destroying Wikipedia (01:12)

Before styling Google, the section has fun "destroying vikipedia.org" (sic). The point is
pedagogical: right-click → inspect, find the stylesheet, and change values to see what breaks.
Editing a real site in DevTools teaches which property does what, with zero risk.

### Width, inline vs block, margin (01:14–01:39)

Working on the Google clone introduces the box model one side at a time:

- **`width`** on the logo image (300px), and on the search bar.
- **inline vs block** (01:19): "you have to learn about inline elements versus block elements."
  Inline elements sit beside each other; a "block level element blocks out the rest of the
  available horizontal space" and forces a new line. `display: inline` / `display: block` convert
  between them.
- **`margin-top`** and friends push elements apart.
- **Classes** (01:26): when two elements need different styling, give them `class` attributes and
  select with a dot: `.search-bar { … }`. Classes are the workhorse; elements are selected only
  when *all* of them should share a style.
- **Learn margin via flags** (01:30): a challenge series where margins recreate national flags —
  the flag of Monaco first ("Really good job creating your first CSS flag"), then the Gambia
  "however, there's a catch. You can only [use margins]" — flags are just coloured blocks with
  controlled spacing.
- **Centering content** (01:36): the classic recipe — a fixed `width` plus
  `margin: 0 auto` — with the reminder that a block element must have a width before auto margins
  can center it.
- **Padding** (01:40): "padding will add space on the inside in between" the border and the
  content — padding lives *inside* the element, margin *outside*.
- **Border and border-radius** (01:48): borders take a width, a style and a colour;
  `border-radius` rounds the corners — "go ahead and change the values of the border and border
  radius and [see] what happens."

### The box model, formally (01:51)

A dedicated practice piece walks the box from the inside out: **content → padding → border →
margin**. Comparing two buttons side by side ("this button has even more [padding]… we've added
half as much [margin]") makes each layer visible before the vocabulary is needed for precision.

### Aside — style a Twitter button (01:54)

The syllabus's "Aside challenge- style Twitter button" is the section's mini-challenge: recreate
Twitter's follow button (background colour, white text, rounded corners, hover state) using only
what has been taught so far.

### Fix the input, center and style the button (01:56–02:03)

Three more Google-clone challenges: match the input field's height and padding to the design,
center an element with margins, and style buttons to look like Google's — including the discovery
that buttons are inline by default and that `display: block` changes everything about their
layout.

### Why we can't have two block-level buttons, and flexbox (02:07–02:15)

> "Well, this is where flexbox comes to the rescue."

The problem: two block buttons stack vertically; made inline, "they will just be crammed all the
way to the left hand side" and lose their width. The simple-but-limited fix is `text-align:
center` on the parent ("that property actually works on all inline elements, not just on text").

The proper fix is flexbox, introduced with a tour of real sites: "Let's just have a look at
Twitter for example… the tweet options [and] the timeline itself… Flexbox is everywhere."

The mental model, verbatim from the lesson:

- "a flexbox layout always consists of **a container and its direct children**";
- wrap the items in a container, add `display: flex`, and the children line up on one row —
  "flexbox, as powerful as it is, overrides [the stacking] and forces them onto one line";
- with flexbox active, "flexbox now has control over these items and can decide" where they sit —
  which is why the old centering trick must be removed: "we don't want to use both techniques at
  the same time."

The section challenge is to center Google's two buttons with flexbox and give the container a
width, closing the loop on the centering problem that opened it.

---

## Section 03 — Build a Business Card (02:21–03:24)

> "Welcome to the second CSS section of this course where you are going to build" — a personal
> business card.

### Fix the image path, and relative paths (02:22–02:26)

The card's image is broken on purpose. The fix teaches relative paths: the image lives in an
`images/` folder next to `index.html`, so the source must be `images/per.jpeg` (transcribed as
"pair.png"). The method taught is itself the lesson: *paste the file-path string into Google*,
land on the W3Schools file-path table, and read off which syntax means "same folder", "child
folder", "parent folder".

Bob Ziroll then takes his first aside (02:24) with the same example: `cat.jpeg` lives inside
`images/`, so the string must be prefixed `images/`. He walks up and down the tree (`./`,
`../`) — a preview of the path reasoning Module 04's command-line section will demand.

### Add the alt attribute (02:31)

Every image should have alternative text: `alt="Per Harald Borgen, CEO of Scrimba"`. Two rules
are given for good alt text: it describes what is in the image, and "should be concise, meaning
less [than a sentence]." The lesson adds the practical motive alongside the accessibility one:
"writing alt text will help your site rank higher on Google."

### Make the image smaller, add a border and padding (02:33–02:39)

The raw headshot is "far too big", so it is sized down; a border and padding turn it into a
proper card. `padding` and `border` are now used deliberately rather than demonstrated.

### Flex item containers, utility class, justify the items (02:42–02:52)

- The card becomes a `display: flex` container, and the image and text become flex items. A
  revealing observation at 02:52: "the card is a display block even though we've set it to display
  flex. So that means that flexbox containers by default are display block" — which is why the
  three-ingredient centering recipe (width + block + auto margins) still applies to the card
  itself.
- A **utility class** is introduced: "It only has one job and that is setting a single CSS
  property." Utility classes get reused everywhere; component classes get composed from them.
- `justify-content` spreads the card's items horizontally.

### Center the card (02:52)

`width: 400px` (fixed, "we don't want that [stretching]" — a stretched card stops looking like a
business card) plus `margin: 0 auto`.

### Aside — inheritance (02:54–03:00)

Styles set on a parent cascade down: set `text-align: center` or a `color` on the body and "we get
the same" result on the children — "now this has been inherited down to" them. The limit is
taught too: **buttons don't inherit font families**, so a button in a custom-font page silently
keeps the default font unless you tell it to `font-family: inherit` (03:43).

### Colors and web-safe fonts (03:00–03:06)

Hex colours are read out of the design (`#` + six hex digits), with the aside that you rarely
hand-pick them — you copy them from a design or a palette. **Web-safe fonts** (Verdana et al.) are
fonts you can use "without worrying about whether or not it's installed on your users' computers,
because most likely it is" — the safe choice before custom webfonts arrive in Section 04.

### Margin & padding shorthand (03:12–03:18)

One value (`padding: 20px`) sets all four sides; two values set vertical/horizontal; four values
go clockwise from the top ("top, right, bottom, left"). The challenge asks the student to convert
longhand rules to shorthand and back, "and of course after you've done that the card should still
be" centred and intact.

### Deploy to Netlify, and share it (03:19–03:24)

The card is pushed to GitHub and deployed via Netlify: pick the repository, "scroll down to the
bottom and hit deploy site", wait for the screenshot, then click through to the live card. The
call to action is community-shaped: share the deployed link on Twitter "and mention me if you
want to alongside a link to your project."

### Bob's aside — Git vs GitHub and version control (03:24–03:32)

Immediately after the deploy, Bob Ziroll delivers an eight-minute aside that previews Module 04:

> "Git is what's called a version control system… it's something that runs locally on your own
> machine… GitHub is an online platform that stores… Git repositories."

- **Commits are save points**: "if you were to write some kind of bug into your code or
  accidentally delete everything… we can revert back to that commit and have everything restored
  the way that it was at that save point."
- **Version control manages other people's changes** — the group-paper-by-email story: emailing
  versions back and forth, "you had to come up with unique names", until someone merges them;
  Git "gives us a way to highlight those changes and decide which one of those changes we want to
  include."
- The analogy offered: "Git is kind of like taking photos on your phone… GitHub is kind of like an
  online photo sharing platform like Instagram."

---

## Section 04 — Build a Space Exploration Layout (03:32–04:17)

> "Welcome to the section where you are going to build a space exploration site."

### Center elements and style the button (03:32)

The section starts from "a basic HTML structure" and styles it piece by piece: centered content,
a styled call-to-action button — reusing every centering and button recipe from the Google build.

### Google Fonts (03:42–03:45)

Custom typography enters via Google Fonts: pick a font, "head over to Google Fonts, fetch the"
embed code, paste the `<link>` into the head, then set `font-family`. The instructor's honest
review of web-safe-only pages: "the font here is a little bit boring" — a custom font "can really
level up the design."

### `@font-face` (03:45)

For fonts Google doesn't host, download the font files and declare them yourself:

```css
@font-face {
  font-family: "My Font";
  src: url("fonts/my-font.woff2");
}
```

"Simply writing an at and then font-face" — the lesson walks through downloading "the recipe for
the font", the folder it lands in, and why the browser needs the declaration before the
`font-family` name means anything.

### Underline with a `span` (03:48)

`span` is the inline equivalent of `div` — a hook for styling a few words inside a sentence. The
design's underlined word is wrapped in a span and styled with a border-bottom, because
`text-decoration` would also affect spacing and colour in ways the design doesn't want.

### Use an ID for the logo (03:51)

`id` attributes select a single unique element (`#logo`), versus classes for groups. IDs are
presented as strictly one-per-page, with classes as the default choice.

### Utility classes again (04:16)

The underline style is refactored into "the underline class, which only has one job" — the same
utility-class discipline from the business card.

### The terms & conditions section (03:51–04:06)

A T&C block with small, grey text and links is added at the bottom — deliberately the least
glamorous part of the page, and the place where `font-size`, `color`, and link styling are
practised in combination.

### The `lang` attribute (04:14)

A short accessibility aside: set `<html lang="…">` because "screen readers use the lang attribute
to determine [pronunciation]" — and "you can find the code for your language with a quick online
search."

### Aside — text shadow, and readability (04:21–04:27)

`text-shadow` takes offsets and a colour (and optionally a blur). The build then reworks the
hero: text over a busy galaxy image is hard to read, so the shadow is tuned until the contrast
works. The lesson's criterion is the right one: shadows are a *readability* tool first and a
decoration second.

---

## Section 05 — Build a Birthday Website (04:17–05:21)

> "Welcome to this section where you are going to build a birthday gift site… what you do is
> basically add their information to the header… [and when] the birthday boy or girl hovers over
> the image, they will see a nice gift."

The site is a gift page for a friend (Nick): a header with his name, date and age, and a grid of
"GIFts" that animate on hover.

### Basic header styling, colors, text shadow (04:18–04:24)

The header is built first — typography, a colour scheme, and a text-shadow lifted straight from
the space exploration site: "you learned [this] in the space exploration section. You're going to
set the blur to…" — the course deliberately makes students *retrieve* earlier lessons rather than
re-teach them.

### `align-items` (04:29–04:36)

Flexbox's cross-axis control arrives with a memorable framing device: the instructor pretends the
two of you work in a lab and must "organize our lab equipment" using `justify-content` and
`align-items`:

- `justify-content` controls the **main axis** (left↔right in a row);
- `align-items` controls the **cross axis** (top↔bottom);
- each accepts `start`, `center`, `end` (and `space-between` for justify).

### `flex-direction` (04:36–04:38)

Setting `flex-direction: column` flips the main axis: "justify-content and align items no longer
work [the same]. However, they work in a [different orientation]" — what justify-content
controlled horizontally is now vertical. The axis-swap is drilled until it is intuitive.

### Turn the header into a flexbox; fix the date and age design (04:39–04:45)

The header's name, date and age are laid out with flexbox and the spacing is tuned — including a
refactor where the birthday-date rule is copied to the age rule and then de-duplicated.

### Create the first GIFt; replace the `img` with a `div` (04:48–04:54)

The gift images are animated GIFs, but "we are not going to use the image tag here in order to
display this gift." The reason (taught here, and expanded in Module 05): a background image on a
`div` can be swapped on hover, and can carry `role` and `aria-label` attributes for screen
readers. `background-size: cover` makes the div behave like a properly-cropped image ("there we
go").

### The hover effect (04:54–04:59)

```css
.gift-img:hover {
  background-image: url("images/gift.gif");
}
```

The pseudo-class `:hover` swaps the wrapped-gift image for the animated one — "Nick hovers over
the image and sees the underlying GIF." The same pattern then gets reused for every gift, and the
copy underneath each one is personalised.

### More GIFts, and the footer (05:00–05:18)

Three more gift cards ("Create the next GIFt", "two more", "the final GIFt") practise the same
steps unaided. The footer gets a dark background, and finally the page background becomes a
gradient:

```css
body {
  background: linear-gradient(blue, pink);
}
```

"Using the linear gradient function which we added to the background of the body" — the
background "slowly fades from blue to pink."

### Section recap (05:21)

The instructor recaps by name: `align-items` (cross-axis), `flex-direction: column` (flip the
main axis), the `:hover` pseudo-class, gradients via `linear-gradient`, and the **grouping
selector** — "which allowed us to make our CSS syntax much more compact as we could target all of
these HTML tags instead of having to recreate this text shadow rule again and again."

---

## The final section — hometown homepage solo project (05:21–05:30)

Not in this module's challenge files, but it is the course's capstone and the first fully solo
build:

> "Now, I'm going to remove the training wheels and you will have to build a full project on your
> own because that's actually the only way you can know whether or not you've truly learned HTML
> and CSS."

- **The project:** "a homepage for your hometown… about a place, area, city, or country that you
  care about" — motivation matters: sharing it in Discord lets other students get to know you.
- **The design source is Figma:** "Figma is the design tool in which you'll get the design for
  your project… It can kind of be seen as the GitHub equivalent for designers." Students sign up,
  duplicate the file, and are pointed to Bob's 10-minute Figma tutorial on YouTube (hosted off
  Scrimba because "learning a browser-based tool like this is actually better to do via a regular
  video").
- **Decomposition is taught explicitly:** the hero is "pretty similar to what we did in the space
  exploration site", the coloured headings are "what we did in the birthday gift card", the card
  "resembles our business card quite a lot", and the three columns are "a job for flexbox". A
  scary design becomes a set of known patterns.
- **Colour palettes:** coolors.co is linked, and using the supplied hex values is a requirement
  while choosing your own palette is a stretch goal.

This segment is also the bridge to [Module 14](../14-user-interface-design/README.md), which
documents the design material that never got its own module.

## Mapping to the syllabus activities

All 67 lessons and 17 practices in the syllabus have a home in the segments above. A few naming
notes, honestly stated:

- **01.01 HTML tags** — covered in [Module 01](../01-introduction/README.md); module 02 picks up
  at nesting.
- **02.17 "Aside challenge- style Twitter button"** — the button-styling challenges at 01:54–02:03
  are the Twitter-button material; the transcript does not say "Twitter button" at that point
  (Twitter is name-checked during the flexbox intro at 02:12 as a site built with flexbox).
- **04.x lesson numbers skip (01, 02, 06…)** — gaps in numbering are the challenge-files' doing,
  not the transcript's; the space exploration segment is continuous from 03:32 to 04:17.
- **05.17 "ARIA roles and attributes for background images"** — taught inside the GIFt lessons at
  04:48–04:54; the full accessibility treatment lives in
  [Module 05](../05-accessible-development/README.md).
- The **hometown homepage solo project (05:21–05:30)** is extra transcript content with no folder
  in this module's challenge files.

## What this module teaches

1. HTML elements describe *meaning*: headings, articles, lists, links, images, inputs, buttons.
2. Nesting creates a tree of parents and children; `div` and `span` are generic containers for
   grouping and styling.
3. Proper documents have `<!DOCTYPE html>`, `head` (metadata, title) and `body`.
4. CSS selects elements (element, `.class`, `#id`) and applies property/value pairs; syntax errors
   break rules silently.
5. The box model — content, padding, border, margin — plus shorthands, and which side of the
   border each layer lives on.
6. Inline vs block, and what `display` can do about it.
7. Centering: width + `margin: 0 auto` for blocks; flexbox for groups.
8. Flexbox = container + direct children; `justify-content` (main axis), `align-items`
   (cross-axis), `flex-direction` flips the axes.
9. Typography: web-safe fonts, Google Fonts, `@font-face`, and `font-family: inherit` for
   buttons.
10. Presentation details that carry meaning: alt text, `lang`, text shadows for readability,
    `:hover` states, gradients.
11. Utility classes ("only one job"), the grouping selector, and inheritance down the tree.
12. Shipping: deploy to the web (Netlify via GitHub), and share the result.

## Small practice task

Build a one-page "conference speaker card" using only this module's techniques:

1. A `div` card, fixed width, centred with `margin: 0 auto`, border and padding.
2. Inside: a photo with proper `alt` text; an `h1` name; an `h2` "fun facts" `ul`; a paragraph
   with a nested link.
3. A Google Font for the name (and `font-family: inherit` on the button so it matches).
4. A flexbox header row for name + photo, using `justify-content` and `align-items`.
5. A `:hover` effect on the photo that swaps a background image (div, not `img`).
6. Deploy it and send the link to one person.

Constraint: no CSS feature that was not named above — the point is to reproduce this module's
vocabulary from memory.

## Readiness check for Module 03

You are ready for JavaScript when you can explain:

- The difference between an element, an attribute and a class.
- What nests inside what in a well-formed document, and where the `title` goes.
- Selector syntax for element, class and id, and when each is appropriate.
- Padding vs margin vs border, and the clockwise shorthand.
- Inline vs block, and one way to change an element's behaviour.
- The two axes of a flex container and which property controls each.
- Why `margin: 0 auto` needs a width to work.
- How to put a custom font on a page two different ways.
- How to deploy a finished page to a public URL.

## Exact syllabus order

1. **Intro to HTML**
   1. 01. HTML tags *(covered in Module 01)*
   2. 02. Write a news article
   3. 03. The _img_ tag
   4. 06. Buttons
   5. 07. Input tags — Exercise 1, Exercise 2
   6. 08. Let_s build Google
   7. 09. Anchor tags
   8. 10. Add an anchor tag to Google.com
   9. 11. Proper document structure
   10. 12. Lists
   11. 13. Build a Personal Website
2. **Intro to CSS**
   1. 02. Write your first lines of CSS
   2. 05. Link to the CSS file
   3. 06. Set the width of the elements
   4. 07. inline vs block elements
   5. 08. Margin top
   6. 10. CSS classes
   7. 11. Learn margin via flags — Exercise 1, Exercise 2
   8. 12. Add space between our elements
   9. 14. Centering our content
   10. 15. Padding
   11. 16. Border and border-radius
   12. 17. Aside- style Twitter button
   13. 18. Fix the input field
   14. 19. Center the button
   15. 20. Style the button
   16. 21. Why we can_t have two block-level buttons
   17. 23. Centering both buttons with flexbox
3. **Build a Business Card**
   1. 02. Fix the image path
   2. 03. More on Relative Paths — Exercises 1–3
   3. 04. Add alt attribute
   4. 05. Make image smaller
   5. 06. Add a border and padding
   6. 08. Flex item containers
   7. 09. Add a utility class
   8. 10. Justify the items
   9. 11. Center the card
   10. 12. Aside- inheritance (Updated)
   11. 13. Center the text via inheritance
   12. 14. Add colors
   13. 15. Web-safe fonts
   14. 16. Margin_padding shorthand — Exercises 1–2
   15. 17. Use the margin&padding shorthands
4. **Build a Space Exploration Layout**
   1. 03. Center elements and style button
   2. 04. Google Fonts
   3. 05. @font-face
   4. 08. Add an underline using a span
   5. 09. Use an ID for the logo
   6. 12. Add the terms & conditions section
   7. 13. Aside- text shadow — Exercises 1–2
   8. 14. Improving the readability with text shadows
5. **Build a Birthday Website**
   1. 02. Add basic header styling
   2. 03. Set the colors
   3. 04. Add shadow on text
   4. 06. Align-items — Exercises 1–3
   5. 07. Flex-direction — Exercises 1–2
   6. 08. Turn the header into a flexbox
   7. 09. Fix date and age design
   8. 10. Create the first gift
   9. 11. Replace the img with div
   10. 13. Add the hover effect
   11. 14. Create the next GIFt
   12. 15. Create two more GIFts
   13. 16. Create the final GIFt
   14. 17. ARIA roles and attributes for background images
   15. 18. Add the footer
   16. 19. Add a background gradient
