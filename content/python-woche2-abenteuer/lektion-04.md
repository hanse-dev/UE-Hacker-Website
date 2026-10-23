# 🪨 Erde: Ganze Zahlen (`int`)

Das Erde-Element ist eine **ganze Zahl**: Level, Gold, Lebenspunkte. Sie steht **ohne** Anführungszeichen.

```python
level = 12
lebenspunkte = 150
print(f"Level: {level}, LP: {lebenspunkte}")
print(type(level))     # <class 'int'>
```

Mit Erd-Elementen kannst du rechnen: `+` (plus), `-` (minus), `*` (mal) und `/` (geteilt).

> 🧮 Python rechnet wie in Mathe **Punkt vor Strich**: erst `*` und `/`, dann `+` und `-`. Soll etwas zuerst gerechnet werden, setz Klammern: `(2 + 3) * 4` ergibt `20`, aber `2 + 3 * 4` ergibt `14`.

```python
tage = 3
gold_pro_tag = 45
print(f"Gesamt: {tage * gold_pro_tag}")
```
