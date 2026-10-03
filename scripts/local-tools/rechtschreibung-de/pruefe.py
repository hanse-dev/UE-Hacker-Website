#!/usr/bin/env python3
"""Deutsche Rechtschreib- und Grammatikprüfung für den Content — lokal, läuft nie im Deploy.

cspell (`npm run lint:spelling`) lässt bei Deutsch zu viel durch (das Wörterbuch erlaubt
beliebige Wortzusammensetzungen, "wiederspiegeln"/"strasse" gelten als richtig). Dieses Skript
zieht den deutschen Fließtext ohne Code aus dem Content und prüft ihn mit LanguageTool
(Open Source, läuft lokal in Docker — es verlässt kein Text den Rechner).

    npm run lint:spelling:de                # Rechtschreibung (Exit-Code 1 bei Funden)
    npm run lint:spelling:de -- --grammatik # zusätzlich Grammatik-Hinweise (Kandidaten zum Lesen)
    npm run lint:spelling:de -- --alle      # auch Wörter aus erlaubt.txt / stille Regeln zeigen
    npm run lint:spelling:de -- --stopp     # den LanguageTool-Container wieder beenden

Der Container `ue-hacker-languagetool` wird beim ersten Lauf gestartet (Image
`erikvl87/languagetool`, ~1,2 GB) und bleibt für weitere Läufe an. Wer LanguageTool anders
betreibt (z.B. per Java), setzt `LANGUAGETOOL_URL=http://host:port`.

Nicht gemeldet werden: Wörter, die im selben Content als Code-Bezeichner vorkommen, Tokens mit
`_`/`.`/Ziffern, alles aus `erlaubt.txt` (ein Wort pro Zeile) und die Regeln in `STILLE_REGELN`.
"""
import bisect, collections, glob, json, os, re, subprocess, sys, time
import urllib.error, urllib.parse, urllib.request

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


CONTAINER = "ue-hacker-languagetool"
PORT = 8011
# Grammatik-/Stilregeln, die im Lern-Content fast nur Rauschen erzeugen: Der Fließtext ist mit
# Code-Bezeichnern, Ausgabetexten und Lücken (entfernter Inline-Code) durchsetzt, daran scheitern
# vor allem Groß-/Kleinschreibungs-, Leerzeichen- und Satzzeichen-Regeln.
STILLE_REGELN = set("""
DE_CASE UPPERCASE_SENTENCE_START DE_DU_UPPER_LOWER KLEIN_NACH_PUNKT DOPPELPUNKT_GROSS
COMMA_PARENTHESIS_WHITESPACE LEERZEICHEN_NACH_VOR_ANFUEHRUNGSZEICHEN LEERZEICHEN_VOR_KLAMMER
LEERZEICHEN_VOR_AUSRUFEZEICHEN_ETC LEERZEICHEN_HINTER_DOPPELPUNKT LEERZEICHEN_RECHENZEICHEN
DE_SENTENCE_WHITESPACE AUSLASSUNGSPUNKTE_LEERZEICHEN EINHEIT_LEERZEICHEN DOPPELTE_SATZZEICHEN
DE_UNPAIRED_QUOTES UNPAIRED_BRACKETS FALSCHES_ANFUEHRUNGSZEICHEN KOMMA_STATT_PUNKT MALZEICHEN
PFEILE KARDINALZAHLEN ALLE ER_LIES DE_VERBAGREEMENT VERB_FEM_SUBST BEI_VERB PRP_VER_PRGK
BINDESTRICH_SUBSTANTIV DE_COMPOUND_COHERENCY GERMAN_WORD_REPEAT_BEGINNING_RULE SENT_START_SIN_PLU
""".split())


def u16(text_, start, laenge):
    """LanguageTool zählt Offsets in UTF-16-Einheiten (Emojis = 2), Python in Zeichen."""
    roh = text_.encode("utf-16-le")
    return roh[2 * start:2 * (start + laenge)].decode("utf-16-le", "replace")


def server():
    url = os.environ.get("LANGUAGETOOL_URL")
    if url:
        return url.rstrip("/")
    url = f"http://127.0.0.1:{PORT}"
    if not erreichbar(url):
        lauf = subprocess.run(["docker", "start", CONTAINER], capture_output=True)
        if lauf.returncode != 0:
            subprocess.run(["docker", "run", "-d", "--name", CONTAINER, "-p", f"127.0.0.1:{PORT}:8010",
                            "-e", "Java_Xms=256m", "-e", "Java_Xmx=1100m",  # Standard-Heap (512m) reicht nicht
                            "erikvl87/languagetool"], check=True, stdout=subprocess.DEVNULL)
        for _ in range(60):
            if erreichbar(url):
                break
            time.sleep(1)
        else:
            sys.exit("LanguageTool-Container antwortet nicht (docker logs " + CONTAINER + ").")
    return url


def erreichbar(url):
    try:
        urllib.request.urlopen(url + "/v2/languages", timeout=2).read()
        return True
    except (urllib.error.URLError, OSError):
        return False


def pruefe(url, text_):
    daten = urllib.parse.urlencode({"language": "de-DE", "text": text_}).encode()
    for versuch in range(5):  # direkt nach dem Start bricht der Server Verbindungen noch ab
        try:
            with urllib.request.urlopen(url + "/v2/check", daten, timeout=120) as antwort:
                return json.load(antwort)["matches"]
        except (urllib.error.URLError, ConnectionError, OSError):
            if versuch == 4:
                raise
            time.sleep(3)


def main():
    if "--stopp" in sys.argv:
        subprocess.run(["docker", "rm", "-f", CONTAINER])
        return
    sammle()
    url = server()
    alle = "--alle" in sys.argv
    grammatik = "--grammatik" in sys.argv
    erlaubt = set() if alle else {
        w.strip() for w in open(os.path.join(HIER, "erlaubt.txt")) if w.strip() and not w.startswith("#")}
    je_datei = collections.defaultdict(list)
    for z in zeilen:
        datei, t = z.split("\t", 1)
        je_datei[datei].append(t)
    woerter = collections.defaultdict(list)
    regeln = []
    # Viele kleine Dateien je Anfrage bündeln (der Server braucht pro Anfrage ~0,7 s Grundzeit).
    pakete, aktuell, groesse = [], [], 0
    for datei in sorted(je_datei):
        t = "\n\n".join(je_datei[datei])
        if aktuell and groesse + len(t) > 12000:
            pakete.append(aktuell)
            aktuell, groesse = [], 0
        aktuell.append((datei, t))
        groesse += len(t) + 2
    if aktuell:
        pakete.append(aktuell)
    for nr, paket in enumerate(pakete, 1):
        print(f"\r{nr}/{len(pakete)}", end="", file=sys.stderr, flush=True)
        starts, pos = [], 0
        for datei, t in paket:
            starts.append(pos)
            pos += len(t.encode("utf-16-le")) // 2 + 2
        for m in pruefe(url, "\n\n".join(t for _, t in paket)):
            datei = paket[bisect.bisect_right(starts, m["offset"]) - 1][0]
            c = m["context"]
            stelle = u16(c["text"], c["offset"], c["length"])
            kontext = c["text"].replace("\n", " ")
            regel = m["rule"]["id"]
            if regel == "GERMAN_SPELLER_RULE":
                if stelle in erlaubt or stelle.lower() in bezeichner or re.search(r"[_.\d/]", stelle):
                    continue
                teile = [t for t in stelle.split("-") if t]
                if len(teile) > 1 and all(t.lower() in bezeichner for t in teile):
                    continue
                woerter[stelle].append((datei, kontext))
            elif alle or (grammatik and regel not in STILLE_REGELN):
                regeln.append((regel, datei, stelle, kontext, m["message"]))
    print(file=sys.stderr)
    for wort in sorted(woerter, key=str.lower):
        datei, kontext = woerter[wort][0]
        print(f"{wort}  ({len(woerter[wort])}×)  {datei}\n    …{kontext}…")
    for regel, datei, stelle, kontext, meldung in sorted(regeln):
        print(f"[{regel}] {datei}\n    «{stelle}» {meldung}\n    …{kontext}…")
    print(f"\n{len(zeilen)} Textstellen geprüft: {len(woerter)} unbekannte Wörter"
          + (f", {len(regeln)} Grammatik-Hinweise." if alle or grammatik else "."))
    sys.exit(1 if woerter else 0)


if __name__ == "__main__":
    main()
