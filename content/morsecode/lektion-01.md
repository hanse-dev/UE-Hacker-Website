# Ein Buchstabe wird zu Punkten und Strichen

Morsecode übersetzt jeden Buchstaben in eine eigene Folge aus Punkten (`.`) und Strichen (`-`). Das berühmteste Beispiel ist der Notruf **SOS**: `... --- ...` – drei Punkte, drei Striche, drei Punkte.

Damit dein Programm weiß, welcher Buchstabe zu welchem Code gehört, brauchst du ein **Dictionary** – eine Zuordnung von Schlüssel zu Wert, hier von Buchstabe zu Morsezeichen:

```python
MORSE = {
    'a': '.-', 'b': '-...', 'c': '-.-.', 'd': '-..', 'e': '.', 'f': '..-.',
    'g': '--.', 'h': '....', 'i': '..', 'j': '.---', 'k': '-.-', 'l': '.-..',
    'm': '--', 'n': '-.', 'o': '---', 'p': '.--.', 'q': '--.-', 'r': '.-.',
    's': '...', 't': '-', 'u': '..-', 'v': '...-', 'w': '.--', 'x': '-..-',
    'y': '-.--', 'z': '--..'
}

print(MORSE['a'])   # .-
```

Mit `MORSE['a']` holst du dir das Morsezeichen für `'a'` aus dem Dictionary.

> 💡 Falls dir Dictionaries noch nicht so vertraut sind, wirf einen Blick in [Woche 8 – Steckbriefe und Artefakte](/kurs/python-12-wochen-grundkurs?week=8&tab=lektion#woche-8) des 12-Wochen-Kurses.
