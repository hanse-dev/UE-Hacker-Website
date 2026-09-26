# Übung: Alles zusammen

Kombiniere Variablen, Listen, Schleifen, Funktionen und Dictionaries. Das sind die Grundbausteine, mit denen sich schon ein großer Teil realer Python-Programme schreiben lässt – von kleinen Skripten bis zu Web-Backends und Datenanalysen.

```python
def analysiere(zahlen):
    gesamt = sum(zahlen)
    durchschnitt = gesamt / len(zahlen)
    print(f"Summe: {gesamt}, Durchschnitt: {durchschnitt}")

noten = [85, 92, 78, 96, 88]
analysiere(noten)
```

In diesem Beispiel steckt praktisch alles, was du bisher gelernt hast: eine Liste (`noten`), eine Funktion, die diese Liste als Parameter entgegennimmt, eingebaute Funktionen (`sum()`, `len()`) statt selbstgeschriebener Schleifen, und ein f-String für die formatierte Ausgabe.

Das zeigt auch ein wichtiges Prinzip: Bevor du selbst eine Schleife schreibst, um z.B. eine Summe zu berechnen, lohnt sich ein Blick, ob Python nicht schon eine eingebaute Funktion dafür hat (`sum()`, `max()`, `min()`, `len()`, `sorted()` …) – das spart Code und ist meist auch schneller.

Du bist bereit für den 12-Wochen Python Grundkurs! Dort baust du dieses Wissen zu größeren Projekten aus – inklusive eigener Klassen, Fehlerbehandlung und einem eigenen Abschlussprojekt.
