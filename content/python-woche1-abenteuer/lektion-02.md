# 🧰 Zauberformel 2: Magische Behälter

Eine Variable ist wie eine **beschriftete Schatztruhe**: Du gibst ihr einen Namen und kannst darin etwas aufbewahren – und später wieder nachschauen.

```python
name = "Aragorn"   # die Truhe heißt 'name', drin liegt der Text "Aragorn"
level = 5          # die Truhe heißt 'level', drin liegt die Zahl 5
```

**Die zwei häufigsten Arten von Werten:**

| Art | Fachbegriff | Beispiel | Erkennungszeichen |
|-----|------------|---------|------------------|
| Text | **String** | `"Hallo"` | Anführungszeichen |
| Ganze Zahl | **Integer** | `42` | keine Anführungszeichen |

Variablen können sich **ändern**: Legst du einen neuen Wert in dieselbe Truhe, ist der alte weg.

```python
gold = 50
gold = 150      # jetzt liegen 150 Gold in der Truhe
print(gold)
```

Willst du sehen, was in der Truhe liegt, schreibst du den Namen **ohne** Anführungszeichen: `print(gold)` zeigt `150`. Mit Anführungszeichen, also `print("gold")`, zeigt Python nur das Wort gold.
