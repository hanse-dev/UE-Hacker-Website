# 🐴 Stage 3: Items

*Knowledge from week 6 + 10: lists and classes*

Every **item** has a name and a description – for this you build the class `Item` (week 10). Every room gets a **list** of its items (week 6):

```python
class Item:
    def __init__(self, name, description):
        self.name = name
        self.description = description

world["yard"]["items"] = [Item("Flashlight", "It lights up dark corners.")]
world["aisle"]["items"] = []
world["saddlery"]["items"] = [Item("Broom", "A sturdy broom. It helps to chase away the goat.")]
world["paddock"]["items"] = [Item("Foal", "The little foal follows you trustfully.")]
```

A room without items simply has an empty list `[]`.
