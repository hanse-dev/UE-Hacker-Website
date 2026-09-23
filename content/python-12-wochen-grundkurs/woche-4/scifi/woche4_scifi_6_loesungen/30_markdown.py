"""## 🐛 Debug-Quest

### Debug-Quest – Aufgabe 1

🐛 Bug #1 – Ziel: Das Programm soll die Zeit von 1 bis 5 zählen und jeden Wert ausgeben (Zeit 1 bis Zeit 5). Was ist falsch?

**Erklärung:** `range(1, 5)` hört vor der 5 auf – die Obergrenze zählt nicht mit. Für 1 bis 5 braucht es `range(1, 6)`."""