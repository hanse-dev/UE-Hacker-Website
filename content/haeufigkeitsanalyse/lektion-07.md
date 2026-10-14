# Wenn das E nicht gewinnt

Dein Knacker hat eine Schwäche. Er verlässt sich auf einen einzigen Buchstaben – und bei kurzen Nachrichten ist das E nicht immer der Spitzenreiter. Diese hier wurde abgefangen:

```
atykx vgyycuxz rgazkz jxginkthraz
```

Der häufigste Buchstabe ist `z`. Dein Knacker hält ihn für ein `e`, rechnet die Verschiebung 21 aus und liefert:

```
fydpc alddhzce wlfepe oclnspymwfe
```

Buchstabensalat! Im echten Klartext ist nämlich das `t` am häufigsten, nicht das `e`.

Die Lösung: Verlass dich nicht auf **einen** Buchstaben, sondern schau dir **alle** an. Du probierst alle 26 Verschiebungen aus (wie beim Brute-Force-Knacker) – aber statt selbst zu lesen, lässt du dein Programm jedem Versuch **Punkte** geben: Häufige deutsche Buchstaben bringen viele Punkte, seltene wenige. Die Punkte stehen im Dictionary `PUNKTE` und entsprechen der Häufigkeit in Prozent (`e` bringt 17, `n` bringt 10, `x` bringt 0).

```
def bewerte(text):
    punkte = 0
    für jedes zeichen in text:
        wenn zeichen in PUNKTE steht:
            zähle PUNKTE[zeichen] zu punkte dazu
    gib punkte zurück
```

Echtes Deutsch sammelt so viel mehr Punkte als Buchstabensalat: `bewerte("hallo welt")` ergibt 49, für das verschlüsselte `"kdoor zhow"` sind es nur 30.

Der bessere Knacker nutzt wieder das "Merke dir den bisher besten"-Muster aus Lektion 4:

```
def knacke_besser(text):
    bester_text = ""
    beste_punkte = -1
    für jede verschiebung von 0 bis 25:
        entschlüssele den text mit dieser Verschiebung
        bewerte den Versuch
        wenn er mehr Punkte hat als beste_punkte:
            merke dir die Punkte und den Versuch
    gib bester_text zurück
```

Ganz unfehlbar ist auch das nicht: Bei sehr kurzen Texten wie einem einzelnen Wort kann der Zufall jede Statistik austricksen. Je länger die Nachricht, desto sicherer der Treffer.

> 💡 So arbeiten auch echte Code-Knacker: nicht eine Regel blind anwenden, sondern alle Möglichkeiten bewerten und die wahrscheinlichste nehmen.
