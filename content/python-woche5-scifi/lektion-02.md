# 📡 Systemprotokoll 2: Ein Parameter

Bisher macht dein Protokoll jedes Mal dasselbe. Mit einem **Parameter** bekommt es eine **Eingabe**, die du bei jedem Aufruf ändern kannst:

```python
def melde(name):
    print(f"Hallo, {name}!")

melde("Nova")
melde("Kira")
```

**Schritt für Schritt:**
1. **`name`** in der Klammer ist der **Parameter** – ein Platzhalter
2. Beim Aufruf übergibst du ein **Argument**, z. B. `"Nova"`
3. In der Funktion ist `name` dann eine ganz normale **Variable** mit diesem Wert
4. Der nächste Aufruf bringt einen neuen Wert mit

> 💡 **Parameter** heißt die Eingabe in der Definition, **Argument** der Wert, den du beim Aufruf einsetzt.

Auch Zahlen funktionieren: `zeige_energie(80)` gibt der Funktion die Zahl 80 – ohne Anführungszeichen.
