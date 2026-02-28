# RojLang interpreter - v1.1
# Kurdish programming language that runs on Python
# Released: 2026
#
# How to run:
#   python interpreter.py myfile.ku
#   python interpreter.py myfile.ku --debug

import re
import sys
import os
import traceback
import random
import math


# Kurdish keywords mapped to their Python equivalents
# order matters - longer/specific patterns come first
TRANSLATIONS = [
    (r"\bfonksîyon\b",  "def"),
    (r"\bnivîs\b",      "print"),
    (r"\beger\b",       "if"),
    (r"\byan\b",        "else"),
    (r"\bdem\b",        "while"),
    (r"\bvegere\b",     "return"),
    (r"\bxwestin\b",    "input"),
    (r"\bbo\b",         "for"),
    (r"\bdi\b",         "in"),
    (r"\brast\b",       "True"),
    (r"\bçewt\b",       "False"),
    (r"\bsinif\b",      "class"),
    (r"\bTune\b",       "None"),

    # nav is a declaration hint, strip it
    (r"\bnav\b\s+",     ""),

    (r"\bnîşe\b",       "pass"),
    (r"\bbişkîne\b",    "break"),
    (r"\bberdewam\b",   "continue"),
    (r"\bderkev\b",     "exit()"),

    (r"\bne\b",         "not"),
    (r"\bû\b",          "and"),
    (r"\ban\b",         "or"),

    # bêje prints on same line
    (r"\bbêje\b",       "_ku_beje"),

    (r"\bdirêj\b",      "len"),
    (r"\bcure\b",       "type"),
    (r"\.têxe\b",       ".append"),
    (r"\bhilbijêre\b",  "random.randint"),
]

POST_FIXES = [
    (r"\belse\s+if\b",       "elif"),
    (r"(?m)(\S)[ \t]{2,}",  r"\1 "),
]


# ── text helper ───────────────────────────────────────────────────

def _ku_beje(*args, **kwargs):
    kwargs.setdefault("end", "")
    print(*args, **kwargs)


# ── GUI helpers (tkinter wrapper with Kurdish names) ──────────────

def _make_gui_env():
    try:
        import tkinter as tk
    except ImportError:
        return {}

    def pencere(serî="RojLang ☀", pîvan="600x450"):
        """Create and return a window / Pencereyek çêdike û vedigere"""
        w = tk.Tk()
        w.title(serî)
        w.geometry(pîvan)
        w.configure(bg="#0a0a0f")
        w.resizable(False, False)
        return w

    def nîşan(w):
        """Show the window / Pencereyê nîşan dide"""
        w.mainloop()

    def kevir(w, fireh=500, bilindî=400, paşreng="#0a0a0f"):
        """Create a canvas / Kevirek çêdike ku lê wênekêşî bê kirin"""
        import tkinter as tk
        c = tk.Canvas(w, width=fireh, height=bilindî,
                      bg=paşreng, highlightthickness=0)
        c.pack()
        return c

    def çargoşe(c, x1, y1, x2, y2, reng="#f0a500", sînor=""):
        """Draw a rectangle / Çargoşeyek xêz dike"""
        c.create_rectangle(x1, y1, x2, y2, fill=reng, outline=sînor)

    def xember(c, x1, y1, x2, y2, reng="#f0a500", sînor=""):
        """Draw an oval/circle / Xemberek xêz dike"""
        c.create_oval(x1, y1, x2, y2, fill=reng, outline=sînor)

    def xêz(c, x1, y1, x2, y2, reng="#f0a500", stûrî=2):
        """Draw a line / Xêzek xêz dike"""
        c.create_line(x1, y1, x2, y2, fill=reng, width=stûrî)

    def nivîskar(c, x, y, nivîs, reng="#e8e8f0", mezinahî=14, font="Arial"):
        """Draw text on canvas / Nivîsek li kevirê çêdike"""
        c.create_text(x, y, text=str(nivîs), fill=reng,
                      font=(font, mezinahî))

    def bişkojk(w, nivîs, kar, reng="#f0a500", paşreng="#1a1a24"):
        """Create a button / Bişkojkek çêdike"""
        import tkinter as tk
        b = tk.Button(w, text=nivîs, command=kar,
                      fg=reng, bg=paşreng, activeforeground=paşreng,
                      activebackground=reng, relief="flat",
                      padx=14, pady=6, cursor="hand2",
                      font=("Arial", 11))
        b.pack(pady=4)
        return b

    def nav_çargoşe(w, nivîs, reng="#e8e8f0", paşreng="#111118", mezinahî=12):
        """Create a text label / Labelek nivîsê çêdike"""
        import tkinter as tk
        l = tk.Label(w, text=nivîs, fg=reng, bg=paşreng,
                     font=("Arial", mezinahî))
        l.pack(pady=2)
        return l

    def rengên_hevber(reng1, reng2, gav=10):
        """Generate gradient color steps between two hex colors"""
        def hex_to_rgb(h):
            h = h.lstrip("#")
            return tuple(int(h[i:i+2], 16) for i in (0, 2, 4))
        def rgb_to_hex(r, g, b):
            return f"#{int(r):02x}{int(g):02x}{int(b):02x}"
        r1, g1, b1 = hex_to_rgb(reng1)
        r2, g2, b2 = hex_to_rgb(reng2)
        return [rgb_to_hex(
            r1 + (r2 - r1) * i / (gav - 1),
            g1 + (g2 - g1) * i / (gav - 1),
            b1 + (b2 - b1) * i / (gav - 1)
        ) for i in range(gav)]

    return {
        "pencere":       pencere,
        "nîşan":         nîşan,
        "kevir":         kevir,
        "çargoşe":       çargoşe,
        "xember":        xember,
        "xêz":           xêz,
        "nivîskar":      nivîskar,
        "bişkojk":       bişkojk,
        "nav_çargoşe":   nav_çargoşe,
        "rengên_hevber": rengên_hevber,
    }


# ── translator ────────────────────────────────────────────────────

def wergerîne(source):
    code = source
    for pattern, replacement in TRANSLATIONS:
        code = re.sub(pattern, replacement, code)
    for pattern, replacement in POST_FIXES:
        code = re.sub(pattern, replacement, code)
    return code


# ── runner ────────────────────────────────────────────────────────

def bijêre(file_path, debug=False):
    if not file_path.endswith(".ku"):
        print(f"[RojLang] Şaşî: '{file_path}' nayê qebûlkirin, pel divê bi .ku biqede")
        sys.exit(1)

    if not os.path.isfile(file_path):
        print(f"[RojLang] Şaşî: Pel '{file_path}' nehat dîtin")
        sys.exit(1)

    with open(file_path, "r", encoding="utf-8") as f:
        source = f.read()

    translated = wergerîne(source)

    if debug:
        sep = "─" * 58
        print(f"\n{sep}\n  [DEBUG] translated output:\n{sep}")
        for i, ln in enumerate(translated.splitlines(), 1):
            print(f"  {i:>4} │ {ln}")
        print(f"{sep}\n")

    env = {
        "__name__":      "__main__",
        "_ku_beje":      _ku_beje,
        "random":        random,
        "math":          math,
    }
    env.update(_make_gui_env())

    try:
        exec(compile(translated, file_path, "exec"), env)
    except SyntaxError as e:
        print(f"\n[RojLang] Şaşiya Syntax li rêza {e.lineno}: {e.msg}")
        print(f"  → {e.text}")
        sys.exit(1)
    except SystemExit:
        pass
    except Exception:
        print("\n[RojLang] Şaşî:")
        traceback.print_exc()
        sys.exit(1)


def main():
    args = sys.argv[1:]
    debug = "--debug" in args
    if debug:
        args.remove("--debug")
    bijêre(args[0] if args else "test.ku", debug=debug)


if __name__ == "__main__":
    main()
