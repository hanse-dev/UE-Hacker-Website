"""### Debug-Quest – Bug #2

🐛 Bug #2 – Ziel: Das Programm soll Gesamtkraft: 150 ausgeben. Was ist falsch?

**Fehler:** `zauberkraft` ist ein Text (`"100"`), `bonus` eine Zahl – Text und Zahl lassen sich nicht mit + addieren (TypeError). Mit `int()` wird der Text zur Zahl. Alternativ schreibst du `zauberkraft = 100`."""