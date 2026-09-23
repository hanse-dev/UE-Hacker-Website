# 🚀 KI-Modul 4: Polymorphismus

**Polymorphismus** heißt „viele Formen“: Du rufst **dieselbe Methode** bei ganz verschiedenen Objekten auf – jedes reagiert auf **seine Art**:

```python
team = [Roboter("Zeta"), Kampfroboter("Nova"), Reparaturroboter("Orbit")]
for f in team:
    f.arbeite()
```

1. Alle drei Objekte haben `arbeite()`, aber jede Klasse macht etwas anderes
2. Die Schleife muss **nicht wissen**, welche Klasse gerade dran ist
3. **Duck Typing:** „Wenn es läuft wie eine Ente und quakt wie eine Ente, ist es eine Ente.“ Eine Klasse **ohne** Vererbung darf auch mitmachen, wenn sie die Methode hat.
