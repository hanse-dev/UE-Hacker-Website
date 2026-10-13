#!/usr/bin/env python3
"""Alles rund um den MXW01-Thermodrucker. Läuft nur lokal, nie auf dem Server.

Ohne Argumente startet ein Menü. Mit Unterbefehl läuft genau eine Aktion:

  drucker.py account <benutzername>   Account anlegen oder, falls es ihn schon gibt, Passwort zurücksetzen
  drucker.py ausdrucke [DATEI]        gespeicherten Ausdruck auswählen und erneut drucken
  drucker.py tabelle [-n ANZAHL]      Forscher-Tabelle aus micro:bit-Stufe 8 drucken
  drucker.py scan [SEKUNDEN]          Drucker-Adresse per Bluetooth suchen

Jeder Ausdruck wird als Bild unter ausdrucke/ gespeichert.

Diese Datei enthält nur Menü und Kommandozeile (alles, was fragt und ausgibt). Die Arbeit machen
druck.py, ausweis.py, tabelle.py und bluetooth.py. Setup: siehe README.md
"""
import argparse
import getpass
import sys
from pathlib import Path

import ausweis
import bluetooth
import tabelle
from druck import (
    AUSDRUCKE_DIR, SCRIPT_DIR, DruckerError,
    describe_printout, list_printouts, load_env_file, reexec_in_venv, require_printer, send_to_printer,
)

MAX_LISTED_PRINTOUTS = 20


def ask(prompt: str, default: str = "") -> str:
    suffix = f" [{default}]" if default else ""
    return input(f"{prompt}{suffix}: ").strip() or default


def set_account(
    username: str, env: dict, printer_address: str | None,
    age_group: str | None = None, reset: bool | None = None,
    server_url_override: str | None = None, no_print: bool = False, session: dict | None = None,
) -> None:
    """Legt den Account an oder setzt, falls es ihn schon gibt, auf Wunsch das Passwort zurück.
    In beiden Fällen entsteht ein Zugangsausweis, der gespeichert und gedruckt wird.

    reset=None fragt nach, reset=True setzt ohne Rückfrage zurück. Fehlt age_group bei einem
    neuen Account, wird danach gefragt. `session` merkt sich die Admin-Anmeldung, damit das Menü
    nur einmal nach dem Admin-Passwort fragt."""
    font_scale = ausweis.receipt_font_scale(env)
    if not no_print:
        require_printer(printer_address)
    session = {} if session is None else session
    if "token" not in session:
        admin_password = getpass.getpass("Admin-Passwort der Website: ") if ausweis.needs_admin_password(env) else None
        session.update(ausweis.admin_login(env, server_url_override, admin_password))

    user = ausweis.find_user(session, username)
    if user:
        username = user["username"]
        if reset is None:
            reset = ask(f"Account '{username}' gibt es schon. Passwort zurücksetzen? (j/n)", "n").lower().startswith("j")
        if not reset:
            # Das alte Passwort lässt sich nicht auslesen — auf dem Server liegt nur ein Hash.
            print("Nichts geändert. Den früheren Zugangsausweis gibt es höchstens noch unter den gespeicherten Ausdrucken.")
            return
        password = ausweis.reset_password(session, user)
        print(f"Passwort von '{username}' zurückgesetzt. Einmal-Passwort: {password}")
    else:
        if not age_group:
            choice = ask(f"Account '{username}' gibt es noch nicht. Altersgruppe: (k)inder oder (j)ugendliche", "k").lower()
            if choice not in ("k", "kinder", "j", "jugendliche"):
                raise DruckerError(f"Abgebrochen: unbekannte Altersgruppe '{choice}'.")
            age_group = "kinder" if choice.startswith("k") else "jugendliche"
        password = ausweis.create_user(session, username, age_group)
        print(f"Account '{username}' angelegt. Passwort: {password}")

    # Erst speichern, dann drucken — schlägt der Druck fehl, bleibt der Ausweis erhalten.
    output(ausweis.save_receipt(session, username, password, font_scale, one_time=bool(user)), printer_address, no_print)


def output(image_path: Path, printer_address: str | None, no_print: bool) -> None:
    print(f"Ausdruck gespeichert: {image_path.relative_to(SCRIPT_DIR)}")
    if not no_print:
        send_to_printer(image_path, printer_address)


def print_table(copies: int, printer_address: str | None, font_scale: float, no_print: bool = False) -> None:
    if not no_print:
        require_printer(printer_address)
    output(tabelle.save_table(copies, font_scale), printer_address, no_print)


def print_saved(printer_address: str | None, name: str | None = None) -> None:
    """Druckt einen gespeicherten Ausdruck: per Dateiname oder per Auswahl aus der Liste (neueste zuerst)."""
    files = list_printouts()
    if not files:
        raise DruckerError(f"Noch keine gespeicherten Ausdrucke in {AUSDRUCKE_DIR}.")
    if name:
        chosen = next((f for f in files if f.name == Path(name).name), None)
        if not chosen:
            raise DruckerError(f"Kein gespeicherter Ausdruck mit dem Namen '{Path(name).name}'.")
    else:
        shown = files[:MAX_LISTED_PRINTOUTS]
        print("Gespeicherte Ausdrucke (neueste zuerst):")
        for number, path in enumerate(shown, 1):
            print(f"  {number:>2}  {describe_printout(path)}")
        if len(files) > len(shown):
            print(f"      … und {len(files) - len(shown)} ältere in {AUSDRUCKE_DIR}")
        answer = ask("Welchen drucken? (Nummer, leer = abbrechen)")
        if not answer:
            return
        if not answer.isdigit() or not 1 <= int(answer) <= len(shown):
            raise DruckerError(f"Abgebrochen: '{answer}' steht nicht in der Liste.")
        chosen = shown[int(answer) - 1]
    send_to_printer(chosen, printer_address)


def scan_bluetooth(seconds: float = bluetooth.DEFAULT_SCAN_SECONDS) -> None:
    print(f"Scanne {seconds:.0f} Sekunden nach BLE-Geräten (Drucker muss an/wach sein)...")
    devices = bluetooth.scan(seconds)
    if not devices:
        print("Keine BLE-Geräte gefunden.")
    for d in devices:
        print(f"{d['address']}  {d['name']}{'  <-- vermutlich der Drucker' if d['is_printer'] else ''}")


MENU = """
UE Hacker – Thermodrucker
  1  Account: anlegen oder Passwort zurücksetzen
  2  Gespeicherten Ausdruck drucken
  3  Forscher-Tabelle drucken (micro:bit, Stufe 8)
  4  Drucker suchen (Bluetooth-Scan)
  0  Beenden"""


def menu_set_account(env: dict, printer_address: str | None, session: dict) -> None:
    username = ask("Benutzername")
    if not username:
        raise DruckerError("Abgebrochen: kein Benutzername.")
    set_account(username, env, printer_address, session=session)


def menu_print_table(printer_address: str | None) -> None:
    answer = ask("Wie viele Tabellen (eine pro Team)?", "1")
    if not answer.isdigit():
        raise DruckerError(f"Abgebrochen: '{answer}' ist keine Anzahl.")
    print_table(int(answer), printer_address, tabelle.DEFAULT_TABLE_FONT_SCALE)


def run_menu(env: dict, printer_address: str | None) -> None:
    session: dict = {}
    actions = {
        "1": lambda: menu_set_account(env, printer_address, session),
        "2": lambda: print_saved(printer_address),
        "3": lambda: menu_print_table(printer_address),
        "4": scan_bluetooth,
    }
    while True:
        print(MENU)
        try:
            choice = input("Auswahl: ").strip()
            if choice in ("0", "q", ""):
                return
            if choice not in actions:
                print(f"'{choice}' gibt es nicht.")
                continue
            actions[choice]()
        except (EOFError, KeyboardInterrupt):
            print()
            return
        except DruckerError as e:
            # Ein Fehler in einer Aktion beendet nur die Aktion, nicht das Menü.
            print(e)


def main() -> None:
    reexec_in_venv(__file__)

    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--printer-address", help="Überschreibt MXW01_PRINTER_ADDRESS aus .env")
    sub = parser.add_subparsers(dest="command", metavar="{account,ausdrucke,tabelle,scan}")

    p_account = sub.add_parser("account", help="Account anlegen oder, falls es ihn schon gibt, Passwort zurücksetzen (Einmal-Passwort)")
    p_account.add_argument("username", help="Benutzername (2-40 Zeichen, a-z/A-Z/0-9/._-)")
    p_account.add_argument("age_group", nargs="?", choices=ausweis.AGE_GROUPS, help="Altersgruppe für einen neuen Account (sonst wird gefragt)")
    p_account.add_argument("--reset", action="store_true", help="Passwort eines bestehenden Accounts ohne Rückfrage zurücksetzen")
    p_account.add_argument("--server-url", help="Überschreibt ACCOUNT_SERVER_URL aus .env")
    p_account.add_argument("--no-print", action="store_true", help="Ausweis nur speichern, nicht drucken")

    p_saved = sub.add_parser("ausdrucke", help="Gespeicherten Ausdruck auswählen und erneut drucken")
    p_saved.add_argument("datei", nargs="?", help="Dateiname aus ausdrucke/ (ohne Angabe: Liste zur Auswahl)")

    p_table = sub.add_parser("tabelle", help="Forscher-Tabelle aus micro:bit-Stufe 8 drucken")
    p_table.add_argument("-n", "--copies", type=int, default=1, help="Anzahl Tabellen, eine pro Team (Default 1)")
    p_table.add_argument("--font-scale", type=float, default=tabelle.DEFAULT_TABLE_FONT_SCALE, help="Skaliert Schrift und Zeilenhöhe (Default 1.0)")
    p_table.add_argument("--no-print", action="store_true", help="Tabelle nur speichern, nicht drucken")

    p_scan = sub.add_parser("scan", help="Drucker-Adresse per Bluetooth suchen")
    p_scan.add_argument("seconds", nargs="?", type=float, default=bluetooth.DEFAULT_SCAN_SECONDS, help="Dauer des Scans (Default 8)")

    args = parser.parse_args()
    env = load_env_file(SCRIPT_DIR / ".env")
    printer_address = args.printer_address or env.get("MXW01_PRINTER_ADDRESS")

    try:
        if args.command == "account":
            set_account(
                args.username, env, printer_address,
                age_group=args.age_group, reset=True if args.reset else None,
                server_url_override=args.server_url, no_print=args.no_print,
            )
        elif args.command == "ausdrucke":
            print_saved(printer_address, args.datei)
        elif args.command == "tabelle":
            print_table(args.copies, printer_address, args.font_scale, args.no_print)
        elif args.command == "scan":
            scan_bluetooth(args.seconds)
        else:
            run_menu(env, printer_address)
    except DruckerError as e:
        sys.exit(str(e))


if __name__ == "__main__":
    main()
