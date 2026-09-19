# ⚖️ Zauberformel 2: if-else

Manchmal soll etwas passieren, wenn die Bedingung stimmt – **und etwas anderes**, wenn sie nicht stimmt. Dafür gibt es `else` ("sonst"):

```python
wurf = 18
if wurf >= 15:
    print("Kritischer Treffer!")
else:
    print("Normaler Schlag")
```

- `else` steht auf **derselben Höhe** wie das zugehörige `if`
- `else` braucht **keine Bedingung**, dafür aber auch einen Doppelpunkt
- Es wird genau **einer** der beiden Wege ausgeführt – nie beide, nie keiner
