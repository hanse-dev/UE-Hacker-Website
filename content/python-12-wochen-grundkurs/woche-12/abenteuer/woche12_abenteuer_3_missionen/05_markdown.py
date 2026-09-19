"""### ⭐⭐⭐☆☆ Mission 2: Das Heilmittel

Der Kampf gegen den Drachen ist hart – ein Heiltrank könnte helfen!

**Schritt 1 – Heilmittel verstecken:**
Lege einen `Gegenstand("Heiltrank", ...)` in den Raum `"quelle"` (zur Liste `welt["quelle"]["gegenstaende"]` hinzufügen).

**Schritt 2 – Neue Methode:**
Schreibe eine Funktion `benutze(self, gegenstand_name)`, die im Inventar sucht. Ist es `"Heiltrank"`, erhöht sie `self.hp` um 10 und entfernt den Gegenstand aus dem Inventar. Bei anderen Gegenständen soll eine Meldung erscheinen, dass man damit nichts anfangen kann. Fehlt der Gegenstand, gibt sie ebenfalls eine Meldung aus.

**Schritt 3 – An die Klasse hängen:**
Mit `Spieler.benutze = benutze` wird die Funktion zur Methode aller Spieler. Teste sie mit einem Spieler, dessen `hp` du vorher auf 5 gesetzt hast.

**Bonus:** Das Heilmittel soll die HP höchstens auf 20 auffüllen."""