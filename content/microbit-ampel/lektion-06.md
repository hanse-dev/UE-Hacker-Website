# Werkstatt 2: Ampeln mit Funk

Echte Ampeln stehen nicht allein. An einer Kreuzung sprechen sie sich ab, und eine Feuerwehr kann sie auf Rot schalten. Eure micro:bits können das auch: Sie schicken sich per Funk kurze Nachrichten.

Für jeden Auftrag hier braucht ihr ein zweites Team, mit dem ihr zusammenarbeitet. Ein gelöster Auftrag reicht für den Abschluss. Alle Aufträge sind knifflig (⭐⭐⭐). Nehmt euch Zeit für den Plan.

## Die Funkgruppe

Alle micro:bits im Raum funken auf denselben Wellen. Damit sich die Teams nicht gegenseitig stören, gibt es **Funkgruppen**: Ein micro:bit hört nur Nachrichten aus seiner eigenen Gruppe.

> Holt euch bei eurer Kursleitung eine Gruppennummer. Ihr und euer Partnerteam nehmt **dieselbe** Nummer, alle anderen eine andere. In den Beispielen steht die 7, setzt dort eure Nummer ein.

## Der erste Funkspruch

Beide Teams übertragen dasselbe Programm. Drückt ein Team Knopf B, zeigt der micro:bit des anderen Teams ein Herz.

:::bloecke

```bloecke
[grundlagen] beim Start
  [funk] setze Funkgruppe auf 7
[eingabe] wenn Knopf B geklickt
  [funk] sende Zeichenkette "hallo" über Funk
[funk] wenn Text empfangen receivedString
  [logik] wenn receivedString = "hallo" dann
    [grundlagen] zeige Symbol Herz
```

Die Funk-Blöcke findet ihr unter **Funk**. Den Vergleich mit Text findet ihr unter **Logik**. **receivedString** zieht ihr aus dem Block **wenn Text empfangen** heraus in den Vergleich.

:::

:::python

```python
from microbit import *
import radio

radio.on()
radio.config(group=7)

while True:
    if button_b.was_pressed():
        radio.send("hallo")
    nachricht = radio.receive()
    if nachricht == "hallo":
        display.show(Image.HEART)
```

`radio.receive()` holt die nächste Nachricht ab. Ist keine da, bekommt ihr `None`.

:::

Klappt es in beide Richtungen? Dann seid ihr bereit für die Aufträge. Nachrichten sind einfache Wörter. Vereinbart mit eurem Partnerteam vorher, welches Wort was bedeutet.

## Auftrag 1: Die Feuerwehr hat Vorfahrt

Ein Team hat seine Ampelanlage aus Stufe 3. Der micro:bit des anderen Teams ist das Feuerwehrauto: Drückt es Knopf B, schickt es einen Notruf. Die Ampelanlage schaltet dann sofort alles auf Rot, Autos und Fußgänger. Nach 10 Sekunden haben die Autos wieder Grün.

Danach tauscht ihr: Das andere Team baut seine Anlage um, und ihr seid die Feuerwehr.

Hinweis: Bei einem Notruf ist keine Zeit für Gelb. Alle grünen LEDs gehen sofort aus, alle roten an.

:::bloecke

Euer Programm hat jetzt zwei Teile, die gleichzeitig laufen können: **wenn Knopf A geklickt** und **wenn Text empfangen**. Kommt der Notruf, während die Fußgänger gerade Grün haben, schaltet der Knopf-Ablauf danach weiter. Fürs Erste reicht es, wenn der Notruf im Grundzustand klappt.

:::

:::python

Euer Programm fragt in der Schleife nacheinander Knopf A und den Funk ab. Kommt der Notruf, während der Ablauf für die Fußgänger läuft, wartet er, bis der Ablauf fertig ist. Fürs Erste reicht das.

:::

## Auftrag 2: Die Kreuzung

Zwei Straßen kreuzen sich. Jedes Team ist eine Autoampel, eine für jede Straße. Es darf immer nur eine der beiden Ampeln Grün haben.

Die Ampeln reichen sich ein Zeichen weiter, wie beim Staffellauf:

1. Ampel 1 hat Grün, Ampel 2 hat Rot.
2. Nach 5 Sekunden schaltet Ampel 1 über Gelb auf Rot, wartet die Räumzeit und funkt dann `du`.
3. Ampel 2 bekommt `du`, schaltet über Rot-Gelb auf Grün.
4. Nach 5 Sekunden schaltet Ampel 2 über Gelb auf Rot, wartet die Räumzeit und funkt `du` zurück.
5. Und so weiter, ohne Ende.

Hinweis: Beide Teams brauchen fast dasselbe Programm. Der einzige Unterschied ist der Anfang: Eine Ampel beginnt mit Grün und fängt an, die andere beginnt mit Rot und wartet. Startet die erste Ampel mit Knopf A, wenn beide bereit sind.

## Auftrag 3: Die Ampel für das Roboterauto

Habt ihr den Kurs [micro:bit: Das Roboterauto](/kurs/projekt-microbit-auto) gemacht? Dann holt euch ein Auto dazu. Die Ampelanlage funkt bei jedem Wechsel der Autoampel ihre Farbe, zum Beispiel `rot` und `gruen`. Das Auto fährt los, wenn es `gruen` bekommt, und hält bei `rot` an.

Hinweis: Das Auto braucht sein eigenes Programm mit der Erweiterung oder der Datei aus dem Roboterauto-Kurs. Wie es losfährt und anhält, steht dort in Stufe 3. Fahrt langsam, damit das Auto nicht vom Tisch fällt. Am besten fahrt ihr auf dem Boden.

## Auftrag 4: Eure eigene Idee

Ihr habt eine eigene Idee für Ampeln mit Funk? Zum Beispiel eine Baustellenampel, bei der zwei Ampeln abwechselnd eine einspurige Straße freigeben, oder ein Ampelknopf auf der anderen Straßenseite: ein zweiter micro:bit, dessen Knopf A die Fußgängerampel startet. Schreibt euren Plan auf und zeigt ihn eurer Kursleitung, bevor ihr loslegt.

## Bonus: Noch ein Funkauftrag

Löst einen zweiten Auftrag, am besten mit einem anderen Partnerteam.

<details>
<summary>Tipps anzeigen</summary>

- Bei der Kreuzung hilft es, wenn ihr die Ampeln nebeneinander aufbaut, so wie sie an einer echten Kreuzung stehen würden.
- Beim Roboterauto: Probiert das Auto zuerst ohne Ampel aus. Schickt die Wörter mit Knopf A und B von einem zweiten micro:bit.

:::bloecke

Die Funkgruppe muss bei jedem micro:bit gleich sein, auch beim Auto.

:::

:::python

Die Funkgruppe muss bei jedem micro:bit gleich sein, auch beim Auto. Vergesst `radio.on()` nicht.

:::

</details>
