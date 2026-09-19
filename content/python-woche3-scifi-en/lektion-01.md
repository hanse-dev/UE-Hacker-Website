# 🚀 Week 3 – The Paths of Decision

Welcome back, Commander! You are reaching the **Crossroads of the Universe** – a place where every decision shapes the future of the galaxy. This week you will learn:

1. **if** – run code only when something is true
2. **Comparison operators** like `==`, `!=`, `<`, `>`, `<=`, `>=`
3. **if-else** – two paths
4. **if-elif-else** – many paths
5. **and, or, not** – combine conditions
6. **Nested conditions** – a decision inside a decision

## 📟 System Protocol 1: if

`if` checks a condition and runs code **only if the condition is true** (that is, evaluates to `True`).

```python
security_level = 5
if security_level == 5:
    print("Access to main system granted!")
```

Watch out for two things:

- The condition is followed by a **colon `:`**
- The code that belongs to it is **indented** (4 spaces or the Tab key). The indentation shows Python what belongs to the `if`.

You can also use a Boolean variable (from Week 2) directly as a condition:

```python
system_online = True
if system_online:
    print("All systems operational.")
```

If the condition is not true, Python simply skips the indented block.

> 📡 **Remember:** A colon after the condition and an indented block – without both, nothing runs!
