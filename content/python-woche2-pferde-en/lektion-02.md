# 🐴 Lesson 2: Walk and Trot – `str` and `int`

Every piece of information at the riding ranch has a **type** – just like a horse shows one of four gaits. You recognise a gait by its rhythm, and you recognise the type of a value with the function **`type()`**.

| Hoofbeat type | Gait | Technical term | Example | Why the gait fits |
|---------------|------|----------------|---------|-------------------|
| 🚶 Walk | calm, steady | `str` (text) | `"Thunder"` | Walk is the gait for talking and communicating |
| 🐎 Trot | firmly timed, countable | `int` (whole number) | `7` | Trot has a clear, countable two-beat rhythm |
| 🏇 Canter | flowing, never quite the same | `float` (decimal number) | `4.25` | Canter is a flowing three-beat |
| 🦘 Jump | cleared or not | `bool` (truth value) | `True` / `False` | A jump is either cleared or knocked down |

In this lesson you meet the first two:

- 🚶 **`str`** – text in quotation marks: `"Windstorm"`
- 🐎 **`int`** – whole numbers without quotation marks: `168`

```python
print(type("Windstorm"))   # <class 'str'>
print(type(168))           # <class 'int'>
```

> 🐴 **Remember:** `type()` is a function like `print()` – you hand it a value in the parentheses and it tells you the hoofbeat type. Use `print(type(...))` to see the answer.
