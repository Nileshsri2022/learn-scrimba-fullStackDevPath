# Module 01: Introduction

## Completion status
**Complete for the supplied source files.** This explanation separates the repository syllabus from the transcript because the syllabus is a challenge-file outline while the transcript is a continuous video transcript without matching chapter markers.

## How the sources relate

The transcript opens by describing the full learning path: HTML, CSS, JavaScript, and later technologies such as React, Node, Next, SQL, TypeScript, testing, and AI engineering. It then begins the first practical HTML lesson. The repository syllabus names the opening challenge activities as **Learn the Platform** and **Your First App**, but those names are not spoken as transcript chapters. Therefore, the explanation below does not pretend that every activity has a separate transcript segment.

## Transcript explanation: the first practical web page

### 1. From an ordinary sentence to structured content

The instructor begins with the idea that a sentence can be written in a normal text editor, but a web page needs more information than the words alone. The browser needs to know whether text is ordinary paragraph content, a heading, an image, or another kind of element.

The example uses the sentence “I code, therefore I am.” The important point is that the sentence and its visual importance are different things. A heading is not just text that happens to look large; it is content identified as a heading.

### 2. Create the HTML file

The lesson creates a file named `index.html`. This is a conventional entry-point name for a basic web page. The extension tells tools and editors that the file contains HTML.

Start with plain text:

```html
I code, therefore I am.
```

When the file is opened in a browser, the browser displays the text. At this stage it is unstructured text, so it does not communicate that the sentence is the main heading of the page.

### 3. Use an opening and closing tag

To identify the sentence as a level-one heading, wrap it in an `h1` element:

```html
<h1>I code, therefore I am.</h1>
```

The two parts have different jobs:

- `<h1>` is the opening tag.
- The sentence is the element content.
- `</h1>` is the closing tag.
- The slash in the closing tag tells the browser that the element ends there.

The browser then renders the content as a prominent heading. The visual change is useful, but the structural meaning is more important: assistive technologies and search engines can recognize the text as the page’s primary heading.

### 4. Add supporting text

The transcript then adds the philosopher’s name below the heading. A simple version is:

```html
<h1>I code, therefore I am.</h1>
<p>René Descartes</p>
```

The `p` element identifies the name as a paragraph-like piece of supporting content. This illustrates a central HTML idea: choose an element because of the meaning of the content, not only because of the default appearance produced by the browser.

### 5. Preview after each change

The lesson repeatedly returns to the browser after editing the file. That is a practical development loop:

1. Make one small change.
2. Save the file.
3. Reload or rerun the page.
4. Check whether the browser output matches the intention.
5. Fix the last change if the result is wrong.

This is the same loop used later for CSS, JavaScript, React, and backend work. Small changes make errors easier to locate and make the relationship between source code and browser output visible.

## Mapping to the syllabus activities

### Section 01 — Learn the Platform: Let’s Make a Cake

The supplied transcript does not explicitly describe the cake exercise. In the repository syllabus, this is the onboarding activity. Its transferable lesson is the challenge workflow: read a requirement, make a focused change, preview it, and continue in sequence. It should not be presented as a transcript quotation.

**Exercise 1 and Exercise 2:** these are listed in the syllabus but are not independently identifiable by name in the transcript file. Their explanation should come from the actual challenge files if those files are later added to the repository.

### Section 02 — Your First App

The repository lists five small visual activities. The transcript’s opening HTML demonstration provides the foundation for understanding them, but the transcript does not label these five activities individually.

- **Add your Name and Emoji:** add page content as text. Choose a suitable HTML element for each piece of content.
- **Display Photos:** use an image element with a valid source and meaningful alternative text. The transcript establishes the broader idea that HTML elements describe content; it does not provide a separate transcript chapter for this activity.
- **Change the Background Image:** this is a CSS presentation task. It belongs after the basic HTML structure even though the syllabus places it in the first-app activity sequence.
- **Choose a Color:** this is also a styling task. Check the color against the surrounding background so content remains readable.
- **Set the Font, Border, and Column Count:** these are presentation and layout settings. Make each change separately and preview the result after each one.

## What this module teaches

1. A browser can render an HTML file directly.
2. `index.html` is a conventional starting filename.
3. HTML tags give content structure and meaning.
4. An opening tag and matching closing tag define an element.
5. `h1` represents a top-level heading; it is not merely a shortcut for making text large.
6. Supporting content should be marked up according to its role.
7. Saving and previewing frequently creates a reliable feedback loop.
8. The repository activity names and the transcript’s spoken lesson boundaries are not identical.

## Small practice task

Create an `index.html` file containing:

```html
<h1>I code, therefore I am.</h1>
<p>René Descartes</p>
```

Then change only one thing at a time:

1. Replace the heading text.
2. Add a second paragraph.
3. Add an emoji to the paragraph.
4. Preview the page after every change.

Do not add CSS yet. The purpose is to verify that the document structure and browser feedback loop are understood before styling is introduced.

## Readiness check for Module 02

You are ready to continue when you can explain:

- Why the browser needs HTML structure rather than plain text alone.
- What each part of `<h1>...</h1>` does.
- Why a closing tag contains a slash.
- Why `h1` should be selected for meaning, not simply for large text.
- How to test a change by saving and previewing the page.
- Which parts of the opening syllabus are not explicitly covered by named transcript sections.

## Exact syllabus order

1. Learn the Platform — Let’s Make a Cake
   - Exercise 1
   - Exercise 2
2. Your First App
   - Add your Name and Emoji
   - Display Photos
   - Change the Background Image
   - Choose a Color
   - Set the Font, Border, and Column Count
