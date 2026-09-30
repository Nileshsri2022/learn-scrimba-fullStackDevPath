# Module 12: Databases

## Completion status

**Section 02 is complete. Section 03 is announced on tape but never delivered.**

- **Section 02 — Writing SQL Queries:** **fully covered**, roughly **25:22 to 26:35**. Every listed
  lesson (SELECT through DELETE) has transcript material and is explained below.
- **Section 03 — Creating and Joining Tables:** **absent from the transcript.** In the project intro
  the teacher *promises* it — "we're going to add tables in some of our later lessons which store
  information about our employees... as well as our dealerships... we're going to learn about creating
  tables using our data definition language" — but the course's closing recap only reviews Section 02
  and says "that is also the end of the course." Verification: `create table`, `left join`,
  `right join`, `inner join`, `foreign key` and `drop table` each return **0 matches** in the
  47-hour transcript. So `CREATE TABLE`, `ALTER TABLE`, and all the JOIN lessons are a **gap**. They
  are still listed at the end of this file for syllabus fidelity, and summarised (not transcribed) in
  the gap section.

The teacher is **Greger** ("My name is Greger... this is my first course with Scrimba"). This is his
only module.

---

## Before the SQL: the introduction (context, not in the numbered syllabus)

The syllabus for Module 12 starts at Section 02, but the transcript opens with a conceptual intro
worth capturing because the rest builds on it.

### What a database is

> "Databases are used in our applications in order to store, manage and retrieve data. The storage is
> **persistent**" — data survives between uses of the app (e.g. an encrypted username and password
> so a returning user can log in).

### SQL vs NoSQL

**SQL** = **Structured Query Language**. Data lives in **tables** defined by a **schema**: columns
(each with a fixed **data type**) and rows (individual records). Relationships between tables are
shown in an **entity-relationship diagram**. The schema is rigid and predefined; scaling is
**vertical** ("scale up" — add CPU/memory/storage).

**NoSQL** is looser and more flexible. Four families the transcript names:

| Type | Example | Stores data as | Typical use |
|---|---|---|---|
| Document store | MongoDB | JSON-like documents | content management system |
| Key-value store | Redis | key → value pairs | APIs without relational data |
| Column-family store | Apache Cassandra | columns grouped into families | time-series / logging / event tracking |
| Graph database | Neo4j | nodes (entities) + edges (relationships) | social networks |

NoSQL can be schemaless / dynamic-schema and scales **horizontally** ("scale out" — add servers).
Rule of thumb: **SQL** for structured data and complex relationships where consistency matters;
**NoSQL** for large-scale, unstructured/semi-structured data and flexibility.

### Application architecture and how code reaches the database

The classic three parts: **front end** (browser) ↔ **back end** (server + API) ↔ **database**. The
point of contact with the database is usually an **RDBMS** (relational database management system)
such as **Postgres**.

Two ways to talk to it:

1. **Write SQL directly** — full control, best for complex apps.
2. **Use an ORM** (Object-Relational Mapping) — you write queries in JavaScript/Python and the ORM
   translates to SQL, returning objects. Good for developers who want to avoid raw SQL or for simpler
   apps. Example given: **Prisma**, whose queries "look much more like calling a method in
   JavaScript":

   ```js
   const user = await prisma.user.findFirst({
     select: { email: true, name: true }
   })
   ```

### Managed vs self-hosted

| | Managed (cloud, third-party) | Self-hosted (own infrastructure) |
|---|---|---|
| Setup | quick, simple | you provision a server / VM / Docker container |
| Security | outsourced to the provider | fully your responsibility (custom layers possible) |
| Cost | cheap when small, expensive at scale | cheaper at scale, more overhead when small |
| Control | limited | full customization |

### The project

**Retro Rides** — a car dealership selling 20th-century vintage cars, owned by **Rodney**. It runs a
small Node app using the **PGlite** library (an in-browser implementation of Postgres) so the focus
stays on SQL. Queries are written in `.sql` files and the output is printed to the console; it's not
a full app — "we're going to be looking a little bit behind the scenes."

The main table is **`cars`**, with columns including `id` (auto-incremented **primary key**),
`brand`, `model`, `year`, `color`, `condition` (0 = worst, 5 = best), `price`, and a boolean `sold`.

---

## Section 02 — Writing SQL Queries

> **Casing convention:** SQL keywords in UPPERCASE (`SELECT`, `FROM`, `WHERE`), column/table names
> in lowercase. "This isn't strictly necessary... it won't matter if you use all caps or all
> lowercase" — it's a readability convention. Statements end with a semicolon.

### Lesson 04 — Selecting columns

```sql
SELECT brand, model, condition, price
FROM cars;
```

`SELECT` names the columns you want; `FROM` names the table. The result is filtered to just those
columns.

### Lesson 05 — WHERE clause

Filter rows with `WHERE`:

```sql
SELECT brand, model, color, price
FROM cars
WHERE color = 'black';
```

Strings go in quotes. "SQL doesn't worry too much about the spacing" — indent freely for readability.

### Lesson 06 — Numerical filtering

Use `<`, `>`, `<=`, `>=`:

```sql
SELECT brand, model, condition, price
FROM cars
WHERE condition > 3;        -- or >= 3 to include 3
```

### Lesson 07 — Not equal

Two symbols mean the same thing — `!=` and `<>`:

```sql
WHERE year != 1965          -- same as WHERE year <> 1965
```

### Lesson 08 — NOT and LIKE (partial matching)

Wildcards let you match partial strings:

| Wildcard | Matches |
|---|---|
| `%` | any number of any characters (including zero) |
| `_` | exactly one character (any) |

```sql
WHERE color LIKE '%green%'    -- light green, greenish yellow, dark green, green
WHERE color NOT LIKE '%green%'  -- anything that isn't a shade of green
WHERE model LIKE 'DB_'        -- DB4, DB5, DB6... any single char after DB
```

### Lesson 09 — AND

Chain multiple conditions that must **all** be true:

```sql
SELECT brand, model, color, year
FROM cars
WHERE color NOT LIKE '%green%'
  AND model LIKE 'DB_'
  AND year > 1964;
```

### Lesson 10 — BETWEEN

`BETWEEN` replaces two comparisons and is **inclusive** of both limits:

```sql
WHERE year BETWEEN 1980 AND 1989    -- same as year >= 1980 AND year <= 1989
```

### Lesson 11 — OR (and the bracket trap)

`OR` matches when **at least one** condition is true:

```sql
WHERE price < 250000 OR brand = 'Porsche'
```

**Critical gotcha:** mixing `OR` and `AND` without brackets changes the meaning. SQL binds `AND`
tighter, so this reads as "price < 250000 **OR** (Porsche AND condition > 3)":

```sql
WHERE price < 250000 OR brand = 'Porsche' AND condition > 3   -- probably NOT what you want
```

Wrap the `OR` in brackets to force "(either price or Porsche) **and** condition > 3":

```sql
WHERE (price < 250000 OR brand = 'Porsche') AND condition > 3
```

> **`=` vs `IS`:** use `=` for strings and numbers; use `IS` for **boolean and null** values
> (`WHERE sold IS false`). They usually agree, but `IS` avoids "tricky edge cases with boolean
> values."

### Lesson 12 — IN operator

Match any value in a set without writing several `OR`s:

```sql
WHERE brand IN ('Ford', 'Chevrolet', 'Ferrari')
WHERE brand NOT IN ('Ford', 'Chevrolet', 'Dodge')   -- exclude a set
```

### Lesson 13 — Challenges 1

The in-scrim challenges combine everything so far — e.g. "a red car OR from the 1960s, and not
already sold," which needs bracketed `OR` plus `AND sold IS false`.

### Lesson 14 — ORDER BY

Sort the output. Default is ascending (A→Z for strings, low→high for numbers); `DESC` reverses it.
List several columns to break ties:

```sql
SELECT brand, model, condition, price
FROM cars
WHERE sold IS false
ORDER BY condition DESC, price ASC;   -- ASC is the default, optional
```

`WHERE` goes **after** `FROM` and **before** `ORDER BY`.

### Lesson 15 — LIMIT

Cap the number of rows returned; combine with `ORDER BY` to get "the top N":

```sql
SELECT brand, model, year, price
FROM cars
ORDER BY price DESC
LIMIT 1;              -- the single most expensive car
```

### Lesson 16 — COUNT and SUM

**Aggregates** reduce a whole column to one value. Use `AS` to alias the output column:

```sql
SELECT COUNT(*) AS total_sold FROM cars WHERE sold IS true;      -- 19
SELECT SUM(price) AS total_earnings FROM cars WHERE sold IS true;
```

### Lesson 17 — MAX, MIN, AVG

```sql
SELECT MAX(price) AS most_expensive FROM cars WHERE sold IS true;
SELECT AVG(price) FROM cars WHERE brand = 'Bentley';
```

Aggregating reduces a column to a single value, so **you can't select other plain columns alongside
an aggregate** (that needs `GROUP BY`). Tidy up long decimals with `FLOOR` (round down) or `CEIL`
(round up), wrapping the aggregate:

```sql
SELECT FLOOR(AVG(price)) AS average,
       MIN(price),
       MAX(price)
FROM cars
WHERE sold IS true;
```

### Lesson 18 — GROUP BY

Aggregate **per group** instead of over the whole table — and now you *can* select the grouping
column:

```sql
SELECT brand, COUNT(brand) AS count
FROM cars
GROUP BY brand;              -- one count per brand

SELECT brand, COUNT(brand) AS count, FLOOR(AVG(price)) AS avg
FROM cars
WHERE sold IS false
GROUP BY brand;             -- WHERE filters rows before grouping
```

### Lesson 19 — HAVING

`WHERE` can't test an aggregate (it throws an error). `HAVING` filters **after** grouping:

```sql
SELECT year, COUNT(year) AS car_count, MAX(price), MIN(price)
FROM cars
WHERE sold IS true
GROUP BY year
HAVING COUNT(year) > 1       -- only years with more than one sale
ORDER BY car_count;
```

Note the full clause order: `SELECT … FROM … WHERE … GROUP BY … HAVING … ORDER BY … LIMIT`.

### Lesson 20 — Challenges 2

More combined drills (oldest 5 unsold cars with `ORDER BY year LIMIT 5`; most common colours with
`GROUP BY color`, `HAVING COUNT > 2`, `ORDER BY count DESC`).

### The CRUD framing (Lessons 21–23)

SQL's data-manipulation commands map to **CRUD** — Create, Read, Update, Delete. You've already been
doing **Read** with `SELECT`. These commands don't return a result set, so the project runs a
follow-up `SELECT` behind the scenes to visualise the change.

### Lesson 21 — INSERT INTO

Add rows. Supply a value for every column except the auto-incremented `id` (avoids nulls that can
cause errors):

```sql
INSERT INTO cars (brand, model, year, color, condition, price, sold)
VALUES ('Ford', 'Escort RS2000', 1977, 'blue', 4, 30000, false);
```

### Lesson 22 — UPDATE

Modify existing rows. **Always include a `WHERE`** or you update every row:

```sql
UPDATE cars
SET condition = 1, price = 10000
WHERE sold IS false;
```

### Lesson 23 — DELETE

Remove rows — again, mind the `WHERE`:

```sql
DELETE FROM cars WHERE condition = 0;   -- scrap the write-offs
DELETE FROM cars WHERE sold IS true;    -- year-end cleanup
```

---

## Section 03 — Creating and Joining Tables (GAP)

**None of this section is in the transcript.** The intro promises staff/dealerships/sold-cars tables
and joins, and the syllabus lists CREATE, populate, ALTER, LEFT/RIGHT/FULL/INNER JOIN, aggregates
across joins, and multi-table joins — but the recorded course ends after DELETE and the recap never
mentions them. For orientation only (this is **not** from the transcript), the standard forms are:

- **`CREATE TABLE`** — define a table, its columns, types, and keys (Data Definition Language).
- **`ALTER TABLE`** — add/modify/drop columns after creation.
- **JOINs** — combine rows across tables on a related column:
  - `INNER JOIN` — only rows matching in both tables.
  - `LEFT JOIN` / `RIGHT JOIN` — all rows from one side plus matches from the other.
  - `FULL JOIN` — all rows from both sides.
- **Foreign keys** — a column referencing another table's primary key, which the joins rely on.

If you need these, follow an external Postgres/SQL tutorial; they cannot be sourced from this course.

---

## Mapping to the syllabus activities

| Syllabus activity | Coverage |
|---|---|
| 02.04 Selecting columns | Covered — `SELECT … FROM` |
| 02.05 WHERE clause | Covered |
| 02.06 Numerical filtering | Covered — `<`, `>`, `<=`, `>=` |
| 02.07 Not equal | Covered — `!=`, `<>` |
| 02.08 NOT and LIKE | Covered — `%`, `_`, `NOT LIKE` |
| 02.09 AND | Covered |
| 02.10 BETWEEN | Covered (inclusive) |
| 02.11 OR | Covered — incl. bracket precedence, `IS` vs `=` |
| 02.12 IN operator | Covered — `IN`, `NOT IN` |
| 02.13 Challenges 1 | Covered (combined drills) |
| 02.14 ORDER BY | Covered — `ASC`/`DESC`, multi-column |
| 02.15 LIMIT | Covered |
| 02.16 COUNT and SUM | Covered — aggregates, `AS` aliases |
| 02.17 MAX, MIN, AVG | Covered — plus `FLOOR`/`CEIL` |
| 02.18 GROUP BY | Covered |
| 02.19 HAVING | Covered |
| 02.20 Challenges 2 | Covered |
| 02.21 INSERT INTO | Covered |
| 02.22 UPDATE | Covered |
| 02.23 DELETE | Covered |
| 03.03 Creating tables | **GAP** — not in transcript |
| 03.04 Populating tables | **GAP** |
| 03.05 Alter table | **GAP** |
| 03.07 Left and Right Join | **GAP** |
| 03.08 Full join, inner join and drop | **GAP** |
| 03.09 Aggregates (joined) | **GAP** |
| 03.10 Joining multiple tables | **GAP** |

The `PRACTICE: Exercise` items throughout Section 02 are the in-scrim customer-scenario challenges
(black car; condition 0 wrecks; cars under $50k; avoid 1965; Aston Martin `DB_`; 80s cars with
`BETWEEN`; budget-or-Porsche with brackets; odd 1960s years with `IN`; etc.), all described inline.

## What this module teaches

- What databases are and why persistence matters; SQL vs NoSQL and the main NoSQL families.
- How apps reach a database (RDBMS, ORMs like Prisma) and managed vs self-hosted trade-offs.
- Reading data: `SELECT`/`FROM`, `WHERE`, comparison and `LIKE` wildcards.
- Combining conditions with `AND`/`OR`/`IN`/`BETWEEN` and the bracket-precedence trap.
- Shaping output with `ORDER BY` and `LIMIT`.
- Aggregating with `COUNT`/`SUM`/`MAX`/`MIN`/`AVG`, `GROUP BY`, and `HAVING`.
- Changing data with `INSERT`, `UPDATE`, `DELETE` (the CRUD commands) — and always scoping
  updates/deletes with `WHERE`.

## Practice task

Against a `cars` table (brand, model, year, color, condition 0–5, price, boolean sold):

1. List the brand, model and price of unsold red cars under $80,000, cheapest first.
2. Show each brand with its car count and average price, only for brands with more than two cars.
3. Find the single oldest unsold car (`ORDER BY` + `LIMIT`).
4. Mark every car in condition 0 as sold and drop its price to $5,000 in **one** `UPDATE`.
5. Delete all cars where `sold IS true`.

Check the bracket-precedence rule on any query that mixes `AND` with `OR`.

## Readiness check for the next module

Before moving on you should be able to:

- write a `SELECT … WHERE … ORDER BY … LIMIT` query from a plain-English request;
- combine `AND`/`OR` correctly with brackets and know when to use `IS` vs `=`;
- aggregate with `GROUP BY`/`HAVING` and alias columns with `AS`;
- `INSERT`, `UPDATE`, and `DELETE` safely with a `WHERE` clause.

This SQL is what **Module 13 (Express.js)** uses when its full-stack app seeds tables, queries
products, and stores users and carts — Express supplies the routes, SQL supplies the data.

---

## Ordered syllabus

MODULE 12. Databases
========================================================================
Learning focus: Relational database concepts, SQL queries, table design, and joins.
  SECTION / UNIT: 02. Writing SQL Queries
    LESSON / ACTIVITY: 04. Selecting columns
    LESSON / ACTIVITY: 05. WHERE clause
    LESSON / ACTIVITY: 06. Numerical filtering
    LESSON / ACTIVITY: 07. Not equal
      PRACTICE: Exercise 1
      PRACTICE: Exercise 2
    LESSON / ACTIVITY: 08. NOT and LIKE
    LESSON / ACTIVITY: 09. AND
      PRACTICE: Exercise 1
      PRACTICE: Exercise 2
    LESSON / ACTIVITY: 10. BETWEEN
      PRACTICE: Exercise 1
      PRACTICE: Exercise 2
    LESSON / ACTIVITY: 11. OR
      PRACTICE: Exercise 1
      PRACTICE: Exercise 2
    LESSON / ACTIVITY: 12. IN operator
      PRACTICE: Exercise 1
      PRACTICE: Exercise 2
    LESSON / ACTIVITY: 13. Challenges 1
      PRACTICE: Exercise 1
      PRACTICE: Exercise 2
      PRACTICE: Exercise 3
    LESSON / ACTIVITY: 14. ORDER BY
      PRACTICE: Exercise 1
      PRACTICE: Exercise 2
    LESSON / ACTIVITY: 15. LIMIT
    LESSON / ACTIVITY: 16. COUNT and SUM
    LESSON / ACTIVITY: 17. MAX, MIN, AVG
      PRACTICE: Exercise 1
      PRACTICE: Exercise 2
    LESSON / ACTIVITY: 18. GROUP BY
      PRACTICE: Exercise 1
      PRACTICE: Exercise 2
    LESSON / ACTIVITY: 19. HAVING
    LESSON / ACTIVITY: 20. Challenges 2
      PRACTICE: Exercise 1
      PRACTICE: Exercise 2
    LESSON / ACTIVITY: 21. INSERT INTO
    LESSON / ACTIVITY: 22. UPDATE
      PRACTICE: Exercise 1
      PRACTICE: Exercise 2
    LESSON / ACTIVITY: 23. DELETE
      PRACTICE: Exercise 1
      PRACTICE: Exercise 2
  SECTION / UNIT: 03. Creating and Joining Tables
    LESSON / ACTIVITY: 03. Creating tables
      PRACTICE: Exercise 1
      PRACTICE: Exercise 2
    LESSON / ACTIVITY: 04. Populating tables
      PRACTICE: Exercise 1
      PRACTICE: Exercise 2
    LESSON / ACTIVITY: 05. Alter table
      PRACTICE: Exercise 1
      PRACTICE: Exercise 2
      PRACTICE: Exercise 3
    LESSON / ACTIVITY: 07. Left and Right Join
      PRACTICE: Exercise 1
      PRACTICE: Exercise 2
    LESSON / ACTIVITY: 08. Full join, inner join and drop
      PRACTICE: Exercise 1
      PRACTICE: Exercise 2
      PRACTICE: Exercise 3
    LESSON / ACTIVITY: 09. Aggregates
      PRACTICE: Exercise 1
      PRACTICE: Exercise 2
      PRACTICE: Exercise 3
    LESSON / ACTIVITY: 10. Joining multiple tables
      PRACTICE: Exercise 1
      PRACTICE: Exercise 2

========================================================================
