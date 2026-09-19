# 🌀 Zauberformel 3: Verschachtelte Schleifen

Im obersten Stock des Turms wartet die **Doppelspirale der Macht**. Eine Schleife kann eine weitere Schleife enthalten – man nennt das **Verschachtelung**. Die **innere** Schleife läuft bei **jedem einzelnen** Durchlauf der äußeren Schleife komplett durch.

```python
for aussen in range(3):
    for innen in range(2):
        print(f"aussen {aussen}, innen {innen}")
```

Dieser `print`-Code läuft **3 × 2 = 6 Mal**.

**Wichtig:** Jede zusätzliche Verschachtelungsebene braucht eine weitere **Einrückung**!

```python
for turm in range(1, 4):
    print(f"Turm {turm}:")
    for stockwerk in range(1, 3):
        print(f"  Stockwerk {stockwerk} wird durchsucht...")
```
