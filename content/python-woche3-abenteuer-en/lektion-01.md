# ⚖️ Magic Formula 1: `if`

Welcome, wise adventurer! You have reached the **Crossroads of Fate** – a magical place where every decision determines victory or defeat. This week you will learn how your programs make decisions:

**Your mission this week:**
- Make decisions with **if**, **if-else** and **if-elif-else**
- Master **comparison operators** for precise judgments
- Command **logical connectors** (`and`, `or`, `not`) for complex conditions
- Understand the **power of indentation** for nested paths

> 💡 **Week 2 recap:** `True` and `False` are the **Air** element (`bool`). Conditions always end up as `True` or `False`.

## The first formula

`if` checks a condition and only runs the code below it when the condition is **true**.

```python
level = 5
if level >= 5:
    print("You are ready for the quest!")
```

> ⚠️ The code after `if` must be **indented** (4 spaces). The line with `if` ends with a colon `:`.

An `if` also works directly with an Air element:

```python
has_key = True
if has_key:
    print("The door opens!")
```

And with text – compare it with `==`:

```python
spell = "Fireball"
if spell == "Fireball":
    print("You cast a Fireball!")
```
