# Leben und Game Over

Ein echtes Spiel geht irgendwann zu Ende. Dafür bekommt dein Spiel jetzt **Leben**: Verpasst der
Ball den Schläger (er fällt über `y = 300` hinaus, ohne dass `istTreffer` zugeschlagen hat), zieht
das ein Leben ab und der Ball startet neu oben. Sind alle Leben aufgebraucht, zeigt das Spielfeld
„Game Over" und die Schleife hört auf, sich selbst erneut aufzurufen.

Das komplette Spiel steht unten schon fast fertig da – Schläger, Ball, Tastatursteuerung,
Treffererkennung und Punktestand aus den letzten vier Lektionen sind bereits eingebaut. Nur eine
Stelle fehlt noch: was passiert, wenn der Ball durchrutscht.

Damit hast du ein vollständiges kleines Spiel mit echtem Spielende. In den nächsten beiden
Lektionen bekommt es noch mehr Tiefe: Hindernisse, die du **nicht** fangen willst, und Bonus-Items,
die deinen Schläger schneller machen.
