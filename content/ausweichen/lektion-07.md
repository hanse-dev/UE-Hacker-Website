# Immer schneller

Hast du schon 20 Punkte geschafft? Dann ist das Spiel zu leicht! Es soll mit der Zeit schwerer werden: Der Stein fällt immer schneller.

Bisher fällt der Stein in jedem Bild um 4. Die 4 ist sein **Tempo**. Wenn das Tempo in einer Variable steht, kann es sich während des Spiels ändern.

In der Vorlage gibt es dafür die Variable **tempo**. Sie fängt bei 4 an.

:::bloecke

Eine Variable kannst du überall dort einsetzen, wo eine Zahl stehen kann. Du findest sie unter **Variablen** und ziehst sie einfach auf das Zahlenfeld.

:::

:::python

Eine Variable kannst du überall dort einsetzen, wo eine Zahl stehen kann: Statt `+= 4` schreibst du dann den Namen der Variable. Auch `tempo` steht in der Zeile `global` am Anfang von `jedes_bild`, weil die Funktion sie ändern soll.

:::

## Schneller werden

Jetzt fehlt nur noch, dass das Tempo steigt. Ein guter Moment dafür: immer dann, wenn du einen Punkt bekommst.

> 💡 Spiel ein paar Runden. Wird es zu schnell zu schwer? Dann lass das Tempo mit einer kleineren Zahl starten.
