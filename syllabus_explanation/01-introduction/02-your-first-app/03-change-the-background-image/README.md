# Lesson 03: Change the Background Image (Hinglish Explanation)

**Path:** MODULE 01. Introduction → SECTION 02. Your First App → LESSON 03. Change the Background Image

---

## Transcript mein kya fit hota hai (honest mapping)

Module 01 ke level par "background image change karna" ek simple personalization step hai.
Transcript mein `background-image` property ka **full detailed lesson** Space Exploration site
build mein aata hai — wahi is lesson ka best fit hai:

| Transcript time | Kya hai |
|---|---|
| `03:34:26 – 03:36:09` | `background-image` property, `url()` function, body par lagana, text color problem, `background-size` ki shuruaat |
| `02:26:10 – 02:26:50` (baad ka context) | CSS file se image ka **relative path** (`../..` wala) kaise kaam karta hai |

Note: Transcript `00:09:47` mein instructor pehle hi hint de chuke hote hain — "baad mein CSS
seekhoge, jo styling ke liye hoti hai." Ab wahi time aa gaya: **background image CSS ka kaam
hai, HTML ka nahi.**

---

## Pehle ye samjho: `<img>` vs background image

Pichle lesson mein humne `<img>` tag se photos daali. To background image mein kya fark?

| | `<img>` tag | `background-image` (CSS) |
|---|---|---|
| Kahan likhte hain | HTML mein | CSS mein |
| Kab use karo | Photo **content** hai (news photo, profile pic) | Image **decoration** hai (page ke piche texture) |
| Content ke saath | Alag element ki tarah dikhta hai | Text/content uske **upar** float karta hai |
| Screen reader | `alt` se padha ja sakta hai | Ignore hota hai (decoration hi hai) |

"Your First App" mein hum page ke piche ek mood/theme image lagate hain — isliye CSS wala
tareeka sahi hai.

---

## Step-by-step (transcript `03:34:26` — Space Exploration site)

Instructor ke paas `universe.jpeg` image hai aur `h1` wala page hai. Unhe image **poori page
ke piche** chahiye:

### Step 1: Kaunsa element target kare? — `body`

Instructor sochte hain: image ko **poori page par** failana hai, isliye `body` element ko
target karte hain. CSS file mein:

```css
body {
}
```

(Page ka saara visible content `body` ke andar hota hai, isliye body ka background = poore page
ka background.)

### Step 2: `background-image` property + `url()` function

Ab property lagate hain. Instructor batate hain ki yahan ek **"CSS function"** use hota hai —
`url()`. Syntax:

```css
body {
    background-image: url("images/universe.jpeg");
}
```

Instructor ke exact points:
- `url` likho, phir **parentheses** `()` kholo
- Parentheses ke andar, **quotes** mein image ka path likho — bilkul waise jaise `<img>` ke
  `src` attribute mein likhte the
- Path yahan `images/universe.jpeg` hai — pehle `images` folder mein jao (slash se), phir file
  choose karo

Code save/run karte hi — **"and boom, there we go, suddenly our background changed"** ✅

### Step 3: Problem #1 — text gaayab ho gaya!

Image lagte hi ek **typical real-world bug** aa jaata hai:

- H1 ka text by-default **black** hota hai
- Universe image bhi almost **black** hai
- Result: heading invisible! 😱

Instructor ka fix — text ka color badalna:

```css
body {
    background-image: url("images/universe.jpeg");
    color: white;
}
```

> **Lesson:** background image lagate hi text ka **contrast** check karo. Ye accessibility ka
> bhi core rule hai (baad mein Module 05 mein detail se aayega).

### Step 4: Problem #2 — image zyada badi hai

Ab doosri problem:

- Image **hazaaron pixels** wide hai, browser utna wide nahi
- Browser ko kitna bhi stretch karo — hume galaxy ka sirf center/edge portion dikhta hai
- Zaroorat: image **shrink** ho kar browser ki width mein fit ho

Iska fix aata hai `background-size` property se (transcript `03:35:57` par shuru hota hai):

```css
body {
    background-image: url("images/universe.jpeg");
    background-size: cover;
    color: white;
}
```

`cover` ka matlab: image ko itna scale karo ki wo container ko **poora cover** kare — chhota ya
bada, fit ho jaaye.

---

## "Your First App" mein kaise apply karein

App ke liye ek background theme choose karo (jaise beach, space, patterns):

```css
body {
    background-image: url("meri-background.jpg");
    background-size: cover;
}
```

- Online image use karni ho? `url("https://...")` mein address paste karo — wahi "copy image
  address" trick jo pichle lesson (`Display Photos`) mein seekhi thi.
- Phir check karo: tumhara naam/text background ke upar **readable** hai ya nahi? Nahi hai to
  `color` badlo — agla lesson (`Choose a Color`) wahi sikhaayega.

---

## Path ki ek aur complexity (advanced note)

Transcript `02:26:10` mein ek zaroori cheez aati hai: agar tumhari **CSS file kisi folder ke
andar** hai (jaise `css/index.css`), to relative path dot-dot-slash se start hota hai:

```css
/* css folder ke andar waali CSS file se, root ke images folder tak */
.image-div {
    background-image: url("../../images/cat.jpg");
}
```

- `..` = **parent directory** mein jao
- Jitne levels upar jaana ho, utne `../`
- Abhi ke liye itna yaad rakho: path hamesha **us file ke perspective** se likha jaata hai jisme
  code likha hai (HTML ya CSS) — folder structure alag ho to path adjust karna padega.

---

## Common mistakes

1. **`url()` mein quotes bhoolna** — kabhi-kabhi bina quotes bhi chal jaata hai, lekin hamesha
   quotes ke saath likho (safe practice).
2. **HTML mein `background-image` likhne ki koshish** — ye CSS property hai; apni `.css` file ya
   `<style>` tag mein jaayegi.
3. **Galat relative path** — CSS file kisi folder ke andar hai to `../` yaad rakhna; nahi to
   image load hi nahi hogi.
4. **Contrast ignore karna** — dark background par dark text = kuch nahi dikhta. Hamesha text
   color verify karo.
5. **`background-size` skip karna** — bina iske badi images ka sirf kona dikhai dega.

---

## Khud se karo (practice)

1. Apne page ke `body` par koi background image lagao (local ya online).
2. `background-size: cover` ke **bina** browser ko wide/narrow karo — problem khud dekho, phir
   `cover` add karke fix karo.
3. Text ka color aisa choose karo jo background par clearly dikhe.

## Agle lesson ke liye ready?

Background set ho gaya, aur humne `color: white` bhi try kar liya. Ab agla lesson naturally
aata hai: **"Choose a Color"** (`04-choose-a-color`) — jahan hum colors properly choose karna
seekhenge: color names, color picker, aur hex codes. 🎨
