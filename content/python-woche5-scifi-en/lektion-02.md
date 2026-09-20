# 📡 System Log 2: One parameter

So far your protocol does the same thing every time. With a **parameter** it gets an **input** that you can change on every call:

```python
def report(name):
    print(f"Hello, {name}!")

report("Nova")
report("Kira")
```

**Step by step:**
1. **`name`** in the parentheses is the **parameter** – a placeholder
2. On the call you pass an **argument**, e.g. `"Nova"`
3. Inside the function `name` is then a completely normal **variable** with that value
4. The next call brings a new value

> 💡 **Parameter** is the input in the definition, **argument** is the value you put in on the call.

Numbers work too: `show_energy(80)` gives the function the number 80 – without quotes.
