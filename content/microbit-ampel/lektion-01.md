# Startklar: Breadboard und erste LED

Ihr arbeitet zu zweit. Damit beide etwas davon haben, gibt es zwei Rollen:

- **Bauprofi:** steckt die Schaltung auf dem Breadboard und prüft sie.
- **Programmierprofi:** sitzt an der Tastatur und baut das Programm.

Nach jeder Stufe tauscht ihr die Rollen.

## Drei Regeln für die Schaltung

> 1. Gesteckt und umgesteckt wird nur, wenn das USB-Kabel **nicht** eingesteckt ist.
> 2. Jede LED bekommt ihren eigenen Widerstand. Ohne Widerstand kann die LED oder der micro:bit kaputtgehen.
> 3. Steckt nie ein Kabel direkt von einem Pin oder von **3V** zu **GND**. Das ist ein Kurzschluss.

## Euer Material

- **micro:bit:** Er steckt oben im schwarzen Schlitz der Platine, die Seite mit den 25 Lampen zeigt nach oben. Er bleibt die ganze Zeit dort.
- **Platine:** Die Stifte neben dem Breadboard führen zu den Pins des micro:bit. Neben jedem Stift steht sein Name: **P0**, **P1** und so weiter. Die Stifte mit **GND** sind der Minuspol, es gibt fünf davon.
- **Steckkabel:** Die Buchse kommt auf einen Stift der Platine, der Stecker ins Breadboard.
- **LED:** eine kleine Lampe. Sie hat ein langes Bein (Plus) und ein kurzes Bein (Minus). Strom fließt nur vom langen zum kurzen Bein. Steckt sie falsch herum, bleibt sie dunkel. Davon geht sie aber nicht kaputt.
- **Widerstand:** bremst den Strom, damit die LED nicht zu viel davon bekommt. Wie herum er steckt, ist egal. Eure Widerstände haben 150 Ω (Ohm) und die Farbringe braun, grün, schwarz, schwarz, braun.

## So funktioniert das Breadboard

Mit einem Breadboard verbindet ihr Bauteile, ohne zu löten. Haltet die Platine so, dass der micro:bit oben ist. Dann zählt ihr die Reihen von oben nach unten: Reihe 1 bis Reihe 17.

<img src="/microbit/ampel/breadboard.svg" alt="Breadboard mit 17 Reihen: Die Löcher einer Reihe sind links und rechts der Lücke jeweils verbunden">

- **Die Löcher einer Reihe sind verbunden.** Unter jeder Reihe liegt ein Metallstreifen. Was ihr in dieselbe Reihe steckt, ist miteinander verbunden.
- **Die Lücke trennt.** In der Mitte läuft eine Lücke von oben nach unten. Links und rechts davon sind zwei getrennte Streifen.
- **Reihe unter Reihe ist getrennt.** Reihe 10 und Reihe 11 haben nichts miteinander zu tun.
- **Links sind nur zwei Löcher frei,** die übrigen liegen unter der Platine. Rechts sind es fünf.

Darum legt ihr jeden Widerstand **über die Lücke**: Er verbindet den linken Streifen einer Reihe mit dem rechten.

## Der Stromkreis

Eine LED leuchtet nur, wenn der Strom einen geschlossenen Kreis hat:

**Pin** → Kabel → **Widerstand** → langes Bein der **LED** → kurzes Bein → Kabel → **GND**

Jede LED in diesem Kurs ist genau so angeschlossen. Wenn ihr den Kreis einmal verstanden habt, könnt ihr jede weitere LED allein stecken.

## Die erste LED stecken

Die erste LED ist die rote Lampe der Fußgängerampel. Sie bleibt bis zum Schluss stecken.

<img src="/microbit/ampel/stufe-0.svg" alt="Steckplan: Kabel von P13 in Reihe 10 links, Widerstand über die Lücke, rote LED mit langem Bein in Reihe 10 rechts und kurzem Bein in Reihe 11, Kabel von Reihe 11 zu GND">

1. Zieht das USB-Kabel ab.
2. **Widerstand:** ein Bein in Reihe 10 links, direkt an der Lücke. Das andere Bein in Reihe 10 rechts, direkt an der Lücke.
3. **Rote LED:** langes Bein in Reihe 10 rechts, kurzes Bein in Reihe 11 rechts.
4. **Kabel von P13:** Buchse auf den Stift **P13**, Stecker in Reihe 10 links ins freie Loch.
5. **Kabel zu GND:** Buchse auf einen Stift **GND**, Stecker in Reihe 11 rechts ins äußerste Loch.

Fahrt den Weg des Stroms mit dem Finger nach: P13, Reihe 10 links, Widerstand, Reihe 10 rechts, langes Bein, kurzes Bein, Reihe 11 rechts, GND. Ist der Kreis geschlossen?

## Editor einrichten

Oben auf dieser Seite wählt ihr, wie die Anleitung den Code zeigt.

- **Blöcke:** Ihr steckt farbige Bausteine zusammen. Gut, wenn ihr noch nie programmiert habt.
- **Python:** Ihr schreibt Text. Gut, wenn ihr Python schon ein wenig kennt.

:::bloecke

Öffnet [makecode.microbit.org](https://makecode.microbit.org) und klickt auf **Neues Projekt**. Die Blöcke für die Pins findet ihr in der Blockliste unter **Fortgeschritten** und dann **Pins**.

:::

:::python

Öffnet [python.microbit.org](https://python.microbit.org). Der Editor zeigt schon ein kleines Programm an. Löscht es, bevor ihr eures schreibt.

:::

## Das erste Programm

Ein Pin kann zwei Zustände haben: **1** heißt Strom an, **0** heißt Strom aus. Dieses Programm lässt die LED an P13 ohne Ende blinken.

:::bloecke

```bloecke
[grundlagen] dauerhaft
  [pins] schreibe digitalen Wert von Pin P13 auf 1
  [grundlagen] pausiere (ms) 500
  [pins] schreibe digitalen Wert von Pin P13 auf 0
  [grundlagen] pausiere (ms) 500
```

Alles im Block **dauerhaft** wiederholt sich immer wieder. **pausiere (ms) 500** wartet 500 Millisekunden, also eine halbe Sekunde.

:::

:::python

```python
from microbit import *

while True:
    pin13.write_digital(1)
    sleep(500)
    pin13.write_digital(0)
    sleep(500)
```

Alles, was unter `while True:` eingerückt ist, wiederholt sich immer wieder. `sleep(500)` wartet 500 Millisekunden, also eine halbe Sekunde.

:::

## Auf den micro:bit übertragen

1. Steckt das USB-Kabel in den micro:bit, nicht in die Platine.

:::bloecke

2. Klickt auf die drei Punkte neben **Herunterladen** und wählt **Gerät verbinden**. Danach reicht ein Klick auf **Herunterladen**.

:::

:::python

2. Klickt auf **An micro:bit senden** und folgt den Schritten zum Verbinden.

:::

Klappt das Verbinden nicht? Dann speichert das Programm als Datei und zieht sie auf das Laufwerk **MICROBIT**.

## Die LED bleibt dunkel?

Geht diese Liste der Reihe nach durch. Zieht vorher das USB-Kabel ab.

1. **LED umdrehen.** Das ist der häufigste Fehler. Das lange Bein gehört in die Reihe mit dem Widerstand.
2. **Reihen zählen.** Stecken alle Beine und Kabel in den Reihen aus dem Steckplan?
3. **Lücke prüfen.** Liegt der Widerstand wirklich über der Lücke und nicht daneben?
4. **Pin prüfen.** Steckt das Kabel auf **P13** und nicht auf dem Stift daneben?
5. **GND prüfen.** Steckt das zweite Kabel auf einem Stift mit **GND**?
6. **Programm prüfen.** Steht im Programm P13? Habt ihr es übertragen?

## Bonus: Der Herzschlag

Lasst die LED wie ein Herz schlagen: zweimal kurz hintereinander aufleuchten, dann eine längere Pause, und das ohne Ende.

<details>
<summary>Tipps anzeigen</summary>

- Schreibt den Ablauf zuerst in Worten auf: an, kurz warten, aus, kurz warten, an, ...
- Ein kurzer Schlag dauert etwa 150 Millisekunden, die lange Pause etwa 700.
- Ihr braucht keine neuen Blöcke oder Befehle, nur mehr von denselben.

</details>
