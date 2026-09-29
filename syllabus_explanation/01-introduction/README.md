# Module 01: Introduction

## Purpose
This opening module introduces the learning environment and turns a small set of visual requirements into a working web page. The important lesson is not the finished page; it is the habit of changing one requirement at a time, previewing the result, and checking that the implementation matches the instruction.

## 01. Learn the Platform — Let’s Make a Cake

The first activity uses a familiar process—making a cake—to teach the course workflow. Treat the instructions as a sequence of small tasks:

1. Read the requirement before changing anything.
2. Identify the item or property that must change.
3. Make the smallest possible edit.
4. Run or preview the project.
5. Compare the result with the requirement.
6. Continue only after the current step works.

This workflow is the foundation for later coding challenges. A coding problem becomes easier when it is divided into observable steps instead of approached as one large task. When something fails, return to the last step that worked and inspect only the change made afterward.

### What to take from this activity

- Follow instructions in order.
- Use the editor and preview together.
- Expect mistakes and correct them incrementally.
- Do not confuse a visually similar result with a correctly implemented one.

## 02. Your First App

This section is a first introduction to changing an existing page through data and style choices. The activities are deliberately small, but together they demonstrate a useful development loop: select an element, provide content, style it, and preview the result.

### Activity 01 — Add your Name and Emoji

Add text content to the page: a name and an emoji. Text belongs in the document content, while styling should be kept separate from the content whenever possible. The emoji is also a reminder that web pages can display Unicode characters directly when the document uses an appropriate character encoding.

**Reasoning:** content answers “what is on the page?”; CSS and presentation answer “how does it look?” Keeping those concerns distinct makes later changes easier.

### Activity 02 — Display Photos

Add image elements and provide valid image sources. An image needs a source, and it should have meaningful alternative text so that users who cannot see the image can still understand its purpose.

A reliable check is:

1. Confirm the image URL or file path.
2. Confirm that the image loads in the preview.
3. Add useful alternative text.
4. Check that the image is not stretched or placed outside the intended layout.

### Activity 03 — Change the Background Image

A background image is a visual layer applied through CSS rather than ordinary document content. This distinction matters: use an HTML image when the image is part of the page’s meaning or content; use a CSS background when it is primarily decorative or part of the visual design.

When changing the background, check the image position, repetition, and scale. A technically correct URL can still produce a poor result if the image is repeated unexpectedly or makes text difficult to read.

### Activity 04 — Choose a Color

Color is introduced as a CSS value. A color can be written using a named color, hexadecimal notation, RGB/RGBA, or another supported CSS format. Choose a value that supports readability rather than choosing only by appearance.

The practical rule is to check foreground and background together. Text that looks acceptable in isolation may become difficult to read against the selected background.

### Activity 05 — Set the Font, Border, and Column Count

This final activity combines several independent style controls:

- **Font:** controls the typeface and affects readability and visual tone.
- **Border:** adds an edge around an element; width, style, and color usually work together.
- **Column count:** changes how repeated content is arranged, introducing the idea that layout is controlled by rules rather than manual positioning.

Make each change separately. If the page stops looking correct, this makes the problematic property easy to identify. Also check narrow and wide previews: a layout that works at one width may need responsive adjustments later in the course.

## How the ideas connect

The module moves from following a sequence to editing a page:

1. A requirement is translated into a small action.
2. Content is added to the document.
3. Images provide visual content.
4. CSS adds decorative backgrounds and colors.
5. Typography, borders, and layout rules refine the interface.
6. Previewing verifies the result after every change.

These are the same habits used in much larger applications. Later modules add HTML semantics, JavaScript behavior, Git, APIs, databases, and frameworks, but the basic loop remains: understand the requirement, make a focused change, test it, and iterate.

## Completion check

Before starting Module 02, you should be able to explain:

- The difference between page content and styling.
- Why an image needs a source and useful alternative text.
- When a background image is decorative rather than meaningful content.
- Why color choices must be checked for readability.
- Why making one change at a time makes debugging easier.

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
