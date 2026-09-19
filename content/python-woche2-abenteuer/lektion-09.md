# 🔮 Zauberformel input(): Das Orakel befragen

`input()` ist eine Zauberformel (Funktion), die eine Frage stellt und die Antwort des Benutzers **zurückliefert**. In die Klammern kommt die Frage. Die Antwort ist immer ein **🔥 Feuer-Element (Text)** – auch wenn jemand eine Zahl tippt. Für 🪨 Erde oder 💧 Wasser musst du sie also umwandeln:

```python
name = input("Wie heißt du? ")             # Feuer (str)
alter = int(input("Wie alt bist du? "))    # Feuer -> Erde (str -> int)
```

Im Browser öffnet sich für `input()` ein Eingabefenster.
