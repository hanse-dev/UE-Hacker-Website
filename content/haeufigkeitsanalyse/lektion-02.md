# Alle Buchstaben auf einmal zählen

Einen Buchstaben zählen kannst du jetzt. Aber für die Häufigkeitsanalyse brauchst du die Anzahl von **allen** Buchstaben – und 26 einzelne Zähler wären ziemlich mühsam.

Die Lösung ist ein **Dictionary**: Der Schlüssel ist der Buchstabe, der Wert ist seine Anzahl. Für das Wort `"otto"` sähe das fertige Dictionary so aus:

```python
{'o': 2, 't': 2}
```

Du gehst den Text nur ein einziges Mal durch und führst für jeden Buchstaben Buch. So läuft das Prinzip ab:

```
def zaehle_buchstaben(text):
    zaehlung = {}   (ein leeres Dictionary)
    für jedes zeichen in text:
        wenn zeichen ein Buchstabe ist (isalpha()):
            wenn zeichen schon in zaehlung steht:
                erhöhe zaehlung[zeichen] um eins
            sonst:
                setze zaehlung[zeichen] auf 1
    gib zaehlung zurück
```

Die `isalpha()`-Prüfung kennst du aus dem Cäsar-Projekt: Leerzeichen, Punkte und Kommas sollen nicht mitgezählt werden – die verschiebt Cäsar ja auch nicht.

Mit `zeichen in zaehlung` fragst du, ob es für diesen Buchstaben schon einen Eintrag gibt. Das ist wichtig: Einen Eintrag, den es noch nicht gibt, kannst du nicht um eins erhöhen – Python meldet dann einen `KeyError`.

> 💡 Falls dir Dictionaries noch nicht so vertraut sind, wirf einen Blick in [Woche 8](/kurs/python-12-wochen-grundkurs?week=8&tab=lektion#woche-8) des 12-Wochen-Kurses oder in das [Morsecode-Projekt](/kurs/projekt-morsecode).
