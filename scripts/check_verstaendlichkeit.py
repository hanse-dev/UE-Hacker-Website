#!/usr/bin/env python3
"""Verstaendlichkeits-Bericht fuer den Python-12-Wochen-Kurs (nur Deutsch).

Wer den Stoff kann, merkt nicht mehr, welche Schritte er im Kopf ueberspringt. Dieses Skript
sucht die typischen Stellen, an denen Teilnehmende deshalb haengen bleiben:

1. **Nie gezeigt:** Die Musterloesung einer Aufgabe braucht einen Python-Baustein (z. B.
   `.upper()`, `//`, `print(end=)`), der bis dahin in keinem Lektionstext, Beispiel oder
   Code-Geruest vorkam. Steht er nur im Aufgabentext, wird er als "nur im Aufgabentext" markiert.
2. **Zu viel Neues:** Eine Lektion fuehrt mehr als MAX_NEW Bausteine auf einmal ein.
3. **Begriff zu frueh:** Ein Fachbegriff aus `content/begriffe.json` steht im Text einer Woche,
   bevor die Woche kommt, die ihn erklaert.
4. **Fachwoerter:** Erstes Auftreten von Fachwoertern wie "Integer" oder "Syntax" - dort muss
   eine Erklaerung stehen (das Skript zeigt nur die Stelle, pruefen muss ein Mensch).
5. **Lesbarkeit:** Saetze mit mehr als MAX_SENTENCE_WORDS Woertern und Lektionen mit hohem
   LIX-Wert (Lesbarkeitsindex: Wortanzahl je Satz + Anteil langer Woerter).

    python3 scripts/check_verstaendlichkeit.py                       # Bericht nach stdout
    python3 scripts/check_verstaendlichkeit.py --wochen 1-3 --out bericht.md
    python3 scripts/check_verstaendlichkeit.py --themen abenteuer --nur nie-gezeigt

Das Skript aendert nichts; es ist ein Bericht, kein Test, der fehlschlaegt.
"""
import argparse
import ast
import builtins
import json
import re
import sys
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
THEMES = ["abenteuer", "pferde", "scifi"]
MAX_NEW = 4
MAX_SENTENCE_WORDS = 20
MAX_LIX = 45
BUILTIN_NAMES = set(dir(builtins))
KNOWN_MODULES = {"random", "math", "time", "json", "os", "datetime", "string", "sys"}
# Begriffe, die der Kurs bewusst frueher benutzt, als begriffe.json sie verlinkt
# (print() & Co. heissen ab Woche 1 "Zauberformel (Funktion)", def kommt erst in Woche 5).
BEGRIFF_AB_WOCHE = {"Funktion": 1}
LITERAL_CONCEPTS = {"Liste [ ]", "Dictionary { : }", "Menge (set) { }", "Tupel ( , )"}

# Fachwoerter, die Kinder nicht kennen. Erstes Auftreten wird gemeldet (Wortanfang, Gross/klein egal).
FACHWOERTER = [
    "Integer", "String", "Float", "Boolean", "Datentyp", "Syntax", "Argument", "Parameter",
    "Index", "Indizes", "Iteration", "iterier", "Operator", "Operand", "Konkaten", "Rückgabewert",
    "Ausdruck", "Bezeichner", "Deklar", "Initialis", "Instanz", "Attribut", "Methode", "Konstruktor",
    "Modul", "Bibliothek", "Exception", "Traceback", "Schlüsselwort", "Keyword", "Modulo",
    "Verkett", "Einrückung", "Kontrollstruktur", "Funktionsaufruf", "Literal", "Typumwandlung",
    "konvertier", "Sequenz", "Objekt", "Klasse", "Vererbung", "Dictionary", "Tupel", "Slicing",
]

OP_NAMES = {
    ast.Add: "+", ast.Sub: "-", ast.Mult: "*", ast.Div: "/", ast.FloorDiv: "//", ast.Mod: "%",
    ast.Pow: "**",
}
CMP_NAMES = {
    ast.Eq: "==", ast.NotEq: "!=", ast.Lt: "<", ast.Gt: ">", ast.LtE: "<=", ast.GtE: ">=",
    ast.In: "in", ast.NotIn: "not in", ast.Is: "is", ast.IsNot: "is not",
}


# ---------------------------------------------------------------- Bausteine aus Code lesen

def _parse(code: str):
    """Ganzer Code, sonst Zeile fuer Zeile (Debug-Vorlagen und Schnipsel sind oft kaputt)."""
    try:
        return [ast.parse(code)]
    except SyntaxError:
        trees = []
        for line in code.split("\n"):
            stripped = line.strip().rstrip(":")
            for candidate in (line.strip(), stripped, stripped + ": pass"):
                try:
                    trees.append(ast.parse(candidate))
                    break
                except SyntaxError:
                    continue
        return trees


def concepts(code: str, loose: bool = False) -> set[str]:
    """loose=True fuer Erklaertexte: `sort(reverse=True)` ohne Punkt zaehlt auch als Methode."""
    found: set[str] = set()
    for tree in _parse(code):
        defined = {n.name for n in ast.walk(tree) if isinstance(n, (ast.FunctionDef, ast.ClassDef))}
        imported = {m: m for m in KNOWN_MODULES}  # Name im Code -> echter Modulname
        for n in ast.walk(tree):
            if isinstance(n, ast.Import):
                imported |= {a.asname or a.name: a.name for a in n.names}
        for n in ast.walk(tree):
            found |= _node_concepts(n, defined, imported, loose)
    return found


def _node_concepts(n, defined, imported, loose=False) -> set[str]:
    c: set[str] = set()
    if isinstance(n, ast.Call):
        f = n.func
        name = None
        if isinstance(f, ast.Name) and f.id in BUILTIN_NAMES and f.id not in defined:
            name = f"{f.id}()"
        elif isinstance(f, ast.Name) and loose and f.id not in defined:
            name = f".{f.id}()"
        elif isinstance(f, ast.Attribute):
            if isinstance(f.value, ast.Name) and f.value.id in imported:
                name = f"{imported[f.value.id]}.{f.attr}()"
            elif f.attr not in defined:
                name = f".{f.attr}()"
        if name:
            c.add(name)
            for kw in n.keywords:
                if kw.arg:
                    c.add(f"{name[:-1]}{kw.arg}=)")
        if any(isinstance(a, ast.Starred) for a in n.args):
            c.add("*-Entpacken beim Aufruf")
    elif isinstance(n, ast.If):
        c.add("if")
        if n.orelse:
            c.add("elif" if len(n.orelse) == 1 and isinstance(n.orelse[0], ast.If) else "else")
    elif isinstance(n, ast.IfExp):
        c.add("x if … else y (in einer Zeile)")
    elif isinstance(n, ast.For):
        c.add("for-Schleife")
        if isinstance(n.target, ast.Tuple):
            c.add("for a, b in …")
        if n.orelse:
            c.add("for … else")
    elif isinstance(n, ast.While):
        c.add("while-Schleife")
    elif isinstance(n, ast.Break):
        c.add("break")
    elif isinstance(n, ast.Continue):
        c.add("continue")
    elif isinstance(n, ast.Pass):
        c.add("pass")
    elif isinstance(n, ast.FunctionDef):
        c.add("def")
        if n.args.defaults or n.args.kw_defaults:
            c.add("Standardwert für Parameter")
        if n.args.vararg:
            c.add("*args")
        if n.args.kwarg:
            c.add("**kwargs")
        if n.returns or any(a.annotation for a in n.args.args):
            c.add("Typ-Hinweise")
    elif isinstance(n, ast.Return):
        c.add("return")
    elif isinstance(n, ast.Lambda):
        c.add("lambda")
    elif isinstance(n, ast.ClassDef):
        c.add("class")
        if n.bases:
            c.add("Vererbung class A(B)")
    elif isinstance(n, ast.Import):
        c |= {f"import {a.name}" for a in n.names}
    elif isinstance(n, ast.ImportFrom):
        c.add(f"from {n.module} import …")
    elif isinstance(n, ast.Try):
        c.add("try/except")
        if n.finalbody:
            c.add("finally")
    elif isinstance(n, ast.ExceptHandler) and n.type is not None:
        c.add("except Fehlerart")
    elif isinstance(n, ast.Raise):
        c.add("raise")
    elif isinstance(n, ast.With):
        c.add("with")
    elif isinstance(n, ast.Global):
        c.add("global")
    elif isinstance(n, ast.Assert):
        c.add("assert")
    elif isinstance(n, ast.Delete):
        c.add("del")
    elif isinstance(n, ast.AugAssign):
        c.add(f"{OP_NAMES.get(type(n.op), '?')}=")
    elif isinstance(n, ast.Assign):
        if any(isinstance(t, ast.Tuple) for t in n.targets):
            c.add("a, b = … (mehrere Variablen auf einmal)")
        if len(n.targets) > 1:
            c.add("a = b = …")
    elif isinstance(n, ast.BinOp):
        c.add(f"Rechenzeichen {OP_NAMES.get(type(n.op), '?')}")
    elif isinstance(n, ast.Compare):
        c |= {f"Vergleich {CMP_NAMES.get(type(op), '?')}" for op in n.ops}
        if len(n.ops) > 1:
            c.add("verketteter Vergleich a < b < c")
    elif isinstance(n, ast.BoolOp):
        c.add("and" if isinstance(n.op, ast.And) else "or")
    elif isinstance(n, ast.UnaryOp):
        if isinstance(n.op, ast.Not):
            c.add("not")
        elif isinstance(n.op, ast.USub) and not isinstance(n.operand, ast.Constant):
            c.add("Minus vor Variable")
    elif isinstance(n, ast.JoinedStr):
        c.add("f-String")
    elif isinstance(n, ast.FormattedValue) and n.format_spec is not None:
        c.add("Format im f-String {x:…}")
    elif isinstance(n, ast.Subscript):
        if isinstance(n.slice, ast.Slice):
            c.add("Slicing [a:b]")
            if n.slice.step is not None:
                c.add("Slicing mit Schritt [::n]")
        else:
            c.add("Zugriff mit [ ]")
            if isinstance(n.slice, ast.UnaryOp) and isinstance(n.slice.op, ast.USub):
                c.add("negativer Index [-1]")
    elif isinstance(n, ast.List):
        c.add("Liste [ ]")
    elif isinstance(n, ast.Dict):
        c.add("Dictionary { : }")
    elif isinstance(n, ast.Set):
        c.add("Menge (set) { }")
    elif isinstance(n, ast.Tuple) and isinstance(getattr(n, "ctx", None), ast.Load):
        c.add("Tupel ( , )")
    elif isinstance(n, (ast.ListComp, ast.SetComp, ast.GeneratorExp)):
        c.add("Listen-Abkürzung [x for x in …]")
    elif isinstance(n, ast.DictComp):
        c.add("Dictionary-Abkürzung {k: v for …}")
    elif isinstance(n, ast.Constant):
        if n.value is True or n.value is False:
            c.add("True/False")
        elif n.value is None:
            c.add("None")
        elif isinstance(n.value, float):
            c.add("Kommazahl (float)")
        elif isinstance(n.value, str) and "\n" in n.value:
            c.add("Zeilenumbruch im Text (\\n)")
    return c


# ---------------------------------------------------------------- Markdown zerlegen

CODE_BLOCK_RE = re.compile(r"```[a-zA-Z]*\n(.*?)```", re.S)
INLINE_CODE_RE = re.compile(r"`([^`\n]+)`")


MENTION_RE = re.compile(r"(?<![\w.])\.?([a-zA-Z_]\w*)\(")


def mentioned(text: str) -> set[str]:
    """Im Fliesstext genannte Aufrufe wie `extend(liste2)` oder "mit strip()": als Funktion und
    als Methode zaehlen, denn Erklaertexte lassen den Punkt oft weg."""
    names = MENTION_RE.findall(text)
    return {f"{n}()" for n in names} | {f".{n}()" for n in names}


def shown_in_markdown(md: str) -> set[str]:
    """Bausteine aus Code-Bloecken und Inline-Code. Inline-Schnipsel wie `{name}` oder `(x)` sind
    meist Teil einer Erklaerung, keine Mengen/Tupel - Literal-Bausteine zaehlen dort nicht."""
    found: set[str] = set()
    for block in CODE_BLOCK_RE.findall(md):
        found |= concepts(block, loose=True)
    rest = CODE_BLOCK_RE.sub("", md)
    for snippet in INLINE_CODE_RE.findall(rest):
        found |= concepts(snippet, loose=True) - LITERAL_CONCEPTS
    return found | mentioned(rest)


def prose(md: str) -> str:
    """Nur der Fliesstext: ohne Code, Ueberschriften, Tabellen, HTML, Emoji."""
    text = CODE_BLOCK_RE.sub("\n", md)
    text = INLINE_CODE_RE.sub(r"\1", text)
    lines = []
    for line in text.split("\n"):
        s = line.strip()
        if not s or s.startswith(("#", "|", "<", ">", "---")):
            lines.append("")
            continue
        s = re.sub(r"^([-*]|\d+\.)\s+", "", s)
        s = re.sub(r"\[([^\]]*)\]\([^)]*\)", r"\1", s)
        s = re.sub(r"[*_]{1,2}", "", s)
        lines.append(s)
    return "\n".join(lines)


WORD_RE = re.compile(r"[A-Za-zÄÖÜäöüß]+(?:-[A-Za-zÄÖÜäöüß]+)*")


def sentences(text: str) -> list[str]:
    out = []
    for para in re.split(r"\n\s*\n", text):
        # Listenpunkte und Zeilenumbrueche beenden auch einen Satz
        for line in para.split("\n"):
            for s in re.split(r"(?<=[.!?:;])\s+", line):
                if WORD_RE.search(s):
                    out.append(s.strip())
    return out


def lix(text: str) -> tuple[float, int]:
    sents = sentences(text)
    words = WORD_RE.findall(text)
    if not words or not sents:
        return 0.0, 0
    long_words = sum(1 for w in words if len(w) > 6)
    return len(words) / len(sents) + 100 * long_words / len(words), len(words)


# ---------------------------------------------------------------- Kurs laden

def load_week(content: Path, week: int, theme: str):
    lessons_dir = content / f"python-woche{week}-{theme}"
    lessons = json.loads((lessons_dir / "lessons.json").read_text(encoding="utf-8"))
    sol_dir = content / "python-12-wochen-grundkurs" / f"woche-{week}" / theme / f"woche{week}_{theme}_6_loesungen"
    cell = re.compile(r"(\d+)_code\.py$")
    files = sorted((f for f in sol_dir.glob("*_code.py")), key=lambda f: int(cell.search(f.name).group(1)))
    solutions = [f.read_text(encoding="utf-8") for f in files]
    real = [t for les in lessons for t in les["tasks"] if not t.get("example")]
    if len(real) != len(solutions):
        raise SystemExit(f"Woche {week} {theme}: {len(real)} Aufgaben, aber {len(solutions)} Lösungen")
    sol_iter = iter(solutions)
    for les in lessons:
        md_path = lessons_dir / les["file"]
        les["_md"] = md_path.read_text(encoding="utf-8") if md_path.is_file() else ""
        for t in les["tasks"]:
            t["_solution"] = None if t.get("example") else next(sol_iter)
    return lessons


def load_begriffe(content: Path):
    path = content / "begriffe.json"
    if not path.is_file():
        return []
    return [b for b in json.loads(path.read_text(encoding="utf-8")).get("python", [])
            if b.get("kurs") == "python-12-wochen-grundkurs"]


# ---------------------------------------------------------------- Pruefen

def analyse(content: Path, weeks: list[int], themes: list[str]):
    """Liefert Funde als dict: (woche, lektion, kategorie, text) -> {themen}."""
    findings = defaultdict(set)
    titles = {}
    begriffe = load_begriffe(content)
    for theme in themes:
        seen: set[str] = set()
        first_fach: set[str] = set()
        early_reported: set[str] = set()
        for week in range(1, max(weeks) + 1):
            lessons = load_week(content, week, theme)
            report = week in weeks
            for les in lessons:
                key = (week, les["id"])
                titles.setdefault(key, les["title"])
                md = les["_md"]

                # 2. Was diese Lektion neu zeigt (Text + Beispiele + Code-Geruest)
                shown = shown_in_markdown(md)
                for t in les["tasks"]:
                    shown |= concepts(t["codeTemplate"])
                new = shown - seen
                # Alle Vergleiche zusammen sind ein Thema, keine sechs
                families = {"Vergleiche" if c.startswith("Vergleich ") else c for c in new}
                if report and les["section"] == "lektion" and len(families) > MAX_NEW:
                    findings[key + ("zu-viel-neu", f"{len(families)} neue Bausteine auf einmal: " + ", ".join(sorted(families)))].add(theme)
                seen |= shown

                # 1. Was die Loesung zusaetzlich braucht
                for i, t in enumerate(les["tasks"], 1):
                    if t["_solution"] is None:
                        continue
                    missing = concepts(t["_solution"]) - seen
                    in_instruction = mentioned(t["instruction"])
                    for code in INLINE_CODE_RE.findall(t["instruction"]):
                        in_instruction |= concepts(code, loose=True)
                    if report:
                        for m in sorted(missing):
                            where = "nur im Aufgabentext" if m in in_instruction else "nirgends"
                            findings[key + ("nie-gezeigt", f"Aufgabe {i}: `{m}` – vorher {where} gezeigt")].add(theme)
                    # Ab jetzt gilt es als bekannt, sonst meldet jede spaetere Aufgabe es erneut
                    seen |= missing

                if not report:
                    continue
                texts = [("Lektionstext", prose(md))] + [(f"Aufgabe {i}", t["instruction"]) for i, t in enumerate(les["tasks"], 1)]

                # 3. Begriff vor seiner Woche
                # (je Begriff nur die erste Stelle, sonst wiederholt sich derselbe Fund jede Lektion)
                for b in begriffe:
                    if BEGRIFF_AB_WOCHE.get(b["begriff"], b["woche"]) <= week or b["begriff"] in early_reported:
                        continue
                    for label, text in texts:
                        hit = next((f for f in b["formen"] if re.search(rf"\b{re.escape(f)}\b", text)), None)
                        if hit:
                            early_reported.add(b["begriff"])
                            findings[key + ("begriff-zu-frueh", f"{label}: „{hit}“ – wird erst in Woche {b['woche']} erklärt")].add(theme)
                            break

                # 4. Erstes Auftreten von Fachwoertern
                for label, text in texts:
                    for s in sentences(text):
                        for fw in FACHWOERTER:
                            if fw in first_fach:
                                continue
                            # Gross/klein zaehlt: "klasse = …" ist ein Variablenname, kein Fachwort
                            pattern = re.escape(fw) if fw[0].isupper() else f"[{fw[0]}{fw[0].upper()}]{re.escape(fw[1:])}"
                            m = re.search(rf"\b({pattern}\w*)", s)
                            if m:
                                first_fach.add(fw)
                                findings[key + ("fachwort", f"{label}: erstes „{m.group(1)}“ – wird es hier erklärt? › {s}")].add(theme)

                # 5. Lesbarkeit
                for label, text in texts:
                    for s in sentences(text):
                        n = len(WORD_RE.findall(s))
                        if n > MAX_SENTENCE_WORDS:
                            findings[key + ("langer-satz", f"{label}: {n} Wörter › {s}")].add(theme)
                value, n_words = lix(texts[0][1])
                if n_words >= 40 and value > MAX_LIX:
                    findings[key + ("lix", f"Lektionstext: LIX {value:.0f} (Ziel ≤ {MAX_LIX}, {n_words} Wörter)")].add(theme)
    return findings, titles


KATEGORIEN = {
    "nie-gezeigt": "Lösung braucht etwas, das nie gezeigt wurde",
    "zu-viel-neu": "Zu viel Neues in einer Lektion",
    "begriff-zu-frueh": "Fachbegriff vor seiner Woche",
    "fachwort": "Erstes Auftreten eines Fachworts (Erklärung prüfen)",
    "langer-satz": f"Satz mit mehr als {MAX_SENTENCE_WORDS} Wörtern",
    "lix": "Schwer lesbarer Lektionstext",
}


def render(findings, titles, themes) -> str:
    counts = defaultdict(int)
    for (_, _, cat, _) in findings:
        counts[cat] += 1
    out = ["# Verständlichkeits-Bericht Python-Kurs", ""]
    out += [f"- **{KATEGORIEN[c]}:** {counts[c]}" for c in KATEGORIEN]
    out.append("")
    out.append("Steht hinter einem Fund kein Thema, betrifft er alle geprüften Themen.")
    by_lesson = defaultdict(list)
    for (week, lid, cat, text), th in findings.items():
        by_lesson[(week, lid)].append((list(KATEGORIEN).index(cat), cat, text, th))
    current_week = None
    for (week, lid) in sorted(by_lesson, key=lambda k: (k[0], list(titles).index(k))):
        if week != current_week:
            out += ["", f"## Woche {week}"]
            current_week = week
        out += ["", f"### {lid} – {titles[(week, lid)]}"]
        for _, cat, text, th in sorted(by_lesson[(week, lid)]):
            suffix = "" if len(th) == len(themes) else f" _({', '.join(sorted(th))})_"
            out.append(f"- [{cat}] {text}{suffix}")
    return "\n".join(out) + "\n"


def parse_weeks(spec: str) -> list[int]:
    weeks = set()
    for part in spec.split(","):
        a, _, b = part.partition("-")
        weeks |= set(range(int(a), int(b or a) + 1))
    return sorted(weeks)


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--wochen", default="1-12", help="z. B. 1-3 oder 1,4,7")
    ap.add_argument("--themen", default=",".join(THEMES))
    ap.add_argument("--nur", help="nur diese Kategorien (Komma-Liste): " + ", ".join(KATEGORIEN))
    ap.add_argument("--out", help="Bericht in diese Datei schreiben statt nach stdout")
    ap.add_argument("--content", default=str(ROOT / "content"), help=argparse.SUPPRESS)
    args = ap.parse_args(argv)

    themes = args.themen.split(",")
    findings, titles = analyse(Path(args.content), parse_weeks(args.wochen), themes)
    if args.nur:
        keep = set(args.nur.split(","))
        findings = {k: v for k, v in findings.items() if k[2] in keep}
    report = render(findings, titles, themes)
    if args.out:
        Path(args.out).write_text(report, encoding="utf-8")
        print(f"{len(findings)} Funde, Bericht: {args.out}")
    else:
        sys.stdout.write(report)


if __name__ == "__main__":
    main()
