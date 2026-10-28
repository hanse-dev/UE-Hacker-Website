# KI-Test-Kind (11 Jahre)

1 Lektionen geprüft, 0 davon ohne Änderungsbedarf. 4 Stellen lohnen eine Änderung, 0 davon wichtig (das Test-Kind wäre ohne Hilfe nicht weitergekommen).
Rechnerische Kosten (Listenpreis, im Abo enthalten): 0.53 $. Einzelheiten je Aufgabe stehen in der .json-Datei daneben.

| Woche | Lektion | Stelle | Problem | Hätte geholfen | Gewicht |
|---|---|---|---|---|---|
| 12 | lektion-07 – Etappe 7: Speichern und das Finale | Aufgabe 2 | `json.dumps` kommt vorher nirgends vor. Ich kenne nur `json.dump` mit Datei und weiß nicht, was das "s" anders macht. | Ein Satz wie: `json.dumps(daten)` macht aus dem Dictionary einen JSON-Text, ohne Datei. Dazu ein kurzes Beispiel mit der Ausgabe. | mittel |
| 12 | lektion-07 – Etappe 7: Speichern und das Finale | Text, Code von speichern() und laden() | `encoding="utf-8"`, `ensure_ascii=False` und `indent=2` werden nicht erklärt. Ich weiß nicht, ob ich die brauche oder weglassen darf. | Kurze Kommentare im Code, z. B. # damit Umlaute und Emojis richtig gespeichert werden, # schön eingerückt, damit man es lesen kann. | mittel |
| 12 | lektion-07 – Etappe 7: Speichern und das Finale | Text, Code von speichern(), laden() und spiele() | `dateiname="stand.json"` in der Klammer bei def kenne ich nicht. Ich verstehe nicht, warum man dann später `laden()` ohne Namen aufrufen kann. | Ein Hinweis: Wenn man beim Aufruf nichts angibt, wird automatisch "stand.json" benutzt (Standardwert). | mittel |
| 12 | lektion-07 – Etappe 7: Speichern und das Finale | Aufgabe 3 | Der Editor ist leer und es gibt keine Klasse Spieler. Ich wusste nicht, was laden zurückgeben soll, wenn die Datei doch da ist. | Dazuschreiben: Wenn die Datei da ist, gib einfach `daten` zurück. | mittel |
