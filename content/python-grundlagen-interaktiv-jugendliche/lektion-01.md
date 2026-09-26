# Dein erstes Programm

Ein Programm ist eine Abfolge von Anweisungen, die der Computer der Reihe nach ausführt. `print()` gibt Text oder Werte auf der Konsole aus – es ist die grundlegendste Python-Funktion, du wirst sie in jedem Programm wiederfinden, ob zum Debuggen oder als echte Ausgabe.

```python
print("Hallo Welt")
print(42)
print(3.14)
```

Text steht in Anführungszeichen (`"..."`) – das nennt man einen **String**. Zahlen schreibst du ohne Anführungszeichen. Der Unterschied ist wichtig: `print("42")` gibt den Text "42" aus, `print(42)` die Zahl 42 – für Python sind das zwei völlig unterschiedliche Dinge (mehr dazu in der Lektion zu Datentypen).

Jeder `print()`-Aufruf erzeugt eine neue Zeile in der Ausgabe:

```python
print("Zeile 1")
print("Zeile 2")
```

Mit `#` schreibst du Kommentare – Python ignoriert alles nach dem `#` bis zum Zeilenende. Wichtig für Erklärungen im Code, gerade wenn andere (oder du selbst, später) den Code lesen müssen.

```python
# Berechnet den Gesamtpreis inklusive Versand
print(29.99 + 4.99)
```

Ein fehlendes Anführungszeichen führt zu einem `SyntaxError` – der Code lässt sich dann gar nicht erst ausführen. Solche Fehler gehören zum Programmieralltag; die Fehlermeldung verrät meist genau, in welcher Zeile das Problem steckt.
