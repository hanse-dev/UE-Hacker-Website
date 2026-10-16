# Fehlersuche

Browser zeigen bei HTML-Fehlern **keine Fehlermeldung**. Sie versuchen, das Beste daraus zu machen – und das sieht dann manchmal seltsam aus. Typische Spuren:

- **Plötzlich ist alles fett oder riesig:** Irgendwo fehlt ein End-Tag, oder dort steht ein Anfangs-Tag statt eines End-Tags (`<h1>…<h1>`).
- **Ein ganzer Teil der Seite fehlt:** Oft ist ein Kommentar nicht richtig geschlossen (`->` statt `-->`). Alles danach gilt dann als Kommentar.
- **Etwas erscheint an der falschen Stelle:** Tags überkreuzen sich.

Lies den Code deshalb Tag für Tag: Hat jedes Anfangs-Tag sein End-Tag? Stimmt die Reihenfolge?
