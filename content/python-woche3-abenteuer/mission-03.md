# ⭐⭐⭐⭐☆ Mission 3: Die Arena des Champions

In der Arena werden Kämpfer nach ihrer Leistung bewertet! Aus Siegen und Niederlagen berechnest du die **Siegquote** (`siege / (siege + niederlagen)`) und prüfst sie zusammen mit dem Level – mit `and`.

Die Siegquote sagt, welcher Anteil der Kämpfe gewonnen wurde: 18 Siege bei 20 Kämpfen ergeben `0.9`, also 9 von 10. `/` heißt geteilt, die Klammer rechnet Python zuerst.

| Rang | Regel |
|------|-------|
| LEGENDÄR | level >= 50 **und** Siegquote > 0.8 |
| MEISTER | level >= 30 **und** Siegquote > 0.6 |
| KÄMPFER | alle anderen |
| Bonus für perfekte Serie | niederlagen == 0 (separat mit einem eigenen `if` prüfen) |

**Bonus (freiwillig, ohne Prüfung):** Berücksichtige auch die Gesamtzahl der Kämpfe!
