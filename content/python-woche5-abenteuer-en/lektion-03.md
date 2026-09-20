# 🧬 Spell Formula 1: Several parameters

Some spells need more than one ingredient. You separate parameters with **commas**:

```python
def create_character(name, class_name, level):
    print(f"Name: {name}")
    print(f"Class: {class_name}")
    print(f"Level: {level}")

create_character("Aria", "Mage", 5)
```

**Important:** The **order** of the arguments must match the order of the parameters. The first argument (`"Aria"`) lands in the first parameter (`name`), the second (`"Mage"`) in the second (`class_name`) and so on.

> ⚠️ If you swap the arguments, every parameter gets the wrong value – Python does not complain, but the spell goes wrong: `create_character(5, "Aria", "Mage")` prints nonsense!

Also: pass **exactly as many** arguments as the function has parameters – otherwise you get an error message.
