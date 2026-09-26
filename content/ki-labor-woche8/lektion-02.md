# 🎭 Der Trick mit der Genauigkeit

Stell dir vor, ein Modell für die Ticket-Dringlichkeit sagt bei **jedem** Ticket einfach "nicht
dringend" voraus – egal, was drinsteht. Bei 8 von 10 nicht-dringenden Tickets in den Daten hat
diese stumpfe Basislinie trotzdem eine **Gesamt-Genauigkeit von 80%**. Klingt gut – ist es aber
nicht: Sie erkennt **kein einziges** dringendes Ticket.

Die Gesamt-Genauigkeit (wie in Woche 4) versteckt genau dieses Problem, weil sie über alle Klassen
gemittelt wird. Die Lösung: die Genauigkeit **je Klasse einzeln** messen.

```python
def genauigkeit(vorhersagen, erwartete_werte):
    richtig = 0
    for i in range(len(vorhersagen)):
        if vorhersagen[i] == erwartete_werte[i]:
            richtig += 1
    return round(richtig / len(vorhersagen) * 100)

def genauigkeit_je_klasse(daten, label_feld, vorhersage_funktion):
    ergebnis = {}
    for klasse in anzahl_je_klasse(daten, label_feld):
        teil = [b for b in daten if b[label_feld] == klasse]
        vorhersagen = [vorhersage_funktion(b) for b in teil]
        erwartete_werte = [klasse for _ in teil]
        ergebnis[klasse] = genauigkeit(vorhersagen, erwartete_werte)
    return ergebnis
```

`genauigkeit_je_klasse()` filtert die Daten für jede Klasse einzeln heraus und berechnet die
Genauigkeit nur innerhalb dieser Gruppe. Für die "immer nicht dringend"-Basislinie zeigt das
gnadenlos: `{"nein": 100, "ja": 0}` – 100% bei der häufigen Klasse, 0% bei der seltenen. Genau
dieses Muster ist **Bias** (Verzerrung) durch schiefe Trainingsdaten: Das Modell hat gelernt, die
seltene Klasse zu ignorieren, weil das die Gesamt-Genauigkeit kaum verschlechtert.
