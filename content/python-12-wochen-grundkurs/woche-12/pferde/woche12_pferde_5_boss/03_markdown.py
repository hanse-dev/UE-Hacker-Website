"""### ⭐⭐⭐⭐☆ Boss-Quest 1: Der vollständige Spielstand

Der Spielstand aus der Lektion hat eine Schwäche: Er merkt sich nicht, **welche Gegenstände noch in den Räumen liegen** und wie viel Leben der Gegner noch hat. Nach dem Laden wäre `Stallbesen` also wieder da!

**Schritt 1 – Speichern:**
Schreibe `speichern_komplett(spieler)`. Das Dictionary enthält den Spieler (wie bisher) **und** den Zustand jedes Raums: die Namen und Beschreibungen seiner Gegenstände sowie die HP des Gegners (oder `None`, wenn es keinen gibt).

**Schritt 2 – Laden:**
Schreibe `laden_komplett()`, die alle Räume wieder herstellt und den `Spieler` zurückgibt. Fehlt die Datei, soll sie `None` zurückgeben.

**Schritt 3 – Beweisen:**
Lass einen Spieler `Stallbesen` nehmen, speichere, zerstöre absichtlich den Inhalt des Raums `"sattelkammer"`, lade – und prüfe, dass der Raum wieder stimmt.

**Bonus:** Speichere zusätzlich, wie oft der Spieler schon gespeichert hat."""