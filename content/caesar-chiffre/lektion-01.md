# Was ist eine Cäsar-Chiffre?

Vor über 2000 Jahren soll der römische Feldherr Julius Cäsar seine Befehle verschlüsselt haben, damit Feinde sie nicht lesen konnten. Sein Trick war einfach: Jeder Buchstabe wird im Alphabet um eine feste Anzahl Stellen verschoben. Verschiebt man z.B. um 3, wird aus `a` ein `d`, aus `b` ein `e`, und so weiter.

Damit du das in Python bauen kannst, brauchst du zwei Funktionen, die Buchstaben und Zahlen ineinander umwandeln:

- `ord(zeichen)` gibt die Zahl (den Zeichencode) eines Buchstabens zurück, z.B. `ord('a')` → `97`
- `chr(zahl)` macht das Gegenteil: aus einer Zahl wird wieder ein Buchstabe, z.B. `chr(97)` → `'a'`

```python
print(ord('m'))   # 109
print(chr(66))     # B
```

Mit diesen beiden Werkzeugen kannst du gleich Buchstaben "rechnen" – das ist die Grundlage der ganzen Cäsar-Chiffre.

> 💡 Falls dir Strings und Datentypen noch nicht so vertraut sind, wirf einen Blick in [Woche 2 – Datentypen](/kurs/python-12-wochen-grundkurs?week=2&tab=lektion#woche-2) des 12-Wochen-Kurses.
