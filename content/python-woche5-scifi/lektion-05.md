# ⚖️ Systemprotokoll 5: return oder print?

`print` und `return` sehen ähnlich aus, tun aber Verschiedenes:

| | `print(...)` | `return ...` |
|---|---|---|
| Zeigt etwas auf dem Bildschirm | ✅ | ❌ |
| Liefert einen Wert an den Aufrufer | ❌ | ✅ |
| Funktion endet sofort | ❌ | ✅ |

**Ohne `return`** gibt eine Funktion automatisch **`None`** zurück – „nichts":

```python
def zeige_status():
    print("Alle Systeme laufen.")

ergebnis = zeige_status()
print(f"Rückgabewert: {ergebnis}")
```

Der Status wird angezeigt, aber `ergebnis` ist `None`. Wenn du mit dem Ergebnis rechnen willst, brauchst du `return`!

> ⚠️ Der häufigste Anfängerfehler: Man berechnet etwas in der Funktion, vergisst aber `return` – und bekommt `None` zurück.
