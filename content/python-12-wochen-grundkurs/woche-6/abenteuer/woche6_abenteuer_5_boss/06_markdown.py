"""### ⭐⭐⭐⭐☆ Boss-Quest 3: Die Quest-Datenbank

Verwalte Quests in einer Liste: anlegen, suchen, filtern und auswerten.

**Schritt 1 – Quest anlegen:**
Erstelle `erstelle_quest(name, ziel, schwierigkeit)`, die ein Dictionary mit \"name\", \"ziel\", \"schwierigkeit\" (und optional \"status\") zurückgibt und gib das Dictionary mit `return` zurück

**Schritt 2 – Quest zur Liste hinzufügen:**
Erstelle eine Liste `quests` und schreibe `fuege_quest_hinzu(quest, questliste)`, die mit `append()` hinzufügt und eine Bestätigung ausgibt

**Schritt 3 – Quests suchen:**
Schreibe `suche_quests(questliste, suchbegriff)`, die alle Quests zurückgibt, in deren Name oder Ziel der Suchbegriff vorkommt

**Schritt 4 – Nach Status filtern:**
Erstelle `filtere_nach_status(questliste, status)` und gib die gefilterte Liste zurück

**Schritt 5 – Statistik ausgeben:**
Schreibe `quest_statistik(questliste)`, die Anzahl und optional Verteilung nach Schwierigkeit ausgibt; rufe im Hauptteil alle Funktionen auf

**Bonus:** Füge zu jeder Quest ein Feld \"belohnung\" oder \"erfolg\" hinzu und gib eine Erfolgsstatistik aus."""
