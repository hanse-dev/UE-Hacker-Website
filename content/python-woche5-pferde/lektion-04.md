# 🎁 Übung 4: Werte zurückgeben mit return

Bisher haben deine Routinen etwas **ausgegeben**. Oft willst du aber ein **Ergebnis**, mit dem du weiterarbeiten kannst. Dafür gibt es **`return`**:

```python
def berechne_strecke(runden, laenge):
    return runden * laenge

strecke = berechne_strecke(3, 200)
print(f"Strecke: {strecke} m")
print(f"Lange Runde: {berechne_strecke(5, 400)} m")
```

**Was `return` tut:**
- Es **beendet** die Funktion sofort
- Es **schickt einen Wert zurück** an die Stelle, an der du die Funktion aufgerufen hast
- Diesen Wert kannst du in einer **Variable speichern** (`strecke = ...`) oder direkt weiterverwenden (z. B. in `print` oder in einer Rechnung)

> 💡 Stell dir `berechne_strecke(3, 200)` wie einen Platzhalter vor: Nach dem Aufruf steht dort einfach das Ergebnis `600`.
