# Werkstatt 2: Ampeln mit Funk

Echte Ampeln stehen nicht allein. An einer Kreuzung sprechen sie sich ab, und eine Feuerwehr kann sie auf Rot schalten. Eure micro:bits können das auch: Sie schicken sich per Funk kurze Nachrichten.

Für jeden Auftrag hier braucht ihr ein zweites Team, mit dem ihr zusammenarbeitet. Ein gelöster Auftrag reicht für den Abschluss. Alle Aufträge sind knifflig (⭐⭐⭐). Nehmt euch Zeit für den Plan.

## Die Funkgruppe

Alle micro:bits im Raum funken auf denselben Wellen. Damit sich die Teams nicht gegenseitig stören, gibt es **Funkgruppen**: Ein micro:bit hört nur Nachrichten aus seiner eigenen Gruppe.

> Holt euch bei eurer Kursleitung eine Gruppennummer. Ihr und euer Partnerteam nehmt **dieselbe** Nummer, alle anderen eine andere. In den Beispielen steht dafür ein **x**. Statt x stellt ihr eure Nummer ein, sonst läuft das Programm nicht.

## Der erste Funkspruch

Beide Teams übertragen dasselbe Programm. Drückt ein Team Knopf B, zeigt der micro:bit des anderen Teams ein Herz.

:::bloecke

```bloecke
[grundlagen] beim Start
  [funk] setze Funkgruppe auf x
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
radio.config(group=x)

while True:
    if button_b.was_pressed():
        radio.send("hallo")
    nachricht = radio.receive()
    if nachricht == "hallo":
        display.show(Image.HEART)
```

`radio.receive()` holt die nächste Nachricht ab. Ist keine da, bekommt ihr `None`.

:::

:::javascript

```javascript
radio.setGroup(x)

input.onButtonPressed(Button.B, function () {
    radio.sendString("hallo")
})

radio.onReceivedString(function (receivedString) {
    if (receivedString == "hallo") {
        basic.showIcon(IconNames.Heart)
    }
})
```

Alles in den geschweiften Klammern von `radio.onReceivedString` passiert, sobald eine Nachricht ankommt. In `receivedString` steht, was angekommen ist.

:::

Klappt es in beide Richtungen? Dann seid ihr bereit für die Aufträge. Nachrichten sind einfache Wörter. Vereinbart mit eurem Partnerteam vorher, welches Wort was bedeutet.

## Auftrag 1: Die Feuerwehr hat Vorfahrt

Ein Team hat seine Ampelanlage aus Stufe 3. Der micro:bit des anderen Teams ist das Feuerwehrauto: Drückt es Knopf B, schickt es einen Notruf. Die Ampelanlage schaltet dann sofort alles auf Rot, Autos und Fußgänger. Nach 10 Sekunden schaltet die Autoampel wie immer über Rot-Gelb auf Grün. Die Fußgänger behalten Rot.

Danach tauscht ihr: Das andere Team baut seine Anlage um, und ihr seid die Feuerwehr.

Hinweis: Bei einem Notruf ist keine Zeit für Gelb. Alle grünen und gelben LEDs gehen sofort aus, alle roten an.

Beide micro:bits brauchen dieselbe Funkgruppe, auch die Ampelanlage. Das Feuerwehrauto bekommt ein kleines eigenes Programm: Funkgruppe setzen und bei Knopf B ein Wort schicken, zum Beispiel `notruf`. Auf genau dieses Wort wartet die Ampelanlage.

:::bloecke

Die Funkgruppe setzt ihr bei beiden in **beim Start**. Die Ampelanlage bekommt einen Block **wenn Text empfangen** und darin **wenn receivedString = "notruf" dann**, wie beim ersten Funkspruch.

Schickt den Notruf beim Testen nur, wenn die Autos Grün haben, und drückt dabei nicht Knopf A.

:::

:::python

Bei beiden micro:bits kommt oben `import radio` dazu und vor die Schleife `radio.on()` und `radio.config(group=x)`. In der Schleife der Ampelanlage fragt ihr nach Knopf A auch den Funk ab:

```python
    if radio.receive() == "notruf":
        # alles auf Rot, 10 Sekunden warten, dann über Rot-Gelb auf Grün
```

Schickt den Notruf beim Testen nur, wenn die Autos Grün haben, und drückt dabei nicht Knopf A.

:::

:::javascript

Bei beiden micro:bits steht `radio.setGroup(x)` ganz oben. Die Ampelanlage bekommt unten dazu:

```javascript
radio.onReceivedString(function (receivedString) {
    if (receivedString == "notruf") {
        // alles auf Rot, 10 Sekunden warten, dann über Rot-Gelb auf Grün
    }
})
```

Schickt den Notruf beim Testen nur, wenn die Autos Grün haben, und drückt dabei nicht Knopf A.

:::

## Auftrag 2: Die Kreuzung

Zwei Straßen kreuzen sich. Jedes Team ist eine Autoampel, eine für jede Straße. Es darf immer nur eine der beiden Ampeln Grün haben.

Die Ampeln reichen sich ein Zeichen weiter, wie beim Staffellauf:

1. Ampel 1 hat Grün, Ampel 2 hat Rot.
2. Nach 5 Sekunden schaltet Ampel 1 über Gelb auf Rot, wartet die Räumzeit (1 Sekunde) und funkt dann `du`.
3. Ampel 2 bekommt `du`, schaltet über Rot-Gelb auf Grün.
4. Nach 5 Sekunden schaltet Ampel 2 über Gelb auf Rot, wartet die Räumzeit (1 Sekunde) und funkt `du` zurück.
5. Und so weiter, ohne Ende.

Hinweis: Lost aus, welches Team Ampel 1 ist. Beide Teams brauchen fast dasselbe Programm. Beim Start zeigen beide Ampeln Rot. Seid ihr beide bereit, drückt Ampel 1 Knopf A: Sie schaltet über Rot-Gelb auf Grün und fängt mit Schritt 1 an. Ampel 2 wartet auf `du`. Die Fußgänger-LEDs bleiben bei diesem Auftrag aus.

Baut den Ablauf einmal als eigene **Funktion**, zum Beispiel `gruenphase`: Rot-Gelb, Grün, 5 Sekunden warten, Gelb, Rot, Räumzeit, `du` senden. Eine Funktion ist ein Ablauf mit Namen. Ihr baut ihn einmal und startet ihn dann mit seinem Namen, so oft ihr wollt. Weil jede Ampel am Ende `du` sendet, geht es von selbst ohne Ende weiter.

:::bloecke

Eine **dauerhaft**-Schleife braucht ihr nicht. Die Funktion legt ihr an wie im Bonus von Stufe 2, nur ohne Parameter. Beide Teams rufen sie in **wenn Text empfangen** auf, wenn `du` ankommt. Der einzige Unterschied: Ampel 1 ruft die Funktion zusätzlich in **wenn Knopf A geklickt** auf und startet so die erste Runde.

:::

:::python

Ihr braucht die Schleife `while True:`, die immer wieder nach Knopf A und dem Funk fragt. Das Gerüst:

```python
def gruenphase():
    # Rot-Gelb, Grün, 5 Sekunden warten, Gelb, Rot, Räumzeit, "du" senden

while True:
    if button_a.was_pressed():
        gruenphase()
    if radio.receive() == "du":
        gruenphase()
```

Die leeren Klammern hinter `gruenphase` heißen: Die Funktion bekommt keine Werte. `gruenphase()` startet sie. Die Frage nach Knopf A braucht nur Ampel 1, sie startet so die erste Runde.

:::

:::javascript

Ein `basic.forever` braucht ihr nicht. Das Gerüst:

```javascript
function gruenphase() {
    // Rot-Gelb, Grün, 5 Sekunden warten, Gelb, Rot, Räumzeit, "du" senden
}

radio.onReceivedString(function (receivedString) {
    if (receivedString == "du") {
        gruenphase()
    }
})

input.onButtonPressed(Button.A, function () {
    gruenphase()
})
```

Die leeren Klammern hinter `gruenphase` heißen: Die Funktion bekommt keine Werte. `gruenphase()` startet sie. Den Teil mit Knopf A braucht nur Ampel 1, sie startet so die erste Runde.

:::

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

:::javascript

Die Funkgruppe muss bei jedem micro:bit gleich sein, auch beim Auto.

:::

</details>
