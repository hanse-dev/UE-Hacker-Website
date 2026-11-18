# Punkte zählen

Ein Spiel braucht Punkte! Jedes Mal, wenn der Stein unten ankommt und wieder oben startet, bist du ihm ausgewichen. Dafür gibt es einen Punkt.

Die Punkte merkt sich die Variable **punkte**. Sie steht schon in der Vorlage und fängt bei 0 an.

:::bloecke

Zum Hochzählen gibt es unter **Variablen** den Block **ändere … um …**. So zählt zum Beispiel ein Zähler um 1 hoch:

```bloecke
[variablen] ändere zaehler um 1
```

Überlege, wo der Block hin muss: Er soll nur laufen, wenn der Stein gerade wieder nach oben gesetzt wird.

:::

:::python

Zum Hochzählen nimmst du `+= 1`, so wie beim Bewegen:

```python
zaehler += 1
```

Überlege, wo die Zeile hin muss: Sie soll nur laufen, wenn der Stein gerade wieder nach oben gesetzt wird.

**Neu: `global`.** In der Vorlage steht am Anfang von `jedes_bild` die Zeile `global punkte`. Die braucht Python, weil `punkte` **außerhalb** der Funktion angelegt wird, in der Funktion aber geändert werden soll. Ohne sie meldet Python einen Fehler. Bei `spieler` und `stein` ist das nicht nötig: Dort änderst du nur `x` und `y`, nicht die Variable selbst.

:::

## Punkte anzeigen

Der Punktestand soll oben links auf der Bühne stehen, zum Beispiel „Punkte: 3“. Dafür setzt du einen Text und eine Zahl zusammen.

:::bloecke

Der Block **zeige** (unter **Spiel**) schreibt etwas oben links auf die Bühne. Mit **erstelle Text aus** (unter **Text**) hängst du Text und Zahl aneinander. So sähe es für Leben aus:

```bloecke
[aktion] zeige
  [text] erstelle Text aus "Leben: " leben
```

:::

:::python

`zeige(...)` schreibt etwas oben links auf die Bühne. Text und Zahl hängst du mit `+` aneinander, dafür muss die Zahl mit `str(...)` erst zu Text werden. So sähe es für Leben aus:

```python
    zeige("Leben: " + str(leben))
```

:::
