# 🌳 Ein Baum lernt die Schieflage mit

Die stumpfe Basislinie ist ein Extremfall – aber übernimmt ein **echter** Entscheidungsbaum (wie
in Woche 5) das Problem auch, wenn er mit einem schiefen Datensatz trainiert wird? `bester_schwellenwert()`
sucht den Trennwert mit den **wenigsten Gesamt-Fehlern** – und wenn eine Klasse nur 2 von 10
Beispielen ausmacht, kann es günstiger sein, sie komplett zu ignorieren, als für sie extra einen
Trennwert zu suchen.

```python
baum = baue_baum(tickets, "wartezeit", "dringend")
print(baum)
print(genauigkeit_je_klasse(tickets, "dringend", lambda b: klassifiziere(baum, b)))
```

Mit den acht "nicht dringend"- und zwei "dringend"-Tickets aus Lektion 1 findet
`bester_schwellenwert()` einen Trennwert, bei dem **beide Seiten** mehrheitlich "nein" sind – der
Baum sagt also, genau wie die Basislinie, praktisch immer "nicht dringend" voraus. Er hat das
Merkmal `wartezeit` benutzt, aber effektiv **nichts über die dringenden Tickets gelernt**. Auch ein
"intelligenter" Algorithmus ist also nicht automatisch fair – er optimiert stur die Zahl, die man
ihm vorgibt (hier: Gesamt-Fehler), und Gesamt-Fehler bestraft das Ignorieren einer kleinen Klasse
kaum.
