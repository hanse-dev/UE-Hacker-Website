# ⚔️ Stage 3: Items

*Knowledge from week 6 + 10: lists and classes*

Every **item** has a name and a description – for this you build the class `Item` (week 10). Every room gets a **list** of its items (week 6):

```python
class Item:
    def __init__(self, name, description):
        self.name = name
        self.description = description

world["entrance"]["items"] = [Item("Torch", "It lights up dark corners.")]
world["hall"]["items"] = []
world["spring"]["items"] = [Item("Sword", "A sharp sword stuck in the stone by the spring.")]
world["treasury"]["items"] = [Item("Treasure", "The legendary treasure of Pyralia!")]
```

A room without items simply has an empty list `[]`.
