"""### ⭐⭐⭐⭐☆ Boss-Quest 3: Die Missions-Datenbank

Verwalte Missionen in einer Liste: anlegen, suchen, filtern und auswerten.

**Schritt 1 – Mission anlegen:**
Erstelle eine Funktion `erstelle_mission(name, ziel, prioritaet)`, die ein Dictionary mit den Keys \"name\", \"ziel\", \"prioritaet\" (und optional \"status\") zurückgibt und gib das Dictionary mit `return` zurück

**Schritt 2 – Mission zur Liste hinzufügen:**
Erstelle eine Liste `missionen` und schreibe eine Funktion `fuege_mission_hinzu(mission, missionsliste)`, die die Mission mit `append()` zur Liste hinzufügt und eine kurze Bestätigung zurückgibt oder ausgibt

**Schritt 3 – Missionen suchen:**
Schreibe eine Funktion `suche_missionen(missionsliste, suchbegriff)`, die alle Missionen zurückgibt, in deren Name oder Ziel der Suchbegriff vorkommt (z.B. mit `in`) und gib die gefundene Liste zurück

**Schritt 4 – Nach Status filtern:**
Erstelle eine Funktion `filtere_nach_status(missionsliste, status)`, die nur Missionen mit dem angegebenen Status zurückgibt (z.B. \"aktiv\", \"abgeschlossen\") und gib die gefilterte Liste zurück

**Schritt 5 – Statistik ausgeben:**
Schreibe eine Funktion `missionen_statistik(missionsliste)`, die die Anzahl der Missionen und optional die Verteilung nach Priorität oder Status berechnet und ausgibt und rufe im Hauptteil alle Funktionen auf: Missionen anlegen, hinzufügen, suchen, filtern, Statistik ausgeben

**Bonus:** Füge zu jeder Mission ein Feld \"ergebnis\" oder \"erfolg\" hinzu und gib eine Erfolgsstatistik aus."""
