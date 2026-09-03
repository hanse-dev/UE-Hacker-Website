#!/usr/bin/env python3
"""
Fortschritt speichern – für lokale Nutzer (Jupyter/VS Code)

Wenn du die Notebooks lokal ausführst, kannst du mit diesem Skript
deine erledigten Missionen in mein-fortschritt.json speichern.
Diese Datei kannst du dann auf der Website unter "Fortschritt importieren"
hochladen. Sobald alle Missionen einer Woche erledigt sind und du den
Wochen-Check (Quiz + Coding-Aufgabe) auf der Website bestanden hast,
bekommst du das Zertifikat dieser Woche.

Verwendung:
  python fortschritt.py              # Interaktiv: fragt, was du beendet hast
  python fortschritt.py add          # Wie oben (interaktiv)
  python fortschritt.py add abenteuer w10-m1     # Direkt über Befehlszeile
  python fortschritt.py unclaim abenteuer w10-m1 # Erledigt-Markierung rückgängig
  python fortschritt.py show                     # Aktuellen Stand anzeigen
"""

import argparse
import json
import os
import sys

COURSE_ID = "python-12-wochen-grundkurs"
FILE_NAME = "mein-fortschritt.json"


def find_manifest():
    """Suche rewards-manifest.json in verschiedenen Pfaden."""
    script_dir = os.path.dirname(os.path.abspath(__file__))
    candidates = [
        os.path.join(os.getcwd(), "rewards-manifest.json"),
        os.path.join(script_dir, "rewards-manifest.json"),
        os.path.join(script_dir, "..", "rewards-manifest.json"),
        os.path.join(script_dir, "..", "public", "rewards-manifest.json"),
    ]
    for path in candidates:
        if os.path.isfile(path):
            return path
    return None


def load_manifest():
    path = find_manifest()
    if not path:
        print(
            "Fehler: rewards-manifest.json nicht gefunden.\n"
            "Lade die Datei von der Website herunter oder lege sie in den gleichen Ordner wie dieses Skript.",
            file=sys.stderr,
        )
        sys.exit(1)
    with open(path, encoding="utf-8") as f:
        return json.load(f)


def mission_exists(manifest, variant, mission_id):
    """Prüft, ob die Mission-ID für die Variante im Manifest bekannt ist."""
    course = manifest.get(COURSE_ID, {})
    variant_data = course.get(variant, {})
    for week_data in variant_data.values():
        for key in ("missions", "bossQuests"):
            ids = week_data.get(key, [])
            if mission_id in ids:
                label = "Mission" if key == "missions" else "Boss-Quest"
                idx = ids.index(mission_id)
                return f"{label} {idx + 1}"
    return None


def default_state():
    return {
        "version": 3,
        "courseId": COURSE_ID,
        "variants": {
            "abenteuer": {"done": []},
            "pferde": {"done": []},
            "scifi": {"done": []},
        },
    }


def load_fortschritt():
    if not os.path.isfile(FILE_NAME):
        return default_state()
    with open(FILE_NAME, encoding="utf-8") as f:
        data = json.load(f)
    if data.get("courseId") != COURSE_ID or data.get("version") != 3:
        return default_state()
    return data


def save_fortschritt(data):
    with open(FILE_NAME, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
    print(f"✓ Gespeichert in {os.path.abspath(FILE_NAME)}")


def cmd_add(manifest, variant, mission_id):
    if variant not in ("abenteuer", "pferde", "scifi"):
        print("Fehler: Variante muss abenteuer, pferde oder scifi sein.", file=sys.stderr)
        sys.exit(1)
    label = mission_exists(manifest, variant, mission_id)
    if not label:
        print(f"Fehler: Mission '{mission_id}' für Variante '{variant}' nicht gefunden.", file=sys.stderr)
        sys.exit(1)
    data = load_fortschritt()
    done = data["variants"][variant]["done"]
    if mission_id in done:
        print("Diese Mission ist bereits als erledigt markiert.")
        return
    done.append(mission_id)
    save_fortschritt(data)
    print(f"✓ {label} ({mission_id}) als erledigt markiert.")


def cmd_unclaim(variant, mission_id):
    data = load_fortschritt()
    done = data["variants"][variant]["done"]
    if mission_id not in done:
        print("Diese Mission war nicht als erledigt markiert.")
        return
    done.remove(mission_id)
    save_fortschritt(data)
    print(f"✓ Mission {mission_id} zurückgenommen.")


def interactive_add(manifest):
    """Interaktiv fragen, was der Nutzer beendet hat, und markieren."""
    variant_choices = [
        ("1", "abenteuer", "🗺️ Abenteuer"),
        ("2", "pferde", "🐴 Pferde"),
        ("3", "scifi", "🚀 Sci-Fi"),
    ]
    mission_choices = [
        ("1", "m1", "Mission 1"),
        ("2", "m2", "Mission 2"),
        ("3", "m3", "Mission 3"),
        ("4", "boss1", "Boss-Quest 1"),
        ("5", "boss2", "Boss-Quest 2"),
        ("6", "boss3", "Boss-Quest 3"),
    ]

    print("\nWas hast du gerade beendet?\n")
    print("Questreihe:")
    for num, _, label in variant_choices:
        print(f"  {num}) {label}")
    v_in = input("Wahl (1–3): ").strip()
    variant = None
    for num, key, _ in variant_choices:
        if v_in == num or v_in.lower() == key:
            variant = key
            break
    if not variant:
        print("Ungültige Eingabe.", file=sys.stderr)
        sys.exit(1)

    week_in = input("\nWelche Woche (1–12): ").strip()
    try:
        week = int(week_in)
        if week < 1 or week > 12:
            raise ValueError("Außerhalb 1–12")
    except ValueError:
        print("Bitte eine Zahl von 1 bis 12 eingeben.", file=sys.stderr)
        sys.exit(1)

    print("\nWas davon:")
    for num, key, label in mission_choices:
        print(f"  {num}) {label}")
    m_in = input("Wahl (1–6): ").strip()
    mission_key = None
    for num, key, label in mission_choices:
        if m_in == num or m_in == key:
            mission_key = key
            break
    if not mission_key:
        print("Ungültige Eingabe.", file=sys.stderr)
        sys.exit(1)

    mission_id = f"w{week}-{mission_key}"
    print(f"\n→ {variant}, Woche {week}, {mission_key} → {mission_id}\n")
    cmd_add(manifest, variant, mission_id)


def cmd_show(data):
    labels = {"abenteuer": "🗺️ Abenteuer", "pferde": "🐴 Pferde", "scifi": "🚀 Sci-Fi"}
    total = 0
    for v in ("abenteuer", "pferde", "scifi"):
        done = data["variants"][v]["done"]
        total += len(done)
        if done:
            print(f"\n{labels[v]}: {len(done)} Missionen erledigt")
            for mission_id in done:
                print(f"  • {mission_id}")
    if total == 0:
        print("Noch keine Missionen als erledigt markiert.")
        print("Beispiel: python fortschritt.py add abenteuer w1-m1")
    else:
        print(f"\nGesamt: {total} Missionen erledigt")
    print(f"\nDatei: {os.path.abspath(FILE_NAME)}")
    print("Diese Datei auf der Website unter 'Fortschritt importieren' hochladen, um zu synchronisieren.")


def main():
    parser = argparse.ArgumentParser(description="Fortschritt lokal speichern (für Import auf der Website)")
    sub = parser.add_subparsers(dest="cmd", required=False)
    add_p = sub.add_parser("add", help="Mission als erledigt markieren (ohne Args: interaktiv)")
    add_p.add_argument("variant", nargs="?", choices=["abenteuer", "pferde", "scifi"])
    add_p.add_argument("mission_id", nargs="?", help="z.B. w1-m1, w10-boss2")
    unclaim_p = sub.add_parser("unclaim", help="Erledigt-Markierung rückgängig machen")
    unclaim_p.add_argument("variant", choices=["abenteuer", "pferde", "scifi"])
    unclaim_p.add_argument("mission_id")
    sub.add_parser("show", help="Aktuellen Stand anzeigen")
    args = parser.parse_args()

    # Ohne Befehl oder "add" ohne Args → interaktiv
    if args.cmd is None or (args.cmd == "add" and (not args.variant or not args.mission_id)):
        manifest = load_manifest()
        interactive_add(manifest)
    elif args.cmd == "add":
        manifest = load_manifest()
        cmd_add(manifest, args.variant, args.mission_id)
    elif args.cmd == "unclaim":
        cmd_unclaim(args.variant, args.mission_id)
    else:
        data = load_fortschritt()
        cmd_show(data)


if __name__ == "__main__":
    main()
