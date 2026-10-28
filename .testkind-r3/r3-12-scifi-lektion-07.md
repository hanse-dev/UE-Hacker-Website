# KI-Test-Kind (11 Jahre)

1 Lektionen geprüft, 0 davon ohne Änderungsbedarf. 6 Stellen lohnen eine Änderung, 1 davon wichtig (das Test-Kind wäre ohne Hilfe nicht weitergekommen).
Rechnerische Kosten (Listenpreis, im Abo enthalten): 0.55 $. Einzelheiten je Aufgabe stehen in der .json-Datei daneben.

| Woche | Lektion | Stelle | Problem | Hätte geholfen | Gewicht |
|---|---|---|---|---|---|
| 12 | lektion-07 – Etappe 7: Speichern und das Finale | Aufgabe 2 | json.dumps wurde nie gezeigt, wir kennen nur json.dump mit einer Datei. Den Unterschied (das s, keine Datei) muss ich raten. | Ein kurzer Satz im Text: json.dumps(daten) macht aus dem Dictionary einen Text, ohne Datei. Dazu ein kleines Beispiel. | **hoch** |
| 12 | lektion-07 – Etappe 7: Speichern und das Finale | Text, Code von speichern()/laden() | encoding="utf-8", ensure_ascii=False und indent=2 stehen im Code, werden aber nicht erklärt. Ich weiß nicht, ob ich die abschreiben muss. | Kleine Kommentare im Code, z. B. '# damit Umlaute wie ä richtig gespeichert werden' und '# schön eingerückt'. | mittel |
| 12 | lektion-07 – Etappe 7: Speichern und das Finale | Text, Funktionen mit dateiname="stand.json" | Ein Parameter mit = und einem Wert wurde nie erklärt. Ich weiß nicht, ob ich trotzdem einen anderen Dateinamen übergeben darf. | Ein Satz: Wenn du keinen Dateinamen angibst, wird automatisch stand.json benutzt. | mittel |
| 12 | lektion-07 – Etappe 7: Speichern und das Finale | Aufgabe 3 | Es steht nicht da, was laden zurückgeben soll, wenn die Datei da ist. Dass ich import json selbst schreiben muss, steht auch nicht da. | 'Gib sonst die gelesenen Daten zurück' und 'Denk an import json' dazuschreiben. | mittel |
| 12 | lektion-07 – Etappe 7: Speichern und das Finale | Aufgabe 2 vs. Text | Im Text ist das Inventar eine Liste von Dictionaries, in der Aufgabe eine 'Liste der Namen'. Das verwirrt mich. | Klar sagen: Hier reicht eine Liste nur mit den Namen, z. B. ['Zugangskarte']. | mittel |
| 12 | lektion-07 – Etappe 7: Speichern und das Finale | Aufgabe 6 | Es steht nicht da, ob ich zuerst auf 'ende' prüfen oder zuerst fuehre_aus aufrufen soll. Falsch herum kommt bei 'ende' eine 🤔-Meldung. | Ein Hinweis: Prüfe zuerst, ob der Befehl 'ende' ist, und führe ihn erst danach aus. | mittel |
