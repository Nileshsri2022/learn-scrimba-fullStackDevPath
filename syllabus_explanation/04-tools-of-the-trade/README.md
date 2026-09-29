# Module 04: Tools of the Trade

## Completion status

**Complete for the parts the transcript covers, with two gaps recorded honestly.**

- **Section 01 — Command Line Fundamentals:** fully covered by the transcript, lesson by lesson.
- **Section 02 — Command Line Power Tools:** **not in the transcript.** The instructor says so out
  loud at the end of section one: *"At the time of recording this scrim, section two of this course
  is still in the making."* The repository lists a `03. Local setup` activity with five exercises,
  but no transcript segment explains it. Nothing below invents that content.
- **Section 03 — Essential Git and GitHub Skills:** fully covered, plus one topic the transcript
  teaches that the repository has no folder for (merge conflicts — see the note on the numbering gap).

## How the sources relate

The module has two teachers. The transcript introduces them at the start:

> "We're going to start out looking at the command line and how you can use Linux commands to
> control your computer via the terminal. And then you're going to take a deeper dive into Git and
> GitHub as there are some key collaboration techniques like branching, pull requests, and merging
> that you need to learn before collaborating with other developers in a team."

The auto-transcription garbles the first teacher's name (it appears as "IO Borqual", "Ay Boval" and
"AB" at different points), so this document just calls them *the command-line instructor*. The
second teacher introduces herself clearly as **Treasure**, and a short closing segment is delivered
by **Bob** on SSH and GPG keys.

### Transcript map

| Transcript time | Content | Syllabus section |
|---|---|---|
| 14:01:27 | Module intro — both teachers named | — |
| 14:02:03 – 14:46:52 | Command line basics course | Section 01 |
| 14:46:52 – 15:05:47 | Branches, pull requests, merge conflicts, pulling | Section 03 |
| 15:05:47 onward | SSH and GPG keys | beyond the syllabus |

---

## Section 01 — Command Line Fundamentals

### The framing device

The whole section is taught as a story. The instructor plays a startup founder building a geography
quiz game ("What is the world's tallest mountain?", "How long is the river Nile?"), who stayed up
all night brainstorming on Post-its and made a mess of the project's file system. You are hired as
the unpaid intern whose job is to clean it up. Every challenge is a cleanup task inside a
`geography-game` directory.

This matters practically: the commands are never taught in the abstract. Each one arrives because a
file is in the wrong place.

### What the command line actually is

> "The command line is a user interface that allows us to utilize the functions of our device."

Key points from the slides:

- The same tool has different names per platform: **Terminal** on macOS, **PowerShell** on Windows.
  Scrimba calls its built-in one **terminal**, and the course uses that word throughout.
- A graphical file manager (the Finder screenshot in the lesson) and the terminal show the **same
  file tree**. The Finder version has icons distinguishing files from directories; the terminal
  version is plain text. Same contents, different interface.
- The analogy used is a **screwdriver and a power drill** — both can do the job, but one is usually
  the better choice for a given task.

Three reasons the lesson gives for preferring the CLI:

1. **File management is faster and more efficient** than clicking.
2. **Developers control their environment with it** — installing packages and dependencies, creating
   virtual environments, handling version control with Git.
3. **Automating repetitive tasks.** The example: add a single dot to the end of 10,000 files. Click
   each one in Finder, or write a script and run it once?

Setting up the terminal in Scrimba: click the small **plus** icon next to the word *runner* at the
bottom of the window, then click **add a terminal**. A path is printed in blue — that is the
directory you are currently working in.

### Lesson 03 — Inspect the file tree

Three commands, introduced together.

The instructor first hides the Scrimba sidebar, on the grounds that using a graphical file list "in
a command line course would basically be cheating."

```bash
pwd     # print working directory
ls      # list the contents of the current directory
cd      # change directory
clear   # clear visual clutter from the terminal
```

- **`pwd`** prints the full path of where you are, in more detail than the blue path already shown.
  At the start it prints something like `/home/projects/<random-id>` — that random-looking id is the
  root directory of the Scrimba project.
- **`ls`** lists what is inside the current directory. Files and directories are not distinguished
  by icons here; you read the names.
- **`cd <name>`** takes a directory name as an **argument**. After `cd geography-game`, nothing is
  printed — but the blue path now ends in `geography-game`, which is how you know it worked.
- **`clear`** only removes visual clutter. The lesson is explicit: **no running action is stopped**.

**The recurring lesson:** most of these commands print nothing on success. You verify by running
`pwd` or `ls` afterwards. This habit is repeated in every single challenge in the section.

**Challenge:** print the working directory, navigate into `geography-game`, list its contents, clear
the terminal. The instructor deliberately runs `clear` before handing over so you cannot copy the
commands off the screen.

**Solution walkthrough:** `pwd` → root. `cd geography-game` → path changes. `ls` → shows
`readme.md`, a `countries` directory, a `forests` directory, and `rainforest.txt`. `clear`.

### Lesson 04 — Rules of navigation

The concept: you cannot jump between branches of the file tree.

> "When we move around in this real-world tree, we are not birds and we are not monkeys either.
> Actually, we are much more like tiny tiny ants."

If you are inside `forests` and want to reach `countries` — a sibling directory — you cannot go
directly. You must go **up** to the common parent `geography-game` and then **down** into
`countries`.

The `..` syntax does both in one command:

```bash
cd ..                  # go one level up, to the parent directory
cd ../countries        # go one level up, then down into countries
ls ..                  # list the parent directory's contents without moving
ls ../countries        # list a sibling directory's contents without moving
cd ../..               # go up two levels
```

Breaking down `../countries` exactly as the lesson does:

- `..` means *go one level up in the file tree, please*.
- Stopping after `..` navigates to the parent, relative to where you are now.
- Adding `/` says *let me enter a new directory, please*.
- The name after the `/` is the directory to enter.

This syntax works with several commands, including `cd` and `ls`.

**Challenge:** navigate into `forests`, then locate three files — `rainforest.txt`,
`large-countries-by-population.txt`, `capitals.txt` — then clear the terminal. You must use `pwd`,
`ls`, `cd`, `..` and `clear`.

**Solution walkthrough — this is the most instructive one in the section**, because it is a genuine
search, not a recital:

1. `pwd` → root. `ls` → no `forests`, but there is `geography-game`.
2. `cd geography-game`, `ls` → `forests` is there. `cd forests`, `pwd` to confirm.
3. `ls` inside `forests` → **no** `rainforest.txt`, but `large-countries-by-population.txt` is here
   (found file 1, in the wrong place).
4. `ls ..` → lists the parent, `geography-game`, and there is `rainforest.txt` (found file 2).
5. `ls ../countries` → `large-countries-by-area.txt`, but no `capitals.txt`.
6. By elimination it must be in the root. `cd ../..` → up past `geography-game` to the root.
   `ls` → `capitals.txt` (found file 3), sitting outside the game directory entirely.

The instructor notes this will have to be fixed later, once moving files has been taught — which is
section two material, and section two is not in the transcript.

### Lesson 05 — Create and delete files

```bash
touch mountains.txt          # create a file
rm mountains.txt             # remove a file
touch ../cities/biggest-cities.txt   # create a file elsewhere using a path
```

- **`touch <name>`** creates a file with that name.
- **`rm <name>`** removes it. `rm` is short for *remove*.
- Both default to acting in the **current working directory**, but — exactly like `ls` and `cd` —
  they accept a path, so you can create or delete somewhere else.

In `touch ../cities/biggest-cities.txt`, `cities` sits at the same level as the current directory,
so the path starts with `..` to reach the common ancestor first.

**Challenge:** the instructor's uncle borrowed the laptop and a file called `virus.exe` has appeared.
Find and delete it, then create a new file `rules.txt` inside `geography-game`.

**Solution walkthrough:** `pwd` first (always). `cd geography-game`, `cd countries`, `ls` → there is
`virus.exe`. `rm virus.exe`. No confirmation message appears, so `ls` again to prove it is gone.

Then step two contains the trap: you are still inside `countries`, but the file must go in
`geography-game`. So `touch ../rules.txt`, then `ls ..` to verify — `geography-game` now holds five
items: `readme.md`, `countries`, `forests`, `rainforest.txt`, `rules.txt`.

### Lesson 06 — Create and delete directories

Same syntax, same path options, different commands:

```bash
mkdir cities            # make a directory
rmdir cities            # remove an EMPTY directory
rm -r family-photos     # remove a directory and everything in it
mkdir ../cities         # create a directory elsewhere using a path
```

The one critical difference:

- **`rmdir` only works if the directory is empty.**
- For a non-empty directory you need **`rm -r`**.
- Using `rmdir` on a non-empty directory **breaks nothing**. It just errors with something like
  `directory not empty`. That error is the signal to switch to `rm -r`.

(The auto-transcription renders `mkdir` as "maked"/"make dur" and `rmdir` as "rm dur"/"rmder". The
real commands are `mkdir` and `rmdir`.)

**Challenge:** the uncle is back, this time with baby photos from a 1988 family holiday. Delete the
directory `family-photos-1988`, then create a directory `cities` as a subdirectory of
`geography-game`.

**Solution walkthrough:** `cd geography-game`, `cd countries`, `ls` → `family-photos-1988` is there.
`rmdir family-photos-1988` → **error: directory not empty**. This failure is deliberate; it is the
error the slides warned about. `rm -r family-photos-1988` → succeeds silently. `ls` to confirm only
`large-countries-by-area.txt` remains. `clear` to tidy up after the error message.

Step two has the same positioning trap as before: you are inside `countries`, so
`mkdir ../cities`, then `ls ..` → `geography-game` now has six items.

### Lesson 07 — Write to files

Start with output to the terminal:

```bash
echo 'hello world'
```

> "Echo echoes or repeats what you just said, and therefore the output of echo will always be the
> same as your input."

**Mini challenge:** `echo 'Hello <your name>!'` — wrap the string in single quotes.

Then redirect that output into a file instead of the terminal:

```bash
echo 'hello world' > hello.txt      # redirection operator — OVERWRITES
echo 'welcome back' >> hello.txt    # append redirection operator — adds a line
```

- **`>`** is the **redirection operator**. It sends the output to a file instead of the terminal.
  It **overwrites all existing content** in that file.
- **`>>`** is the **append redirection operator**. It adds below what is already there.
- Both will **create the file** if it does not already exist.

The overwrite-versus-append distinction is the single most important idea in this lesson, and the
challenge is built specifically to make you feel it.

**Challenge (this is where the syllabus's Exercise 1 and Exercise 2 sit):**

1. Create a directory `about-the-game` inside `geography-game`.
2. Write the string `AB, CEO and creative genius` to a new file `team-members.txt` inside it.
3. Append a string with your own initials and the phrase `hardworking intern` to the same file.
4. Open the file in the sidebar to check — because you have not learned how to read files yet.

**Solution walkthrough:**

```bash
pwd                                  # verify position BEFORE creating anything
cd geography-game
mkdir about-the-game
ls                                   # confirm
cd about-the-game
touch team-members.txt
ls                                   # confirm
echo 'AB, CEO and creative genius' > team-members.txt
echo 'NN, hardworking intern' >> team-members.txt
```

The instructor's line about step three is the point of the whole lesson: *"we don't want to
overwrite me, the most important person in the organization, from the team members file. So we have
to use the append redirection operator."* Using `>` twice would leave only the intern in the file.

### Lesson 08 — Read from files

```bash
cat hello.txt                       # print a file's contents to the terminal
cat hello.txt > hello-copy.txt      # copy one file's contents into another
cat hello.txt >> other.txt          # append one file's contents onto another
```

**`cat`** is short for *concatenate*. The instructor admits the name is unhelpful for reading files
and offers a mnemonic involving a dog fetching the newspaper and a cat walking across the keyboard.
The mnemonic is not the lesson; the behaviour is:

- `cat <file>` prints the contents to the terminal.
- `cat` output can be **redirected just like `echo` output**. `cat a.txt > b.txt` sends the content
  straight from one file to the other and prints nothing.
- `cat` will **create the destination file** if it does not exist.
- `>` still overwrites; use `>>` to append. This rule is universal, not per-command.

**Challenge:** a file `external-people.txt` has appeared. Print its contents, then append them to
`team-members.txt`, then print `team-members.txt` to check, then delete `external-people.txt`.

**Solution walkthrough:**

```bash
cd geography-game/cities
ls
cat external-people.txt                                   # three lines of people
cat external-people.txt >> ../about-the-game/team-members.txt
cd ../about-the-game
ls
cat team-members.txt                                      # CEO + four people
rm ../cities/external-people.txt
ls ../cities                                              # empty — proof it worked
```

Note the relative path in the append step: `cities` and `about-the-game` are siblings, so the path
goes up one level and back down. And the deletion at the end is done from `about-the-game`, so it
needs `../cities/external-people.txt`. Same navigation rules as lesson 04, now applied while doing
real work.

### Section 01 recap, as the instructor gives it

- Navigate the file tree: `pwd`, `ls`, `cd`, and the `..` syntax.
- Create: `touch` (files), `mkdir` (directories).
- Delete: `rm` (files), `rmdir` (empty directories), `rm -r` (non-empty directories).
- Write: `echo`. Read: `cat`.
- Redirect and append: `>` and `>>`.

---

## Section 02 — Command Line Power Tools

**Not covered by the transcript.** The instructor's own words at the end of section one:

> "At the time of recording this scrim, section two of this course is still in the making, and I
> really hope that you will come back and continue learning about the command line when we launch it."

The intended curriculum for section two was listed in the course overview, so it is recorded here as
a topic list only — **not** as an explanation:

- copying, moving, and renaming files and directories
- performing searches and replacements in a project
- counting and organizing the contents of files

The repository's `03. Local setup` activity and its five exercises belong to this section. Treasure
refers back to it in passing at the start of section three — *"last time you learned a little bit
about setting up a local dev environment using VS Code and GitHub Desktop, VS Code for editing, and
GitHub Desktop to publish and sync your local repositories with GitHub"* — but that segment is not
in this transcript. Explain it from the actual challenge files if they are added later.

This is also why `capitals.txt` is never moved back into `geography-game`. The command that would do
it is section two material.

---

## Section 03 — Essential Git and GitHub Skills

Taught by Treasure, using **GitHub Desktop** plus **VS Code** rather than the `git` CLI.

### The concepts, before any lesson

**A branch** is "a copy or a version of your codebase." GitHub can track many at once.

**A feature branch** is the branch you create *before* starting work on a bug or a feature. Names
for it vary by company, but the idea is constant: you work "without affecting your main codebase at
all."

Why bother, if you could just edit `main` directly? On a small solo project you may not need to. But
as a team and a project grow, "more bugs may be introduced, more conflicts might arise in the code,
and there's just a whole lot more room for things to go wrong."

**A pull request** is "a collaborative feature on GitHub that gives teams a way to review each
other's changes before introducing the new code back into the main branch."

The full loop: a developer spins a feature branch off `main` → does the work → opens a pull request
→ a teammate (or several) reviews it → it is merged back into `main`.

### Lesson 02 — Make an issue in GitHub

You need something to solve before you can practise the workflow.

1. Pick a solo project you have already completed.
2. Choose a **very small** change — the lesson repeats the word *simple*. Modify a piece of text,
   change a colour, adjust a font size.
3. Go to that repo on GitHub → **Issues** tab → **New issue**.
4. Give it a descriptive **title** and a **description** explaining the change and why it is needed.

Treasure's own example: the scoreboard project, changing the header text.

**The detail that matters later:** every issue gets an **assigned number**. Hers is issue #1. You
will use that number in the branch name in the next lesson.

Issues can also be labelled and filtered, and how formal the process is "is going to depend a lot on
the process of the company that you work for."

### Lesson 03 — Creating a Branch

In GitHub Desktop: make sure you are in the right repository → **Branch** menu → **New branch**.

**Naming.** There are many conventions and they vary by workplace. The one taught here, from
Treasure's last company:

```
sb-1-modify-headers
│  │ └── short descriptive name of the work
│  └──── the issue number
└─────── abbreviated project/codebase name (sb = scoreboard)
```

The sequence for the challenge:

1. Create the branch. **GitHub Desktop switches you onto it automatically.**
2. Open the project in VS Code (there is an *Open in Visual Studio Code* button in GitHub Desktop).
3. Make the change described in your issue. Save.
4. Back in GitHub Desktop, the changes appear in the list.
5. **Commit** them. "A commit is like making a record of the changes so that we can publish or push
   to our branch." Write a commit message.
   - Check the branch name on the commit button. You are committing to the **feature branch**, not
     `main`. "We want all of our changes to be on this feature branch."
6. **Publish branch.**

The challenge deliberately stops before publishing so you make the code change first — commit, then
publish, then look at the result with **View on GitHub**. The branch menu on GitHub now shows two
branches.

You may see a **"your main branch isn't protected"** warning. Clicking it leads to branch protection
rules — things that must happen before anyone can merge into `main`. Not required now, worth looking at.

### Lesson 04 — Creating a Pull Request

> "A pull request is called a pull request because it's basically like saying, 'Hey, I'd like to
> pull my changes into your branch.'"

You can open a PR between **any two branches**; here it is feature → `main`.

From GitHub Desktop, click **Create pull request**. Then write a short description of the change and
the reason for it — similar in spirit to the issue text. The example given:

> "This PR changes the background color from white to black to enhance accessibility."

On the PR page:

- **Base branch** (`main`) and **compare branch** (your feature branch) are shown at the top. Both
  are dropdown menus; you could pick any available branches.
- **Request reviewers** — on a group project, search for GitHub users and ask them to review.
- **Files changed** tab shows the **diff**: additions highlighted in green, deletions in red. This
  is the same idea as the diff in GitHub Desktop. It is what makes reviewing someone else's PR
  practical — "you can easily see and concentrate only on the parts of the codebase that they've
  changed."
- A review can **comment**, **approve**, or **request changes** that must be made before merging.
- Then **merge**, **confirm**, and **delete the branch** — it is no longer needed.
- Finally, go back to the **Issues** tab and **close the issue**, because the work is done.
- To delete the branch locally: GitHub Desktop → branch menu → right-click the branch → delete.

### The numbering gap: lesson 05 is merge conflicts

The repository jumps from `04. Creating a Pull Request` to `06. Pulling`. The transcript fills in
what activity 05 was: **resolving merge conflicts**. There is no folder for it in the repository,
but the transcript teaches it fully, so it is explained here.

**What a merge conflict is:** "when two people try to make different changes to the same line of
code in a file." Git cannot decide which version wins, so GitHub refuses to merge the pull request.

**The worked example:**

1. You and a coworker each branch off `main`.
2. Their ticket: increase the heading size. They change the `<h3>` tags to `<h2>`.
3. Their PR is approved and merged. `main` now has `<h2>`.
4. Your ticket: change the header *text* from "Team One"/"Team Two" to "Best Team"/"Worst Team". Your
   ticket says nothing about heading levels, so you leave them as `<h3>`.
5. You commit, publish, and try to create a PR → **"Can't automatically merge."**

The two branches now differ on the same lines, and Git does not know what you want.

**Resolving it — one of several possible methods, and the simplest:**

1. **Create the pull request anyway.** You get "This branch has conflicts that must be resolved."
2. Check the **Files changed** tab to see exactly where the versions diverge.
3. Back on the **Conversation** tab, click **Resolve conflicts**.
4. GitHub opens a small editor. Between the first marker line and the middle label is the **main
   branch's** code; between the middle label and the last marker is **your branch's** code.
5. Edit it so the code looks the way it should — here, change your `<h3>`s to `<h2>`s, keeping your
   new header text, then delete the base-branch block.
6. **Mark as resolved** → **Commit merge**.
7. Merge the pull request, confirm, delete the branch.

The result keeps **both** changes: the new text *and* the larger heading.

Treasure's framing is worth keeping: "Resolving merge conflicts can get incredibly complicated. I'm
going to show you one of the quickest and easiest ways." And: "Git in general is really hard, so
you're likely going to need a lot of exposure and practice before everything starts to click, and
that's totally normal."

### Lesson 06 — Pulling

The setup for this lesson is the consequence of the previous one: the merge conflict was resolved
**in GitHub's web editor**, which changed the **remote** repo. Your **local** repo is now out of date.

- **Pushing** sends your local code up to GitHub.
- **Pulling** brings the remote code down into your local repo.

When several people push, "your remote code is constantly changing." Pulling is how your local copy
keeps up.

> "One of the ways to prevent [merge conflicts] from happening is to pull down the most up-to-date
> code from the remote before you get started on your work."

**Demonstration:** switch back to `main` in GitHub Desktop, open in VS Code — the `<h3>` tags are
still there locally, while the remote has `<h2>`. Then:

1. Click **Fetch origin**. **`origin` refers to the remote version of whatever branch you are on.**
   Fetching checks GitHub for commits on the remote `main` that your local `main` does not have.
2. GitHub Desktop reports: "the current branch has commits on GitHub that do not exist on your machine."
3. Click **Pull origin**. The changes come down.
4. Open in VS Code again — the `<h2>` tags are now present locally.

Note the two-step shape: **fetch** finds out what exists remotely; **pull** brings it in.

**Challenge:**

1. Pick a solo project repo.
2. On GitHub, click the **pencil icon** on the README to edit it in the browser. Make a simple edit.
3. Write a commit message. GitHub offers to commit directly to `main` or to open a PR — **commit
   directly to `main`** this time, to keep it simple.
4. In GitHub Desktop, **Fetch origin**, then **Pull origin**.
5. Open in VS Code and confirm the change is there locally.

---

## Beyond the syllabus: SSH and GPG keys

A short closing segment by Bob, not represented by any repository folder, but part of this module in
the transcript. Kept brief here because the segment itself is deliberately high-level.

Both SSH and GPG use **public key cryptography**. You keep a **private key** on your machine and
give GitHub the matching **public key**. The benefit is not only that data moves securely, but —
emphasised as "perhaps an even more important benefit" — that it "provides a super high level of
confidence that the data being sent is actually coming from the place that it claims to be coming
from."

Applied to GitHub:

- An **SSH key** authenticates you when pushing and pulling. The alternative is **HTTPS**, which is
  "a little less convenient because we have to provide our username and password periodically."
- A **GPG key** verifies that the **commits** you make actually came from you.

Action items from the lesson:

1. Create an SSH key on your machine and add it to your GitHub account (GitHub's own docs cover both
   halves — creating the key, then adding it).
2. Create a GPG key and add it to your GitHub account.
3. Both live under **Settings → SSH and GPG keys**, each added with its own green button.
4. When cloning, the green **Code** button lets you switch the URL from HTTPS to **SSH**. Not
   required, but more convenient and generally more secure.

A follow-on segment adds a career note: push your code to GitHub frequently, because the contribution
graph on your profile is public evidence that you have been coding consistently over time.

---

## What this module teaches

1. The terminal and a graphical file manager operate on the same file tree; only the interface differs.
2. Terminal commands usually succeed **silently** — verify with `pwd` and `ls` rather than assuming.
3. Know your position in the file tree **before** creating or deleting anything.
4. You cannot jump sideways in a file tree; you go up to a common parent and back down, and `..`
   expresses that in one command.
5. `touch`/`rm` for files, `mkdir`/`rmdir`/`rm -r` for directories — and `rmdir` failing on a
   non-empty directory is information, not a disaster.
6. `>` overwrites and `>>` appends, for `echo` and `cat` alike.
7. A branch is an isolated version of the codebase; a pull request is the review gate back into `main`.
8. An issue gives the work a number, and that number goes into the branch name.
9. Commit to the feature branch, never to `main`, while the work is in progress.
10. A diff is what makes review tractable in a large codebase.
11. Merge conflicts come from two branches editing the same lines; resolving one means deciding, by
    hand, what the final code should be.
12. `origin` means the remote; fetch discovers remote commits, pull brings them down; pulling before
    you start work prevents conflicts.

## Small practice task

**Part A — terminal only.** Rebuild a miniature of the geography game from scratch, verifying after
every single command:

```bash
mkdir geography-game
cd geography-game
mkdir countries forests
touch readme.md
echo 'Quiz game about geography' > readme.md
cat readme.md
echo 'Rule 1: no phones' > rules.txt
echo 'Rule 2: no atlases' >> rules.txt
cat rules.txt                       # must show BOTH rules
cd forests
ls ..                               # read the parent without moving
cat ../rules.txt                    # read a parent file without moving
cd ..
rmdir countries                     # empty, so this works
```

Then deliberately break it: `touch countries/x.txt`, try `rmdir countries`, read the error, and fix
it with `rm -r countries`. Provoking the error on purpose is the point.

**Part B — Git workflow.** On any finished project of yours, run the full loop once:

1. Open an issue describing one tiny change. Note its number.
2. Create a branch named `<issue-number>-<short-description>`.
3. Make the change, commit to the feature branch, publish.
4. Open a PR, read your own diff in the **Files changed** tab, merge, delete the branch, close the issue.
5. Edit the README directly on GitHub, commit to `main`, then **fetch origin** and **pull origin**
   locally and confirm the change arrived.

## Readiness check for Module 05

You are ready to continue when you can explain:

- What `pwd`, `ls`, `cd`, `clear`, `touch`, `rm`, `mkdir`, `rmdir`, `rm -r`, `echo` and `cat` do.
- Why most of them print nothing on success, and what you do about that.
- What `..`, `../name` and `../..` each mean, and why sideways movement is impossible.
- The difference between `>` and `>>`, and what happens if you use the wrong one twice.
- When `rmdir` fails and what to use instead.
- What a branch, a commit, a pull request, and a diff each are.
- Why work happens on a feature branch instead of `main`.
- What causes a merge conflict and what "resolving" one actually consists of.
- What `origin` refers to, and the difference between fetch and pull.
- Which parts of this module the transcript does **not** cover (all of Section 02 — copying, moving,
  renaming, search and replace, counting and organizing file contents, and the local setup activity).

## Exact syllabus order

1. **Command Line Fundamentals**
   1. 03. Inspect the file tree
   2. 04. Rules of navigation
   3. 05. Create & delete files
   4. 06. Create & delete directories
   5. 07. Write to files — Exercise 1, Exercise 2
   6. 08. Read from files
2. **Command Line Power Tools** *(no transcript coverage)*
   1. 03. Local setup — Exercise 1, Exercise 2, Exercise 3, Exercise 4, Exercise 5
3. **Essential Git and GitHub Skills**
   1. 02. Make an issue in GitHub
   2. 03. Creating a Branch
   3. 04. Creating a Pull Request
   4. *(05. — no repository folder; the transcript covers merge conflicts here)*
   5. 06. Pulling
