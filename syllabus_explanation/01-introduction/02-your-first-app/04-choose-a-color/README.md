# Lesson 04: Choose a Color (Hinglish Explanation)

**Path:** MODULE 01. Introduction → SECTION 02. Your First App → LESSON 04. Choose a Color

---

## Transcript mein kya fit hota hai (honest mapping)

Colors choose karne ke liye transcript mein **teen anchors** milte hain — teeno mil kar is
lesson ka complete context banate hain:

| Transcript time | Kya hai |
|---|---|
| `01:05:01 – 01:06:52` | Pehli CSS: `body` selector aur uske andar ke **values badal kar** cookie widget redesign karna (color properties ka pehla use) |
| `01:11:32 – 01:12:18` | **Hex codes** ka sneak peek — `#` wala code = red/green/blue ki recipe |
| `00:27:49 – 00:28:00` | `type="color"` input — browser ka built-in **color picker** |

---

## Ye lesson kya sikhaata hai

"Your First App" mein ab apne page ke liye **colors choose** karna hai — text ka color,
background ka color. Lagta hai chhota kaam, lekin yahan 3 practical cheezein seekhni hain:

1. CSS mein color **kaise likhte** hain (named colors, hex codes)
2. Color **dhundhte kaise** hain (color picker tools)
3. Kaunsa color **kaam karega** kaise decide karein (readability/contrast)

---

## Step-by-step

### Step 1: Color property = kaunsa color, kabhi bhi value badal sakte ho

Transcript mein pehli baar colors tab aate hain jab instructor CSS introduce karte hain
(`01:05:01`). `body` selector ke andar kuch properties pehle se likhi hoti hain, aur tumhara
challenge hota hai: **values badal-badal kar experiment karo** — cookie widget ko apne hisaab se
redesign karo.

Color set karne ka basic syntax:

```css
body {
    background-color: saddlebrown;
    color: white;
}
```

- `background-color` → element ke piche ka color (pichle lesson ki tarah, lekin ye image nahi,
  solid color hai)
- `color` → us element ke **text** ka color (yaad karo: background image wale lesson mein
  `color: white` se invisible heading fix ki thi!)
- Value ke roop mein English **color names** likh sakte ho: `white`, `black`, `red`,
  `saddlebrown`, `tomato`, `rebeccapurple`... (CSS mein 140+ named colors hain)

### Step 2: Sneak peek — hex codes (`01:11:32`)

Challenge ke baad instructor ek **sneak peek** dete hain — colors likhne ka doosra tareeka,
**hex codes**:

```css
body {
    background-color: #8B4513;   /* saddlebrown ka hex code */
}
```

Instructor ke points bilkul saaf hain:

- Ye **hashtag (`#`) se shuru** hone wala ajeeb-sa code hota hai
- Ye actually ek **recipe** hai — batata hai ki us color mein kitna **red**, kitna **green**,
  kitna **blue** mila hai
- Proof: instructor code ka ek digit (`8` ko `1` se) badalte hain — color **poori tarah badal
  jaata hai**
- Aur instructor ki baat note karo: *"agar ye confusing lage, don't worry — baad mein detail se
  aayega."* Abhi sirf itna jaan lo ki ye exist karta hai.

```
#8B4513
 │││││└── blue
 │││└──── green
 │└────── red
 (har pair 00–FF tak hota hai — 0 = kuch nahi, FF = full)
```

### Step 3: Color kaise chuno? — color picker tools

Colors ko guess karne ki zaroorat nahi — tools use karo:

**a) Browser ka built-in color picker (transcript `00:27:49`)**
Instructor `input` tags sikhate waqt dikhate hain — agar input ka `type="color"` karo to user ko
ek **powerful color picker** mil jaata hai, jisme dots ghuma kar virtually koi bhi color ban
sakta hai:

```html
<input type="color">
```

Apne page par ye daal kar khelo — color chunoge to uska hex code wahi dikhta hai; use apni CSS
mein copy kar sakte ho.

**b) Online tools** — coolers/jo bhi color palette site (transcript mein baad ke modules mein
use hote hain) — wahan se palette banao aur hex copy karo.

### Step 4: Readability check (sabse important practical rule)

Color choose karne ka asli skill **decoration nahi, readability** hai:

- Pichle lesson mein dekha tha: black background + black text = heading **invisible**
- Rule: **light background → dark text; dark background → light text**
- Apne page ko door se (ya aankhein thodi band karke) dekho — text padh sakte ho? Nahi? To
  color combo badlo.

(Ye accessibility ka topic hai — Module 05 mein contrast ka poora section aata hai. Abhi basic
rule kaafi hai.)

---

## "Your First App" mein kaise apply karein

```css
body {
    background-image: url("meri-background.jpg");
    background-size: cover;

    color: white;            /* naam ka color — readable on dark bg */
}

h2 {
    color: #FFD700;          /* gold-ish hex — subtitle highlight */
}
```

- Ek main text color choose karo jo background par padha ja sake
- Chaaho to `h2`/`p` ke liye alag accent color do — hex code color picker se uthao

---

## Common mistakes

1. **`#` bhoolna** — hex code bina hashtag ke kaam nahi karta (`8B4513` ❌, `#8B4513` ✅).
2. **Spelling** — `colour` likhna (British spelling) ya color name galti se `saddle-brown`
   likhna. Properties US spelling mein hain: `color`, `background-color`.
3. **`color` vs `background-color` confuse hona** — `color` sirf text badalta hai; element ke
   piche ka color `background-color` hai.
4. **Sirf color par info dena** — readability ka rule ignore karna. Har combo "dikhne mein cool"
   nahi hota — padhne mein bhi aasan hona chahiye.
5. **Semicolon (`;`) miss karna** — har CSS declaration ke baad `;` lagta hai, warna agli
   property toot jaati hai.

---

## Khud se karo (practice)

1. Apne page ke text ka color ek named color se set karo; phir use color picker se usi color ke
   **hex code** mein convert karo — dono baar page same dikhega.
2. Ek jaan-boojh kar **bekaar combo** banao (dark bg + dark text) — feel karo kyu readability
   matter karti hai. Phir fix karo.
3. `<input type="color">` apne page par temporarily add karo, ek mast color banao, uska hex
   copy karo, aur apne `h1` par laga do.

## Agle lesson ke liye ready?

Ab page par naam, photos, background, aur colors — sab hain. Section 02 ka aakhri lesson baaki
hai: **"Set the Font, Border, and Column Count"** (`05-set-the-font-border-and-column-count`) —
final polish touches jo page ko proper "app" jaisa bana dengi. ✨
