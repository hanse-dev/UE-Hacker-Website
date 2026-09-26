# 🧠 Was ist ein künstliches Neuron?

Ein **künstliches Neuron** (auch **Perzeptron** genannt) trifft eine Ja/Nein-Entscheidung anhand
mehrerer Eingaben – ähnlich wie der Entscheidungsbaum aus Woche 5, aber statt eines einzigen
Merkmals mit einem Schwellenwert kombiniert es **mehrere** Eingaben gleichzeitig: Jede Eingabe
bekommt ein **Gewicht** (wie wichtig sie ist), alle gewichteten Eingaben werden aufsummiert, und
diese Summe wird am Ende mit einem **Schwellenwert** verglichen.

Stell dir einen Rauchmelder vor, der zwei Sensoren kombiniert: Rauch und Hitze. Rauch ist
wichtiger als Hitze, bekommt also ein größeres Gewicht:

```python
def neuron(eingaben, gewichte, schwelle):
    summe = 0
    for i in range(len(eingaben)):
        summe += eingaben[i] * gewichte[i]
    if summe >= schwelle:
        return 1
    else:
        return 0

print(neuron([1, 0], [2, 3], 2))
print(neuron([0, 0], [2, 3], 2))
```

`eingaben[i] * gewichte[i]` ist der gewichtete Beitrag jeder einzelnen Eingabe, die Summe aller
Beiträge nennt man die **gewichtete Summe**. Erreicht oder übertrifft sie den Schwellenwert, "feuert"
das Neuron (gibt `1` zurück) – sonst bleibt es still (`0`). In den nächsten Lektionen zerlegst du
diese eine Funktion in wiederverwendbare Bausteine.
