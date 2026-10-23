#!/usr/bin/env python3
"""KI als Test-Kind für den Python-12-Wochen-Kurs (nur Deutsch, lokal, nie im Deploy).

Claude spielt ein Kind, das NUR kennt, was der Kurs bis zu dieser Lektion gezeigt hat: die
Glossare der früheren Wochen und die bisherigen Lektionen dieser Woche (Text, Aufgaben,
Beispiele - keine Musterlösungen). Es liest die Lektion, versucht jede Aufgabe und sagt ehrlich,
was es nicht versteht. Danach führt das Skript den Code des Test-Kinds mit python3 aus und prüft
ihn wie die Website gegen `expected`.

Läuft über die `claude`-CLI (Claude-Code-Abo, kein API-Schlüssel nötig), ohne Werkzeuge und in
einem leeren Ordner, damit keine CLAUDE.md mitgelesen wird.

    python3 scripts/ki_testkind.py --wochen 1 --thema abenteuer --out bericht.md
    python3 scripts/ki_testkind.py --wochen 3 --lektion lektion-02 --alter 10
    python3 scripts/ki_testkind.py --wochen 2 --trocken            # nur den Prompt zeigen
    python3 scripts/ki_testkind.py --kurs microbit-ampel --variante python --alter 10

Mit --kurs prüft es einen Anleitungs-Kurs (engine "anleitung", micro:bit): Das Test-Kind arbeitet zu
zweit an der Hardware, kennt die Materialliste aus beschreibung.md, die Einführung "Erste Schritte"
und die bisherigen Stufen, sieht von Blöcken/Python/JavaScript nur die gewählte Variante und statt
der Steckplan-Bilder deren Beschreibung (alt). Ausgeführt wird nichts - für jeden Abhakpunkt sagt
es, ob es dort ohne Hilfe ankäme.

Ein Sprachmodell unterschätzt, wie schwer etwas für echte Kinder ist: Der Bericht ist ein
Vorfilter, kein Ersatz für Beobachten. Was das Test-Kind nicht schafft oder nicht versteht, ist
aber fast immer auch für Kinder ein Problem.
"""
import argparse
import ast
import json
import os
import re
import subprocess
import sys
import tempfile
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
MARKER = "@@UE-TESTKIND-AUFGABE@@"

SCHEMA = {
    "type": "object",
    "additionalProperties": False,
    "required": ["aufgaben", "schwere_woerter", "verwirrende_saetze", "gesamteindruck", "aendern"],
    "properties": {
        "aufgaben": {
            "type": "array",
            "items": {
                "type": "object",
                "additionalProperties": False,
                "required": ["nr", "verstanden", "was_ich_tun_soll", "code", "unklar"],
                "properties": {
                    "nr": {"type": "integer"},
                    "verstanden": {"type": "string", "enum": ["ja", "teilweise", "nein"]},
                    "was_ich_tun_soll": {"type": "string"},
                    "code": {"type": "string"},
                    "unklar": {"type": "string"},
                },
            },
        },
        "schwere_woerter": {"type": "array", "items": {"type": "string"}},
        "verwirrende_saetze": {"type": "array", "items": {"type": "string"}},
        "gesamteindruck": {"type": "string"},
        "aendern": {
            "type": "array",
            "items": {
                "type": "object",
                "additionalProperties": False,
                "required": ["stelle", "problem", "haette_geholfen", "gewicht"],
                "properties": {
                    "stelle": {"type": "string"},
                    "problem": {"type": "string"},
                    "haette_geholfen": {"type": "string"},
                    "gewicht": {"type": "string", "enum": ["hoch", "mittel"]},
                },
            },
        },
    },
}


def system_prompt(alter: int) -> str:
    return f"""Du spielst ein {alter}-jähriges Kind in einem Python-Kurs für Anfänger. Ein Kursleiter will
herausfinden, wo sein Material für Kinder zu schwer ist. Hilf ihm, indem du ehrlich so liest und
arbeitest, wie ein {alter}-jähriges Kind es täte.

- Du kennst NUR das, was im mitgelieferten Kursmaterial steht. Alles andere über Python weißt du
  nicht - auch wenn du es eigentlich weißt. Benutze keinen Befehl, kein Zeichen und keinen Trick,
  den das Material nicht gezeigt hat. Fehlt dir etwas, sag es unter "unklar".
- Du liest wie ein Kind in deinem Alter: Fachwörter und lange Sätze verwirren dich, Englisch
  verstehst du nur, wenn es erklärt wird. Nenne solche Wörter und Sätze wörtlich.
- Mach keine absichtlichen Fehler. Wenn eine Aufgabe unklar ist, mach das, was du am ehesten
  verstehst, und schreib dazu, was du dir gedacht hast.
- "was_ich_tun_soll": In eigenen, kindlichen Worten, was die Aufgabe von dir will.
- "code": Dein vollständiger Code für diese Aufgabe, so wie du ihn in den Editor tippen würdest
  (die Vorlage mit deinen Ergänzungen).
- "unklar": Was du nicht verstanden hast oder raten musstest. Leer lassen, wenn alles klar war.
- "gesamteindruck": Ein bis zwei Sätze: Wie ging es dir mit dieser Lektion?
- "aendern": Nur die Stellen, an denen ein echtes Kind in deinem Alter wahrscheinlich hängen
  bleibt, etwas falsch versteht oder raten muss - also wo sich eine Änderung wirklich lohnt.
  Lass Stellen weg, die nach dem ganzen Absatz, dem Beispiel oder der Vorlage doch klar werden,
  und einzelne schwere Wörter, die der Zusammenhang erklärt. Ist die Lektion insgesamt klar,
  bleibt die Liste leer. Je Eintrag: "stelle" (z. B. "Aufgabe 3" oder "Text, 2. Absatz"),
  "problem" (kurz, was du nicht verstanden hast), "haette_geholfen" (kurz, was dir geholfen
  hätte), "gewicht" ("hoch" = du wärst ohne Hilfe nicht weitergekommen, sonst "mittel")."""


def parse_markdown_cell(path: Path) -> str:
    return ast.parse(path.read_text(encoding="utf-8")).body[0].value.value


def glossary(content: Path, week: int, theme: str) -> str:
    d = content / "python-12-wochen-grundkurs" / f"woche-{week}" / theme / f"woche{week}_{theme}_0_glossar"
    cells = sorted(d.glob("*_markdown.py"), key=lambda p: int(p.name.split("_")[0])) if d.is_dir() else []
    return "\n\n".join(parse_markdown_cell(c) for c in cells)


def load_lessons(content: Path, week: int, theme: str) -> list[dict]:
    d = content / f"python-woche{week}-{theme}"
    lessons = json.loads((d / "lessons.json").read_text(encoding="utf-8"))
    for les in lessons:
        md = d / les["file"]
        les["_md"] = md.read_text(encoding="utf-8") if md.is_file() else ""
    return lessons


def render_lesson(les: dict) -> str:
    """So, wie ein Kind die Lektion sieht: Text, Beispiele, Aufgaben mit Vorlage."""
    parts = [les["_md"].strip()]
    for i, task in enumerate(les["tasks"], 1):
        kind = "Beispiel (schon fertig, nur ausführen)" if task.get("example") else "Aufgabe"
        parts.append(f"--- {kind} {i} ---\n{task['instruction']}")
        if task.get("codeTemplate", "").strip():
            parts.append(f"Vorlage im Editor:\n```python\n{task['codeTemplate'].rstrip()}\n```")
        stdin = task.get("validation", {}).get("stdin")
        if stdin and not task.get("example"):
            parts.append("Beim Prüfen wird automatisch eingegeben: " + ", ".join(map(str, stdin)))
    return "\n\n".join(parts)


def build_prompt(content: Path, week: int, theme: str, lessons: list[dict], index: int) -> str:
    earlier = [f"### Woche {w}\n{glossary(content, w, theme)}" for w in range(1, week)]
    this_week = [f"### {l['title']}\n{render_lesson(l)}" for l in lessons[:index]]
    les = lessons[index]
    numbers = [i for i, t in enumerate(les["tasks"], 1) if not t.get("example")]
    return "\n\n".join([
        "# Was du bisher im Kurs gelernt hast",
        "## Frühere Wochen (Glossar)" if earlier else "Das ist deine erste Woche.",
        *earlier,
        f"## Woche {week} bis jetzt" if this_week else "",
        *this_week,
        "# Die Lektion, die du jetzt machst",
        f"## {les['title']}",
        render_lesson(les),
        f"Bearbeite die Aufgaben {', '.join(map(str, numbers))} (Beispiele nicht). Antworte nur im verlangten JSON-Format.",
    ])


def ask_claude(prompt: str, system: str, schema: dict, model: str | None) -> dict:
    cmd = ["claude", "-p", "--tools", "", "--no-session-persistence", "--disable-slash-commands",
           "--system-prompt", system, "--output-format", "json",
           "--json-schema", json.dumps(schema)]
    if model:
        cmd += ["--model", model]
    with tempfile.TemporaryDirectory() as empty:
        proc = subprocess.run(cmd, input=prompt, capture_output=True, text=True, cwd=empty, timeout=900)
    if proc.returncode != 0:
        raise RuntimeError(f"claude fehlgeschlagen: {proc.stderr.strip() or proc.stdout.strip()}")
    data = json.loads(proc.stdout)
    if data.get("is_error") or "structured_output" not in data:
        raise RuntimeError(f"claude ohne Ergebnis: {data.get('result', '')[:300]}")
    answer = data["structured_output"]
    answer["_kosten_usd"] = data.get("total_cost_usd", 0)
    return answer


def normalize(s: str) -> str:
    """Wie normalizeForComparison() in src/composables/useTaskValidation.js."""
    return re.sub(r"[.,!?:;]+$", "", re.sub(r"\s+", " ", str(s or "").lower()).strip())


def output_ok(output: str, validation: dict) -> bool:
    expected = validation.get("expected")
    if expected is None:
        return True
    if validation.get("type") == "output_equals":
        return output.strip() == expected
    return normalize(expected) in normalize(output.strip())


def run_attempt(earlier_codes: list[str], code: str, validation: dict) -> tuple[bool, str]:
    """Führt den Code des Test-Kinds aus; frühere Aufgaben der Lektion laufen vorher mit (wie im
    selben Python-Kernel der Website), gezählt wird nur die Ausgabe nach der Markierung. Wie auf der
    Website bekommt nur die geprüfte Aufgabe `validation.stdin` - frühere input()-Aufrufe dürfen es
    nicht wegessen, sie bekommen Füll-Eingaben."""
    filler = "1\n" * 20
    own = "\n".join(map(str, validation.get("stdin") or [])) + "\n" + filler
    program = "\n".join(["import io as __io, sys as __sys", f"__sys.stdin = __io.StringIO({filler!r})", *earlier_codes,
                         f"__sys.stdin = __io.StringIO({own!r})", f"print({MARKER!r})", code])
    with tempfile.TemporaryDirectory() as work:
        try:
            proc = subprocess.run([sys.executable, "-I", "-c", program], capture_output=True,
                                  text=True, cwd=work, timeout=10, stdin=subprocess.DEVNULL)
        except subprocess.TimeoutExpired:
            return False, "Zeitüberschreitung (Endlosschleife?)"
    out = proc.stdout.split(MARKER, 1)[-1].lstrip("\n")
    if proc.returncode != 0:
        last = (proc.stderr.strip().splitlines() or ["Fehler"])[-1]
        return False, f"Fehler: {last}"
    return output_ok(out, validation), out.strip()[:200]


def evaluate(les: dict, answer: dict) -> list[dict]:
    by_nr = {a["nr"]: a for a in answer.get("aufgaben", [])}
    results, earlier = [], []
    for i, task in enumerate(les["tasks"], 1):
        if task.get("example"):
            earlier.append(task["codeTemplate"])
            continue
        attempt = by_nr.get(i)
        if not attempt:
            results.append({"nr": i, "fehlt": True})
            continue
        ok, out = run_attempt(earlier, attempt["code"], task.get("validation", {}))
        earlier.append(attempt["code"])
        results.append({**attempt, "geschafft": ok, "ausgabe": out, "erwartet": task.get("validation", {}).get("expected")})
    return results


# ---------------------------------------------------------------- Anleitungs-Kurse (micro:bit)

VARIANTEN = ("bloecke", "python", "javascript")
_AENDERN = SCHEMA["properties"]["aendern"]
GUIDE_SCHEMA = {
    "type": "object",
    "additionalProperties": False,
    "required": ["aufgaben", "schwere_woerter", "verwirrende_saetze", "gesamteindruck", "aendern"],
    "properties": {
        "aufgaben": {
            "type": "array",
            "items": {
                "type": "object",
                "additionalProperties": False,
                "required": ["nr", "schaffe_ich", "was_ich_tue", "unklar"],
                "properties": {
                    "nr": {"type": "integer"},
                    "schaffe_ich": {"type": "string", "enum": ["ja", "unsicher", "nein"]},
                    "was_ich_tue": {"type": "string"},
                    "unklar": {"type": "string"},
                },
            },
        },
        "schwere_woerter": {"type": "array", "items": {"type": "string"}},
        "verwirrende_saetze": {"type": "array", "items": {"type": "string"}},
        "gesamteindruck": {"type": "string"},
        "aendern": _AENDERN,
    },
}
VARIANT_NAMES = {"bloecke": "Blöcken in MakeCode", "python": "Python", "javascript": "JavaScript in MakeCode"}


def guide_system_prompt(alter: int, variante: str) -> str:
    return f"""Du spielst ein {alter}-jähriges Kind in einem micro:bit-Kurs. Du arbeitest zu zweit mit
einem anderen Kind an einem echten micro:bit; die Teile aus der Materialliste liegen vor euch, ein
Computer ist da. Ihr programmiert mit {VARIANT_NAMES[variante]}. Ein Kursleiter will herausfinden, wo
seine Anleitung für Kinder zu schwer ist. Hilf ihm, indem du ehrlich so liest, wie ein
{alter}-jähriges Kind es täte.

- Du kennst NUR das, was im mitgelieferten Material steht. Alles andere über micro:bit, Elektronik
  und Programmieren weißt du nicht - auch wenn du es eigentlich weißt.
- Bilder (Steckpläne, Fotos) siehst du hier als [Bild: Beschreibung]. Stell dir vor, du siehst das
  Bild. Bemängle nicht, dass ein Bild fehlt.
- Du kannst nichts ausprobieren. Geh jeden Schritt in Gedanken durch: Was steckst du, wohin
  klickst du, welchen Block oder welche Zeile nimmst du? Wo müsstest du raten oder einen
  Erwachsenen fragen?
- Fachwörter, lange Sätze und Englisch verwirren dich. Nenne solche Wörter und Sätze wörtlich.
- "aufgaben" sind die Abhakpunkte am Ende der Stufe (Nummern wie angegeben). "schaffe_ich": "ja",
  wenn ihr dort ohne Hilfe ankommt; "unsicher", wenn ihr raten müsst; "nein", wenn ihr ohne einen
  Erwachsenen nicht weiterkommt. "was_ich_tue": in eigenen, kindlichen Worten, wie ihr dorthin kommt.
  "unklar": was ihr nicht verstanden habt (leer, wenn alles klar war).
- "gesamteindruck": Ein bis zwei Sätze: Wie ging es euch mit dieser Stufe?
- "aendern": Nur die Stellen, an denen echte Kinder in deinem Alter wahrscheinlich hängen bleiben,
  etwas falsch stecken oder programmieren oder raten müssen - also wo sich eine Änderung wirklich
  lohnt. Lass Stellen weg, die nach dem ganzen Absatz, dem Bild oder dem Code doch klar werden, und
  einzelne schwere Wörter, die der Zusammenhang erklärt. Ist die Stufe insgesamt klar, bleibt die
  Liste leer. Je Eintrag: "stelle", "problem", "haette_geholfen" (je kurz) und "gewicht" ("hoch" =
  ohne Hilfe nicht weitergekommen, sonst "mittel")."""


_SECTION_RE = re.compile(r"^:::(bloecke|python|javascript)\s*\n(.*?)^:::\s*$", re.S | re.M)
_IMG_RE = re.compile(r'<img [^>]*alt="([^"]*)"[^>]*>')


def render_guide_text(md: str, variante: str) -> str:
    """Nur die gewählte Variante behalten (gibt es sie in der Stufe nicht: Blöcke), Bilder als Beschreibung."""
    present = {m[0] for m in _SECTION_RE.findall(md)}
    keep = variante if variante in present or not present else "bloecke"
    text = _SECTION_RE.sub(lambda m: m.group(2).strip() + "\n" if m.group(1) == keep else "", md)
    return _IMG_RE.sub(lambda m: f"[Bild: {m.group(1)}]", text).strip()


def load_guide(content: Path, kurs: str) -> tuple[str, list[dict]]:
    d = content / kurs
    lessons = json.loads((d / "lessons.json").read_text(encoding="utf-8"))
    for les in lessons:
        md = d / les["file"]
        les["_md"] = md.read_text(encoding="utf-8") if md.is_file() else ""
    desc = d / "beschreibung.md"
    return (desc.read_text(encoding="utf-8") if desc.is_file() else ""), lessons


def render_guide_lesson(les: dict, variante: str, with_tasks: bool = True) -> str:
    parts = [render_guide_text(les["_md"], variante)]
    if with_tasks:
        parts.append("Am Ende der Stufe hakt ihr ab:")
        for i, task in enumerate(les["tasks"], 1):
            parts.append(f"{i}. {task['instruction']}" + (" (Bonus, freiwillig)" if task.get("isBonus") else ""))
    return "\n\n".join(parts)


def build_guide_prompt(content: Path, kurs: str, variante: str, lessons: list[dict], index: int) -> str:
    desc, _ = load_guide(content, kurs)
    intro = []
    if kurs != "microbit-einfuehrung" and (content / "microbit-einfuehrung").is_dir():
        _, einf = load_guide(content, "microbit-einfuehrung")
        intro = ["## Schon gemacht: die Einführung „Erste Schritte“", *[f"### {l['title']}\n{render_guide_lesson(l, variante, False)}" for l in einf]]
    earlier = [f"### {l['title']}\n{render_guide_lesson(l, variante, False)}" for l in lessons[:index]]
    les = lessons[index]
    return "\n\n".join([
        "# Der Kurs", desc.strip(), *intro,
        "## Bisherige Stufen dieses Kurses" if earlier else "", *earlier,
        "# Die Stufe, die ihr jetzt macht", f"## {les['title']}", render_guide_lesson(les, variante),
        f"Geh die Abhakpunkte 1 bis {len(les['tasks'])} durch. Antworte nur im verlangten JSON-Format.",
    ])


def evaluate_guide(les: dict, answer: dict) -> list[dict]:
    by_nr = {a["nr"]: a for a in answer.get("aufgaben", [])}
    results = []
    for i, _task in enumerate(les["tasks"], 1):
        a = by_nr.get(i)
        results.append({"nr": i, "fehlt": True} if not a else {**a, "anleitung": True, "geschafft": a["schaffe_ich"] != "nein"})
    return results


def _cell(text) -> str:
    return " ".join(str(text or "").split()).replace("|", "\\|")


def change_rows(entries: list[dict]) -> list[dict]:
    """Was sich zu ändern lohnt: nicht geschaffte Aufgaben immer, dazu die Einträge aus `aendern`."""
    rows = []
    for e in entries:
        where = (e["woche"], e["id"], e["titel"])
        for r in e["ergebnisse"]:
            if r.get("fehlt"):
                rows.append((*where, f"Aufgabe {r['nr']}", "Test-Kind hat keine Lösung abgegeben", "", "hoch"))
            elif not r["geschafft"] and r.get("anleitung"):
                rows.append((*where, f"Abhaken {r['nr']}", f"ohne Hilfe nicht geschafft – {r.get('unklar') or r.get('was_ich_tue')}", "", "hoch"))
            elif not r["geschafft"]:
                problem = f"nicht geschafft: Ausgabe `{r['ausgabe']}` statt `{r['erwartet']}`"
                if r.get("unklar"):
                    problem += f" – {r['unklar']}"
                rows.append((*where, f"Aufgabe {r['nr']}", problem, "", "hoch"))
        for c in e["antwort"].get("aendern", []):
            rows.append((*where, c["stelle"], c["problem"], c["haette_geholfen"], c["gewicht"]))
    return [dict(zip(("woche", "id", "titel", "stelle", "problem", "hilfe", "gewicht"), r)) for r in rows]


def render_report(entries: list[dict], alter: int) -> str:
    rows = change_rows(entries)
    high = sum(1 for r in rows if r["gewicht"] == "hoch")
    clear = sum(1 for e in entries if not any(r["id"] == e["id"] and r["woche"] == e["woche"] for r in rows))
    cost = sum(e["antwort"].get("_kosten_usd", 0) for e in entries)
    out = [f"# KI-Test-Kind ({alter} Jahre)", "",
           f"{len(entries)} Lektionen geprüft, {clear} davon ohne Änderungsbedarf. "
           f"{len(rows)} Stellen lohnen eine Änderung, {high} davon wichtig (das Test-Kind wäre ohne Hilfe nicht weitergekommen).",
           f"Rechnerische Kosten (Listenpreis, im Abo enthalten): {cost:.2f} $. Einzelheiten je Aufgabe stehen in der .json-Datei daneben.", ""]
    if not rows:
        return "\n".join(out + ["Alles klar – nichts zu ändern."]) + "\n"
    out += [f"| {'Kurs' if entries and entries[0].get('kurs') else 'Woche'} | Lektion | Stelle | Problem | Hätte geholfen | Gewicht |",
            "|---|---|---|---|---|---|"]
    for r in rows:
        weight = "**hoch**" if r["gewicht"] == "hoch" else "mittel"
        out.append(f"| {r['woche']} | {_cell(r['id'])} – {_cell(r['titel'])} | {_cell(r['stelle'])} | "
                   f"{_cell(r['problem'])} | {_cell(r['hilfe'])} | {weight} |")
    return "\n".join(out) + "\n"


def parse_weeks(spec: str) -> list[int]:
    weeks = set()
    for part in spec.split(","):
        a, _, b = part.partition("-")
        weeks |= set(range(int(a), int(b or a) + 1))
    return sorted(weeks)


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--wochen", help="Python-12-Wochen-Kurs: z. B. 1, 1-3 oder 2,5")
    ap.add_argument("--kurs", help="Anleitungs-Kurs (Content-Ordner), z. B. microbit-ampel")
    ap.add_argument("--variante", default="bloecke", choices=VARIANTEN, help="bei --kurs: Blöcke (Standard), Python oder JavaScript")
    ap.add_argument("--thema", default="abenteuer", choices=["abenteuer", "pferde", "scifi"])
    ap.add_argument("--lektion", help="nur diese Lektions-ID (z. B. lektion-03)")
    ap.add_argument("--alter", type=int, default=11, help="Alter des Test-Kinds (Standard 11)")
    ap.add_argument("--modell", help="an claude --model weitergeben (Standard: wie in Claude Code)")
    ap.add_argument("--parallel", type=int, default=3, help="gleichzeitige Anfragen (Standard 3)")
    ap.add_argument("--out", help="Bericht in diese Datei (sonst stdout); Rohdaten daneben als .json")
    ap.add_argument("--trocken", action="store_true", help="nur den Prompt der ersten Lektion zeigen, nichts senden")
    ap.add_argument("--antworten", help=argparse.SUPPRESS)  # Tests: Ordner mit <woche>-<id>.json statt claude
    ap.add_argument("--content", default=str(ROOT / "content"), help=argparse.SUPPRESS)
    args = ap.parse_args(argv)
    content = Path(args.content)
    if bool(args.wochen) == bool(args.kurs):
        ap.error("genau eins von --wochen oder --kurs angeben")
    if args.kurs:
        return main_guide(args, content)

    jobs = []
    for week in parse_weeks(args.wochen):
        lessons = load_lessons(content, week, args.thema)
        for idx, les in enumerate(lessons):
            if args.lektion and les["id"] != args.lektion:
                continue
            if not any(not t.get("example") for t in les["tasks"]):
                continue
            jobs.append((week, lessons, idx))
    if not jobs:
        raise SystemExit("Keine passende Lektion gefunden.")

    if args.trocken:
        week, lessons, idx = jobs[0]
        print("=== System ===\n" + system_prompt(args.alter) + "\n\n=== Prompt ===\n" + build_prompt(content, week, args.thema, lessons, idx))
        return

    def work(job):
        week, lessons, idx = job
        les = lessons[idx]
        if args.antworten:
            answer = json.loads((Path(args.antworten) / f"{week}-{les['id']}.json").read_text(encoding="utf-8"))
        else:
            answer = ask_claude(build_prompt(content, week, args.thema, lessons, idx), system_prompt(args.alter), SCHEMA, args.modell)
        print(f"  Woche {week} {les['id']} fertig", file=sys.stderr)
        return {"woche": week, "thema": args.thema, "id": les["id"], "titel": les["title"],
                "antwort": answer, "ergebnisse": evaluate(les, answer)}

    print(f"{len(jobs)} Lektionen …", file=sys.stderr)
    with ThreadPoolExecutor(max_workers=max(1, args.parallel)) as pool:
        entries = list(pool.map(work, jobs))
    write_report(args, entries)


def main_guide(args, content: Path):
    _, lessons = load_guide(content, args.kurs)
    jobs = [i for i, l in enumerate(lessons) if not args.lektion or l["id"] == args.lektion]
    if not jobs:
        raise SystemExit("Keine passende Lektion gefunden.")
    system = guide_system_prompt(args.alter, args.variante)
    if args.trocken:
        print("=== System ===\n" + system + "\n\n=== Prompt ===\n" + build_guide_prompt(content, args.kurs, args.variante, lessons, jobs[0]))
        return

    def work(idx):
        les = lessons[idx]
        if args.antworten:
            answer = json.loads((Path(args.antworten) / f"{args.kurs}-{les['id']}.json").read_text(encoding="utf-8"))
        else:
            answer = ask_claude(build_guide_prompt(content, args.kurs, args.variante, lessons, idx), system, GUIDE_SCHEMA, args.modell)
        print(f"  {args.kurs} {les['id']} fertig", file=sys.stderr)
        return {"woche": f"{args.kurs} ({args.variante})", "kurs": args.kurs, "id": les["id"], "titel": les["title"],
                "antwort": answer, "ergebnisse": evaluate_guide(les, answer)}

    print(f"{len(jobs)} Stufen …", file=sys.stderr)
    with ThreadPoolExecutor(max_workers=max(1, args.parallel)) as pool:
        entries = list(pool.map(work, jobs))
    write_report(args, entries)


def write_report(args, entries):
    report = render_report(entries, args.alter)
    if args.out:
        Path(args.out).write_text(report, encoding="utf-8")
        Path(args.out).with_suffix(".json").write_text(json.dumps(entries, ensure_ascii=False, indent=1), encoding="utf-8")
        print(f"Bericht: {args.out}", file=sys.stderr)
    else:
        sys.stdout.write(report)


if __name__ == "__main__":
    os.environ.setdefault("PYTHONIOENCODING", "utf-8")
    main()
