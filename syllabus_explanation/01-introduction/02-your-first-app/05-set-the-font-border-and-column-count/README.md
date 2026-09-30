# Lesson 05: Set the Font, Border, and Column Count (Hinglish Explanation)

**Path:** MODULE 01. Introduction → SECTION 02. Your First App → LESSON 05. Set the Font, Border, and Column Count

---

## Transcript mein kya fit hota hai (honest mapping)

Ye "Your First App" ka aakhri polish step hai — teen styling properties: **font**, **border**,
**column count**. Transcript mein in teeno ke detailed lessons baad ke builds mein aate hain,
jo is activity ka best context hain:

| Property | Transcript time | Kya sikhaya |
|---|---|---|
| `font-family` | `03:08:14 – 03:08:51` | Body target karke font set karna, aur **font stack** (comma-separated fallbacks) |
| `border` | `01:46:10 – 01:47:13` | `border: 2px solid red` — teen values, aur border page layout mein kahan baithta hai |
| Columns | `02:40:13+` | Do-column layout banane ka concept (transcript mein `column-count` property seedha nahi aati — honest note neeche) |

---

## Pehle samjho: ye teeno properties kyun?

Page par ab naam, emoji, photos, background, colors — sab hai. Ab final polish:

1. **Font** — text ki personality (simple vs elegant vs playful)
2. **Border** — elements ko frame/definition dena
3. **Columns** — content ko side-by-side arrange karna (taki sab kuch sirf upar-neeche na ho)

---

## Step 1: Font set karna — `font-family` (transcript `03:08:14`)

Instructor ke steps bilkul clear hain:

### a) `body` ko target karo

Font poore page par chahiye, isliye `body` selector:

```css
body {
    font-family: Verdana;
}
```

### b) VS Code ka magic — suggestions

Instructor dikhate hain: jaise hi `font-family` ke baad `V` type karte ho, **VS Code** (jo
Scrimba ke editor ko power karta hai) suggestions nikal deta hai. Sirf `Verdana` hi nahi — uske
saath **aur bhi fonts, sab comma se separated**, automatically aa jaate hain.

### c) Font stack — ye kya hai?

Enter dabate hi jo banta hai use **font stack** kehte hain:

```css
body {
    font-family: Verdana, Geneva, Tahoma, sans-serif;
}
```

Matlab (instructor ke hisaab se):
- Browser pehle **Verdana** dhundhega user ke system par
- Na mile to agla font try karega, phir agla...
- Last mein `sans-serif` — "koi bhi sans-serif font chala do" wala generic fallback

**Kyu?** Kyunki tumhare computer par jo font hai, wo dusre ke computer par ho — zaroori nahi.
Fallbacks rakhte hain taaki page kahin bhi sahi dikhe.

---

## Step 2: Border lagana — `border` (transcript `01:46:10`)

Instructor ek example par `border` property dete hain. Syntax mein **teen values**:

```css
h1 {
    border: 2px solid red;
}
```

1. **`2px`** — thickness (kitni moti line)
2. **`solid`** — style/shape (solid, dashed, dotted...)
3. **`red`** — color (name, ya `#fff` jaisa hex — dono chalte hain)

Instructor experiment karte hain:
- `2px` → `8px`: border noticeably **moti** ho jaati hai
- `solid` ki jagah doosra style: alag (aur kaafi weird 😄) lagta hai
- `red` ki jagah `fff` (hex) ya `white` ya `blue`: color badal jaata hai

Aur ek important positioning detail: **border, padding ke BAHAAR aur margin ke ANDAR** hoti hai
(content → padding → border → margin — ise "box model" kehte hain, Module 02/06 mein detail
se aayega).

Instructor ka rule: *"kai tarah ki borders hain, lekin **99.9% cases mein tum `solid` hi use
karoge**."*

---

## Step 3: Columns — content ko side-by-side karna

"Your First App" activity mein `column-count` jaisi setting se gallery jaisa layout banta hai.
Honest note: transcript mein `column-count` property **seedha nahi padhai gayi** — uski jagah
course multi-column layouts ke liye aage chalkar **flexbox** sikhata hai (transcript
`02:40:13` se), jahan "two columns, one for the image and one [for the text]" banaye jaate hain:

```css
.container {
    display: flex;   /* children side-by-side columns ban jaate hain */
}
```

Abhi ke liye concept ye samjho:

- **Single column (default):** saare elements upar se neeche stack hote hain — kyunki `p`,
  `h1` jaise block elements poori width le lete hain
- **Multiple columns:** content text-newspaper style ya image-gallery style mein do (ya zyada)
  vertical columns mein baat do
- Simple text-column ke liye CSS mein milta hai:

```css
.gallery {
    column-count: 2;   /* content do columns mein baant do */
}
```

- Asli layout control (kya left, kya right, kitni width) flexbox/grid se hota hai — wo Module 02
  (Business Card, Birthday site) mein detail se aayega.

---

## "Your First App" ka final look

Sab polish ek saath:

```css
body {
    background-image: url("meri-background.jpg");
    background-size: cover;
    font-family: Verdana, Geneva, Tahoma, sans-serif;
    color: white;
}

h1 {
    border: 2px solid white;   /* heading ko frame kar do */
}

.gallery {
    column-count: 2;           /* photos/notes do columns mein */
}
```

Ab page sirf text nahi — ek **personalized mini app** lagti hai. 🎉

---

## Common mistakes

1. **Font naam mein space ho to quotes do** — `font-family: "Times New Roman", serif;` (bina
   quotes ke multi-word font names unreliable hain).
2. **Font stack ke end mein generic fallback na bhoolo** — `sans-serif`/`serif` last mein
   rakho, warna kisi ke system par default ugly font aa sakta hai.
3. **Border ke teeno parts ka order** — CSS mein order flexible hai, lekin teeno (width, style,
   color) dena zaroori hai; sirf `border: red` se kaam nahi chalega (style missing hai).
4. **Columns mein images phool jaana** — column layout mein `img` apni natural size leti hai;
   `width: 100%` yaad rakhna (pichla `Display Photos` hack!).
5. **Sab kuch ek saath badalna** — instructor har jagah yahi loop dikhate hain: ek change karo,
  preview karo, phir agla. Polish ke time sabse zyada galtiyan yahi hoti hain.

---

## Khud se karo (practice)

1. Apne page par 2 alag fonts try karo (ek serif, ek sans-serif) — dono baar full font stack ke
   saath. Feel karo ki font badalne se page ka mood kaise badalta hai.
2. `h1` par `2px solid`, phir `8px dashed` border lagao — difference dekho.
3. Apni photos ko ek `div` mein daal kar 2-column layout do — phir 3 columns try karo.

---

## Module 01 complete! 🎓

Ye "Your First App" ka aakhri lesson tha. Is module mein tumne seekha:

- ✅ Platform workflow: edit → run → preview → challenge
- ✅ HTML structure: `h1/h2/p` tags, opening/closing ke rules
- ✅ Images: `<img src>`, local + online, `width="100%"` hack
- ✅ CSS basics: `background-image`, `background-size`, `color`, `font-family`, `border`
- ✅ Sabse important: **khud type karke seekhne** ki aadat

## Agla module ke liye ready?

Ab **MODULE 02: HTML and CSS Fundamentals** shuru hoga — wahan hum HTML ko properly, aadhar se
seekhenge: pehla lesson **"HTML tags"** (`02-html-and-css-fundamentals/01-intro-to-html/01-html-tags`).
Wahan transcript ka "I code, therefore I am" wala hissa native lesson ke roop mein aayega.
🚀
