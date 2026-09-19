# ⚗️ Fusing Elements

**What it is:** how you combine and change elements of the same nature.

## 🪨 Fusing Earth (numbers)

```python
gold_a = 150
gold_b = 75
print(f"Total gold: {gold_a + gold_b}")
print(f"Difference: {gold_a - gold_b}")
print(f"Double gold: {gold_a * 2}")
print(f"Divided: {gold_a / 3}")
```

## 🔥 Fusing Fire (texts)

Texts can be joined with `+` and repeated with `*`:

```python
first_name = "Luna"
last_name = "Silvermoon"
full_name = first_name + " " + last_name
print(full_name)            # Luna Silvermoon
print(first_name * 3)       # LunaLunaLuna
```

> ⚠️ Fire and Earth resist direct fusion: `"Level: " + 5` causes a `TypeError`. You need a **conversion** – that is the next chapter!
