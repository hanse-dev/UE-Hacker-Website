# Startklar: Spielfeld und erstes Bild

<img src="/microbit/sterne/ziel.svg" alt="Vier Bilder vom fertigen Spiel: Ein Stern fällt von oben, der Korb in der unteren Reihe fährt mit Knopf B hinterher und fängt ihn, das gibt einen Punkt">

Das baut ihr: Von oben fallen Sterne, unten fangt ihr sie mit dem Korb.

## Das Spielfeld

<img src="/microbit/sterne/spielfeld.svg" alt="Die LED-Anzeige des micro:bit mit 5 mal 5 Lampen. Die Spalten heißen x 0 bis 4 von links nach rechts, die Reihen y 0 bis 4 von oben nach unten. Der Stern leuchtet bei x 2, y 0, der Korb bei x 2, y 4">

- **x** zählt von links nach rechts: 0, 1, 2, 3, 4.
- **y** zählt von oben nach unten: 0, 1, 2, 3, 4.
- Der **Korb** steht immer in der untersten Reihe, also bei y = 4.

## Editor öffnen

Nehmt **Chrome** oder **Edge**. Nur diese Browser können den micro:bit direkt über das Kabel erreichen.

Oben auf dieser Seite wählt ihr, wie die Anleitung den Code zeigt: **Blöcke**, wenn ihr noch nie programmiert habt, sonst **Python** oder **JavaScript**.

:::bloecke

Öffnet [makecode.microbit.org](https://makecode.microbit.org) und klickt auf **Neues Projekt**. Die Blöcke zum Zeichnen findet ihr unter **LED**.

:::

:::python

Öffnet [python.microbit.org](https://python.microbit.org). Löscht das kleine Programm, das schon im Editor steht.

:::

:::javascript

Öffnet [makecode.microbit.org](https://makecode.microbit.org), klickt auf **Neues Projekt** und oben in der Mitte auf **JavaScript**. Löscht, was schon im Editor steht.

:::

## Das erste Bild

<img src="/microbit/sterne/start.svg" alt="Der micro:bit zeigt zwei leuchtende Punkte: oben in der Mitte und unten in der Mitte">

:::bloecke

```bloecke
[grundlagen] beim Start
  [led] Zeichne x 2 y 0
  [led] Zeichne x 2 y 4
```

:::

:::python

```python
from microbit import *

display.set_pixel(2, 0, 9)
display.set_pixel(2, 4, 9)
```

Die letzte Zahl ist die Helligkeit: 0 ist aus, 9 ist ganz hell.

:::

:::javascript

```javascript
led.plot(2, 0)
led.plot(2, 4)
```

:::

## Auf den micro:bit übertragen

1. Steckt das USB-Kabel in den micro:bit und in den Computer.

:::bloecke

2. Klickt auf die drei Punkte neben **Herunterladen** und wählt **Gerät verbinden**.
3. Im kleinen Fenster klickt ihr auf **BBC micro:bit** und dann auf **Verbinden**.
4. Ab jetzt reicht ein Klick auf **Herunterladen**.

:::

:::python

2. Klickt auf **An micro:bit senden**.
3. Im kleinen Fenster klickt ihr auf **BBC micro:bit** und dann auf **Verbinden**.
4. Ab jetzt reicht ein Klick auf **An micro:bit senden**.

:::

:::javascript

2. Klickt auf die drei Punkte neben **Herunterladen** und wählt **Gerät verbinden**.
3. Im kleinen Fenster klickt ihr auf **BBC micro:bit** und dann auf **Verbinden**.
4. Ab jetzt reicht ein Klick auf **Herunterladen**.

:::

## Verbindet sich nicht?

<img src="/microbit/einfuehrung/hilfe.svg" alt="Prüfliste: 1. Chrome oder Edge? Sonst die Seite dort öffnen. 2. Leuchtet hinten die gelbe Lampe? Sonst Kabel fester stecken oder anderen USB-Anschluss nehmen. 3. Zeigt der Computer ein Laufwerk MICROBIT? Sonst ein anderes Kabel nehmen, manche Kabel laden nur. 4. Nur ein Tab mit dem Editor offen? Sonst andere Tabs schließen und das Kabel ab- und anstecken. 5. Im Fenster den micro:bit ausgewählt? Sonst noch einmal verbinden und BBC micro:bit anklicken. Klappt es immer noch nicht: Plan B">

Noch drei Fälle:

- **Das Laufwerk heißt MAINTENANCE statt MICROBIT:** Kabel ab- und wieder anstecken, ohne dabei den Knopf auf der Rückseite zu drücken.
- **Das Fenster bleibt leer oder kommt gar nicht:** Manche Schul-Computer erlauben das nicht. Nehmt Plan B.
- **Der micro:bit zeigt ein trauriges Gesicht, eine Zahl oder Laufschrift:** Die Verbindung klappt, aber im Programm steckt ein Fehler. Vergleicht es mit der Anleitung.

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

Zieht die Datei auf das Laufwerk **MICROBIT**. Blinkt die gelbe Lampe nicht mehr, läuft euer Programm. Das Laufwerk verschwindet dabei kurz, das ist normal.

## Bonus: Euer eigenes Bild

Zeichnet aus einzelnen Punkten ein eigenes Bild, zum Beispiel ein Gesicht, einen Pfeil oder euren Anfangsbuchstaben.

<details>
<summary>Tipps anzeigen</summary>

- Malt das Bild zuerst auf kariertes Papier, 5 mal 5 Kästchen groß. Schreibt an jedes Kästchen x und y.
- Jeder leuchtende Punkt braucht einen eigenen Zeichne-Befehl.

</details>
