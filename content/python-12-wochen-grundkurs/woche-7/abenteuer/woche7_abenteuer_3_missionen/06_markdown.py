"""### ⭐⭐⭐⭐☆ Mission 3: Die Runenschmiede

Die letzte Prüfung: Schmiede einen Runen-Schlüssel und finde die richtige Stunde, um das Archiv endgültig zu öffnen.

**Schritt 1 – Runen-Alphabet:**
Baue ein Alphabet aus `string.ascii_letters` und `string.digits` (zusammengefügt) und gib es aus

**Schritt 2 – Runen-Schlüssel schmieden:**
Ziehe mit einer Schleife oder List Comprehension 8 zufällige Zeichen aus deinem Alphabet (mit `random.choice()`) und füge sie mit `\"\".join()` zu einem Schlüssel zusammen

**Schritt 3 – Die richtige Stunde:**
Prüfe mit `datetime.now().hour`, ob gerade Tag (6–18 Uhr) oder Nacht ist, und gib eine passende Meldung aus

**Schritt 4 – Das Archiv öffnen:**
Kombiniere Runen-Schlüssel und Tageszeit-Meldung zu einer Abschluss-Ausgabe (z.B. „Das Archiv öffnet sich für dich!“)

**Bonus:** Nutze `random.seed()` vor Schritt 2, um denselben Runen-Schlüssel reproduzierbar zu erzeugen – ein Trick, den echte Archivare zum Testen benutzen."""
