# Module 12: Databases

## Completion status

**Section 02 (Writing SQL Queries) is well covered — 24:54–26:33, one continuous course.
Section 03 (Creating and Joining Tables) is not in the transcript.**

The instructor introduces himself at the start: "My name is Greger [auto-transcribed]. I'm a
software developer and coding tutor, and this is my first course with Scrimba." The course runs
on a single running example — **Retro Rides**, a fictional US vintage-car dealership whose CEO
Rodney manages stock in a SQL database.

The boundary is stated by the instructor himself. The intro promises a full arc — "we will
finish off with an introduction to our SQL project, which you'll be able to enjoy in our
upcoming lessons on SQL" — and the closing lesson says: "Congratulations, you've reached the end
of this section. And that is also the end of the course. In the next lesson, we'll recap
everything we've learned so far." The "upcoming lessons" (more tables, joins) are not part of
this video. The intro even sketches them — "as we move through our SQL course, we will start to
add new tables, including about our staff and the locations of our different dealerships" — and
then never gets there.

One further deferred topic inside Section 02: `GROUP BY` is teased but not taught — "we've
turned a column into a single value. We'll look in a later scrim at how we can group together
[rows]" (26:06) — and no such scrim exists in this transcript. `HAVING` never appears.

## How the sources relate

The transcript course is an *introduction to databases* plus a hands-on SQL chapter; the
syllabus is the challenge-file skeleton of the SQL chapter. Section 02's lesson list matches the
transcript almost one-to-one. Section 03's folder exists in the challenge files but its lessons
were never recorded here.

### Transcript map

| Transcript time | Content | Syllabus section |
|---|---|---|
| 24:54–24:57 | What databases are; persistence; tables, types, schema | — (fundamentals) |
| 24:57–25:06 | SQL vs NoSQL; Redis, document, graph, column stores | — (fundamentals) |
| 25:06–25:21 | RDBMSes; Prisma and ORMs; managed vs self-hosted; Postgres | — (fundamentals) |
| 25:21–26:02 | SELECT, WHERE, comparisons, NOT/LIKE, AND, BETWEEN, OR, IN, challenges, ORDER BY, LIMIT | 02 |
| 26:02–26:15 | Aggregates: COUNT, SUM, aliases (AS), MAX/MIN/AVG | 02 |
| 26:15–26:29 | CRUD: INSERT INTO (auto-increment primary key), UPDATE, DELETE | 02 |
| 26:29–26:33 | Course recap | — |

---

## Fundamentals: what a database is (24:54–25:21)

### Persistence and structure (24:54)

> "Databases are used in our applications in order to store, manage and retrieve data. The
> storage is persistent and that means that between uses of an application, we can store
> information… a username and password are stored encrypted in a database and that means that
> when the user comes back to use a site again, then they can log in."

Structure: "We often store our information within tables and each piece of data will have a
different data type which can be enforced for the different columns. Every database has its own
schema which helps define the shape of the data within it. But for NoSQL databases, maybe we
have a bit of a looser schema."

### SQL vs NoSQL, and the database zoo (24:57–25:06)

- **Relational** databases organise data in related tables.
- **Key-value** stores — "a technology like Redis" — for data "we're not [using] relational
  data" with, e.g. caching.
- **Document** stores — MongoDB, with a JSON-shaped query example.
- **Graph** databases — "an example of a graph database like Neo4j."
- Also name-checked: time-series data and event logging as use cases that pull away from
  relational modelling.

### RDBMS, ORMs, hosting, Postgres (25:06–25:21)

- An RDBMS — "a relational database management system" — is the software that runs the database.
- **Prisma** is introduced as the bridge to application code: "the technology Prisma. Prisma
  queries [look] much more like calling a method in [JavaScript]… we're querying a table"
  (25:08) — an ORM, in other words, which matters later because the Next.js course (Module 19)
  uses Prisma directly at 44:48.
- **Managed vs self-hosted**: a managed database is "hosted by a cloud service" with "CPU,
  memory, and storage" somebody else manages; self-hosting means running "perhaps even a virtual
  machine or a Docker container from which we will host [it]" — trading cost against control.
- **Postgres** — "Postgres is very common across the industry and it's a really popular
  [choice]" — is the RDBMS the course will assume.

---

## Section 02 — Writing SQL Queries (25:21–26:29)

All examples run against the `cars` table: brand, model, year, price, color, condition
(numeric), `isSold` (boolean), and an auto-incrementing `id`.

### Selecting columns (25:21)

```sql
SELECT brand, model, price FROM cars;
```

- Keywords are typed "in uppercase… lowercase for things like the names of [columns]" —
  convention, not requirement.
- The dealer's boss "only wants the essentials" — selecting specific columns, not `*`.

### WHERE and numerical filtering (25:24–25:30)

```sql
SELECT * FROM cars WHERE color = 'black';
SELECT * FROM cars WHERE condition > 3;
```

Equality for strings (quotes required), comparisons for numbers. Then **not-equal**, twice —
both spellings, with the why:

> "We're going to say where the year exclamation mark equals… that just means not equal to…
> There is another symbol you might see in SQL. We can combine the less than and greater than
> signs and we will get the same result. This also means not equal to… I'm going to usually use
> exclamation mark equals."

Challenge: the customer "who is quite well-to-do and they don't want to be seen in a yellow
car" → `WHERE color != 'yellow'`.

### NOT and LIKE (25:40, 25:45)

Wildcards arrive via paint colours — "any shade of red":

```sql
SELECT * FROM cars WHERE color LIKE '%red%';
```

> "Like the string red, and we can have anything before or after red."

Exclusion combines with it — a customer who wants "a red car, but they want to avoid buying a
Ferrari": `color LIKE '%red%' AND brand != 'Ferrari'` (25:52), with the note "don't worry about
using LIKE in this case, just find exact equality" when the match is exact.

### AND, BETWEEN, OR, IN (25:41–25:55)

- **AND** — the budget customer: "they would like to spend less than $250,000" and the car must
  be driveable: two clauses joined (25:41).
- **BETWEEN** — "Between is inclusive of those lower and upper limits" — the 1980–1989 vintage
  window (25:38).
- **OR** — "either is red or is from the [1960s]" (25:44).
- **IN** — "The brand can be any of these three. It can be a Ford, Chevrolet or a Ferrari"
  (25:48), with the usual companion condition "sold must be false."

### Challenges 1 (25:54–26:00)

The section's consolidation challenge combines everything — "we have 12 cars coming back. All of
them have not been sold and the condition is less than five" — solvable with `!=` or `<`, the
student's choice, and the instructor shows both.

### ORDER BY and LIMIT (25:56–26:02)

```sql
SELECT brand, model, year, price FROM cars
ORDER BY price DESC
LIMIT 1;
```

- Sorting defaults to ascending; "`DESC`, which is short for descending," flips it.
- The worked example finds the Mercedes-Benz 300 SLR — "the most expensive car that we have in
  stock" — by ordering by price descending and limiting to one.
- The follow-up challenge inverts it: the five *least* expensive red cars — ascending order,
  `LIMIT 5`, with the LIKE condition still applied.

### Aggregates: COUNT, SUM, MAX, MIN, AVG (26:02–26:15)

```sql
SELECT COUNT(*) AS total_sold FROM cars WHERE is_sold = true;
SELECT SUM(price) AS total_earnings FROM cars WHERE is_sold = true;
```

> "Aggregations allow us to turn the values within a single column from multiple values into one
> single value."

- `COUNT` — "for every row that it finds, it's simply going to count that and add one to our
  total" → 19 sold cars.
- **Aliases** with `AS` rename the output column — `total_sold`, `total_earnings`.
- `SUM` totals a column; the challenge sums `price` where sold.
- `MAX`, `MIN`, `AVG` — "get back the average, minimum, and maximum price of all the cars."
- `GROUP BY` is explicitly deferred ("We'll look in a later scrim at how we can group
  together") and **never arrives in this video** — the same for `HAVING`.

### INSERT, UPDATE, DELETE (26:15–26:29)

The CRUD section opens with the definition — "read, update, delete. These are the four main
operations for manipulating data" — then does the three writes:

- **INSERT INTO** (26:20): "with our keywords insert into" — listing columns and values, and
  *not* the `id`, because "that ID is our primary key and the primary key is auto-incremented."
  The new car "is blue and is in pretty good condition."
- **UPDATE** (26:22): "how we can update existing records… to update details of the cars that
  we" already stock — when the RS2000 sells: `UPDATE cars SET is_sold = true WHERE …`. The
  lesson is careful that an UPDATE without a WHERE hits every row.
- **DELETE** (26:26–26:29): first with a condition (`condition = 0` removes one decrepit Ford
  Mustang), then the year-end cleanup — "write a delete statement where you delete any record
  from the database where the sold value is true… we're ready to enter the new financial year
  with a nice fresh database." Same warning applies: the WHERE clause is the safety catch.

### The recap (26:29–26:33)

> "We selected data from our table. We were using the select and from keywords… we then learned
> about writing conditions using the where clause in order to filter rows… we started looking at
> equality and comparison."

And the send-off: "Rodney has written you a splendid letter of recommendation for all your hard
work maintaining the database at Retro Rides."

## Section 03 — Creating and Joining Tables *(absent)*

Zero transcript coverage — verified: "join", "left join", "foreign key", "drop table",
"create table" and "alter" return no matches inside the database segment. What this section
would teach, and where its ideas *do* appear elsewhere in the path:

- **Creating tables** (`CREATE TABLE`, column types, constraints) — never written in the
  transcript. The closest exposure is Module 13's syllabus itself (`users` table, `cart_table`,
  `seedTable.js`) — which is also uncovered (see Module 13's README).
- **Populating and altering** — `INSERT INTO` is taught (26:20) for rows, but `ALTER TABLE`
  never appears.
- **Joins** (left/right/full/inner, joining multiple tables, aggregates over joins) — never
  taught. The one conceptual hook the transcript provides is the fundamentals talk about
  *related* tables (24:57) and the promised-but-missing `staff` and `locations` tables (24:56).
- **Primary keys** — taught only in passing, as the auto-incrementing `id` you don't insert
  (26:20).

## Mapping to the syllabus activities

- **Section 01 does not exist** in the challenge files (numbering starts at 02) — the
  fundamentals content at 24:54–25:21 maps to nothing in the folder list, but it is genuine
  transcript content worth reading first.
- **02.13 "Challenges 1"** — covered at 25:54–26:00.
- **02.18 GROUP BY, 02.19 HAVING, 02.20 "Challenges 2"** — **not covered** (GROUP BY deferred
  at 26:06 and never returned to).
- **03.x (all 10 lessons)** — **not covered.**
- Transcript-only extras: the database-types tour (Redis, MongoDB, Neo4j, time-series), the
  ORM/Prisma aside, managed-vs-self-hosted hosting, and the Postgres recommendation.

## What this module teaches (from the parts that exist)

1. What a database is: persistent, structured storage with a schema.
2. The relational model and its alternatives (key-value, document, graph), with named examples.
3. RDBMS, Postgres, ORMs (Prisma), and managed vs self-hosted trade-offs.
4. `SELECT` / `FROM`, choosing columns, and keyword casing convention.
5. `WHERE` with equality, string quoting, numeric comparison, `!=`/`<>`, `NOT`.
6. `LIKE` with `%` wildcards for substring matching.
7. Combining conditions with `AND`, `OR`, `IN`, and range windows with `BETWEEN` (inclusive).
8. `ORDER BY` (asc/desc) and `LIMIT`.
9. Aggregates `COUNT`, `SUM`, `MAX`, `MIN`, `AVG`, and output aliases with `AS`.
10. Writes: `INSERT INTO` (letting the auto-increment key do its job), `UPDATE … WHERE`,
    `DELETE … WHERE` — and why the WHERE clause matters.

## Small practice task

Run the Retro Rides drills against a table of your own — say, a `books` table (title, author,
year, pages, price, genre, is_sold):

1. Select only `title` and `price` (the essentials).
2. Filter: exact genre match; pages greater than 300; everything *except* one author
   (both `!=` and `<>`); any title containing the word "night" (LIKE with wildcards).
3. Combine: `AND` (cheap and long), `OR` (two genres), `IN` (three authors), `BETWEEN`
   (publication years 1990–1999, inclusive — verify the inclusivity claim).
4. Order by price descending and limit to 1 (the most expensive); then the five cheapest of one
   genre, ascending.
5. Aggregate: `COUNT` of unsold with an alias, `SUM` of prices of sold books, and
   `AVG`/`MIN`/`MAX` of pages.
6. Write: insert a book without an id; mark one book sold; delete every sold book — and *say
   out loud* what each statement would do without its WHERE clause before running it.
7. The part the transcript can't teach: write a `GROUP BY genre` with a `COUNT(*)` and get one
   row per genre — then note that you've exceeded the video course, because that is exactly
   where it stopped.

## Readiness check for Module 13

Module 13 (Express) is a verified gap in this transcript — see its README. Before moving on, be
able to:

- Explain persistence and what a schema enforces.
- Write a filtered, sorted, limited SELECT from memory.
- Explain the difference between `WHERE` and `ORDER BY`/`LIMIT`, and where each goes.
- Say what `COUNT(*)` counts when a WHERE clause is present.
- Explain why an INSERT omits the primary key, and what an UPDATE or DELETE does without WHERE.

Carry forward honestly: **multi-table design and joins are gaps** — Module 13's authentication
and cart sections would have been the place they were used.

## Exact syllabus order

1. **Writing SQL Queries**
   1. 04. Selecting columns
   2. 05. WHERE clause
   3. 06. Numerical filtering
   4. 07. Not equal — Exercises 1–2
   5. 08. NOT and LIKE
   6. 09. AND — Exercises 1–2
   7. 10. BETWEEN — Exercises 1–2
   8. 11. OR — Exercises 1–2
   9. 12. IN operator — Exercises 1–2
   10. 13. Challenges 1 — Exercises 1–3
   11. 14. ORDER BY — Exercises 1–2
   12. 15. LIMIT
   13. 16. COUNT and SUM
   14. 17. MAX, MIN, AVG — Exercises 1–2
   15. 18. GROUP BY — Exercises 1–2 *(deferred at 26:06, never taught)*
   16. 19. HAVING *(not covered)*
   17. 20. Challenges 2 — Exercises 1–2 *(not covered)*
   18. 21. INSERT INTO
   19. 22. UPDATE — Exercises 1–2
   20. 23. DELETE — Exercises 1–2
2. **Creating and Joining Tables** *(no transcript coverage)*
   1. 03. Creating tables — Exercises 1–2
   2. 04. Populating tables — Exercises 1–2
   3. 05. Alter table — Exercises 1–3
   4. 07. Left and Right Join — Exercises 1–2
   5. 08. Full join, inner join and drop — Exercises 1–3
   6. 09. Aggregates — Exercises 1–3
   7. 10. Joining multiple tables — Exercises 1–2
