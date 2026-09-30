# Lesson 01: Add your Name and Emoji (Hinglish Explanation)

**Path:** MODULE 01. Introduction → SECTION 02. Your First App → LESSON 01. Add your Name and Emoji

---

## Transcript mein kya fit hota hai (honest mapping)

"Your First App" Scrimba ka ek interactive mini-app hai jisme tum ek page ko **personalize**
karte ho — apna naam, emoji, photos, colors waghera. Video transcript mein ye exact activity
naam se **nahi aati**, lekin is activity ke peeche ki **core skill** transcript ke shuruaati
hisso mein clearly hai:

| Transcript time | Kya hai | Is lesson se connection |
|---|---|---|
| `00:01:30 – 00:04:25` | "I code, therefore I am" — h1 banana, text edit karna | Page par apna text/naam daalna |
| `00:04:25 – 00:05:47` | Challenge + solution: naam ko `h2` banana | Sahi element choose karna (h1 vs h2) |
| `04:29:52` (baad mein) | Lab equipment ko emojis se visualize karna — `<div>` ke andar emoji | Proof ki emoji HTML mein normal content ki tarah use hota hai |

---

## Ye lesson kya sikhaata hai

Pehli baar kisi page ko **apna** banana. Ab tak humne instructor ka text ("I code, therefore I
am") use kiya — ab page par **tumhara naam** aur **tumhari pasand ka emoji** aayega. Skill do
chhoti cheezein hain:

1. **Content edit karna** — element ke opening aur closing tag ke beech ka text badalna.
2. **Sahi element choose karna** — sabse important text (naam) ke liye `h1`, supporting text
   ke liye `p`/`h2`.

---

## Step-by-step (transcript ke workflow par)

### Step 1: Naam ke liye `h1` use karo

Page ka sabse prominent content tumhara naam hai, to usse top-level heading banao:

```html
<h1>Nilesh</h1>
```

Pichle lesson se yaad karo: jo text `<h1>...</h1>` ke **andar** hai, wahi heading banta hai.
Baahar ka text normal rehta hai.

### Step 2: Emoji add karo — koi special tag nahi chahiye!

Emoji koi HTML feature nahi hai — wo bas ek **character** hai, bilkul letters ki tarah. Tum usse
seedha text ki tarah paste kar sakte ho:

```html
<h1>Nilesh 🚀</h1>
```

Bas. No extra tag, no attribute. Emoji utna hi simple hai jitna koi letter type karna —
keyboard ka emoji panel kholo (Windows: `Win + .`, macOS: `Ctrl + Cmd + Space`) ya kahin se copy
karke paste kar do.

> **Transcript evidence:** Baad ke course mein (`04:29:52`) instructor `<div>` elements ke
> andar emojis rakhte hain lab equipment dikhane ke liye — bina kisi special syntax ke. Ye
> proof hai ki emoji aam text content ki tarah hi HTML mein rehta hai.

### Step 3: Ek supporting line add karo

Naam ke neeche ek chhota intro — kyunki ye heading nahi hai, isliye `h2` ya `p` use karo.
Transcript mein instructor ne create kiya tha: heading ke neeche philosopher ka naam — ye wahi
pattern hai:

```html
<h1>Nilesh 🚀</h1>
<h2>Aspiring Fullstack Developer</h2>
<p>Hi! This is my first app.</p>
```

Yaad rakho transcript wali baat: `h2` ka syntax h1 jaisa hi hota hai, bas number badalta hai
(hint tha: *"What comes after one?"*).

### Step 4: Run karke preview dekho

Har change ke baad code rerun karo aur browser mein dekho:

- Naam bada bold heading mein dikhna chahiye ✅
- Emoji ka color/rendering OS ke hisaab se thoda alag dikh sakta hai — normal hai
- `p` wali line normal size mein honi chahiye

---

## Sahi element kaise chuno — ek rule of thumb

| Content | Element | Kyu |
|---|---|---|
| Tumhara naam (page ka sabse important text) | `h1` | Page par sirf ek main heading |
| Subtitle / role | `h2` | Heading hai, lekin h1 se chhoti |
| Lambi intro line / paragraph | `p` | Normal text content |

Instructor transcript mein baar-baar ye point dete hain: **element ko uske default look ke liye
nahi, uske meaning ke liye choose karo.** Styling baad mein CSS se aayegi.

---

## Common mistakes (is stage par)

1. **Closing tag bhoolna** — `<h1>Nilesh` likh diya, `</h1>` nahi. Result: saara baaki page bhi
   heading ban sakta hai.
2. **Slash galat jagah** — `<h1>` closing mein aur `</h1>` opening mein likh dena. Opening tag
   mein slash nahi hota.
3. **Text tags ke baahar** — naam ke baad ka text heading ka hissa ban gaya? Check karo ki text
   `</h1>` se pehle hi khatam ho raha hai.
4. **Run karna bhoolna** — edit kiya, preview nahi dekha, phir confuse hue ki change kahan hai. 😄

---

## Khud se karo (practice)

1. Apne naam ke aage-apni favourite emoji lagao — ek nahi, **teen alag jagah** try karo:
   naam se pehle, naam ke baad, apni hi line mein.
2. Ek naya `h2` add karo jisme aaj ki date ya apna goal likho.
3. Har step ke baad preview karo — aur dekho kya badla.

## Agle lesson ke liye ready?

Ab page par text hai. Agla lesson: **"Display Photos"** (`02-display-photos`) — jahan hum
`<img>` tag se page par images laayenge, aur transcript mein instructor ka famous "hacker
mindset" wala trick (`width="100%"`) bhi seekhenge. 📸
