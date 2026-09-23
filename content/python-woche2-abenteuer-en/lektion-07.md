# ⚗️ Fusing Elements

How you combine elements depends on their type.

## 🪨 Earth and 💧 Water: calculating

```python
gold_a = 150
gold_b = 75
print(gold_a + gold_b)    # 225
print(gold_a - gold_b)    # 75
print(gold_a * 2)         # 300
print(gold_a / 3)         # 50.0  (dividing always gives a decimal number!)
```

## 🔥 Fire: gluing and repeating

```python
first_name = "Luna"
last_name = "Silvermoon"
print(first_name + " " + last_name)    # Luna Silvermoon
print(first_name * 3)                  # LunaLunaLuna
```

## Not everything fuses

🔥 Fire (text) and 🪨 Earth (number) resist a direct fusion with `+`: `"Level: " + 5` is an error. For that you need a conversion – that's coming in the next lesson.
