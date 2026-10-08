# Startklar: Team, Auto und Editor

Ihr arbeitet zu zweit an einem Auto. Damit beide etwas davon haben, gibt es zwei Rollen:

- **Pilot:** sitzt an der Tastatur und baut das Programm.
- **Navigator:** liest die Anleitung, denkt mit und testet das Auto.

Nach jeder Stufe tauscht ihr die Rollen.

## Drei Regeln für das Auto

> 1. Beim Übertragen steht der Schalter **POWER** am Auto auf **OFF**. Sonst fährt es los und zieht am Kabel.
> 2. Gefahren wird auf dem Boden, nicht auf dem Tisch.
> 3. Macht das Auto etwas Seltsames: Schalter auf OFF, dann in Ruhe nachdenken.

## Blöcke oder Python?

Oben auf dieser Seite wählt ihr, wie die Anleitung den Code zeigt. Beide Wege steuern dasselbe Auto.

- **Blöcke:** Ihr steckt farbige Bausteine zusammen. Gut, wenn ihr noch nie programmiert habt.
- **Python:** Ihr schreibt Text. Gut, wenn ihr Python schon ein wenig kennt.

Ihr könnt jederzeit umschalten und euch den anderen Weg ansehen.

## Editor einrichten

:::bloecke

1. Öffnet [makecode.microbit.org](https://makecode.microbit.org) und klickt auf **Neues Projekt**.
2. Klickt in der Blockliste auf **Erweiterungen**.
3. Tragt diese Adresse in das Suchfeld ein und drückt Enter: `https://github.com/keyestudio2019/MiniCar`
4. Klickt die Erweiterung an. In der Blockliste gibt es jetzt den Eintrag **MiniCar**.

Die Blöcke von MiniCar sind englisch beschriftet. Die Anleitung zeigt sie genau so, wie sie im Editor heißen.

:::

:::python

1. Ladet die Datei <a href="/microbit/keyes_MiniCar.py" download>keyes_MiniCar.py</a> herunter. Sie bringt dem micro:bit bei, wie er mit dem Auto spricht.
2. Öffnet [python.microbit.org](https://python.microbit.org).
3. Klickt links auf **Projekt** und dann auf **Öffnen**. Wählt die heruntergeladene Datei aus und bestätigt, dass sie zum Projekt hinzugefügt wird.
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

1. Steckt den micro:bit in das Auto. Die Seite mit den Lampen zeigt nach vorn.
2. Verbindet den micro:bit per USB-Kabel mit dem Computer.

:::bloecke

3. Klickt auf die drei Punkte neben **Herunterladen** und wählt **Gerät verbinden**. Danach reicht ein Klick auf **Herunterladen**.

:::

:::python

3. Klickt auf **An micro:bit senden** und folgt den Schritten zum Verbinden.

:::

Klappt das Verbinden nicht? Dann speichert das Programm als Datei und zieht sie auf das Laufwerk **MICROBIT**.

## Bonus: Ein anderes Bild

Das Herz kennt ihr jetzt. Lasst den micro:bit ein anderes Bild zeigen, das zu eurem Team passt.

<details>
<summary>Tipps anzeigen</summary>

:::bloecke

Klickt im Block **zeige Symbol** auf das kleine Bild. Es klappt eine Auswahl mit vielen Symbolen auf.

:::

:::python

Löscht `HEART` und tippt hinter `Image.` einen Punkt neu. Der Editor schlägt euch dann alle Bilder vor, zum Beispiel `DUCK`, `GHOST` oder `ROLLERSKATE`.

:::

Ein neues Bild erscheint erst, wenn ihr das Programm noch einmal übertragt.

</details>
