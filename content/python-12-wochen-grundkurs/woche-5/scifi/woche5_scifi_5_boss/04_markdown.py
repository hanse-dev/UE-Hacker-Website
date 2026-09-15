"""### ⭐⭐⭐⭐⭐ Boss-Quest 2: Der Raumstation-Manager

Baue ein System, das die wichtigsten Bereiche einer Raumstation verwaltet: Sektoren, Energie und Personal.

**Schritt 1 – Sektoren erzeugen:**
Erstelle eine Funktion `erstelle_sektor(sektor_id, groesse)`, die ein Dictionary mit ID, Größe und Anfangsenergie zurückgibt und lege eine Liste mit mehreren Sektoren an

**Schritt 2 – Energie verteilen:**
Schreibe eine Funktion `verteile_energie(sektoren, gesamt_energie)`, die die Energie proportional zur Größe auf die Sektoren verteilt und aktualisiere dafür die Einträge in den Sektor-Dictionaries

**Schritt 3 – Schichtplanung vereinfachen:**
Erstelle eine Funktion `plane_schichten(anzahl_personal, schichten)`, die eine einfache Verteilung (z.B. gleichmäßig) berechnet und gib eine Liste mit Personalzahlen pro Schicht zurück

**Schritt 4 – Stations-Übersicht erzeugen:**
Schreibe eine Funktion `erzeuge_stationsbericht(sektoren, energie, personal)`, die eine Übersicht als Text zurückgibt und nutze Informationen aus den Sektoren, der Gesamtenergie und der Personalzahl

**Bonus:** Füge eine einfache Notfall-Funktion hinzu, die bei zu wenig Energie in einem Sektor eine Warnung zurückgibt."""
