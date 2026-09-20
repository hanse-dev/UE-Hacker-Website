# 🧪 Zauberformel 1: Ein Parameter

Bisher macht deine Formel jedes Mal dasselbe. Mit einem **Parameter** bekommt sie eine **Zutat**, die du bei jedem Aufruf ändern kannst:

```python
def begruesse(name):
    print(f"Willkommen, {name}!")

begruesse("Aria")
begruesse("Thorin")
```

**Schritt für Schritt:**
1. **`name`** in der Klammer ist der **Parameter** – ein Platzhalter
2. Beim Aufruf übergibst du ein **Argument**, z. B. `"Aria"`
3. In der Funktion ist `name` dann eine ganz normale **Variable** mit diesem Wert
4. Der nächste Aufruf bringt einen neuen Wert mit

> 💡 **Parameter** heißt die Zutat in der Definition, **Argument** der Wert, den du beim Aufruf einsetzt.

Auch Zahlen funktionieren: `zeige_level(5)` gibt der Funktion die Zahl 5 – ohne Anführungszeichen.
