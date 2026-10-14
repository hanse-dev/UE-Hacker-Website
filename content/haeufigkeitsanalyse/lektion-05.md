# Die Verschiebung erraten

Du weißt jetzt: Im Geheimtext ist `o` der häufigste Buchstabe. Und in deutschen Texten ist das `e` der häufigste. Die Vermutung liegt nahe: **Aus jedem `e` wurde ein `o`.**

Dann musst du nur noch ausrechnen, wie weit die beiden im Alphabet auseinanderliegen – genau wie im Cäsar-Projekt mit `ord()`:

```python
print(ord('h') - ord('e'))   # 3 – wäre 'h' am häufigsten, wäre die Verschiebung 3
```

Eine Falle gibt es: Liegt der häufigste Geheimbuchstabe im Alphabet **vor** dem `e` (zum Beispiel `c`), wird das Ergebnis negativ. Das passiert, wenn beim Verschlüsseln über das `z` hinaus wieder vorne angefangen wurde. Der Wraparound-Trick aus dem Cäsar-Projekt repariert das: Hänge `% 26` an, dann landet das Ergebnis immer zwischen 0 und 25.

```python
print((ord('c') - ord('e')) % 26)   # 24 statt -2
```

So läuft das Prinzip ab:

```
def errate_verschiebung(text):
    finde den häufigsten Buchstaben im text (deine Funktion aus Lektion 4)
    berechne seinen Abstand zum 'e' mit ord() und % 26
    gib diesen Abstand zurück
```

Wichtig: Das Ergebnis ist eine **Vermutung**, kein Beweis. Sie stimmt, wenn der Text lang genug ist und normales Deutsch enthält. Ob sie stimmt, siehst du in der nächsten Lektion – wenn du damit entschlüsselst.

> 💡 `ord()` und den Wraparound mit `% 26` kennst du aus [Lektion 1 und 2 des Cäsar-Projekts](/kurs/projekt-caesar-chiffre).
