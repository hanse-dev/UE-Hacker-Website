# Warum ist Vigenère schwerer zu knacken?

Erinnere dich an deinen Brute-Force-Knacker aus dem Cäsar-Projekt: Weil es nur 26 mögliche Verschiebungen gibt, konntest du einfach alle durchprobieren. Bei der Vigenère-Chiffre hängt die Anzahl der Möglichkeiten vom **Schlüsselwort** ab – und die Zahl explodiert, je länger es ist:

- Schlüsselwort mit 1 Buchstabe: 26 Möglichkeiten (das ist eigentlich nur eine Cäsar-Chiffre in Verkleidung!)
- Schlüsselwort mit 3 Buchstaben: 26 × 26 × 26 = 17.576 Möglichkeiten
- Schlüsselwort mit 8 Buchstaben: über 200 Milliarden Möglichkeiten

Ein Geheimtext mit einem einzelnen Buchstaben als Schlüsselwort lässt sich also genau wie eine Cäsar-Chiffre knacken:

```python
geheim = "surmhnw"
for versuch in range(26):
    schluessel = chr(ord('a') + versuch)
    print(versuch, schluessel, entschluesseln(geheim, schluessel))
```

Eine der 26 Zeilen ergibt ein lesbares Wort. Schon bei einem 3-Buchstaben-Schlüsselwort müsstest du 17.576 statt 26 Möglichkeiten durchprobieren – und ohne zu wissen, *wie lang* das Schlüsselwort überhaupt ist, wird das schnell aussichtslos. Genau deshalb galt die Vigenère-Chiffre jahrhundertelang als unknackbar.

> 💡 Damit hast du dein zweites eigenes Verschlüsselungsprojekt gebaut – und verstanden, warum ein längeres Schlüsselwort echten Schutz bietet.
