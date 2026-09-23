"""# 📖 Glossar – 🐴 Woche 8 – Dictionaries und Tupel: Die Stall-Archive des Reiterhofs
> Dieses Notebook kannst du die ganze Woche offen lassen.

| Begriff | Bedeutung | Beispiel |
|---------|-----------|----------|
| **Dictionary** `{}` | Sammlung von Schlüssel-Wert-Paaren | `{\"name\": \"Aria\", \"level\": 5}` |
| **Schlüssel (Key)** | Name eines Eintrags im Dictionary | `held[\"name\"]` |
| **Wert (Value)** | Inhalt eines Eintrags | `held[\"level\"]` → `5` |
| `.get()` | Sicherer Zugriff – kein Fehler wenn Schlüssel fehlt | `held.get(\"xp\", 0)` |
| `.pop()` | Eintrag löschen und Wert zurückgeben | `held.pop(\"level\")` |
| `.keys()` | Alle Schlüssel als Liste | `held.keys()` |
| `.values()` | Alle Werte als Liste | `held.values()` |
| `.items()` | Alle Schlüssel-Wert-Paare – nützlich für Schleifen | `for k, v in held.items():` |
| **Tupel** `()` | Unveränderliche geordnete Sammlung | `punkt = (3, 5)` |
| **Tupel-Unpacking** | Tupel-Werte direkt in Variablen aufteilen | `x, y = (3, 5)` |
| `try` / `except` | Fehler abfangen, z.B. wenn ein Tupel verändert werden soll | `try: ... except TypeError:` |
| **List Comprehension** | Kurzschreibweise, um aus einer Liste eine neue zu erzeugen | `[x for x in liste if x > 5]` |"""
