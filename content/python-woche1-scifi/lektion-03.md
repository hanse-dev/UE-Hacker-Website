# 🔗 Systemprotokoll 3: Texte verbinden

Mit `+` kannst du Texte zusammenkleben – wie Bausteine aneinanderlegen.

```python
print("Schiff: " + schiff_name)
```

## Warum brauche ich `str()`?

Python behandelt Text und Zahlen als verschiedene *Typen*. Das ist wie Äpfel und Orangen – man kann sie nicht einfach zusammenzählen. `str()` ist ebenfalls eine Funktion: Du gibst ihr eine Zahl in die Klammern, und sie liefert dir den passenden Text zurück:

```python
mission = 5
print("Mission: " + mission)       # ❌ Fehler – Zahl und Text passen nicht zusammen
print("Mission: " + str(mission))  # ✅ klappt – str() macht aus 5 den Text "5"
```
