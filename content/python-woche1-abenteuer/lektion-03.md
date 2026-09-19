# 🔗 Zauberformel 3: Texte verbinden

Mit `+` kannst du Texte zusammenkleben – wie Bausteine aneinanderlegen.

```python
print("Held: " + name)
```

## Warum brauche ich `str()`?

Python behandelt Text und Zahlen als verschiedene *Typen*. Das ist wie Äpfel und Orangen – man kann sie nicht einfach zusammenzählen. `str()` ist ebenfalls eine Zauberformel (Funktion): Du gibst ihr eine Zahl in die Klammern, und sie liefert dir den passenden Text zurück. `str()` verwandelt eine Zahl in Text, sodass sie sich verbinden lässt:

```python
gold = 50
print("Gold: " + gold)       # ❌ Fehler – Zahl und Text passen nicht zusammen
print("Gold: " + str(gold))  # ✅ klappt – str() macht aus 50 den Text "50"
```

So baust du ganze Sätze:

```python
print(name + " hat einen " + waffe + " mit " + str(pfeile) + " Pfeilen.")
```
