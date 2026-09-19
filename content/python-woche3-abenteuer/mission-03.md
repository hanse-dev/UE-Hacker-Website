# ⭐⭐⭐⭐☆ Mission 3: Die Arena des Champions

In der Arena werden Kämpfer nach ihrer Leistung bewertet! Aus Siegen und Niederlagen berechnest du die **Siegquote** (`siege / (siege + niederlagen)`) und prüfst sie zusammen mit dem Level – mit `and`.

| Rang | Regel |
|------|-------|
| LEGENDÄR | level >= 50 **und** Siegquote > 0.8 |
| MEISTER | level >= 30 **und** Siegquote > 0.6 |
| KÄMPFER | alle anderen |
| Bonus für perfekte Serie | niederlagen == 0 (separat mit einem eigenen `if` prüfen) |

**Bonus (freiwillig, ohne Prüfung):** Berücksichtige auch die Gesamtzahl der Kämpfe!
