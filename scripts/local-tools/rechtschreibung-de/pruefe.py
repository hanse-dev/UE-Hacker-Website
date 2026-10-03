#!/usr/bin/env python3
"""Deutsche Rechtschreibprüfung für den Content — nur macOS, läuft nie im Deploy.

cspell (`npm run lint:spelling`) lässt bei Deutsch zu viel durch (das Wörterbuch erlaubt
beliebige Wortzusammensetzungen, "wiederspiegeln"/"strasse" gelten als richtig). Dieses Skript
zieht den deutschen Fließtext ohne Code aus dem Content und prüft ihn mit der macOS-eigenen
Rechtschreibprüfung (NSSpellChecker, `check.swift`).

    npm run lint:spelling:de           # neue unbekannte Wörter mit Fundstelle
    npm run lint:spelling:de -- --alle # auch die Wörter aus erlaubt.txt zeigen

Nicht gemeldet werden: Wörter, die im selben Content als Code-Bezeichner vorkommen, Tokens mit
`_`/`.`/Ziffern und alles aus `erlaubt.txt` (ein Wort pro Zeile).
"""
import collections, glob, json, os, re, subprocess, sys, tempfile

HIER = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HIER, "..", "..", ".."))
CODE_KEYS = {"codeTemplate", "solution", "referenceSolution", "expected", "id", "file", "section",
             "type", "target", "click", "name", "nextCourseId", "stdin", "text", "codeContains",
             "functionCalls", "variables"}
WORT = re.compile(r"[A-Za-zÄÖÜäöüß]+")
bezeichner = set()
zeilen = []


def code(s):
    for t in WORT.findall(s):
        bezeichner.add(t.lower())


def text(datei, s):
    s = re.sub(r"```.*?```", lambda m: (code(m.group(0)), " ")[1], s, flags=re.S)
    s = re.sub(r"`[^`\n]+`", lambda m: (code(m.group(0)), " ")[1], s)
    s = re.sub(r"https?://\S+", " ", s)
    s = re.sub(r"\s+", " ", s).strip()
    if s:
        zeilen.append(f"{datei}\t{s}")


def json_texte(datei, o, key=None):
    if isinstance(o, dict):
        for k, v in o.items():
            if not k.endswith("_en"):
                json_texte(datei, v, k)
    elif isinstance(o, list):
        for x in o:
            json_texte(datei, x, key)
    elif isinstance(o, str):
        code(o) if key in CODE_KEYS else text(datei, o)


def deutsch(p):
    return not re.search(r"-en/", p) and "_generated" not in p and "_bundle" not in p


def sammle():
    os.chdir(ROOT)
    for f in sorted(glob.glob("content/**/*.md", recursive=True)):
        if deutsch(f):
            text(f, open(f).read())
    for f in sorted(glob.glob("content/**/*.json", recursive=True)):
        if deutsch(f):
            json_texte(f, json.load(open(f)))
    for f in sorted(glob.glob("content/**/*_markdown.py", recursive=True)):
        if deutsch(f):
            t = re.sub(r'^"""|"""$', "", open(f).read().strip()).replace('\\"', '"')
            text(f, t)
    for f in sorted(glob.glob("content/**/*_code.py", recursive=True)):
        if deutsch(f):
            code(open(f).read())
    json_texte("public/kurse.json", json.load(open("public/kurse.json")))
    for m in re.finditer(r"""(['"`])((?:\\.|(?!\1).)*)\1""", open("src/locales/de.js").read(), re.S):
        if " " in m.group(2) or len(m.group(2)) > 12:
            text("src/locales/de.js", m.group(2).replace("\\n", " "))


def main():
    if sys.platform != "darwin":
        sys.exit("Nur auf macOS lauffähig (nutzt NSSpellChecker).")
    sammle()
    cache = os.path.join(tempfile.gettempdir(), "ue-hacker-rechtschreibung-de")
    os.makedirs(cache, exist_ok=True)
    binary, quelle = os.path.join(cache, "check"), os.path.join(HIER, "check.swift")
    if not os.path.exists(binary) or os.path.getmtime(binary) < os.path.getmtime(quelle):
        subprocess.run(["swiftc", "-O", quelle, "-o", binary], check=True)
    tsv = os.path.join(cache, "prosa.tsv")
    open(tsv, "w").write("\n".join(zeilen) + "\n")
    treffer = subprocess.run([binary, tsv], capture_output=True, text=True, check=True).stdout
    erlaubt = set() if "--alle" in sys.argv else {
        w.strip() for w in open(os.path.join(HIER, "erlaubt.txt")) if w.strip() and not w.startswith("#")}
    funde = collections.defaultdict(list)
    for z in treffer.splitlines():
        datei, wort, kontext = z.split("\t")
        if wort in erlaubt or wort.lower() in bezeichner or re.search(r"[_.\d/]", wort):
            continue
        teile = [t for t in wort.split("-") if t]
        if len(teile) > 1 and all(t.lower() in bezeichner for t in teile):
            continue
        funde[wort].append((datei, kontext))
    for wort in sorted(funde, key=str.lower):
        datei, kontext = funde[wort][0]
        print(f"{wort}  ({len(funde[wort])}×)  {datei}\n    …{kontext}…")
    print(f"\n{len(zeilen)} Textstellen geprüft, {len(funde)} unbekannte Wörter.")
    sys.exit(1 if funde else 0)


if __name__ == "__main__":
    main()
