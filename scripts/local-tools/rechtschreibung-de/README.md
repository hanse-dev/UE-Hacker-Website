# Lokales Tool: Deutsche Rechtschreib- und Grammatikprüfung (`rechtschreibung-de/`)

`npm run lint:spelling:de` — zieht den deutschen Fließtext (ohne Code) aus `content/`,
`public/kurse.json` und `src/locales/de.js` und prüft ihn mit [LanguageTool](https://languagetool.org)
(Open Source). Läuft auf jedem System mit Docker und Python 3: beim ersten Lauf wird der Container
`ue-hacker-languagetool` gestartet (Image `erikvl87/languagetool`, ~1,2 GB, nur an `127.0.0.1`
gebunden — kein Text verlässt den Rechner). Ein Volllauf dauert etwa 6 Minuten. **Nicht Teil von
Hooks/CI/Deploy.** Ergänzt `npm run lint:spelling` (cspell), das bei Deutsch zu viel durchlässt.

- `npm run lint:spelling:de` — nur Rechtschreibung, Exit-Code 1 bei Funden. Legitime Wörter
  (Fachbegriffe, Namen) kommen in `rechtschreibung-de/erlaubt.txt`; Code-Bezeichner aus dem
  Content werden automatisch ignoriert.
- `npm run lint:spelling:de -- --grammatik` — zusätzlich Grammatik-Hinweise (Kongruenz, Kommas).
  Das sind Kandidaten zum Nachlesen, kein Gate: Wegen der Code-Bezeichner im Fließtext sind viele
  Treffer Fehlalarme; laute Regeln stehen in `STILLE_REGELN` in `pruefe.py`.
- `npm run lint:spelling:de -- --stopp` — Container wieder entfernen.
- Ohne Docker: LanguageTool anders starten (z.B. per Java) und `LANGUAGETOOL_URL` setzen.

Verständlichkeit, kaputte Sätze und Aufgaben, die nicht zur Prüfung passen, findet kein Tool
zuverlässig — dafür bleibt nur Lesen.

## Fallstricke

- Die Docker-VM mit 2 GB verträgt nur einen Request gleichzeitig und höchstens ~1,1 GB Heap.
- Nicht parallel zu Playwright-Läufen starten: Die Last lässt Tests mit Timeouts scheitern.
- Der Extraktor löscht Inline-Code; dadurch entstehen Fehlalarme wie „Mit teilst du“ (aus „Mit `<h2>` teilst du“).
