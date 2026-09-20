# 🥕 Lesson 2: One parameter

So far your routine does the same thing every time. With a **parameter** it gets an **ingredient** that you can change on every call:

```python
def greet(name):
    print(f"Hello, {name}!")

greet("Stormwind")
greet("Luna")
```

**Step by step:**
1. **`name`** in the parentheses is the **parameter** – a placeholder
2. On the call you pass an **argument**, e.g. `"Stormwind"`
3. Inside the function `name` is then a completely normal **variable** with that value
4. The next call brings a new value

> 💡 **Parameter** is the ingredient in the definition, **argument** is the value you put in on the call.

Numbers work too: `show_age(4)` gives the function the number 4 – without quotes.
