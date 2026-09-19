## 🏇 Übung 3: range(start, ende, schritt)

Die dritte Zahl ist die **Schrittweite**. Damit überspringst du Zahlen:

```python
for hurde in range(0, 11, 2):
    print(f"Hürde {hurde}: Gesprungen!")
```

Das gibt 0, 2, 4, 6, 8, 10 aus – jede zweite Hürde.

Mit einer **negativen** Schrittweite zählst du **rückwärts**:

```python
for i in range(5, 0, -1):
    print(f"{i}...")
print("🏇 LOS!")
```

> 💡 Das `print("🏇 LOS!")` ist **nicht eingerückt** – es gehört nicht mehr zur Schleife und läuft erst **nach** allen Durchläufen.
