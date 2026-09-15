"""# 📖 Glossar – 🚀 Woche 11 – OOP Fortgeschritten: Die magische Evolution!
> Dieses Notebook kannst du die ganze Woche offen lassen.

| Begriff | Bedeutung | Beispiel |
|---------|-----------|----------|
| **Vererbung** | Eine Klasse erbt alle Eigenschaften und Methoden einer anderen | `class Magier(Held):` |
| `super()` | Auf die Elternklasse zugreifen | `super().__init__(name)` |
| **Polymorphismus *(= gleiche Methode, die je nach Klasse unterschiedlich funktioniert)*** | Gleiche Methode – je nach Klasse unterschiedliches Verhalten | `tier.laut()` – Hund: Wuff, Katze: Miau |
| `__str__` | Textdarstellung eines Objekts – aufgerufen von `print()` und `str()` | `def __str__(self): return f\"{self.name}\"` |
| `__repr__` | Entwickler-Darstellung eines Objekts | `def __repr__(self): return f\"Held({self.name})\"` |
| `__add__` | `+`-Operator für eigene Klassen überladen | `def __add__(self, other):` |
| `__len__` | `len()` für eigene Klassen ermöglichen | `def __len__(self): return len(self.mitglieder)` |
| `__eq__` | `==`-Operator für eigene Klassen überladen | `def __eq__(self, other): return self.name == other.name` |"""
