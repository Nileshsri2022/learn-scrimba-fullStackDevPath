# Lesson 02: Write a news article (Hinglish Explanation)

**Path:** MODULE 02. HTML and CSS Fundamentals → SECTION 01. Intro to HTML → LESSON 02. Write a news article

---

## Transcript mein kya fit hota hai (direct match ✅)

Ye lesson transcript mein **exactly** hai — instructor ab tumse khud se ek layout banwate hain.
Pehli baar tumhe poora chhota design diya jaata hai jise tumhe HTML mein convert karna hai:

| Transcript time | Kya hai |
|---|---|
| `00:05:47 – 00:06:22` | News article challenge — design slide + `h1`, `h3`, `p` + copy-paste text |
| `00:06:22 – 00:07:00` | Solution — teeno tags step-by-step |

---

## Ye lesson kya hai

Ab tak tumne instructor ke saath mil kar code likha. Ab **tumhe** ek news article ka design diya
jaata hai aur kehte hain — "line 13 se shuru karke wo HTML likho jo ye layout banaye." Ye course
ki asli teaching style hai: dekhna → pause karna → **khud karna** → solution dekhna.

Article Mars ke baare mein hai (course aage bhi isi article par kaam karega — isliye is lesson
ko dhyan se karna).

---

## Challenge kya tha (transcript ke words mein)

Instructor dete hain:

1. **Ek design slide** — jisme title bada, ek medium heading, aur bottom mein text
2. **Syntax hint** — teen tags use karne hain:
   - `h1` — tum jante hi ho
   - `h3` — *"tumne abhi tak use nahi kiya, lekin mujhe lagta hai tumhe pata hai kaise karna hai"* 😉
   - `p` — **naya tag**, short for **paragraph** (bottom text ke liye). Chhota syntax example bhi
     diya jaata hai, lekin instructor kehte hain: "agar tumne tags likhne ka logic samajh liya
     hai, to ye surprise nahi honi chahiye"
3. **Ready-made text** — article ka poora text copy-paste ke liye de diya jaata hai, taaki tumhe
   type na karna pade

---

## Solution — step-by-step (transcript `00:06:22`)

Instructor teeno elements ek-ek karke add karte hain, **har baar code rerun karke**:

```html
<h1>Mars article ka title</h1>
```

Rerun → kaam kar raha hai ✅ ("Yes, it works.")

Phir `h3`:

```html
<h3>Article ki sub-heading</h3>
```

Rerun → dikhta hai ✅

Aur paragraph:

```html
<p>Article ka poora paragraph text...</p>
```

Rerun → **exact design wala layout** ban gaya. ✅

Final pattern kuch aisa:

```html
<h1>Humans have reached Mars</h1>
<img> <!-- (agle lesson mein yahan image aayegi) -->
<h3>The Starship rocket successfully landed on the red planet</h3>
<p>Early this morning, a crew of seven people ... </p>
```

---

## Is lesson se kya seekhna hai (chat par taangen nahi, concept par dhyan do)

### 1. Headings ka hierarchy = content ka outline

- `h1` → article ka **main title** (page par sirf ek)
- `h3` → article ki **sub-heading/summary**
- `p` → article ka **body text**

Ye bas "alag sizes" nahi hain — ye content ka **structure** hai. Screen reader wala user inhi
headings se page "navigate" karta hai, aur Google bhi isi se samajhta hai page kis baare mein
hai.

### 2. `p` tag — paragraph

- `p` = **paragraph** — normal text blocks ke liye
- Syntax bilkul wahi: `<p>content</p>`
- `p` ek **block-level** element hai — poori width leta hai aur next element ko agli line par
  dhakel deta hai (isliye article ke tukde alag-alag lines par dikhte hain)

### 3. Copy-paste karna bhi ek skill hai (sahi jagah se)

Instructor jaan-boojh kar text provide karte hain — typing practice ka time baad mein bhi
milega. Yahan focus **structure sahi banana** par hai. Real job mein bhi content aapko copy se
milega; tumhara kaam use sahi tags mein wrap karna hota hai.

### 4. Har element ke baad rerun karo

Instructor har tag ke baad code rerun karte hain ("Running the code and there we go").
**Ek-ek step = ek-ek risk.** Agar teeno ek saath likh kar rerun karte aur kuch tootta, to pata
nahi chalta kis line mein galti hai.

---

## Common mistakes

1. **Tags ka order badal dena:** design mein jo upar hai wo HTML mein bhi upar — browser
   elements ko **usi order** mein dikhata hai jis order mein likha hai.
2. **`h3` ko `h2` ki jagah (ya ulta) use karna bina soche:** levels skip karna (h1 → h3) tab
   theek hai jab design aisa maange, lekin hierarchy samajh kar chuno — ye accessibility bhi
   hai (Module 05 mein detail).
3. **`p` ke andar `h1` likhne ki koshish:** paragraph sirf text content ke liye hai; headings
   uske baahar raho.
4. **Closing tag mein tag ka naam galat likhna:** `<p>...</h3>` — browser confuse, result
   anap-shanap. Opening-closing ka pair same hona chahiye.

---

## Khud se karo (practice)

1. Aaj ki koi real news headline uthao aur uska Mars-article jaisa structure banao: `h1`
   (headline), `h3` (summary), `p` (2-3 sentences). Rerun karke verify karo.
2. Ab usme jaan-boojh kar ek galti daalo (closing tag hatao) — browser kya karta hai dekho,
   phir fix karo. Galti karna bhi seekhna hai. 😄
3. Do `p` lagatar likho — kya wo alag paragraphs ban-te hain? Yes/No kyu?

## Agle lesson ke liye ready?

Article text to ready hai, lekin boring lag raha hai — **photo** kahan hai? Agle lesson
**"The img tag"** (`03-the-img-tag`) mein instructor isi Mars article mein image add karte
hain — aur saath mein `self-closing tags`, `src` attribute aur wo famous `width="100%"` hack.
📷
