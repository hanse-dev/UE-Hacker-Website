# 🐴 Week 3: The Switches of the Riding Trail

Welcome, horse friend! You have reached the **Crossroads of the Pasture** – here every choice decides the right riding trail. This week you will learn how your program makes **decisions**:

1. **if** – run code only when something is true
2. **Comparison operators** – `==`, `!=`, `<`, `>`, `<=`, `>=`
3. **if-else** – two paths
4. **if-elif-else** – many paths
5. **and, or, not** – combine conditions
6. **Nested conditions** – a decision inside a decision

Ride wisely! Your horse trusts you...

## 🚦 Lesson 1: if

`if` checks a **condition** and runs the code below it **only when the condition is true (`True`)**.

```python
horse_age = 5
if horse_age >= 5:
    print("The horse is ready for training!")
```

> ⚠️ **Important:** After the condition comes a **colon `:`**, and the code that belongs to it is **indented** (4 spaces or the Tab key). The indentation shows Python what belongs to the `if`.

A condition can also be a truth value (`bool`) from Week 2:

```python
has_saddle = True
if has_saddle:
    print("You can mount up!")
```

If the condition is `False`, the indented code is simply skipped.
