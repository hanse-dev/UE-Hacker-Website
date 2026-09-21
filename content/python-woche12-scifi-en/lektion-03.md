# 🚀 Stage 3: Items

*Knowledge from week 6 + 10: lists and classes*

Every **item** has a name and a description – for this you build the class `Item` (week 10). Every room gets a **list** of its items (week 6):

```python
class Item:
    def __init__(self, name, description):
        self.name = name
        self.description = description

world["airlock"]["items"] = [Item("Keycard", "It opens secured doors.")]
world["corridor"]["items"] = []
world["lab"]["items"] = [Item("Welder", "A tool that can also stop broken robots.")]
world["reactor"]["items"] = [Item("Switch", "The red emergency stop switch of the reactor.")]
```

A room without items simply has an empty list `[]`.
