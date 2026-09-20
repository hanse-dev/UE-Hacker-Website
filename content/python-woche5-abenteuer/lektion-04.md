# 🎁 Zauberformel 2: Werte zurückgeben mit return

Bisher haben deine Formeln etwas **ausgegeben**. Oft willst du aber ein **Ergebnis**, mit dem du weiterarbeiten kannst. Dafür gibt es **`return`**:

```python
def berechne_schaden(basis, multiplikator):
    return basis * multiplikator

schaden = berechne_schaden(10, 2)
print(f"Schlag: {schaden} Schaden")
print(f"Kritisch: {berechne_schaden(20, 5)} Schaden")
```

**Was `return` tut:**
- Es **beendet** die Funktion sofort
- Es **schickt einen Wert zurück** an die Stelle, an der du die Funktion aufgerufen hast
- Diesen Wert kannst du in einer **Variable speichern** (`schaden = ...`) oder direkt weiterverwenden (z. B. in `print` oder in einer Rechnung)

> 💡 Stell dir `berechne_schaden(10, 2)` wie einen Platzhalter vor: Nach dem Aufruf steht dort einfach das Ergebnis `20`.
