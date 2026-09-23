# Buchstaben verschieben

Um einen Buchstaben zu verschieben, rechnest du mit seiner Zahl aus `ord()` weiter und wandelst das Ergebnis mit `chr()` wieder in einen Buchstaben um. So läuft das Prinzip ab:

```
start = Zeichencode von 'a'
position = Zeichencode des Buchstabens minus start
neue_position = (position + Verschiebung) modulo 26
neuer_buchstabe = Buchstabe zum Zeichencode (start + neue_position)
```

Das Modulo (`%`) sorgt für den Wraparound: Am Ende des Alphabets geht es wieder bei `a` weiter. Ohne das Modulo würde ein Buchstabe nahe am Ende des Alphabets bei einer Verschiebung auf ein Zeichen *hinter* `z` landen – mit Modulo springt die Zählung korrekt wieder an den Alphabet-Anfang zurück.

> 💡 Schleifen und Modulo aus [Woche 4 – Schleifen](/kurs/python-12-wochen-grundkurs?week=4&tab=lektion#woche-4) helfen dir gleich in der nächsten Lektion weiter.
