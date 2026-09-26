# Bedingungen mit if

`if` führt Code nur aus, wenn eine Bedingung wahr ist. `elif` prüft weitere Bedingungen, `else` fängt den Rest ab.

```python
alter = 16
if alter >= 18:
    print("Zugang erlaubt")
elif alter >= 16:
    print("Eingeschränkter Zugang")
else:
    print("Kein Zugang")
```

Python prüft die Bedingungen von oben nach unten und führt nur den **ersten** zutreffenden Block aus – trifft `if alter >= 18` nicht zu, wird `elif alter >= 16` geprüft, und erst wenn auch das nicht zutrifft, kommt `else` zum Zug. Die Reihenfolge ist also entscheidend.

Vergleichsoperatoren: `==` (gleich – zwei Gleichheitszeichen, nicht zu verwechseln mit der Zuweisung `=`), `!=` (ungleich), `<`, `>`, `<=`, `>=`.

Mit `and` und `or` lassen sich mehrere Bedingungen kombinieren:

```python
alter = 15
hat_erlaubnis = True
if alter >= 16 or hat_erlaubnis:
    print("Zugang erlaubt")
```

`and` verlangt, dass **beide** Seiten wahr sind, `or` reicht schon, wenn **eine** der beiden Seiten wahr ist. Die Einrückung (4 Leerzeichen) ist in Python kein Stilmittel, sondern Teil der Syntax – sie legt fest, welcher Code zu welchem Block gehört.
