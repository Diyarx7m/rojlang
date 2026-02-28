# ☀ RojLang

A programming language with Kurdish keywords. Write code in Kurdish, runs on Python.

**v1.1** — released 2025

---

## What is this?

RojLang lets you write programs using Kurdish words instead of English. `eger` instead of `if`, `dem` instead of `while`, `fonksîyon` instead of `def`, and so on. The interpreter translates your `.ku` file to Python and runs it — including graphical windows with shapes, colors and buttons.

```
nav x = 10

eger x > 5:
    nivîs("mezin ji 5")
yan:
    nivîs("biçûk ji 5")
```

---

## Installation (Windows)

1. Download `interpreter.py` and `install_rojlang.bat` — put them in the same folder
2. Right-click `install_rojlang.bat` → **Run as administrator**
3. Open a new terminal
4. Done:

```
rojlang myfile.ku
```

Or double-click any `.ku` file.

> **Python required.** Get it at [python.org/downloads](https://python.org/downloads) — check "Add Python to PATH" during install.

---

## Running files

```bash
rojlang game.ku          # run the guessing game
rojlang art.ku           # run the Kurdish art demo (opens a window)
rojlang myfile.ku --debug    # show translated Python code
```

---

## Keyword reference

### Core language

| RojLang | Python | meaning |
|---|---|---|
| `nivîs` | `print()` | print to screen |
| `bêje` | `print(end="")` | print, no newline |
| `nav x = …` | `x = …` | declare variable |
| `xwestin` | `input()` | read user input |
| `hilbijêre(a, b)` | `random.randint(a, b)` | random number |
| `eger` | `if` | if condition |
| `yan eger` | `elif` | else-if |
| `yan` | `else` | else |
| `dem` | `while` | while loop |
| `bo … di` | `for … in` | for loop |
| `fonksîyon` | `def` | define function |
| `vegere` | `return` | return value |
| `rast` | `True` | boolean true |
| `çewt` | `False` | boolean false |
| `Tune` | `None` | null / none |
| `ne` | `not` | logical not |
| `û` | `and` | logical and |
| `an` | `or` | logical or |
| `bişkîne` | `break` | break loop |
| `berdewam` | `continue` | continue loop |
| `nîşe` | `pass` | do nothing |
| `derkev` | `exit()` | exit program |
| `dirêj(x)` | `len(x)` | length |
| `x.têxe(y)` | `x.append(y)` | append to list |
| `cure(x)` | `type(x)` | type of variable |
| `sinif` | `class` | define class |

### Graphics (GUI)

| RojLang | what it does |
|---|---|
| `pencere(serî, pîvan)` | create a window — `pencere("Title", "600x400")` |
| `nîşan(w)` | show the window / start the app |
| `kevir(w, fireh, bilindî, paşreng)` | create a canvas to draw on |
| `çargoşe(c, x1, y1, x2, y2, reng)` | draw a filled rectangle |
| `xember(c, x1, y1, x2, y2, reng)` | draw a filled oval / circle |
| `xêz(c, x1, y1, x2, y2, reng, stûrî)` | draw a line |
| `nivîskar(c, x, y, nivîs, reng, mezinahî)` | draw text on canvas |
| `bişkojk(w, nivîs, kar)` | create a clickable button |
| `nav_çargoşe(w, nivîs, reng)` | create a text label |
| `rengên_hevber(reng1, reng2, gav)` | generate gradient color list |

---

## Example programs

### Console — guessing game

```
nav veşartî = hilbijêre(1, 10)
nav çalak = rast

nivîs("hejmarek ji 1 heta 10 texmîn bike")

dem çalak:
    nav texmîn = int(xwestin("texmîna te: "))
    eger texmîn > veşartî:
        nivîs("mezintir e")
    yan eger texmîn < veşartî:
        nivîs("biçûktir e")
    yan:
        nivîs("rast!")
        nav çalak = çewt
```

### Graphics — Kurdish art

```
nav xalan  = pencere("Hunerê Kurdî", "500x400")
nav kevça  = kevir(xalan, 500, 400, "#0a0a0f")

# draw shapes
çargoşe(kevça, 50,  50,  200, 200, "#e63946")
xember(kevça,  250, 50,  450, 250, "#f0a500")
xêz(kevça,     50,  300, 450, 300, "#06d6a0", 3)

# add text
nivîskar(kevça, 250, 360, "☀ RojLang", "#f0a500", 18)

nîşan(xalan)
```

---

## File structure

```
rojlang/
├── interpreter.py       # the interpreter
├── install_rojlang.bat  # windows installer
├── game.ku              # console demo — guessing game
├── art.ku               # graphics demo — Kurdish art
└── README.md
```

---

## How it works

The interpreter reads your `.ku` file, replaces Kurdish keywords with Python equivalents using regex, injects helper functions (including the full graphics API), then executes everything. Graphics use Python's built-in `tkinter` library — no extra installs needed.

---

## Contact

- Instagram: [@d7r.x_](https://www.instagram.com/d7r.x_?igsh=cG9xZG55M2traTVn)
- Email: didad9683@gmail.com

---

## License

MIT — do whatever you want with it.
