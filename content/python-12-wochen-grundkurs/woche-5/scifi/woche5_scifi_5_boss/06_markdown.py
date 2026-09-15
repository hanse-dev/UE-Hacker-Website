"""### ⭐⭐⭐⭐☆ Boss-Quest 3: Die Kampf-Simulation

Baue ein vereinfachtes Kampfsimulationssystem für zwei Flotten mit klar getrennten Funktionen.

**Schritt 1 – Kampf initialisieren:**
Erstelle eine Funktion `initialisiere_kampf(flotte1, flotte2)`, die einen Startzustand (z.B. Dictionary) zurückgibt und speichere Namen, Schilde und Hülle beider Flotten darin

**Schritt 2 – Schaden berechnen:**
Schreibe eine Funktion `berechne_schaden(basis_schaden, schild_staerke)`, die den tatsächlichen Schaden (z.B. `basis_schaden - schild_staerke/10`) zurückgibt und nutze diese Funktion später in den Kampfrunden

**Schritt 3 – Kampfrunde ausführen:**
Erstelle eine Funktion `fuehre_runde_aus(status)`, die: und zufällig eine angreifende Flotte wählt,

**Schritt 4 – Kampf steuern:**
Schreibe eine Funktion `starte_simulation(flotte1, flotte2, max_runden)`, die mehrere Runden durchführt, bis eine Flotte besiegt ist oder `max_runden` erreicht sind und gib am Ende eine Zusammenfassung mit Sieger, Verlierer und verbleibender Hülle aus

**Bonus:** Füge Spezialwaffen hinzu, die mit einer kleinen Wahrscheinlichkeit doppelten Schaden verursachen."""
