# 🐴 Woche 3: Die Weichen des Reitwegs

Willkommen, Pferdefreund! Du erreichst den **Scheideweg der Weide** – hier entscheidet jede Wahl über den richtigen Reitweg. In dieser Woche lernst du, wie dein Programm **Entscheidungen** trifft:

1. **if** – Code nur ausführen, wenn etwas stimmt
2. **Vergleichsoperatoren** – `==`, `!=`, `<`, `>`, `<=`, `>=`
3. **if-else** – zwei Wege
4. **if-elif-else** – viele Wege
5. **and, or, not** – Bedingungen verknüpfen
6. **Verschachtelte Bedingungen** – Entscheidung in der Entscheidung

Reite weise! Dein Pferd vertraut auf dich...

## 🚦 Übung 1: if

`if` prüft eine **Bedingung** und führt den Code darunter **nur aus, wenn die Bedingung wahr (`True`) ist**.

```python
alter_pferd = 5
if alter_pferd >= 5:
    print("Das Pferd ist reif für das Training!")
```

> ⚠️ **Wichtig:** Nach der Bedingung steht ein **Doppelpunkt `:`**, und der Code, der dazugehört, wird **eingerückt** (4 Leerzeichen bzw. Tab-Taste). Die Einrückung zeigt Python, was zum `if` gehört.

Eine Bedingung kann auch direkt ein Wahrheitswert (`bool`) aus Woche 2 sein:

```python
hat_sattel = True
if hat_sattel:
    print("Du kannst aufsteigen!")
```

Ist die Bedingung `False`, wird der eingerückte Code einfach übersprungen.
