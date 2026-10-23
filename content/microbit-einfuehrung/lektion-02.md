# Das erste Programm

## Editor öffnen

Nehmt **Chrome** oder **Edge**. Nur diese Browser können den micro:bit direkt über das Kabel erreichen.

Oben auf dieser Seite wählt ihr, wie die Anleitung den Code zeigt:

- **Blöcke:** Ihr steckt farbige Bausteine zusammen. Gut, wenn ihr noch nie programmiert habt.
- **Python:** Ihr schreibt Text. Gut, wenn ihr Python schon ein wenig kennt.
- **JavaScript:** Ihr schreibt Text im selben Editor wie bei den Blöcken.

:::bloecke

Öffnet [makecode.microbit.org](https://makecode.microbit.org) und klickt auf **Neues Projekt**. Gebt dem Projekt einen Namen.

:::

:::python

Öffnet [python.microbit.org](https://python.microbit.org). Löscht alles, was schon im Editor steht.

:::

:::javascript

Öffnet [makecode.microbit.org](https://makecode.microbit.org), klickt auf **Neues Projekt** und oben in der Mitte auf **JavaScript**. Löscht, was schon im Editor steht.

:::

## Ein Herz

<img src="/microbit/einfuehrung/herz.svg" alt="Der micro:bit zeigt ein Herz aus leuchtenden Lampen">

:::bloecke

```bloecke
[grundlagen] beim Start
  [grundlagen] zeige Symbol Herz
```

Den Block **zeige Symbol** findet ihr unter **Grundlagen**. Zieht ihn in **beim Start** hinein. Rechts neben den Blöcken seht ihr einen micro:bit auf dem Bildschirm: Dort probiert ihr das Programm sofort aus.

:::

:::python

```python
from microbit import *

display.show(Image.HEART)
```

Die erste Zeile braucht jedes Programm: Sie holt die Befehle für den micro:bit. Rechts seht ihr einen micro:bit auf dem Bildschirm. Mit **Ausführen** (▶) probiert ihr das Programm dort sofort aus.

Tippt genau ab, auch große und kleine Buchstaben, Punkte und Klammern. Sonst versteht der micro:bit das Programm nicht.

:::

:::javascript

```javascript
basic.showIcon(IconNames.Heart)
```

Rechts seht ihr einen micro:bit auf dem Bildschirm: Dort probiert ihr das Programm sofort aus.

Tippt genau ab, auch große und kleine Buchstaben, Punkte und Klammern. Sonst versteht der micro:bit das Programm nicht.

:::

## Auf den micro:bit übertragen

1. Steckt das USB-Kabel in den micro:bit und in den Computer.

:::bloecke

2. Klickt auf die drei Punkte neben **Herunterladen** und wählt **Gerät verbinden**.
3. Im kleinen Fenster klickt ihr auf **BBC micro:bit** und dann auf **Verbinden**.
4. Klickt jetzt auf **Herunterladen**. Das macht ihr ab jetzt nach jeder Änderung.

:::

:::python

2. Klickt auf **An micro:bit senden**.
3. Im kleinen Fenster klickt ihr auf **BBC micro:bit** und dann auf **Verbinden**.
4. Ab jetzt reicht nach jeder Änderung ein Klick auf **An micro:bit senden**.

:::

:::javascript

2. Klickt auf die drei Punkte neben **Herunterladen** und wählt **Gerät verbinden**.
3. Im kleinen Fenster klickt ihr auf **BBC micro:bit** und dann auf **Verbinden**.
4. Klickt jetzt auf **Herunterladen**. Das macht ihr ab jetzt nach jeder Änderung.

:::

Die Lampe auf der Rückseite blinkt kurz. Dann zeigt euer micro:bit das Herz.

## Verbindet sich nicht?

<img src="/microbit/einfuehrung/hilfe.svg" alt="Prüfliste: 1. Chrome oder Edge? Sonst die Seite dort öffnen. 2. Leuchtet hinten die gelbe Lampe? Sonst Kabel fester stecken oder anderen USB-Anschluss nehmen. 3. Zeigt der Computer ein Laufwerk MICROBIT? Sonst ein anderes Kabel nehmen, manche Kabel laden nur. 4. Nur ein Tab mit dem Editor offen? Sonst andere Tabs schließen und das Kabel ab- und anstecken. 5. Im Fenster den micro:bit ausgewählt? Sonst noch einmal verbinden und BBC micro:bit anklicken. Klappt es immer noch nicht: Plan B">

Das Laufwerk **MICROBIT** findet ihr im Explorer (Windows) oder Finder (Mac) links in der Liste. Ein Tab ist ein Reiter oben im Browser.

Noch drei Fälle:

- **Das Laufwerk heißt MAINTENANCE statt MICROBIT:** Kabel ab- und wieder anstecken, ohne dabei den kleinen Knopf neben der USB-Buchse auf der Rückseite zu drücken.
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

Öffnet den Ordner **Downloads** (Windows: Explorer, Mac: Finder). Das Laufwerk **MICROBIT** steht links in der Liste. Zieht die Datei mit gedrückter Maustaste aus **Downloads** auf **MICROBIT** und lasst dort los. Blinkt die gelbe Lampe nicht mehr, läuft euer Programm. Das Laufwerk verschwindet dabei kurz, das ist normal.

## Bonus: Eure Namen als Laufschrift

Nach dem Herz laufen eure Namen über die Anzeige.

<details>
<summary>Tipps anzeigen</summary>

:::bloecke

Unter **Grundlagen** gibt es **zeige Text**. Hängt ihn unter **zeige Symbol**.

:::

:::python

`display.scroll("Hallo")` lässt Text über die Anzeige laufen. Schreibt die Zeile unter die Herz-Zeile und eure Namen zwischen die Anführungszeichen:

```python
display.show(Image.HEART)
display.scroll("Mia und Ben")
```

Dann wieder **An micro:bit senden**.

:::

:::javascript

`basic.showString("Hallo")` lässt Text über die Anzeige laufen. Schreibt die Zeile unter die Herz-Zeile und eure Namen zwischen die Anführungszeichen:

```javascript
basic.showIcon(IconNames.Heart)
basic.showString("Mia und Ben")
```

Dann wieder **Herunterladen**.

:::

</details>
