# Stufe 10: Meisterstufe

Ihr kennt jetzt alle Teile des Autos. Hier gibt es keine fertigen Programme mehr, nur Aufträge und Hinweise. Sucht euch aus, was euch reizt. Zwei gelöste Aufträge reichen für den Abschluss. Ist danach noch Zeit, löst ihr einen weiteren oder verbindet zwei Aufträge zu einem Programm.

## Auftrag 1: Sicher auf der Linie

Das Auto folgt der Linie wie in Stufe 9. Steht ein Hindernis auf der Strecke, hält es an und wartet, bis der Weg wieder frei ist.

Hinweis: Prüft zuerst den Abstand wie in Stufe 6. Nur wenn der Weg frei ist, kommt der Linienfolger an die Reihe: Steckt den ganzen wenn-Block aus Stufe 9 in das **ansonsten** der Abstandsprüfung. Ein wenn-Block darf in einem anderen stecken.

## Auftrag 2: Der Lichtsucher

Vorn am Auto sitzen zwei Lichtsensoren. Das Auto soll einer Taschenlampe folgen: Es dreht sich zu der Seite, auf der es heller ist.

:::bloecke

Die Blöcke **LDR_L** und **LDR_R** findet ihr bei **MiniCar**. Sie melden die Helligkeit links und rechts als Zahl von 0 bis 1023. Lasst euch die Werte zuerst mit **zeige Zahl** anzeigen.

:::

:::python

```python
hell_links = pin1.read_analog()
hell_rechts = pin0.read_analog()
```

Beide Werte liegen zwischen 0 und 1023. Lasst sie euch zuerst mit `display.scroll` anzeigen.

:::

Hinweis: Findet heraus, welche Zahl im Raum normal ist und welche im Licht der Taschenlampe: Leuchtet nacheinander auf jeden Sensor und schaut, ob die Zahl größer oder kleiner wird. Vergleicht dann die beiden Werte direkt miteinander, zum Beispiel mit **wenn … dann … ansonsten** und dem Vergleich **>**: Ist links heller, dreht das Auto nach links, sonst nach rechts. Eine Grenze braucht ihr erst, wer mag, als Extra: Ist es auf beiden Seiten dunkel, bleibt das Auto stehen.

## Auftrag 3: Das Einsatzfahrzeug

Das Auto fährt ein Quadrat. Dabei blinken die Scheinwerfer abwechselnd blau und rot, und der micro:bit spielt eine Sirene.

Hinweis: Das Auto kann nicht gleichzeitig warten und blinken. Der Trick: Blinkt **während** des Wartens. Statt 1000 Millisekunden geradeaus zu warten, schaltet ihr viermal die Farben um und wartet jedes Mal 250 Millisekunden. Das dauert auch 1000 Millisekunden. Ein Ton dauert selbst einen Moment: Er kann eine der Pausen ersetzen.

:::bloecke

Töne findet ihr in der Blockliste unter **Musik**.

:::

:::python

```python
import music

music.pitch(880, 200)
music.pitch(660, 200)
```

`music.pitch(880, 200)` spielt einen Ton mit 880 Hertz für 200 Millisekunden.

:::

## Auftrag 4: Der Parcours

Baut mit einem anderen Team eine Strecke mit Start, Ziel und mindestens zwei Kurven. Jedes Team programmiert sein Auto so, dass es die Strecke ohne Sensoren schafft, nur mit Fahren, Drehen und Warten. Wer kommt dem Ziel am nächsten?

## Auftrag 5: Eure eigene Idee

Ein Auto, das tanzt? Das einparkt? Das bei Dunkelheit das Licht einschaltet? Schreibt eure Idee zuerst als Plan in Worten auf und zeigt sie eurer Kursleitung.
