"""### ⭐⭐⭐☆☆ Mission 2: Das polymorphe Training

Die Reitschule braucht ein System für verschiedene Trainingsmethoden!

**Schritt 1 – Drei Trainings-Klassen anlegen:**
Erstelle `class Dressur:`, `class Springen:`, `class Western:` jeweils mit `__init__(self, name)` und einer Methode `training(self)` und jede `training()` gibt eine andere Übung aus (z.B. \"Piaffe üben!\", \"Parcours springen!\", \"Slalom reiten!\")

**Schritt 2 – Polymorphe Funktion:**
Erstelle eine Funktion `trainiere_pferd(pferd, training)`, die `training.training()` aufruft (oder die Übung ausgibt) und die Funktion soll mit allen drei Trainingsarten funktionieren

**Schritt 3 – Alle Trainings testen:**
Erstelle je ein Objekt Dressur, Springen und Western und rufe die polymorphe Funktion für jede Trainingsart auf

**Bonus:** Erstelle eine Trainer-Fabrik-Funktion, die je nach Typ das passende Training erzeugt."""
