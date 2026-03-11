<div align="center">

<br/>

# ☀ RojLang

**Zimanê Bernamesaziyê yê Kurdî**

Write code in Kurdish. Run anywhere.

[![Version](https://img.shields.io/badge/version-v2.1-06d6a0?style=flat-square)](https://github.com/d7rx/rojlang)
[![License](https://img.shields.io/badge/license-All%20Rights%20Reserved-f0a500?style=flat-square)](#license)
[![Python](https://img.shields.io/badge/Python-3.8+-3776ab?style=flat-square)](https://python.org)
[![Platform](https://img.shields.io/badge/platform-Windows-0078d4?style=flat-square)]()

</div>

---

## Çi ye? — What is this?

RojLang lets you write programs using Kurdish words instead of English.  
`eger` instead of `if`, `dem` instead of `while`, `fonksîyon` instead of `def`.  
The interpreter translates your `.ku` file into Python and runs it — including GUI windows, animations, images, and sound.

```python
nav navê = xwestin("Navê xwe binivîse: ")
nivîs("Silav", navê)

bo i di bijmare(5):
    nivîs("RojLang ☀", i)
```

---

## Sazkirin — Install (Windows)

**Step 1** — Download `interpreter.py` + `install_rojlang.bat` into the same folder

**Step 2** — Right-click `install_rojlang.bat` → **Run as administrator**

**Step 3** — Open a **new** terminal

```
cd "C:\your\folder"
rojlang myfile.ku
```

> Python 3.8+ required — [python.org/downloads](https://python.org/downloads)  
> During install, check **"Add Python to PATH"**

---

## IDE — Editor v3.0

Full Kurdish editor with syntax highlighting, autocomplete, file tree, multi-tab, built-in terminal, and image/sound support.

```
python rojlang_ide.py
```

| Shortcut | Action |
|---|---|
| `F5` / `Ctrl+B` | Run |
| `Ctrl+T` | New tab |
| `Ctrl+\`` | Toggle terminal |
| `Ctrl+F` | Find & Replace |
| `Ctrl+S` | Save |

---

## Keywords — Peyvên Sereke

### Core

| RojLang | Python | Meaning |
|---|---|---|
| `nivîs(x)` | `print(x)` | Print |
| `nav x = …` | `x = …` | Variable |
| `xwestin("?")` | `input("?")` | User input |
| `eger / yan eger / yan` | `if / elif / else` | Conditionals |
| `dem … :` | `while … :` | While loop |
| `bo … di … :` | `for … in … :` | For loop |
| `fonksîyon` | `def` | Function |
| `vegere` | `return` | Return |
| `rast / çewt / Tune` | `True / False / None` | Boolean / Null |
| `ne / û / an` | `not / and / or` | Logic |
| `bişkîne / berdewam / nîşe` | `break / continue / pass` | Loop control |
| `derkev` | `exit()` | Exit |
| `dirêj(x)` | `len(x)` | Length |
| `cure(x)` | `type(x)` | Type |

### Types & Collections

| RojLang | Python |
|---|---|
| `hejmar(x)` | `int(x)` |
| `nivîsok(x)` | `str(x)` |
| `hejimarFloat(x)` | `float(x)` |
| `pêl([…])` | `list([…])` |
| `ferhenga({…})` | `dict({…})` |
| `koma({…})` | `set({…})` |

### Math & Random

| RojLang | Python |
|---|---|
| `mezin(a,b) / nizim(a,b)` | `max / min` |
| `jimartina(lst)` | `sum(lst)` |
| `bijmare(a,b)` | `range(a,b)` |
| `tomkirin(x,n)` | `round(x,n)` |
| `şikeftin(x)` | `abs(x)` |
| `hilbijêre(a,b)` | `randint(a,b)` |
| `mathSqrt / mathPow / mathPi` | `math.sqrt / pow / pi` |

### Exceptions

| RojLang | Python |
|---|---|
| `êşk:` | `try:` |
| `girtin Exception:` | `except Exception:` |
| `dewam:` | `finally:` |
| `avêtin` | `raise` |

### String & List Methods

| RojLang | Python |
|---|---|
| `s.jorê() / s.jêrê()` | `.upper() / .lower()` |
| `s.xêz()` | `.strip()` |
| `s.veqetîne(x)` | `.split(x)` |
| `s.biguhêze(a,b)` | `.replace(a,b)` |
| `lst.têxe(x)` | `.append(x)` |
| `lst.jêbike(x)` | `.remove(x)` |
| `lst.rêzkirin()` | `.sort()` |

### GUI

| RojLang | What it does |
|---|---|
| `pencere("Title", "800x600")` | Create window |
| `kevir(w, 800, 600, "#000")` | Drawing canvas |
| `çargoşe(c, x1,y1,x2,y2, "#reng")` | Rectangle → ID |
| `xember(c, x1,y1,x2,y2, "#reng")` | Oval/Circle → ID |
| `xêz(c, x1,y1,x2,y2, "#reng", 2)` | Line → ID |
| `nivîskar(c, x,y, "text", "#reng", 14)` | Text → ID |
| `bişkojk(w, "Label", fn)` | Button |
| `peyam("Title", "Message")` | Message dialog |
| `nîşan(w)` | Show window — **must be last line** |

### Keyboard & Animation

| RojLang | Python |
|---|---|
| `klavBiGire(w, "<Left>", fn)` | `w.bind("<Left>", fn)` |
| `bilivîne(c, id, dx, dy)` | `c.move(id, dx, dy)` |
| `piştî(w, 16, fn)` | `w.after(16, fn)` ← 60fps loop |
| `jêbike_item(c, id)` | `c.delete(id)` |
| `biguherêze_reng(c, id, "#reng")` | `c.itemconfig(fill=)` |

### Image — v2.1

| RojLang | What it does |
|---|---|
| `wêne("logo.png")` | Load PNG/GIF |
| `wêne("photo.jpg")` | Load JPG/WebP *(needs pillow)* |
| `wêne_pîvandî("p.jpg", 300, 200)` | Load + resize |
| `wêne_nîşan(c, x, y, img)` | Show on canvas → ID |
| `wêne_label(w, img)` | Show in Label widget |

```
pip install pillow
```

### Sound — v2.1

| RojLang | What it does |
|---|---|
| `deng("muzik.mp3")` | Play once |
| `deng("muzik.mp3", rast)` | Play looping |
| `deng_bilindî(0.7)` | Set volume 0.0–1.0 |
| `deng_rawest()` | Stop all sound |
| `deng_dengdank("boom.wav")` | Short sound effect |

```
pip install pygame
```

---

## Mînak — Examples

### Keyboard movement

```python
nav w   = pencere("Lîstik", "400x300")
nav c   = kevir(w, 400, 300, "#0a0a0f")
nav top = xember(c, 190, 140, 220, 170, "#f0a500")

fonksîyon kbsa(e):
    eger e.keysym=="Left":  bilivîne(c, top, -6, 0)
    yan eger e.keysym=="Right": bilivîne(c, top, 6, 0)
    yan eger e.keysym=="Up":    bilivîne(c, top, 0, -6)
    yan eger e.keysym=="Down":  bilivîne(c, top, 0, 6)

klavBiGire(w, "<KeyPress>", kbsa)
nîşan(w)
```

### Animation loop

```python
nav w   = pencere("Animasyon", "400x300")
nav c   = kevir(w, 400, 300, "#0a0a0f")
nav top = xember(c, 10, 140, 50, 180, "#f0a500")

fonksîyon loop():
    bilivîne(c, top, 3, 0)
    piştî(w, 16, loop)

loop()
nîşan(w)
```

### Try / Except

```python
êşk:
    nav x = hejmar(xwestin("Hejmar: "))
    nivîs("Çar:", x * 4)
girtin ValueError:
    nivîs("Şaşî! Hejmar binivîse.")
dewam:
    nivîs("Qediya.")
```

### Image + Sound

```python
nav w   = pencere("Media", "400x400")
nav c   = kevir(w, 400, 400, "#111")
nav img = wêne_pîvandî("logo.png", 200, 200)
wêne_nîşan(c, 200, 200, img)
deng("muzik.mp3", rast)
nîşan(w)
```

---

## Pelên Proje — File Structure

```
rojlang/
├── interpreter.py           ← Interpreter v2.1  (required)
├── rojlang_ide.py           ← IDE v3.0
├── install_rojlang.bat      ← Windows installer
├── uninstall_rojlang.bat    ← Uninstaller
├── auto_build.bat           ← Build .exe
├── BUILD.ps1                ← PowerShell build script
├── installer.nsi            ← NSIS installer script
├── rojlang.ico              ← App icon
├── examples/
│   ├── spaceship.ku         ← Space shooter game
│   ├── calculator.ku        ← Calculator GUI
│   ├── matrix_rain.ku       ← Matrix rain animation
│   ├── adventure.ku         ← Kurdish text adventure
│   └── photo_viewer.ku      ← Photo viewer + sound
├── README.md
└── LICENSE
```

---

## Malpera Fermî — Website

🌐 Coming soon

📸 Instagram: [@d7r.x_](https://www.instagram.com/d7r.x_)

---

## License

© 2026 Diyar — All Rights Reserved.  
See [LICENSE](LICENSE) for full terms.
