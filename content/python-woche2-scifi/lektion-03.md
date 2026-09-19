# 🌡️ Systemprotokoll 2: Floats und Booleans

Die anderen beiden Quanten-Typen:

| Typ | Python-Name | Bedeutung | Beispiel |
|---|---|---|---|
| **Float** | `float` | Kommazahl (mit **Punkt**!) | `2.5` |
| **Boolean** | `bool` | Ja/Nein-Wert | `True` oder `False` |

- **Float:** Für präzise Werte wie Geschwindigkeit oder Koordinaten. Achtung: In Python schreibst du einen **Punkt** statt eines Kommas – `2.5`, nicht `2,5`.
- **Boolean:** Für Systemzustände. Es gibt genau zwei Werte: `True` (wahr) und `False` (falsch) – **groß** geschrieben und **ohne** Anführungszeichen!

```python
geschwindigkeit = 2.5
system_online = True
print(type(geschwindigkeit))   # <class 'float'>
print(type(system_online))     # <class 'bool'>
```

Booleans brauchst du ab Woche 3 ständig – dort entscheidet dein Programm damit, was es tut.
