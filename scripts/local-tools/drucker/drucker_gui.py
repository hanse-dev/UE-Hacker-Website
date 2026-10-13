#!/usr/bin/env python3
"""Fenster für den MXW01-Thermodrucker: dieselben Aktionen wie drucker.py, aber zum Anklicken
und mit Vorschau der gespeicherten Ausdrucke. Läuft nur lokal, nie auf dem Server.

Braucht tkinter (macOS/Homebrew: brew install python-tk@3.14). Setup sonst wie in README.md.
"""
import queue
import threading
import tkinter as tk
from tkinter import messagebox, simpledialog, ttk

import ausweis
import bluetooth
import tabelle
from druck import (
    SCRIPT_DIR, DruckerError,
    describe_printout, list_printouts, load_env_file, reexec_in_venv, require_printer, send_to_printer,
)

PAD = 8


class DruckerApp:
    def __init__(self, root: tk.Tk):
        self.root = root
        self.env = load_env_file(SCRIPT_DIR / ".env")
        self.printer_address = self.env.get("MXW01_PRINTER_ADDRESS")
        self.session: dict = {}  # Admin-Anmeldung, einmal pro Programmstart
        self.user = None  # zuletzt geprüfter Account (dict) oder None, wenn es ihn nicht gibt
        self.checked_username = ""
        self.printouts: list = []
        self.preview_image = None
        self.busy = False
        self.results: queue.Queue = queue.Queue()

        root.title("UE Hacker – Thermodrucker")
        root.minsize(760, 560)

        tabs = ttk.Notebook(root)
        tabs.pack(fill="both", expand=True, padx=PAD, pady=(PAD, 0))
        self.tabs = tabs
        self._build_account_tab(tabs)
        self._build_printouts_tab(tabs)
        self._build_table_tab(tabs)
        self._build_printer_tab(tabs)

        self.no_print = tk.BooleanVar(value=False)
        bottom = ttk.Frame(root)
        bottom.pack(fill="x", padx=PAD, pady=PAD)
        ttk.Checkbutton(bottom, text="Nur speichern, nicht drucken", variable=self.no_print).pack(side="left")
        self.status = tk.StringVar(value="Bereit.")
        ttk.Label(bottom, textvariable=self.status, anchor="e").pack(side="right", fill="x", expand=True)

        self.refresh_printouts()
        self.root.after(100, self._poll_results)

    # -- Aufbau ---------------------------------------------------------------------------

    def _build_account_tab(self, tabs: ttk.Notebook) -> None:
        tab = ttk.Frame(tabs, padding=PAD * 2)
        tabs.add(tab, text="Account")

        ttk.Label(tab, text="Benutzername").grid(row=0, column=0, sticky="w")
        self.username = tk.StringVar()
        entry = ttk.Entry(tab, textvariable=self.username, width=30)
        entry.grid(row=0, column=1, sticky="w", padx=PAD)
        entry.bind("<Return>", lambda _event: self.check_account())
        entry.focus_set()
        self.check_button = ttk.Button(tab, text="Prüfen", command=self.check_account)
        self.check_button.grid(row=0, column=2, sticky="w")
        # Ein geänderter Name macht das Prüfergebnis ungültig.
        self.username.trace_add("write", lambda *_: self._show_account_state(None, checked=False))

        self.account_info = tk.StringVar(value="Benutzername eingeben und prüfen.")
        ttk.Label(tab, textvariable=self.account_info, wraplength=560, justify="left").grid(
            row=1, column=0, columnspan=3, sticky="w", pady=(PAD * 2, PAD))

        # Neuer Account: Altersgruppe wählen und anlegen
        self.create_frame = ttk.Frame(tab)
        self.age_group = tk.StringVar(value=ausweis.AGE_GROUPS[0])
        ttk.Label(self.create_frame, text="Altersgruppe").pack(side="left")
        for group in ausweis.AGE_GROUPS:
            ttk.Radiobutton(self.create_frame, text=group.capitalize(), value=group, variable=self.age_group).pack(
                side="left", padx=(PAD, 0))
        self.create_button = ttk.Button(self.create_frame, text="Anlegen und Ausweis drucken", command=self.create_account)
        self.create_button.pack(side="left", padx=(PAD * 2, 0))

        # Vorhandener Account: Passwort zurücksetzen
        self.reset_frame = ttk.Frame(tab)
        self.reset_button = ttk.Button(
            self.reset_frame, text="Passwort zurücksetzen und Ausweis drucken", command=self.reset_account)
        self.reset_button.pack(side="left")

        self.create_frame.grid(row=2, column=0, columnspan=3, sticky="w")
        self.reset_frame.grid(row=2, column=0, columnspan=3, sticky="w")
        self._show_account_state(None, checked=False)

    def _build_printouts_tab(self, tabs: ttk.Notebook) -> None:
        tab = ttk.Frame(tabs, padding=PAD)
        tabs.add(tab, text="Gespeicherte Ausdrucke")
        tab.columnconfigure(1, weight=1)
        tab.rowconfigure(0, weight=1)

        left = ttk.Frame(tab)
        left.grid(row=0, column=0, sticky="ns")
        self.printout_list = tk.Listbox(left, width=34, exportselection=False)
        self.printout_list.pack(side="left", fill="y", expand=True)
        scroll = ttk.Scrollbar(left, command=self.printout_list.yview)
        scroll.pack(side="left", fill="y")
        self.printout_list.configure(yscrollcommand=scroll.set)
        self.printout_list.bind("<<ListboxSelect>>", lambda _event: self.show_preview())
        self.printout_list.bind("<Double-Button-1>", lambda _event: self.print_selected())

        # Vorschau in einer scrollbaren Fläche: mehrere Tabellen am Stück sind lang.
        right = ttk.Frame(tab)
        right.grid(row=0, column=1, sticky="nsew", padx=(PAD, 0))
        self.preview = tk.Canvas(right, background="#d9d9d9", highlightthickness=0)
        preview_scroll = ttk.Scrollbar(right, command=self.preview.yview)
        self.preview.configure(yscrollcommand=preview_scroll.set)
        self.preview.pack(side="left", fill="both", expand=True)
        preview_scroll.pack(side="left", fill="y")

        buttons = ttk.Frame(tab)
        buttons.grid(row=1, column=0, columnspan=2, sticky="w", pady=(PAD, 0))
        self.print_button = ttk.Button(buttons, text="Ausgewählten Ausdruck drucken", command=self.print_selected)
        self.print_button.pack(side="left")
        ttk.Button(buttons, text="Liste aktualisieren", command=self.refresh_printouts).pack(side="left", padx=PAD)

    def _build_table_tab(self, tabs: ttk.Notebook) -> None:
        tab = ttk.Frame(tabs, padding=PAD * 2)
        tabs.add(tab, text="Forscher-Tabelle")
        ttk.Label(tab, text="Tabelle aus micro:bit-Stufe 8 („Die Linie sehen“) zum Ausfüllen.").grid(
            row=0, column=0, columnspan=3, sticky="w", pady=(0, PAD * 2))
        ttk.Label(tab, text="Anzahl (eine pro Team)").grid(row=1, column=0, sticky="w")
        self.copies = tk.IntVar(value=1)
        ttk.Spinbox(tab, from_=1, to=30, textvariable=self.copies, width=5).grid(row=1, column=1, sticky="w", padx=PAD)
        self.table_button = ttk.Button(tab, text="Tabelle drucken", command=self.print_table)
        self.table_button.grid(row=1, column=2, sticky="w")

    def _build_printer_tab(self, tabs: ttk.Notebook) -> None:
        tab = ttk.Frame(tabs, padding=PAD * 2)
        tabs.add(tab, text="Drucker")
        tab.columnconfigure(0, weight=1)
        tab.rowconfigure(2, weight=1)
        address = self.printer_address or "nicht gesetzt (MXW01_PRINTER_ADDRESS in .env)"
        ttk.Label(tab, text=f"Drucker-Adresse: {address}").grid(row=0, column=0, sticky="w")
        self.scan_button = ttk.Button(tab, text="Drucker suchen (8 Sekunden)", command=self.scan)
        self.scan_button.grid(row=1, column=0, sticky="w", pady=PAD)
        self.scan_result = tk.Text(tab, height=12, state="disabled", wrap="none")
        self.scan_result.grid(row=2, column=0, sticky="nsew")

    # -- Hintergrundarbeit ----------------------------------------------------------------

    def run_async(self, label: str, work, on_done) -> None:
        """Führt `work` in einem Thread aus (Netz, Bluetooth und Druck dauern Sekunden) und ruft
        `on_done(ergebnis)` wieder im Fenster-Thread auf. Fehler landen in der Statuszeile."""
        if self.busy:
            return
        self._set_busy(True, label)

        def runner():
            try:
                self.results.put((on_done, work(), None))
            except DruckerError as e:
                self.results.put((None, None, str(e)))
            except Exception as e:  # unerwartet, aber das Fenster soll weiter bedienbar bleiben
                self.results.put((None, None, f"Unerwarteter Fehler: {e!r}"))

        threading.Thread(target=runner, daemon=True).start()

    def _poll_results(self) -> None:
        try:
            while True:
                on_done, result, error = self.results.get_nowait()
                self._set_busy(False, "Bereit.")
                if error:
                    self.status.set(error.splitlines()[0])
                    messagebox.showerror("Fehler", error, parent=self.root)
                else:
                    on_done(result)
        except queue.Empty:
            pass
        self.root.after(100, self._poll_results)

    def _set_busy(self, busy: bool, text: str) -> None:
        self.busy = busy
        self.status.set(text)
        state = "disabled" if busy else "normal"
        for button in (self.check_button, self.create_button, self.reset_button,
                       self.print_button, self.table_button, self.scan_button):
            button.configure(state=state)

    # -- Account --------------------------------------------------------------------------

    def _ensure_session(self) -> bool:
        """Fragt bei Bedarf einmal nach dem Admin-Passwort. False, wenn abgebrochen wurde."""
        if "token" in self.session or not ausweis.needs_admin_password(self.env) or self.session.get("password"):
            return True
        password = simpledialog.askstring("Admin-Passwort", "Admin-Passwort der Website:", show="•", parent=self.root)
        if not password:
            return False
        self.session["password"] = password
        return True

    def _login(self) -> dict:
        """Läuft im Hintergrund-Thread: meldet sich an, falls noch nicht geschehen."""
        if "token" not in self.session:
            try:
                self.session.update(ausweis.admin_login(self.env, admin_password=self.session.get("password")))
            except DruckerError:
                self.session.pop("password", None)  # falsches Passwort: beim nächsten Versuch neu fragen
                raise
        return self.session

    def _can_output(self) -> bool:
        """Vor jeder Änderung prüfen, ob gedruckt werden kann — sonst gäbe es ein neues Passwort ohne Ausweis."""
        if self.no_print.get():
            return True
        try:
            require_printer(self.printer_address)
            return True
        except DruckerError as e:
            messagebox.showerror("Drucker nicht eingerichtet", str(e), parent=self.root)
            return False

    def _show_account_state(self, user, checked: bool) -> None:
        self.user = user
        self.checked_username = self.username.get().strip() if checked else ""
        self.create_frame.grid_remove()
        self.reset_frame.grid_remove()
        if not checked:
            self.account_info.set("Benutzername eingeben und prüfen.")
        elif user:
            self.account_info.set(
                f"Den Account „{user['username']}“ gibt es schon ({user['ageGroup']}).\n"
                "Das alte Passwort lässt sich nicht anzeigen. Beim Zurücksetzen entsteht ein Einmal-Passwort; "
                "beim nächsten Login muss ein eigenes gewählt werden.")
            self.reset_frame.grid()
        else:
            self.account_info.set(f"Den Account „{self.checked_username}“ gibt es noch nicht.")
            self.create_frame.grid()

    def check_account(self) -> None:
        username = self.username.get().strip()
        if not username or not self._ensure_session():
            return
        self.run_async(
            f"Suche „{username}“ …",
            lambda: ausweis.find_user(self._login(), username),
            lambda user: self._show_account_state(user, checked=True),
        )

    def create_account(self) -> None:
        username, age_group = self.checked_username, self.age_group.get()
        if not username or not self._can_output():
            return

        def work():
            session = self._login()
            password = ausweis.create_user(session, username, age_group)
            return self._save_receipt(session, username, password, one_time=False)

        self.run_async(f"Lege „{username}“ an …", work, lambda path: self._after_account_change(path, "angelegt"))

    def reset_account(self) -> None:
        user = self.user
        if not user or not self._can_output():
            return
        if not messagebox.askyesno(
            "Passwort zurücksetzen",
            f"Passwort von „{user['username']}“ wirklich zurücksetzen?\n\n"
            "Das bisherige Passwort gilt danach nicht mehr und der Account wird überall abgemeldet.",
            parent=self.root,
        ):
            return

        def work():
            session = self._login()
            password = ausweis.reset_password(session, user)
            return self._save_receipt(session, user["username"], password, one_time=True)

        self.run_async(
            f"Setze „{user['username']}“ zurück …", work,
            lambda path: self._after_account_change(path, "zurückgesetzt"))

    def _save_receipt(self, session: dict, username: str, password: str, one_time: bool):
        font_scale = ausweis.receipt_font_scale(self.env)
        return ausweis.save_receipt(session, username, password, font_scale, one_time=one_time)

    def _after_account_change(self, path, what: str) -> None:
        self._show_account_state(None, checked=False)
        self.output(path, f"Account {what}.")

    # -- Ausdrucke ------------------------------------------------------------------------

    def output(self, path, message: str) -> None:
        """Zeigt einen frisch gespeicherten Ausdruck in der Liste und druckt ihn (außer bei „nur speichern“)."""
        self.refresh_printouts(select=path)
        if self.no_print.get():
            self.status.set(f"{message} Gespeichert: {path.name}")
            return
        self.print_path(path, message)

    def print_path(self, path, message: str = "") -> None:
        self.run_async(
            f"{message} Drucke {path.name} …".strip(),
            lambda: send_to_printer(path, self.printer_address),
            lambda _result: self.status.set(f"Gedruckt: {path.name}"),
        )

    def refresh_printouts(self, select=None) -> None:
        self.printouts = list_printouts()
        self.printout_list.delete(0, "end")
        for path in self.printouts:
            self.printout_list.insert("end", describe_printout(path))
        if self.printouts:
            index = self.printouts.index(select) if select in self.printouts else 0
            self.printout_list.selection_set(index)
            self.printout_list.see(index)
        self.show_preview()

    def selected_printout(self):
        selection = self.printout_list.curselection()
        return self.printouts[selection[0]] if selection else None

    def show_preview(self) -> None:
        self.preview.delete("all")
        self.preview_image = None
        path = self.selected_printout()
        if not path:
            self.preview.create_text(PAD, PAD, anchor="nw", text="Noch keine gespeicherten Ausdrucke.")
            return
        try:
            self.preview_image = tk.PhotoImage(file=str(path))  # Referenz halten, sonst bleibt die Fläche leer
        except tk.TclError:
            self.preview.create_text(PAD, PAD, anchor="nw", text=f"{path.name} lässt sich nicht anzeigen.")
            return
        self.preview.create_image(PAD, PAD, anchor="nw", image=self.preview_image)
        self.preview.configure(scrollregion=(0, 0, self.preview_image.width() + 2 * PAD, self.preview_image.height() + 2 * PAD))
        self.preview.yview_moveto(0)

    def print_selected(self) -> None:
        path = self.selected_printout()
        if not path:
            return
        try:
            require_printer(self.printer_address)
        except DruckerError as e:
            messagebox.showerror("Drucker nicht eingerichtet", str(e), parent=self.root)
            return
        self.print_path(path)

    # -- Tabelle und Drucker --------------------------------------------------------------

    def print_table(self) -> None:
        try:
            copies = int(self.copies.get())
        except (tk.TclError, ValueError):
            messagebox.showerror("Anzahl", "Die Anzahl muss eine Zahl sein.", parent=self.root)
            return
        if not self._can_output():
            return
        self.run_async(
            "Baue Tabelle …",
            lambda: tabelle.save_table(copies),
            lambda path: self.output(path, "Tabelle gebaut."),
        )

    def scan(self) -> None:
        def show(devices):
            lines = [
                f"{d['address']}  {d['name']}{'   ← vermutlich der Drucker' if d['is_printer'] else ''}"
                for d in devices
            ] or ["Keine BLE-Geräte gefunden. Ist der Drucker an und wach?"]
            self.scan_result.configure(state="normal")
            self.scan_result.delete("1.0", "end")
            self.scan_result.insert("end", "\n".join(lines))
            self.scan_result.configure(state="disabled")
            self.status.set(f"{len(devices)} Geräte gefunden. Die Adresse gehört als MXW01_PRINTER_ADDRESS in .env.")

        self.run_async("Suche Bluetooth-Geräte …", lambda: bluetooth.scan(), show)


def main() -> None:
    reexec_in_venv(__file__)
    root = tk.Tk()
    DruckerApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()
