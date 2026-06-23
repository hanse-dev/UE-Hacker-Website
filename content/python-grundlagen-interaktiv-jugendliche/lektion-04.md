# f-Strings

f-Strings sind die modernste Art, Variablen in Strings einzubetten (seit Python 3.6). Schneller zu lesen als Konkatenation mit `+`.

```python
name = "Alex"
follower = 1200
print(f"{name} hat {follower} Follower.")
```

In `{}` können auch Ausdrücke stehen:

```python
preis = 29.99
print(f"Preis mit MwSt: {preis * 1.19:.2f} €")
```
