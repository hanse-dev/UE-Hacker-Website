# 🛰️ System Log 3: Several parameters

Some protocols need more than one input. You separate parameters with **commas**:

```python
def register_crew(name, role, level):
    print(f"Name: {name}")
    print(f"Role: {role}")
    print(f"Level: {level}")

register_crew("Nova", "Pilot", 5)
```

**Important:** The **order** of the arguments must match the order of the parameters. The first argument (`"Nova"`) lands in the first parameter (`name`), the second in the second (`role`) and so on.

> ⚠️ If you swap the arguments, every parameter gets the wrong value – Python does not complain, but the output is nonsense: `register_crew(5, "Nova", "Pilot")`!

Also: pass **exactly as many** arguments as the function has parameters – otherwise you get an error message.
