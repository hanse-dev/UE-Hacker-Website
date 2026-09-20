# 🐴 Lesson 1: Defining a routine

Welcome to the **Hall of Perfection**! The trainer says: *"You develop a good exercise once – and repeat it with every horse."*

That is exactly what a **function** does: a piece of code with a name that you can call again and again.

```python
def greet_horse():
    print("Hello, Stormwind!")
    print("Time for training!")

greet_horse()
greet_horse()
```

**Step by step:**
1. **`def`** starts the definition – here you only *define* the routine
2. **`greet_horse`** is the name of the routine
3. **`()`** and the **colon `:`** always belong there
4. The **indented** code (4 spaces) is the routine itself
5. **`greet_horse()`** – with parentheses – *runs* it

> ⚠️ Defining does not run anything yet! Only the **call with parentheses** runs the code. Without parentheses (`greet_horse`) nothing starts.

Every call runs the code again – so you save yourself copy & paste.
