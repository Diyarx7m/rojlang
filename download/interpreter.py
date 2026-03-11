import re
import sys
import os
import traceback
import random
import math


TRANSLATIONS = [
    (r'\bfonksîyon\b',  'def'),
    (r'\bfonksiyon\b',  'def'),

    (r'\bnivîs\b',      'print'),
    (r'\bnivis\b',      'print'),

    (r'\bbêje\b',       '_ku_beje'),
    (r'\bbeje\b',       '_ku_beje'),

    (r'\bxwestin\b',    'input'),

    (r'\bhilbijêre\b',  'random.randint'),
    (r'\bhilbijere\b',  'random.randint'),

    (r'\beger\b',       'if'),
    (r'\byan\b',        'else'),
    (r'\bdem\b',        'while'),
    (r'\bvegere\b',     'return'),
    (r'\bbo\b',         'for'),
    (r'\bdi\b',         'in'),

    (r'\brast\b',       'True'),

    (r'\bçewt\b',       'False'),
    (r'\bcewt\b',       'False'),

    (r'\bsinif\b',      'class'),
    (r'\bTune\b',       'None'),

    (r'\bnav\b\s+',     ''),

    (r'\bnîşe\b',       'pass'),
    (r'\bnise\b',       'pass'),

    (r'\bbişkîne\b',    'break'),
    (r'\bbiskine\b',    'break'),

    (r'\bberdewam\b',   'continue'),
    (r'\bderkev\b',     'exit()'),

    (r'\bne\b',         'not'),
    (r'\bû\b',          'and'),
    (r'\bu\b',          'and'),
    (r'\ban\b',         'or'),

    (r'\bdirêj\b',      'len'),
    (r'\bdirej\b',      'len'),

    (r'\bcure\b',       'type'),

    (r'\.têxe\b',       '.append'),
    (r'\.texe\b',       '.append'),

    (r'\bhejmar\b',         'int'),
    (r'\bnivîsok\b',        'str'),
    (r'\bnivisok\b',        'str'),
    (r'\bhejimarFloat\b',   'float'),

    (r'\bpêl\b',            'list'),
    (r'\bpel\b',            'list'),
    (r'\bferhenga\b',       'dict'),
    (r'\bkoma\b',           'set'),

    (r'\bnizim\b',          'min'),
    (r'\bmezin\b',          'max'),
    (r'\btomkirin\b',       'round'),
    (r'\bjimartina\b',      'sum'),
    (r'\bbijmare\b',        'range'),
    (r'\bşikeftin\b',       'abs'),
    (r'\bsikeftin\b',       'abs'),
    (r'\bmathSqrt\b',       'math.sqrt'),
    (r'\bmathPow\b',        'math.pow'),
    (r'\bmathPi\b',         'math.pi'),
    (r'\bhilbijêreFloat\b', 'random.uniform'),
    (r'\bhilbijereFloat\b', 'random.uniform'),

    (r'\bçap\b',            'print'),
    (r'\bcap\b',            'print'),

    (r'\bêşk\b',            'try'),
    (r'\besk\b',            'try'),
    (r'\bgirtin\b',         'except'),
    (r'\bdewam\b',          'finally'),
    (r'\bavêtin\b',         'raise'),
    (r'\bavitin\b',         'raise'),

    (r'\.jorê\(\)',        '.upper()'),
    (r'\.jore\(\)',        '.upper()'),
    (r'\.jêrê\(\)',        '.lower()'),
    (r'\.jere\(\)',        '.lower()'),
    (r'\.veqetîne\b',       '.split'),
    (r'\.veqetine\b',       '.split'),
    (r'\.biguhêze\b',       '.replace'),
    (r'\.biguhez\b',        '.replace'),
    (r'\.bibîne\b',         '.find'),
    (r'\.bibine\b',         '.find'),
    (r'\.xêz\(\)',         '.strip()'),
    (r'\.xez\(\)',         '.strip()'),
    (r'\.hejmarê\b',        '.count'),
    (r'\.hejmare\b',        '.count'),
    (r'\.bike\b',           '.join'),
    (r'\.jêbike\b',         '.remove'),
    (r'\.jebike\b',         '.remove'),
    (r'\.rêzkirin\(\)',     '.sort()'),
    (r'\.rezkirin\(\)',     '.sort()'),
    (r'\.berevajikirin\(\)','.reverse()'),

    (r'\bklavBiGire\b',     'klavBiGire'),
    (r'\bbilivîne\b',       'bilivîne'),
    (r'\bbilivine\b',       'bilivîne'),
    (r'\bbiguherêze_reng\b','biguherêze_reng'),
    (r'\bjêbike_item\b',    'jêbike_item'),
    (r'\bjebike_item\b',    'jêbike_item'),
    (r'\bpiştî\b',          'piştî'),
    (r'\bpistî\b',          'piştî'),
    (r'\bpeyam\b',          'peyam'),
    (r'\bbipirse\b',        'bipirse'),
    (r'\bwêne\b',            'wêne'),
    (r'\bwene\b',            'wêne'),
    (r'\bwêne_pîvandî\b',   'wêne_pîvandî'),
    (r'\bwene_pivandi\b',   'wêne_pîvandî'),
    (r'\bwêne_nîşan\b',     'wêne_nîşan'),
    (r'\bwene_nishan\b',    'wêne_nîşan'),
    (r'\bwêne_label\b',     'wêne_label'),
    (r'\bwene_label\b',     'wêne_label'),
    (r'\bdeng\b',            'deng'),
    (r'\bdeng_lêde\b',      'deng'),
    (r'\bdeng_leyide\b',    'deng'),
    (r'\bdeng_rawest\b',    'deng_rawest'),
    (r'\bdeng_dengdank\b',  'deng_dengdank'),
    (r'\bdeng_bilindî\b',   'deng_bilindî'),
    (r'\bdeng_bilindi\b',   'deng_bilindî'),
]

POST_FIXES = [
    (r'\belse\s+if\b',      'elif'),
    (r'(?m)(\S)[ \t]{2,}',  r'\1 '),
]


def _ku_beje(*args, **kwargs):

    kwargs.setdefault('end', '')
    print(*args, **kwargs)


def _make_gui_env():
    try:
        import tkinter as tk
    except ImportError:
        return {}

    def pencere(seri='RojLang ☀', pivan='600x450'):
        w = tk.Tk()
        w.title(seri)
        w.geometry(pivan)
        w.configure(bg='#0a0a0f')
        w.resizable(False, False)
        return w

    def _nishan(w):
        w.mainloop()

    def kevir(w, fireh=500, bilindi=400, pasreng='#0a0a0f'):
        c = tk.Canvas(w, width=fireh, height=bilindi,
                      bg=pasreng, highlightthickness=0)
        c.pack()
        return c

    def _cargosse(c, x1, y1, x2, y2, reng='#f0a500', sinor=''):
        c.create_rectangle(x1, y1, x2, y2, fill=reng, outline=sinor)

    def _xember(c, x1, y1, x2, y2, reng='#f0a500', sinor=''):
        c.create_oval(x1, y1, x2, y2, fill=reng, outline=sinor)

    def _xez(c, x1, y1, x2, y2, reng='#f0a500', sturi=2):
        c.create_line(x1, y1, x2, y2, fill=reng, width=sturi)

    def _niviskar(c, x, y, nivis, reng='#e8e8f0', mezinahi=14, font='Arial'):
        c.create_text(x, y, text=str(nivis), fill=reng, font=(font, mezinahi))

    def _biskojk(w, nivis, kar, reng='#f0a500', pasreng='#1a1a24'):
        b = tk.Button(w, text=nivis, command=kar,
                      fg=reng, bg=pasreng, activeforeground=pasreng,
                      activebackground=reng, relief='flat',
                      padx=14, pady=6, cursor='hand2', font=('Arial', 11))
        b.pack(pady=4)
        return b

    def _nav_cargosse(w, nivis, reng='#e8e8f0', pasreng='#111118', mezinahi=12):
        l = tk.Label(w, text=nivis, fg=reng, bg=pasreng,
                     font=('Arial', mezinahi))
        l.pack(pady=2)
        return l

    def _rengen_hevber(reng1, reng2, gav=10):
        def h2r(h):
            h = h.lstrip('#')
            return tuple(int(h[i:i+2], 16) for i in (0, 2, 4))
        def r2h(r, g, b):
            return f'#{int(r):02x}{int(g):02x}{int(b):02x}'
        r1, g1, b1 = h2r(reng1)
        r2, g2, b2 = h2r(reng2)
        return [r2h(
            r1 + (r2 - r1) * i / (gav - 1),
            g1 + (g2 - g1) * i / (gav - 1),
            b1 + (b2 - b1) * i / (gav - 1),
        ) for i in range(gav)]


    def _pistad(w, ms, fn):

        w.after(int(ms), fn)

    def _peyam(sernav='RojLang', nivis=''):
        from tkinter import messagebox as _mb
        _mb.showinfo(sernav, str(nivis))

    def _bipirse(sernav='RojLang ☀', nivis='Erê / Na?'):
        from tkinter import messagebox as _mb
        return _mb.askyesno(sernav, str(nivis))


    def _klav_bi_gire(w, klav, kar):

        w.bind(str(klav), kar)

    def _klav_bide(canvas_or_widget, klav, kar):
        canvas_or_widget.bind(str(klav), kar)

    def _klav_gişt(w, kar):

        w.bind("<KeyPress>", kar)

    _KLAV_CTRL   = "<Control-%s>".__mod__
    _KLAV_ALT    = "<Alt-%s>".__mod__
    _KLAV_SHIFT  = "<Shift-%s>".__mod__

    def _nivisa_enter(kar):
        return "<Return>"

    def _nivisa_escape(kar):
        return "<Escape>"

    def _nivisa_space(kar):
        return "<space>"

    def _bilivine(c, item_id, dx, dy):

        c.move(item_id, dx, dy)

    def _biguheze_reng(c, item_id, reng):

        try:    c.itemconfig(item_id, fill=reng)
        except: c.itemconfig(item_id, fg=reng)

    def _cargosse2(c, x1, y1, x2, y2, reng='#f0a500', sinor=''):

        return c.create_rectangle(x1, y1, x2, y2, fill=reng, outline=sinor)

    def _xember2(c, x1, y1, x2, y2, reng='#f0a500', sinor=''):

        return c.create_oval(x1, y1, x2, y2, fill=reng, outline=sinor)

    def _xez2(c, x1, y1, x2, y2, reng='#f0a500', sturi=2):

        return c.create_line(x1, y1, x2, y2, fill=reng, width=sturi)

    def _niviskar2(c, x, y, nivis, reng='#e8e8f0', mezinahi=14, font='Arial'):

        return c.create_text(x, y, text=str(nivis), fill=reng, font=(font, mezinahi))

    def _jebike_item(c, item_id):

        c.delete(item_id)

    def _wene_bar(path):
        try:
            from PIL import Image as _I, ImageTk as _IT
            return _IT.PhotoImage(_I.open(str(path)))
        except ImportError:
            import tkinter as _tk2
            return _tk2.PhotoImage(file=str(path))
        except Exception as _ex:
            print(f"[RojLang] wêne: {_ex}"); return None

    def _wene_pivandi(path, fireh=None, bilindi=None):
        try:
            from PIL import Image as _I, ImageTk as _IT
            _img = _I.open(str(path))
            if fireh and bilindi:
                _img = _img.resize((int(fireh), int(bilindi)))
            elif fireh:
                _r = int(fireh) / _img.width
                _img = _img.resize((int(fireh), int(_img.height * _r)))
            elif bilindi:
                _r = int(bilindi) / _img.height
                _img = _img.resize((int(_img.width * _r), int(bilindi)))
            return _IT.PhotoImage(_img)
        except Exception as _ex:
            print(f"[RojLang] wêne_pîvandî: {_ex} — pip install pillow")
            return None

    def _wene_nishan(canvas, x, y, img_ref, anchor_s='center'):
        if img_ref is None: return None
        return canvas.create_image(int(x), int(y), image=img_ref, anchor=anchor_s)

    def _wene_label(widget, img_ref):
        if img_ref is None: return None
        import tkinter as _tk2
        _lbl = _tk2.Label(widget, image=img_ref, bg='#0a0a0f')
        _lbl.image = img_ref; _lbl.pack(); return _lbl

    def _deng_lede(path, loop=False):
        try:
            import pygame as _pg
            if not _pg.get_init(): _pg.init()
            if not _pg.mixer.get_init(): _pg.mixer.init()
            _pg.mixer.music.load(str(path))
            _pg.mixer.music.play(-1 if loop else 0)
        except ImportError:
            print("[RojLang] deng: pip install pygame")
        except Exception as _ex:
            print(f"[RojLang] deng: {_ex}")

    def _deng_dengdank(path):
        try:
            import pygame as _pg
            if not _pg.get_init(): _pg.init()
            if not _pg.mixer.get_init(): _pg.mixer.init()
            _snd = _pg.mixer.Sound(str(path)); _snd.play(); return _snd
        except ImportError:
            print("[RojLang] deng_dengdank: pip install pygame")
        except Exception as _ex:
            print(f"[RojLang] deng_dengdank: {_ex}")

    def _deng_rawest():
        try:
            import pygame as _pg; _pg.mixer.music.stop()
        except: pass

    def _deng_bilindi(vol):
        try:
            import pygame as _pg; _pg.mixer.music.set_volume(float(vol))
        except: pass

    return {
        'pencere':              pencere,
        'nîşan':                _nishan,
        'kevir':                kevir,
        'çargoşe':              _cargosse2,
        'xember':               _xember2,
        'xêz':                  _xez2,
        'nivîskar':             _niviskar2,
        'bişkojk':              _biskojk,
        'nav_çargoşe':          _nav_cargosse,
        'rengên_hevber':        _rengen_hevber,
        'piştî':                _pistad,
        'peyam':                _peyam,
        'bipirse':              _bipirse,
        'klavBiGire':           _klav_bi_gire,
        'klav_bide':            _klav_bide,
        'klavGişt':             _klav_gişt,
        'bilivîne':             _bilivine,
        'biguherêze_reng':      _biguheze_reng,
        'jêbike_item':          _jebike_item,
        'wêne':                 _wene_bar,
        'wene':                 _wene_bar,
        'wêne_pîvandî':         _wene_pivandi,
        'wene_pivandi':         _wene_pivandi,
        'wêne_nîşan':           _wene_nishan,
        'wene_nishan':          _wene_nishan,
        'wêne_label':           _wene_label,
        'wene_label':           _wene_label,
        'deng':                 _deng_lede,
        'deng_lêde':            _deng_lede,
        'deng_leyide':          _deng_lede,
        'deng_rawest':          _deng_rawest,
        'deng_dengdank':        _deng_dengdank,
        'deng_bilindî':         _deng_bilindi,
        'deng_bilindi':         _deng_bilindi,
        'nishan':               _nishan,
        'cargose':              _cargosse2,
        'xez':                  _xez2,
        'niviskar':             _niviskar2,
        'biskojk':              _biskojk,
        'nav_cargose':          _nav_cargosse,
        'rengen_hevber':        _rengen_hevber,
        'pistî':                _pistad,
        'bilivine':             _bilivine,
        'biguhereze_reng':      _biguheze_reng,
        'jebike_item':          _jebike_item,
    }


def _inject_globals(code: str) -> str:

    import re as _re

    lines = code.splitlines(keepends=True)

    asgn = _re.compile(r'^([\w\u00C0-\u024F\u0600-\u06FF]+)\s*(?:[+\-*/%&|^]?=)(?!=)', _re.UNICODE)
    global_names: set = set()
    for ln in lines:
        s = ln.lstrip()
        if len(ln) - len(s) == 0:
            if not _re.match(r'(def|class|if|elif|else|for|while|try|except|finally|with|import|from|@|#)', s):
                m = asgn.match(s)
                if m:
                    global_names.add(m.group(1))

    if not global_names:
        return code

    result   = []
    i        = 0
    n        = len(lines)
    func_re  = _re.compile(r'^( *)def\s+([\w\u00C0-\u024F]+)', _re.UNICODE)

    while i < n:
        ln = lines[i]
        fm = func_re.match(ln)
        if not fm:
            result.append(ln)
            i += 1
            continue

        func_base_indent = len(fm.group(1))
        result.append(ln)
        i += 1

        body_indent = func_base_indent + 4
        for j in range(i, n):
            s2 = lines[j].lstrip()
            if s2 and not s2.startswith('#'):
                body_indent = len(lines[j]) - len(s2)
                break

        body_lines = []
        while i < n:
            bln  = lines[i]
            bs   = bln.lstrip()
            bind = len(bln) - len(bs)
            if bs == '' or bs.startswith('#'):
                body_lines.append(bln)
                i += 1
                continue
            if bind <= func_base_indent:
                break
            body_lines.append(bln)
            i += 1

        needs_global = set()
        for bln in body_lines:
            bs = bln.lstrip()
            if bs.startswith(('#', 'def ', 'class ')):
                continue
            m2 = asgn.match(bs)
            if m2 and m2.group(1) in global_names:
                needs_global.add(m2.group(1))

        if needs_global:
            prefix   = ' ' * body_indent
            g_stmt   = prefix + 'global ' + ', '.join(sorted(needs_global)) + '\n'
            result.append(g_stmt)

        result.extend(body_lines)

    return ''.join(result)


def wergerine(source):

    strings_saved  = []
    comments_saved = []

    def save_str(m):
        strings_saved.append(m.group(0))
        return f'__ROJSTR{len(strings_saved) - 1}__'

    code = re.sub(
        r'("""[\s\S]*?"""|\'\'\'[\s\S]*?\'\'\'|'
        r'"[^"\n\\]*(?:\\.[^"\n\\]*)*"|'
        r"'[^'\n\\]*(?:\\.[^'\n\\]*)*')",
        save_str, source
    )

    def save_com(m):
        comments_saved.append(m.group(0))
        return f'__ROJCOM{len(comments_saved) - 1}__'

    code = re.sub(r'#[^\n]*', save_com, code)

    for pattern, replacement in TRANSLATIONS:
        code = re.sub(pattern, replacement, code)
    for pattern, replacement in POST_FIXES:
        code = re.sub(pattern, replacement, code)

    code = _inject_globals(code)

    for i, s in enumerate(strings_saved):
        code = code.replace(f'__ROJSTR{i}__', s)
    for i, c in enumerate(comments_saved):
        code = code.replace(f'__ROJCOM{i}__', c)

    return code

wergerîne = wergerine


def bijere(file_path, debug=False):
    if sys.platform == "win32":
        try:
            sys.stdout.reconfigure(encoding="utf-8", errors="replace")
            sys.stderr.reconfigure(encoding="utf-8", errors="replace")
        except AttributeError:
            pass

    if not file_path.endswith('.ku'):
        print(f"[RojLang] Sasi: '{file_path}' naye qebulkirin, pel dive bi .ku biqede")
        sys.exit(1)

    if not os.path.isfile(file_path):
        print(f"[RojLang] Sasi: Pel '{file_path}' nehat ditin")
        sys.exit(1)

    with open(file_path, 'r', encoding='utf-8') as f:
        source = f.read()

    translated = wergerine(source)

    if debug:
        sep = '-' * 58
        print(f'\n{sep}\n  [DEBUG] translated output:\n{sep}')
        for i, ln in enumerate(translated.splitlines(), 1):
            print(f'  {i:>4} | {ln}')
        print(f'{sep}\n')

    env = {
        '__name__': '__main__',
        '_ku_beje': _ku_beje,
        'random':   random,
        'math':     math,
    }
    env.update(_make_gui_env())

    try:
        compiled = compile(translated, file_path, 'exec')
        exec(compiled, env)
    except SyntaxError as e:
        ln   = e.lineno or 0
        text = e.text or ""
        src_lines = source.splitlines()
        ku_line = src_lines[ln-1].strip() if 0 < ln <= len(src_lines) else text.strip()
        print(f'\n[RojLang] !! Sasiya Syntax li reza {ln}:')
        print(f'  >> {ku_line}')
        print(f'  ({e.msg})')
        sys.exit(1)
    except SystemExit:
        pass
    except Exception as e:
        tb = traceback.extract_tb(sys.exc_info()[2])
        src_lines = source.splitlines()
        ku_frame = None
        for frame in tb:
            if frame.filename == file_path:
                ku_frame = frame
        if ku_frame:
            ln = ku_frame.lineno
            ku_line = src_lines[ln-1].strip() if 0<ln<=len(src_lines) else ""
            print(f'\n[RojLang] !! Sasi li reza {ln}:')
            print(f'  >> {ku_line}')
            print(f'  ({type(e).__name__}: {e})')
        else:
            print(f'\n[RojLang] !! Sasi: {type(e).__name__}: {e}')
        sys.exit(1)


bijêre = bijere


def main():
    args = sys.argv[1:]
    debug = '--debug' in args
    if debug:
        args.remove('--debug')
    bijere(args[0] if args else 'test.ku', debug=debug)


if __name__ == '__main__':
    main()
