"""# 📖 Glossary – 🚀 Week 11 – Advanced OOP: The Magic Evolution!
> You can keep this notebook open all week.

| Term | Meaning | Example |
|------|---------|--------|
| **Inheritance** | A class inherits all properties and methods from another | `class Wizard(Hero):` |
| `super()` | Access the parent class | `super().__init__(name)` |
| **Polymorphism *(= same method that works differently depending on the class)*** | Same method – different behavior depending on the class | `animal.sound()` – Dog: Woof, Cat: Meow |
| `__str__` | Text representation of an object – called by `print()` and `str()` | `def __str__(self): return f\"{self.name}\"` |
| `__repr__` | Developer representation of an object | `def __repr__(self): return f\"Hero({self.name})\"` |
| `__add__` | Overload the `+` operator for custom classes | `def __add__(self, other):` |
| `__len__` | Enable `len()` for custom classes | `def __len__(self): return len(self.members)` |
| `__eq__` | Overload the `==` operator for custom classes | `def __eq__(self, other): return self.name == other.name` |"""
