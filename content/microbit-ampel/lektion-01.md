# Startklar: Breadboard und erste LED

## Drei Regeln für die Schaltung

> 1. Gesteckt und umgesteckt wird nur, wenn das USB-Kabel **nicht** eingesteckt ist.
> 2. Jede LED bekommt ihren eigenen Widerstand. Ohne Widerstand kann die LED oder der micro:bit kaputtgehen.
> 3. Steckt nie ein Kabel von einem Pin oder von **3.3V** direkt zu **GND** oder in eine GND-Reihe. Das ist ein Kurzschluss. (Ein Kabel von einem **GND**-Stift in die GND-Reihe ist dagegen richtig, genauso eine Brücke vom kurzen Bein einer LED in die GND-Reihe. Das macht ihr gleich.)

## Euer Material

- **micro:bit:** Er steckt oben im schwarzen Schlitz der Platine, die Seite mit den 25 Lampen zeigt nach oben. Er bleibt die ganze Zeit dort.
- **Platine (Extension Board):** Die Stiftleiste neben dem Breadboard führt zu den Pins des micro:bit. Neben jedem Stift steht seine Nummer, zum Beispiel **P13**. Genau diese Nummer schreibt ihr später ins Programm. Die Leiste sieht so aus:

  **3.3V · GND · GND · P20 · P19 · P16 · P15 · P14 · P13 · P12 · P11 · P10 · 3.3V**

  Die beiden Stifte mit **GND** sind der Minuspol. **3.3V** ist der Pluspol.
- **Steckkabel:** Die Buchse kommt auf einen Stift der Platine, der Stecker ins Breadboard.
- **Brücke:** ein kurzes Kabel mit Steckern an beiden Enden. Es verbindet zwei Reihen auf dem Breadboard.
- **LED:** eine kleine Lampe. Sie hat ein langes Bein (Plus) und ein kurzes Bein (Minus). Strom fließt nur vom langen zum kurzen Bein. Steckt sie falsch herum, bleibt sie dunkel. Davon geht sie aber nicht kaputt.
- **Widerstand:** bremst den Strom, damit die LED nicht zu viel davon bekommt. Wie herum er steckt, ist egal. Eure Widerstände haben 150 Ω (Ohm) und die Farbringe braun, grün, schwarz, schwarz, braun.

## So funktioniert das Breadboard

Mit einem Breadboard verbindet ihr Bauteile, ohne zu löten. Haltet die Platine so, dass der micro:bit oben ist. Dann zählt ihr die Reihen von oben nach unten: Reihe 1 bis Reihe 17. Zählt mit dem Finger nach, bevor ihr steckt. Steht keine Zahl daneben, klebt euch an Reihe 10 und Reihe 14 ein kleines Stück Klebeband.

<img src="/microbit/ampel/breadboard.svg" alt="Breadboard mit 17 Reihen: Die Löcher einer Reihe sind links und rechts der Lücke jeweils verbunden">

- **Die Löcher einer Reihe sind verbunden.** Unter jeder Reihe liegt ein Metallstreifen. Was ihr in dieselbe Reihe steckt, ist miteinander verbunden.
- **Die Lücke trennt.** In der Mitte läuft eine Lücke von oben nach unten. Links und rechts davon sind zwei getrennte Streifen.
- **Reihe unter Reihe ist getrennt.** Reihe 10 und Reihe 11 haben nichts miteinander zu tun.
- **Links sind nur zwei Löcher frei,** die übrigen liegen unter der Platine. Rechts sind es fünf.

Darum legt ihr jeden Widerstand **über die Lücke**: Er verbindet den linken Streifen einer Reihe mit dem rechten.

## Der Stromkreis

Eine LED leuchtet nur, wenn der Strom einen geschlossenen Kreis hat:

**Pin** → Kabel → **Widerstand** → langes Bein der **LED** → kurzes Bein → Brücke → **GND-Reihe** → Kabel → **GND**

Die Platine hat nur zwei GND-Stifte, ihr baut aber fünf LEDs. Darum bekommt jede Ampel eine **GND-Reihe**: eine Reihe, in die ein einziges Kabel von GND kommt. Alle LEDs dieser Ampel sind mit einer Brücke dorthin verbunden und teilen sich so das eine GND-Kabel.

Ganz am Anfang nehmt ihr statt eines Pins den Stift **3.3V**. Er gibt immer Strom, sobald der micro:bit über USB Strom bekommt.

Jede LED in diesem Kurs ist genau so angeschlossen. Wenn ihr den Kreis einmal verstanden habt, könnt ihr jede weitere LED allein stecken.

Übrigens: In der Technik zeichnet man den Strom von Plus nach Minus, so wie oben. Die Elektronen im Draht wandern in Wirklichkeit andersherum. Für das Stecken ändert das nichts: Das lange Bein gehört auf die Seite des Pins, das kurze auf die Seite von GND.

## Die erste LED stecken

Die erste LED ist die rote Lampe der Fußgängerampel. Sie bleibt bis zum Schluss stecken.

Zuerst schließt ihr sie an **3.3V** an. Dieser Stift gibt immer Strom, ganz ohne Programm. So seht ihr sofort, ob eure Schaltung stimmt.

<img src="/microbit/ampel/erste-led-3v3.svg" alt="Steckplan: Kabel von 3.3V in Reihe 10 links, Widerstand über die Lücke, rote LED mit langem Bein in Reihe 10 rechts und kurzem Bein in Reihe 11, Brücke von Reihe 11 in die GND-Reihe 14, Kabel von GND in Reihe 14">

1. Zieht das USB-Kabel ab.
2. **Widerstand:** ein Bein in Reihe 10 links, direkt an der Lücke. Das andere Bein in Reihe 10 rechts, direkt an der Lücke.
3. **Rote LED:** langes Bein in Reihe 10 rechts, kurzes Bein in Reihe 11 rechts.
4. **Kabel von 3.3V:** Buchse auf einen Stift **3.3V**, Stecker in Reihe 10 links ins freie Loch.
5. **GND-Reihe:** Buchse auf einen Stift **GND**, Stecker in Reihe 14 rechts ins innerste Loch, direkt an der Lücke. Reihe 14 ist ab jetzt die GND-Reihe der Fußgängerampel.
6. **Brücke:** ein Ende in Reihe 11 rechts ins äußerste Loch, das andere Ende in Reihe 14 rechts.

Fahrt den Weg des Stroms mit dem Finger nach: 3.3V, Reihe 10 links, Widerstand, Reihe 10 rechts, langes Bein, kurzes Bein, Reihe 11, Brücke, Reihe 14, GND. Ist der Kreis geschlossen?

Steckt jetzt das USB-Kabel in den micro:bit, nicht in die Platine. Die LED leuchtet sofort. Bleibt sie dunkel, geht die Liste unter **Die LED bleibt dunkel?** durch.

Der Widerstand ist auch hier wichtig: Ohne ihn bekommt die LED zu viel Strom.

## Umstecken auf P13

Mit 3.3V leuchtet die LED immer. Damit euer Programm sie ein- und ausschalten kann, kommt das Kabel auf einen Pin.

<img src="/microbit/ampel/stufe-0.svg" alt="Steckplan: Kabel von P13 in Reihe 10 links, Widerstand über die Lücke, rote LED mit langem Bein in Reihe 10 rechts und kurzem Bein in Reihe 11, Brücke von Reihe 11 in die GND-Reihe 14, Kabel von GND in Reihe 14">

1. Zieht das USB-Kabel ab.
2. Steckt nur die Buchse vom Stift **3.3V** auf den Stift **P13**. Der Stecker bleibt in Reihe 10, alles andere bleibt, wie es ist.
3. Steckt das USB-Kabel wieder in den micro:bit.

Jetzt kann zweierlei passieren. Beides ist in Ordnung:

- **Die LED bleibt dunkel.** P13 gibt nur Strom, wenn ein Programm es sagt. Auf eurem micro:bit ist noch kein Programm, das P13 einschaltet.
- **Die LED leuchtet oder blinkt schon.** Der micro:bit behält sein letztes Programm, auch ohne Strom. Vielleicht hat ihn vorher jemand in einem anderen Kurs benutzt, und sein altes Programm schaltet P13 noch ein. Sobald ihr euer eigenes Programm überträgt, ist das alte weg.

## Editor einrichten

Oben auf dieser Seite wählt ihr, wie die Anleitung den Code zeigt.

- **Blöcke:** Ihr steckt farbige Bausteine zusammen. Gut, wenn ihr noch nie programmiert habt.
- **Python:** Ihr schreibt Text. Gut, wenn ihr Python schon ein wenig kennt.
- **JavaScript:** Ihr schreibt Text im selben Editor wie bei den Blöcken. Gut, wenn ihr JavaScript schon ein wenig kennt.

:::bloecke

Öffnet [makecode.microbit.org](https://makecode.microbit.org) und klickt auf **Neues Projekt**. Die Blöcke für die Pins findet ihr in der Blockliste unter **Fortgeschritten** und dann **Pins**.

:::

:::python

Öffnet [python.microbit.org](https://python.microbit.org). Der Editor zeigt schon ein kleines Programm an. Löscht es, bevor ihr eures schreibt.

:::

:::javascript

Öffnet [makecode.microbit.org](https://makecode.microbit.org), klickt auf **Neues Projekt** und oben in der Mitte auf **JavaScript**. Im Textfeld steht schon etwas. Löscht alles, bevor ihr euer Programm schreibt.

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

Im Pin-Block steht zuerst ein anderer Pin: Klickt darauf und wählt **P13**. Alles im Block **dauerhaft** wiederholt sich immer wieder. **pausiere (ms) 500** wartet 500 Millisekunden, also eine halbe Sekunde.

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

:::javascript

```javascript
basic.forever(function () {
    pins.digitalWritePin(DigitalPin.P13, 1)
    basic.pause(500)
    pins.digitalWritePin(DigitalPin.P13, 0)
    basic.pause(500)
})
```

Alles in den geschweiften Klammern von `basic.forever` wiederholt sich immer wieder. `basic.pause(500)` wartet 500 Millisekunden, also eine halbe Sekunde.

:::

## Auf den micro:bit übertragen

1. Steckt das USB-Kabel in den micro:bit, nicht in die Platine.

:::bloecke

2. Klickt auf die drei Punkte neben **Herunterladen** und wählt **Gerät verbinden**. Danach reicht ein Klick auf **Herunterladen**.

:::

:::python

2. Klickt auf **An micro:bit senden** und folgt den Schritten zum Verbinden.

:::

:::javascript

2. Klickt auf die drei Punkte neben **Herunterladen** und wählt **Gerät verbinden**. Danach reicht ein Klick auf **Herunterladen**.

:::

Klappt das Verbinden nicht, zum Beispiel weil der Schul-Computer es nicht erlaubt? Dann nehmt Plan B.

## Plan B: Datei aufs Laufwerk ziehen

<img src="/microbit/einfuehrung/plan-b.svg" alt="Plan B in drei Schritten: Programm als .hex-Datei herunterladen oder speichern, die Datei auf das Laufwerk MICROBIT ziehen, warten, bis die gelbe Lampe auf der Rückseite nicht mehr blinkt">

:::bloecke

Ohne verbundenes Gerät speichert **Herunterladen** eine Datei, die auf **.hex** endet. Ihr findet sie im Ordner **Downloads**.

:::

:::python

Klickt auf **Speichern**. Die Datei endet auf **.hex** und liegt im Ordner **Downloads**.

:::

:::javascript

Ohne verbundenes Gerät speichert **Herunterladen** eine Datei, die auf **.hex** endet. Ihr findet sie im Ordner **Downloads**.

:::

Öffnet den Ordner **Downloads** (Windows: Explorer, Mac: Finder). Das Laufwerk **MICROBIT** steht links in der Liste. Zieht die Datei mit gedrückter Maustaste aus **Downloads** auf **MICROBIT** und lasst dort los. Blinkt die gelbe Lampe nicht mehr, läuft euer Programm. Das Laufwerk verschwindet dabei kurz, das ist normal.

## Die LED bleibt dunkel?

Geht diese Liste der Reihe nach durch. Zieht vorher das USB-Kabel ab.

1. **LED umdrehen.** Das ist der häufigste Fehler. Das lange Bein gehört in die Reihe mit dem Widerstand.
2. **Reihen zählen.** Stecken alle Beine und Kabel in den Reihen aus dem Steckplan?
3. **Lücke prüfen.** Liegt der Widerstand wirklich über der Lücke und nicht daneben?
4. **Pin prüfen.** Steckt das Kabel auf **P13** und nicht auf dem Stift daneben?
5. **GND prüfen.** Steckt das Kabel der GND-Reihe auf einem Stift mit **GND**? Führt die Brücke von Reihe 11 in Reihe 14?
6. **Mit 3.3V testen.** Steckt die Buchse von P13 kurz auf **3.3V** und dann das USB-Kabel ein. Leuchtet die LED jetzt, ist die Schaltung richtig. Dann liegt es am Pin oder am Programm. Danach wieder zurück auf P13.
7. **Programm prüfen.** Steht im Programm P13? Habt ihr es übertragen?

## Bonus: Der Herzschlag

Lasst die LED wie ein Herz schlagen: zweimal kurz hintereinander aufleuchten, dann eine längere Pause, und das ohne Ende.

<details>
<summary>Tipps anzeigen</summary>

- Schreibt den Ablauf zuerst in Worten auf: an, kurz warten, aus, kurz warten, an, ...
- Ein kurzer Schlag dauert etwa 150 Millisekunden, die lange Pause etwa 700.
- Ihr braucht keine neuen Blöcke oder Befehle, nur mehr von denselben.

</details>
