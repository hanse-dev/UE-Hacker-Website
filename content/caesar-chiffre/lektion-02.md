# Buchstaben verschieben

Um einen Buchstaben zu verschieben, rechnest du mit seiner Zahl aus `ord()` weiter und wandelst das Ergebnis mit `chr()` wieder in einen Buchstaben um. Für `'b'` um 3 verschoben:

```python
start = ord('a')          # 97 – der Start des Alphabets
zahl = ord('b') - start   # Position von b im Alphabet: 1
neue_position = (zahl + 3) % 26
print(chr(start + neue_position))   # e
```

Das `% 26` (Modulo) sorgt für den Wraparound: Am Ende des Alphabets geht es wieder bei `a` weiter. Ohne das `% 26` würde aus `'y'` um 3 verschoben ein Zeichen *hinter* `z` werden – mit `% 26` wird daraus korrekt `'b'`.

> 💡 Schleifen und Modulo aus [Woche 4 – Schleifen](/kurs/python-12-wochen-grundkurs?week=4&tab=lektion#woche-4) helfen dir gleich in der nächsten Lektion weiter.
