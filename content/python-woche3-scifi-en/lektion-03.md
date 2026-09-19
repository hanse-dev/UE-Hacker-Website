# 📟 System Protocol 3: if-else

`if-else` offers **two paths**: one for "condition true" and one for "condition false".

```python
signals = 18
if signals >= 15:
    print("Life forms detected!")
else:
    print("Sector empty.")
```

- `else` needs **no condition** – it applies to everything that does not match the `if`.
- `else` also gets a **colon** and an **indented** block.
- **Exactly one** of the two paths is always executed.

Handy when you need a calculation in the message:

```python
energy = 45
consumption = 50
if energy >= consumption:
    print(f"Jump possible! Remaining: {energy - consumption}%")
else:
    print(f"Jump impossible! Missing: {consumption - energy}%")
```
