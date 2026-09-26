# f-Strings

f-Strings sind die modernste Art, Variablen in Strings einzubetten (seit Python 3.6). Schneller zu lesen als Konkatenation mit `+`.

```python
name = "Alex"
follower = 1200
print(f"{name} hat {follower} Follower.")
```

Der Unterschied zur älteren Schreibweise mit `+` fällt besonders bei mehreren Variablen auf – ohne f-String müsstest du jeden Wert einzeln mit `str()` umwandeln und verketten:

```python
# Ohne f-String – umständlicher und fehleranfälliger:
print(name + " hat " + str(follower) + " Follower.")

# Mit f-String – kürzer und klarer:
print(f"{name} hat {follower} Follower.")
```

In `{}` können auch beliebige Ausdrücke stehen, nicht nur einzelne Variablen – Python wertet sie zur Laufzeit aus:

```python
preis = 29.99
print(f"Preis mit MwSt: {preis * 1.19:.2f} €")
```

Der Teil nach dem Doppelpunkt (`:.2f`) ist eine Formatangabe – sie rundet die Zahl hier auf zwei Nachkommastellen. Ohne sie könnte das Ergebnis unschön viele Nachkommastellen haben (z.B. `35.6881` statt `35.69`).
