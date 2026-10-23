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
    "required": ["aufgaben", "schwere_woerter", "verwirrende_saetze", "gesamteindruck"],
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
- "gesamteindruck": Ein bis zwei Sätze: Wie ging es dir mit dieser Lektion?"""


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


def ask_claude(prompt: str, alter: int, model: str | None) -> dict:
    cmd = ["claude", "-p", "--tools", "", "--no-session-persistence", "--disable-slash-commands",
           "--system-prompt", system_prompt(alter), "--output-format", "json",
           "--json-schema", json.dumps(SCHEMA)]
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
    selben Python-Kernel der Website), gezählt wird nur die Ausgabe nach der Markierung."""
    program = "\n".join(earlier_codes + [f"print({MARKER!r})", code])
    stdin = "\n".join(map(str, validation.get("stdin") or [])) + "\n" + "1\n" * 20
    with tempfile.TemporaryDirectory() as work:
        try:
            proc = subprocess.run([sys.executable, "-I", "-c", program], input=stdin, capture_output=True,
                                  text=True, cwd=work, timeout=10)
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


def render_report(entries: list[dict], alter: int) -> str:
    failed = sum(1 for e in entries for r in e["ergebnisse"] if r.get("fehlt") or not r.get("geschafft"))
    unclear = sum(1 for e in entries for r in e["ergebnisse"] if r.get("unklar") or r.get("verstanden") not in (None, "ja"))
    cost = sum(e["antwort"].get("_kosten_usd", 0) for e in entries)
    out = [f"# KI-Test-Kind ({alter} Jahre)", "",
           f"- **Aufgaben nicht geschafft:** {failed}",
           f"- **Aufgaben mit Unklarheiten:** {unclear}",
           f"- Rechnerische Kosten (Listenpreis, im Abo enthalten): {cost:.2f} $", ""]
    for e in entries:
        a = e["antwort"]
        out += ["", f"## Woche {e['woche']} · {e['thema']} · {e['id']} – {e['titel']}", "", f"> {a.get('gesamteindruck', '')}"]
        for r in e["ergebnisse"]:
            if r.get("fehlt"):
                out.append(f"- ❌ **Aufgabe {r['nr']}:** keine Antwort vom Test-Kind")
                continue
            mark = "✅" if r["geschafft"] else "❌"
            line = f"- {mark} **Aufgabe {r['nr']}** ({r['verstanden']} verstanden): {r['was_ich_tun_soll']}"
            if r.get("unklar"):
                line += f"\n  - Unklar: {r['unklar']}"
            if not r["geschafft"]:
                line += f"\n  - Ausgabe: `{r['ausgabe']}` – erwartet: `{r['erwartet']}`"
            out.append(line)
        if a.get("schwere_woerter"):
            out.append("- Schwere Wörter: " + ", ".join(f"„{w}“" for w in a["schwere_woerter"]))
        for s in a.get("verwirrende_saetze", []):
            out.append(f"- Verwirrender Satz: „{s}“")
    return "\n".join(out) + "\n"


def parse_weeks(spec: str) -> list[int]:
    weeks = set()
    for part in spec.split(","):
        a, _, b = part.partition("-")
        weeks |= set(range(int(a), int(b or a) + 1))
    return sorted(weeks)


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--wochen", required=True, help="z. B. 1, 1-3 oder 2,5")
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
            answer = ask_claude(build_prompt(content, week, args.thema, lessons, idx), args.alter, args.modell)
        print(f"  Woche {week} {les['id']} fertig", file=sys.stderr)
        return {"woche": week, "thema": args.thema, "id": les["id"], "titel": les["title"],
                "antwort": answer, "ergebnisse": evaluate(les, answer)}

    print(f"{len(jobs)} Lektionen …", file=sys.stderr)
    with ThreadPoolExecutor(max_workers=max(1, args.parallel)) as pool:
        entries = list(pool.map(work, jobs))
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
