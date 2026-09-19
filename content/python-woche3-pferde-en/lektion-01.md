# 🐴 Week 3 – Lesson 1: if

Welcome to the **Crossroads of the Pasture**! Every good rider has to make decisions: is the horse ready for training? Is the saddle on? This week your programs learn to decide, too.

## 🐎 The `if` condition

`if` checks a condition and only runs the code below it when the condition is **true**:

```python
horse_age = 5
if horse_age >= 5:
    print("The horse is ready for training!")
```

> 🐴 **Important:** the line with `if` ends with a **colon `:`** and the code that belongs to it must be **indented** (four spaces)!

The condition can also be a Boolean variable that is already `True` or `False`:

```python
has_saddle = True
if has_saddle:
    print("You can mount up!")
```

If the condition is false, Python simply skips the indented block.
