# 🏇 Lesson 3: Several parameters

Some exercises need more than one ingredient. You separate parameters with **commas**:

```python
def introduce_horse(name, breed, age):
    print(f"Name: {name}")
    print(f"Breed: {breed}")
    print(f"Age: {age}")

introduce_horse("Stormwind", "Hanoverian", 6)
```

**Important:** The **order** of the arguments must match the order of the parameters. The first argument (`"Stormwind"`) lands in the first parameter (`name`), the second in the second (`breed`) and so on.

> ⚠️ If you swap the arguments, every parameter gets the wrong value – Python does not complain, but the output is nonsense: `introduce_horse(6, "Stormwind", "Hanoverian")`!

Also: pass **exactly as many** arguments as the function has parameters – otherwise you get an error message.
