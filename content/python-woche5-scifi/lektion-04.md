# 📦 Systemprotokoll 4: Werte zurückgeben mit return

Bisher haben deine Protokolle etwas **ausgegeben**. Oft willst du aber ein **Ergebnis**, mit dem du weiterarbeiten kannst. Dafür gibt es **`return`**:

```python
def berechne_verbrauch(module, leistung):
    return module * leistung

verbrauch = berechne_verbrauch(3, 20)
print(f"Verbrauch: {verbrauch} kW")
print(f"Volllast: {berechne_verbrauch(10, 50)} kW")
```

**Was `return` tut:**
- Es **beendet** die Funktion sofort
- Es **schickt einen Wert zurück** an die Stelle, an der du die Funktion aufgerufen hast
- Diesen Wert kannst du in einer **Variable speichern** (`verbrauch = ...`) oder direkt weiterverwenden (z. B. in `print` oder in einer Rechnung)

> 💡 Stell dir `berechne_verbrauch(3, 20)` wie einen Platzhalter vor: Nach dem Aufruf steht dort einfach das Ergebnis `60`.
