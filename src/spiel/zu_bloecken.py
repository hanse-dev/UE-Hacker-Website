"""Uebersetzt ein Spiel-Programm (Python) in Blockly-Bloecke (JSON fuer Blockly.serialization).

So gibt es fuer jede Aufgabe nur EINE Quelle: Vorlage und Loesung stehen als Python in
lessons.json, die Blocks-Ansicht erzeugt daraus ihre Bloecke (src/composables/useSpiel.js ruft
`zu_bloecken()` in Pyodide auf). Unterstuetzt wird genau der Sprachumfang, fuer den es Bloecke gibt
(src/spiel/bloecke.js); alles andere wirft einen ValueError mit Zeilennummer - der Test
`tests/spiel-ausweichen.spec.js` uebersetzt jede Vorlage und Loesung und faellt dann auf.
"""

import ast
import json

EIGENSCHAFTEN = ("x", "y", "breite", "hoehe", "farbe")
VERGLEICHE = {ast.Eq: "EQ", ast.NotEq: "NEQ", ast.Lt: "LT", ast.LtE: "LTE", ast.Gt: "GT", ast.GtE: "GTE"}
RECHNEN = {ast.Add: "ADD", ast.Sub: "MINUS", ast.Mult: "MULTIPLY", ast.Div: "DIVIDE", ast.Pow: "POWER"}
ANWEISUNGEN = {"zeige": "spiel_zeige", "spiel_ende": "spiel_ende"}


class _Uebersetzer:
    def __init__(self):
        self.variablen = []

    def fehler(self, knoten, was):
        return ValueError(f"Zeile {getattr(knoten, 'lineno', '?')}: {was} gibt es nicht als Block")

    def var(self, name):
        if name not in self.variablen:
            self.variablen.append(name)
        return {"id": "v_" + name}

    # ------------------------------------------------------------------ Anweisungen

    def kette(self, anweisungen):
        """Liste von Anweisungen -> erster Block mit `next`-Kette (oder None)."""
        bloecke = []
        for a in anweisungen:
            block = self.anweisung(a)
            if block is not None:
                bloecke.append(block)
        for vorne, hinten in zip(bloecke, bloecke[1:]):
            vorne["next"] = {"block": hinten}
        return bloecke[0] if bloecke else None

    def mit_inhalt(self, block, name, anweisungen):
        inhalt = self.kette(anweisungen)
        if inhalt is not None:
            block.setdefault("inputs", {})[name] = {"block": inhalt}
        return block

    def anweisung(self, k):
        if isinstance(k, (ast.Pass, ast.Global, ast.Import, ast.ImportFrom)):
            return None
        if isinstance(k, ast.Assign) and len(k.targets) == 1:
            ziel = k.targets[0]
            if isinstance(ziel, ast.Name):
                return {"type": "variables_set", "fields": {"VAR": self.var(ziel.id)},
                        "inputs": {"VALUE": {"block": self.ausdruck(k.value)}}}
            if self.ist_eigenschaft(ziel):
                return {"type": "spiel_setze",
                        "fields": {"EIG": ziel.attr, "VAR": self.var(ziel.value.id)},
                        "inputs": {"WERT": {"block": self.ausdruck(k.value)}}}
        if isinstance(k, ast.AugAssign) and isinstance(k.op, (ast.Add, ast.Sub)):
            wert = self.ausdruck(k.value)
            if isinstance(k.op, ast.Sub):
                wert = self.negiert(k.value, wert)
            if isinstance(k.target, ast.Name):
                return {"type": "math_change", "fields": {"VAR": self.var(k.target.id)},
                        "inputs": {"DELTA": {"block": wert}}}
            if self.ist_eigenschaft(k.target):
                return {"type": "spiel_aendere",
                        "fields": {"EIG": k.target.attr, "VAR": self.var(k.target.value.id)},
                        "inputs": {"WERT": {"block": wert}}}
        if isinstance(k, ast.If):
            return self.wenn(k)
        if isinstance(k, ast.For) and not k.orelse:
            if (isinstance(k.iter, ast.Call) and isinstance(k.iter.func, ast.Name)
                    and k.iter.func.id == "range" and len(k.iter.args) == 1):
                block = {"type": "controls_repeat_ext",
                         "inputs": {"TIMES": {"block": self.ausdruck(k.iter.args[0])}}}
                return self.mit_inhalt(block, "DO", k.body)
            if isinstance(k.target, ast.Name):
                block = {"type": "controls_forEach", "fields": {"VAR": self.var(k.target.id)},
                         "inputs": {"LIST": {"block": self.ausdruck(k.iter)}}}
                return self.mit_inhalt(block, "DO", k.body)
        if isinstance(k, ast.Expr) and isinstance(k.value, ast.Call):
            return self.aufruf_anweisung(k.value)
        raise self.fehler(k, f"„{ast.unparse(k).splitlines()[0]}“")

    def wenn(self, k):
        bedingungen, koerper = [], []
        sonst = None
        while True:
            bedingungen.append(k.test)
            koerper.append(k.body)
            if len(k.orelse) == 1 and isinstance(k.orelse[0], ast.If):
                k = k.orelse[0]
                continue
            sonst = k.orelse or None
            break
        block = {"type": "controls_if", "inputs": {}}
        if len(bedingungen) > 1 or sonst:
            block["extraState"] = {}
            if len(bedingungen) > 1:
                block["extraState"]["elseIfCount"] = len(bedingungen) - 1
            if sonst:
                block["extraState"]["hasElse"] = True
        for i, (bed, inhalt) in enumerate(zip(bedingungen, koerper)):
            block["inputs"][f"IF{i}"] = {"block": self.ausdruck(bed)}
            self.mit_inhalt(block, f"DO{i}", inhalt)
        if sonst:
            self.mit_inhalt(block, "ELSE", sonst)
        return block

    def aufruf_anweisung(self, c):
        f = c.func
        if isinstance(f, ast.Name) and f.id in ANWEISUNGEN and len(c.args) <= 1 and not c.keywords:
            block = {"type": ANWEISUNGEN[f.id]}
            if c.args:
                block["inputs"] = {"TEXT": {"block": self.ausdruck(c.args[0])}}
            return block
        if isinstance(f, ast.Name) and f.id == "hintergrund" and len(c.args) == 1:
            return {"type": "spiel_hintergrund", "fields": {"FARBE": self.farbname(c.args[0])}}
        if isinstance(f, ast.Name) and f.id == "print" and len(c.args) == 1:
            return {"type": "text_print", "inputs": {"TEXT": {"block": self.ausdruck(c.args[0])}}}
        if isinstance(f, ast.Attribute) and isinstance(f.value, ast.Name):
            if f.attr == "append" and len(c.args) == 1:
                return {"type": "spiel_liste_add", "fields": {"VAR": self.var(f.value.id)},
                        "inputs": {"WERT": {"block": self.ausdruck(c.args[0])}}}
            if f.attr == "entferne" and not c.args:
                return {"type": "spiel_entferne", "fields": {"VAR": self.var(f.value.id)}}
        raise self.fehler(c, f"„{ast.unparse(c)}“")

    # ------------------------------------------------------------------ Ausdruecke

    def ist_eigenschaft(self, k):
        return isinstance(k, ast.Attribute) and isinstance(k.value, ast.Name) and k.attr in EIGENSCHAFTEN

    def zahl(self, wert):
        return {"type": "math_number", "fields": {"NUM": wert}}

    def negiert(self, knoten, block):
        """Fuer `x -= 5`: der Block "aendere um" bekommt -5."""
        if isinstance(knoten, ast.Constant) and isinstance(knoten.value, (int, float)):
            return self.zahl(-knoten.value)
        return {"type": "math_arithmetic", "fields": {"OP": "MINUS"},
                "inputs": {"A": {"block": self.zahl(0)}, "B": {"block": block}}}

    def farbname(self, k):
        if isinstance(k, ast.Constant) and isinstance(k.value, str):
            return k.value
        raise self.fehler(k, "Eine Farbe, die kein fester Text ist,")

    def ist_text(self, k):
        return ((isinstance(k, ast.Constant) and isinstance(k.value, str))
                or (isinstance(k, ast.Call) and isinstance(k.func, ast.Name) and k.func.id == "str")
                or (isinstance(k, ast.BinOp) and isinstance(k.op, ast.Add)
                    and (self.ist_text(k.left) or self.ist_text(k.right))))

    def textteile(self, k):
        if isinstance(k, ast.BinOp) and isinstance(k.op, ast.Add) and self.ist_text(k):
            return self.textteile(k.left) + self.textteile(k.right)
        if isinstance(k, ast.Call) and isinstance(k.func, ast.Name) and k.func.id == "str" and len(k.args) == 1:
            return [k.args[0]]
        return [k]

    def ausdruck(self, k):
        if isinstance(k, ast.Constant):
            if isinstance(k.value, bool):
                return {"type": "logic_boolean", "fields": {"BOOL": "TRUE" if k.value else "FALSE"}}
            if isinstance(k.value, (int, float)):
                return self.zahl(k.value)
            if isinstance(k.value, str):
                return {"type": "text", "fields": {"TEXT": k.value}}
        if isinstance(k, ast.UnaryOp):
            if isinstance(k.op, ast.USub) and isinstance(k.operand, ast.Constant) \
                    and isinstance(k.operand.value, (int, float)):
                return self.zahl(-k.operand.value)
            if isinstance(k.op, ast.Not):
                return {"type": "logic_negate", "inputs": {"BOOL": {"block": self.ausdruck(k.operand)}}}
        if isinstance(k, ast.Name):
            return {"type": "variables_get", "fields": {"VAR": self.var(k.id)}}
        if self.ist_eigenschaft(k):
            return {"type": "spiel_eigenschaft", "fields": {"EIG": k.attr, "VAR": self.var(k.value.id)}}
        if isinstance(k, ast.BinOp) and self.ist_text(k):
            teile = self.textteile(k)
            return {"type": "text_join", "extraState": {"itemCount": len(teile)},
                    "inputs": {f"ADD{i}": {"block": self.ausdruck(t)} for i, t in enumerate(teile)}}
        if isinstance(k, ast.BinOp) and type(k.op) in RECHNEN:
            return {"type": "math_arithmetic", "fields": {"OP": RECHNEN[type(k.op)]},
                    "inputs": {"A": {"block": self.ausdruck(k.left)}, "B": {"block": self.ausdruck(k.right)}}}
        if isinstance(k, ast.Compare) and len(k.ops) == 1 and type(k.ops[0]) in VERGLEICHE:
            return {"type": "logic_compare", "fields": {"OP": VERGLEICHE[type(k.ops[0])]},
                    "inputs": {"A": {"block": self.ausdruck(k.left)},
                               "B": {"block": self.ausdruck(k.comparators[0])}}}
        if isinstance(k, ast.BoolOp):
            op = "AND" if isinstance(k.op, ast.And) else "OR"
            block = self.ausdruck(k.values[0])
            for weiter in k.values[1:]:
                block = {"type": "logic_operation", "fields": {"OP": op},
                         "inputs": {"A": {"block": block}, "B": {"block": self.ausdruck(weiter)}}}
            return block
        if isinstance(k, ast.List):
            if not k.elts:
                return {"type": "lists_create_empty"}
            return {"type": "lists_create_with", "extraState": {"itemCount": len(k.elts)},
                    "inputs": {f"ADD{i}": {"block": self.ausdruck(e)} for i, e in enumerate(k.elts)}}
        if isinstance(k, ast.Call) and not k.keywords:
            return self.aufruf_ausdruck(k)
        raise self.fehler(k, f"„{ast.unparse(k)}“")

    def aufruf_ausdruck(self, c):
        f, args = c.func, c.args
        if isinstance(f, ast.Name):
            if f.id == "figur" and len(args) == 5:
                block = {"type": "spiel_figur", "fields": {"FARBE": self.farbname(args[4])}, "inputs": {}}
                for name, wert in zip(("X", "Y", "B", "H"), args[:4]):
                    block["inputs"][name] = {"block": self.ausdruck(wert)}
                return block
            if f.id == "taste" and len(args) == 1:
                return {"type": "spiel_taste", "fields": {"TASTE": self.farbname(args[0])}}
            if f.id == "zufall" and len(args) == 2:
                return {"type": "spiel_zufall", "inputs": {"VON": {"block": self.ausdruck(args[0])},
                                                           "BIS": {"block": self.ausdruck(args[1])}}}
            if f.id == "len" and len(args) == 1:
                return {"type": "lists_length", "inputs": {"VALUE": {"block": self.ausdruck(args[0])}}}
            if f.id == "str" and len(args) == 1:
                return {"type": "text_join", "extraState": {"itemCount": 1},
                        "inputs": {"ADD0": {"block": self.ausdruck(args[0])}}}
        if (isinstance(f, ast.Attribute) and f.attr == "beruehrt" and isinstance(f.value, ast.Name)
                and len(args) == 1 and isinstance(args[0], ast.Name)):
            return {"type": "spiel_beruehrt", "fields": {"A": self.var(f.value.id), "B": self.var(args[0].id)}}
        raise self.fehler(c, f"„{ast.unparse(c)}“")


def zu_bloecken(quelltext):
    """Python-Quelltext -> Blockly-JSON (als Text). Wirft ValueError bei nicht uebersetzbarem Code."""
    baum = ast.parse(quelltext)
    u = _Uebersetzer()
    start, bild = [], None
    for k in baum.body:
        if isinstance(k, ast.FunctionDef):
            if k.name != "jedes_bild" or k.args.args or bild is not None:
                raise u.fehler(k, f"Die Funktion „{k.name}“")
            bild = k
        else:
            start.append(k)
    # "beim Start" gibt es immer - auch leer ist er der Ort, an den die Kinder Bloecke ziehen.
    oben = [u.mit_inhalt({"type": "spiel_start"}, "DO", start)]
    if bild is not None:
        oben.append(u.mit_inhalt({"type": "spiel_jedes_bild"}, "DO", bild.body))
    for i, block in enumerate(oben):
        block["x"], block["y"] = 20, 20 + 300 * i
    return json.dumps({
        "blocks": {"languageVersion": 0, "blocks": oben},
        "variables": [{"name": n, "id": "v_" + n} for n in u.variablen],
    }, ensure_ascii=False)
