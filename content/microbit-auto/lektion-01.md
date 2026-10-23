# Startklar: Auto und Editor

## Drei Regeln für das Auto

> 1. Beim Übertragen steht der Schalter **POWER** am Auto auf **OFF**. Sonst fährt es los und zieht am Kabel.
> 2. Gefahren wird auf dem Boden, nicht auf dem Tisch.
> 3. Macht das Auto etwas Seltsames: Schalter auf OFF, dann in Ruhe nachdenken.

## Blöcke oder Python?

Oben auf dieser Seite wählt ihr, wie die Anleitung den Code zeigt. Beide Wege steuern dasselbe Auto.

- **Blöcke:** Ihr steckt farbige Bausteine zusammen. Gut, wenn ihr noch nie programmiert habt.
- **Python:** Ihr schreibt Text. Gut, wenn ihr Python schon ein wenig kennt.

Ihr könnt jederzeit umschalten und euch den anderen Weg ansehen. JavaScript gibt es in diesem Kurs nicht. Habt ihr in der Einführung JavaScript genommen, nehmt hier die Blöcke: Sie sind im selben Editor.

## Editor einrichten

:::bloecke

1. Öffnet [makecode.microbit.org](https://makecode.microbit.org) und klickt auf **Neues Projekt**.
2. Klickt in der Blockliste ganz unten auf **Fortgeschritten**. Darunter erscheint ganz unten **Erweiterungen**: Klickt darauf.
3. Markiert diese Adresse hier auf der Seite, kopiert sie (`Strg` + `C`, am Mac `⌘` + `C`) und fügt sie in das Suchfeld ein (`Strg` + `V`, am Mac `⌘` + `V`). Drückt dann Enter: `https://github.com/keyestudio2019/MiniCar`
4. Es erscheint eine Karte mit dem Namen der Erweiterung. Klickt die Karte an. In der Blockliste gibt es jetzt den Eintrag **MiniCar**.

Die Blöcke von MiniCar sind englisch beschriftet. Die Anleitung zeigt sie genau so, wie sie im Editor heißen.

:::

:::python

1. Ladet die Datei <a href="/microbit/keyes_MiniCar.py" download>keyes_MiniCar.py</a> herunter. Sie bringt dem micro:bit bei, wie er mit dem Auto spricht.
2. Öffnet [python.microbit.org](https://python.microbit.org).
3. Klickt links auf **Projekt** und dann auf **Öffnen**. Wählt die heruntergeladene Datei aus. Der Editor fragt, ob die Datei euer Programm ersetzen oder dazukommen soll: Wählt **hinzufügen**. Euer Programm `main.py` bleibt.
4. Unter **Projekt** stehen jetzt zwei Dateien: `main.py` (euer Programm) und `keyes_MiniCar.py`.

Der Simulator rechts im Editor kennt das Auto nicht. Ob etwas klappt, seht ihr nur am echten Auto.

:::

## Das erste Programm

Der micro:bit hat 25 kleine Lampen. Lasst ein Herz leuchten.

:::bloecke

```bloecke
[grundlagen] beim Start
  [grundlagen] zeige Symbol Herz
```

:::

:::python

```python
from microbit import *

display.show(Image.HEART)
```

:::

## Auf den micro:bit übertragen

1. Stellt den Schalter **POWER** am Auto auf **OFF**.
2. Steckt den micro:bit in das Auto. Die Seite mit den 25 Lampen des micro:bit zeigt nach vorn. Vorn ist die Seite mit den beiden „Augen“ und den Scheinwerfern.
3. Verbindet den micro:bit per USB-Kabel mit dem Computer.

:::bloecke

4. Klickt auf die drei Punkte neben **Herunterladen** und wählt **Gerät verbinden**. Danach reicht ein Klick auf **Herunterladen**.

:::

:::python

4. Klickt auf **An micro:bit senden** und folgt den Schritten zum Verbinden.

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

Öffnet den Ordner **Downloads** (Windows: Explorer, Mac: Finder). Das Laufwerk **MICROBIT** steht links in der Liste. Zieht die Datei mit gedrückter Maustaste aus **Downloads** auf **MICROBIT** und lasst dort los. Blinkt die gelbe Lampe nicht mehr, läuft euer Programm. Das Laufwerk verschwindet dabei kurz, das ist normal.

## Bonus: Ein anderes Bild

Das Herz kennt ihr jetzt. Lasst den micro:bit ein anderes Bild zeigen, das zu euch passt.

<details>
<summary>Tipps anzeigen</summary>

:::bloecke

Klickt im Block **zeige Symbol** auf das kleine Bild. Es klappt eine Auswahl mit vielen Symbolen auf.

:::

:::python

Löscht `HEART` und den Punkt davor. Tippt den Punkt dann noch einmal: Jetzt schlägt der Editor euch alle Bilder vor, zum Beispiel `DUCK`, `GHOST` oder `ROLLERSKATE`.

:::

Ein neues Bild erscheint erst, wenn ihr das Programm noch einmal übertragt.

</details>
