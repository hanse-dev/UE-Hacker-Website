"""## 🎒 Stage 3: Items and inventory

*Knowledge from Weeks 6 + 10: lists and classes*

Every **item** has a name and a description. For that we build a class `Item` (Week 10). Every room gets a list of its items (Week 6).

### 💡 New: Objects inside objects (composition)

So far objects only stored simple values (texts, numbers). But an object can also **contain other objects**. The `Player` has an inventory – and that is a list full of `Item` objects.

This is called **composition** and it answers the question: *"Does the object have another object?"*

| Relation | Question | Example |
|----------|----------|---------|
| Inheritance (Week 11) | Is a warrior **a** hero? | `class Warrior(Hero):` |
| Composition | Does the player **have** an item? | `self.inventory = [Item(...)]` |

Both ideas matter: inheritance says "is a", composition says "has a"."""