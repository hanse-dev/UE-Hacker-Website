"""### ⭐⭐⭐⭐☆ Boss-Quest 1: Der Zauber-Generator

Baue ein System, das automatisch verschiedene Zauber mit Element, Stufe und Macht erzeugt und in einem Zauberbuch speichert.

**Schritt 1 – Zaubernamen erzeugen:**
Schreibe eine Funktion `generiere_zauber_name(element_typ, stufe)`, die aus Element und Stufe einen Namen bildet (z.B. \"FEUER-L3\") und gib den Namen als String zurück

**Schritt 2 – Zaubermacht berechnen:**
Erstelle eine Funktion `berechne_macht(komplexitaet, element_typ)`, die einen Wert zwischen 0 und 100 zurückgibt und nutze unterschiedliche Faktoren je nach `element_typ` (z.B. Feuer stärker, Wasser ausgeglichen, Erde defensiv)

**Schritt 3 – Zauber-Daten erstellen:**
Schreibe eine Funktion `erstelle_zauber(element_typ, stufe, komplexitaet)`, die ein Dictionary mit Name, Element, Stufe und Macht zurückgibt und verwende dafür deine beiden vorherigen Funktionen

**Schritt 4 – Zauberbuch verwalten:**
Erstelle eine Liste `zauberbuch` und schreibe eine Funktion `speichere_zauber(buch, zauber)`, die den Zauber hinzufügt

**Schritt 5 – Generator nutzen:**
Erzeuge im Hauptteil mindestens 5 unterschiedliche Zauber und speichere sie im Zauberbuch und gib eine kleine Statistik (Anzahl, durchschnittliche Macht) aus

**Bonus:** Füge eine Funktion hinzu, die alle Zauber nach Macht sortiert ausgibt."""
