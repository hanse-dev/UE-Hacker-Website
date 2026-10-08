# Stufe 10: Meisterstufe

Ihr kennt jetzt alle Teile des Autos. Hier gibt es keine fertigen Programme mehr, nur Aufträge und Hinweise. Sucht euch aus, was euch reizt. Zwei gelöste Aufträge reichen für den Abschluss.

## Auftrag 1: Sicher auf der Linie

Das Auto folgt der Linie wie in Stufe 9. Steht ein Hindernis auf der Strecke, hält es an und wartet, bis der Weg wieder frei ist.

Hinweis: Prüft zuerst den Abstand wie in Stufe 6. Nur wenn der Weg frei ist, kommt der Linienfolger an die Reihe.

## Auftrag 2: Der Lichtsucher

Vorn am Auto sitzen zwei Lichtsensoren. Das Auto soll einer Taschenlampe folgen: Es dreht sich zu der Seite, auf der es heller ist.

:::bloecke

Die Blöcke **LDR_L** und **LDR_R** melden die Helligkeit links und rechts als Zahl von 0 bis 1023. Lasst euch die Werte zuerst mit **zeige Zahl** anzeigen.

:::

:::python

```python
hell_links = pin1.read_analog()
hell_rechts = pin0.read_analog()
```

Beide Werte liegen zwischen 0 und 1023. Lasst sie euch zuerst mit `display.scroll` anzeigen.

:::

Hinweis: Findet heraus, welche Zahl im Raum normal ist und welche im Licht der Taschenlampe. Dazwischen liegt eure Grenze.

## Auftrag 3: Das Einsatzfahrzeug

Das Auto fährt ein Quadrat. Dabei blinken die Scheinwerfer abwechselnd blau und rot, und der micro:bit spielt eine Sirene.

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

## Bonus: Noch ein Auftrag

Zwei Aufträge sind geschafft und es ist noch Zeit? Dann löst einen dritten. Oder verbindet zwei Aufträge zu einem Programm.
