# 🔄 Systemprotokoll 5: Typen umwandeln

Sensoren liefern Daten oft als **Text**: `"273"` ist ein String, mit dem du nicht rechnen kannst. Die Lösung sind vier **Systemprotokolle** (Funktionen) zum Umwandeln – du gibst den Wert in die Klammern, sie liefern ihn im neuen Typ zurück:

| Funktion | Macht daraus | Beispiel | Ergebnis |
|---|---|---|---|
| `int()` | ganze Zahl | `int("273")` | `273` |
| `float()` | Kommazahl | `float("42.5")` | `42.5` |
| `str()` | Text | `str(5)` | `"5"` |
| `bool()` | Ja/Nein | `bool(1)` | `True` |

`bool()` liefert bei `0` und leerem Text `""` den Wert `False`, sonst `True`.

```python
temperatur_str = "273"
temperatur_int = int(temperatur_str)
print(temperatur_int + 1)   # 274 – jetzt kannst du rechnen!
```

## Eingaben des Benutzers

Auch `input()` (aus Woche 1) liefert **immer** einen String – auch wenn jemand eine Zahl tippt. Wandle die Antwort erst um:

```python
alter = int(input("Wie alt ist dein Schiff? "))
print(alter + 1)
```

> 📡 **Merke:** Bekommst du `"80" - 30`-Fehler, ist meist ein Text im Spiel, der eine Zahl sein sollte – `int()` oder `float()` hilft!
