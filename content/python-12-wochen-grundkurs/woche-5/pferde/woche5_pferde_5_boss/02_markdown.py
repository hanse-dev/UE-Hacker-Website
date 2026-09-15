"""### ⭐⭐⭐⭐☆ Boss-Quest 1: Der Trainings-Generator

Baue ein System, das automatisch verschiedene Trainings für Pferde erzeugt, bewertet und in einem Trainingsplan speichert.

**Schritt 1 – Trainingsnamen erzeugen:**
Schreibe eine Funktion `generiere_training_name(pferde_typ, schwierigkeit)`, die aus Typ und Schwierigkeit einen Namen bildet (z.B. \"SPRINGEN-L3\") und gib den Namen als String zurück

**Schritt 2 – Intensität berechnen:**
Erstelle eine Funktion `berechne_intensitaet(dauer, pferde_typ)`, die einen Wert zwischen 0 und 100 zurückgibt und nutze unterschiedliche Faktoren je nach `pferde_typ` (z.B. \"Sportpferd\", \"Freizeitpferd\")

**Schritt 3 – Trainings-Daten erstellen:**
Schreibe eine Funktion `erstelle_training(pferde_typ, schwierigkeit, dauer)`, die ein Dictionary mit Name, Typ, Schwierigkeit und Intensität zurückgibt und verwende dafür deine beiden vorherigen Funktionen

**Schritt 4 – Trainingsplan verwalten:**
Erstelle eine Liste `trainings_plan` und schreibe eine Funktion `speichere_training(plan, training)`, die das Training hinzufügt

**Schritt 5 – Generator nutzen:**
Erzeuge im Hauptteil mindestens 5 Trainings mit verschiedenen Parametern und speichere sie im Plan und gib eine kleine Statistik (Anzahl, durchschnittliche Intensität) aus

**Bonus:** Füge eine Funktion hinzu, die alle Trainings nach Intensität sortiert ausgibt."""
