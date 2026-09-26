# Zahlen und Rechnen 🔢

Python kann rechnen! Nutze `+`, `-`, `*` und `/` genauso wie in der Schule.

```python
aepfel = 5
birnen = 3
obst = aepfel + birnen
print(obst)  # gibt 8 aus
```

Und mit Variablen macht es noch mehr Spaß, weil du dieselbe Rechnung immer wieder mit anderen Zahlen benutzen kannst:

```python
punkte = 10 * 3
print(punkte)  # gibt 30 aus
```

Es gibt noch zwei nützliche Rechenzeichen, die du vielleicht noch nicht kennst:

```python
print(17 // 5)  # 3 – ganzzahlige Division, der Rest wird abgeschnitten
print(17 % 5)   # 2 – der Rest, der bei 17 : 5 übrig bleibt
```

`//` ist praktisch, wenn du z.B. wissen willst, wie viele volle Sechserpackungen Eier du aus 20 Eiern bekommst (`20 // 6` → 3 Packungen), und `%` sagt dir, wie viele dann noch übrig sind (`20 % 6` → 2 Eier).

Python rechnet übrigens genau wie in der Mathematik gelernt – **Punkt vor Strich**. Bei Unsicherheit helfen Klammern:

```python
ergebnis = (2 + 3) * 4
print(ergebnis)  # gibt 20 aus, nicht 14!
```
