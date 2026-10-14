# Eine Nachricht ohne Schlüssel

Alarm in der Zentrale! Deine Agentin hat eine verschlüsselte Nachricht abgefangen:

```
dboppox gsb exc roedo kloxn ew csolox erb rsxdob nob kvdox lslvsydrou.
lbsxqo nso ukbdo exn nox cmrveoccov wsd. xsowkxn nkbp exc corox, noxx
nob posxn vsocd tono xkmrbsmrd. goxx nob wyxn kepqord, qorox gsb
qowosxckw jew fobcdomu.
```

Du weißt nur: Es ist eine Cäsar-Chiffre. Die Verschiebung kennt niemand.

Im [Cäsar-Projekt](/kurs/projekt-caesar-chiffre) hast du dafür den Brute-Force-Knacker gebaut: alle 26 Verschiebungen ausgeben und selbst nachsehen, welche Zeile lesbar ist. Das klappt – aber *du* musst dabei 26 Zeilen Buchstabensalat lesen. In diesem Projekt findet dein Programm den Schlüssel ganz allein.

Der Trick heißt **Häufigkeitsanalyse**. In deutschen Texten kommen nicht alle Buchstaben gleich oft vor: Das **E** ist mit Abstand der häufigste, ein Q oder X siehst du fast nie. Und genau hier ist Cäsar schwach: Jedes `e` wird immer zum **selben** Geheimbuchstaben. Der häufigste Buchstabe im Geheimtext ist also sehr wahrscheinlich ein verkleidetes `e`.

Dafür musst du zuerst zählen können. So zählst du, wie oft ein bestimmter Buchstabe in einem Text steckt:

```
anzahl = 0
für jedes zeichen im text:
    wenn zeichen der gesuchte Buchstabe ist:
        zähle anzahl um eins hoch
gib anzahl aus
```

Wie im Cäsar-Projekt schreiben wir alle Texte klein und ohne Umlaute (`ae`, `ue`, `ss`) – deine Funktionen rechnen nur mit den 26 Buchstaben von `a` bis `z`.

In der Bonus-Aufgabe steht der lange Geheimtext in runden Klammern über mehrere Zeilen verteilt. Python klebt solche Stücke automatisch zu **einem** String zusammen – das ist nur besser lesbar als eine einzige, endlos lange Zeile.

> 💡 `for`-Schleifen über einen Text kennst du aus [Woche 4](/kurs/python-12-wochen-grundkurs?week=4&tab=lektion#woche-4) des 12-Wochen-Kurses und aus dem [Cäsar-Projekt](/kurs/projekt-caesar-chiffre).
