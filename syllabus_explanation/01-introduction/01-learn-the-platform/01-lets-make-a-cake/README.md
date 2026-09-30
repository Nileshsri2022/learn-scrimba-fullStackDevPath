# Lesson 01: Let's Make a Cake (Hinglish Explanation)

**Path:** MODULE 01. Introduction → SECTION 01. Learn the Platform → LESSON 01. Let's Make a Cake
**Practices:** Exercise 1, Exercise 2 (neeche cover kiye hain)

---

## Transcript mein kya fit hota hai (honest mapping)

Ye syllabus ka sabse pehla lesson hai, aur ye Scrimba platform ka **onboarding activity** hai —
matlab iska maqsad HTML seekhna nahi, balki **platform par kaam karna seekhna** hai (editor kahan
hai, preview kahan aata hai, code kaise run karte hain, exercise kaise solve karte hain).

Transcript (video) mein "cake" shabd **bilkul nahi bola gaya** — kyunki video ek continuous
recording hai aur cake exercise hosted scrimba.com course ka interactive hissa hai. Lekin
transcript ke shuruaati 5 minute is lesson ke liye **perfect context** dete hain:

| Transcript time | Kya hai | Is lesson se connection |
|---|---|---|
| `00:00:00 – 00:01:29` | Per Borgen (Scrimba CEO) ka welcome | Platform ka philosophy: khud type karo, 500+ challenges, projects banao |
| `00:01:30 – 00:04:25` | Pehla hands-on HTML: "I code, therefore I am" | Wahi kaam jo cake exercise sikhaata hai: file banana, code likhna, run karke preview dekhna |

---

## Step 1: Pehle samjho — ye course kaise kaam karta hai

Transcript ki shuruaat mein Per Borgen (Scribba/Scrimba ke CEO) khud aate hain aur batate hain
(transcript `00:00:00–00:01:29` approx):

1. **Ye massive fullstack path hai** — HTML, CSS, JavaScript se shuru hokar React, Node, Next,
   SQL, TypeScript, Testing aur AI Engineering tak jaata hai. "One-stop shop" fullstack developer
   banne ke liye.
2. **Boring theory nahi** — tum games banaoge, Google aur Instagram clone banaoge, AI investing
   app banaoge, Chrome extension bhi.
3. **Sabse important line:** *"the only way to learn this is to type the code out yourself"*.
   Sirf dekhne se nahi hoga — teachers tumhe **500+ baar challenges** denge, aur unka starter
   code GitHub par aur scrimba.com ke interactive version par milega.

**Iska matlab:** "Let's Make a Cake" exercise ka asli maqsad yahi habit daalna hai — video ko
pause karo, khud code type karo, result dekho. Cake sirf ek fun example hai; skill wo nahi,
**workflow** seekhna hai.

---

## Step 2: Platform workflow (jo cake exercise sikhaata hai)

Scrimba ke interactive lessons (scrim) mein ye loop hota hai — aur yehi loop transcript mein
har jagah repeat hota hai:

```
1. Instructor ek chhota change karta hai      (code edit)
2. Code run hota hai                          ("run the code")
3. Mini-browser mein result dikhta hai        (preview)
4. Tumhe challenge milta hai                  ("pause and try it yourself")
5. Tum solve karte ho, phir solution milta hai
```

Cake exercise mein bhi yahi hota hai: ek ready-made "cake" page diya jaata hai, aur tum
Exercise 1 aur Exercise 2 mein chhote-chhote changes karke platform ke controls seekhte ho.

---

## Step 3: Transcript se — pehla practical kaam (cake ke turant baad wali skill)

Transcript `00:01:30` par instructor ek joke ke saath hands-on shuru karte hain:
French philosopher René Descartes ne kaha tha *"Cogito, ergo sum"* — course ke version mein:
**"I code, therefore I am."** Ab isse HTML mein likhte hain:

### 3a. Pehle plain text (text editor wali soch)

Normal text editor mein aap sentence likhte aur use bold/heading banate ho. HTML mein bhi
pehle sentence likhte ho:

```html
I code, therefore I am.
```

### 3b. `index.html` file banana

File ka naam `index.html` rakhte hain — instructor batate hain ki ye HTML files ke liye ek
**common convention** hai. Browser mein kholo to text dikhta hai, lekin chhota aur plain.

### 3c. `h1` tag se heading banana

Text ko heading banane ke liye use **tags** mein wrap karte hain:

```html
<h1>I code, therefore I am.</h1>
```

- `<h1>` = **opening tag** (angle brackets ke andar H1 — "heading one")
- `</h1>` = **closing tag** — naam se pehle **slash (`/`)** lagta hai, ye browser ko batata hai
  ke element yahin khatam hota hai
- Beech ka text = **content**
- Code rerun karo → text bada aur prominent ho jaata hai ✅

### 3d. Neeche naam add karna — sirf wahi text format hota hai jo tags ke ANDAR ho

Instructor heading ke neeche `Rene Descartes` likhte hain aur rerun karte hain — wo text
**normal** reh jaata hai. Kyu? Kyunki sirf wo text heading banta hai jo `<h1>` aur `</h1>` ke
**beech** ho. Baahar ka text par h1 ka effect nahi.

### 3e. Pehla challenge (hint: "What comes after one?" 🙂)

Instructor chahte hain ki naam thoda bada ho lekin h1 jitna nahi. Hint dete hain: *"What comes
after one?"* Matlab — `h2`:

```html
<h1>I code, therefore I am.</h1>
<h2>René Descartes</h2>
```

`h2` ka syntax **bilkul h1 jaisa** hai, bas `1` ki jagah `2`. (Solution transcript `00:04:25` ke
aas-paas.)

---

## Practice: Exercise 1 aur Exercise 2

Hosted course mein ye dono exercises cake page par chhote edits hain. Transcript ke context se
inke **equivalent tasks** ye hain — inhe zaroor karke dekho:

**Exercise 1 (platform warm-up):**
1. Apne editor mein `index.html` banao.
2. `<h1>I code, therefore I am.</h1>` likh kar run karo.
3. Ab h1 ka text badalkar apna naam likho aur **dobara run** karo.
   → Maqsad: edit → run → preview loop ko muscle-memory banana.

**Exercise 2 (khud se sochna):**
1. Heading ke neeche apna naam `h2` mein likho (bina solution dekhe).
2. Phir ek aur line add karo normal text mein (jaise apna hometown) aur dekho ki wo heading
   nahi banti.
   → Maqsad: samajhna ki tag *content ko meaning deta hai*, aur sirf tags ke andar ka text
   style hota hai.

---

## Yaad rakhne wali 5 baatein

1. **Khud type karo** — dekhne se nahi, karne se seekhoge (course ka core rule).
2. Har change ke baad **run/preview** karo — chhote steps = aasan debugging.
3. `index.html` ek conventional file name hai.
4. Closing tag mein **slash** hota hai: `</h1>`.
5. Jo text tags ke **andar** hai, sirf wahi format hota hai.

## Agle lesson ke liye ready?

Agar tum ye kar sakte ho — file banao, h1/h2 likho, text badlo, preview dekho — to chalo agle
lesson mein: **"Add your Name and Emoji"** (`02-your-first-app/01-add-your-name-and-emoji`),
jahan hum page ko personal banana shuru karenge. 🎂➡️👤
