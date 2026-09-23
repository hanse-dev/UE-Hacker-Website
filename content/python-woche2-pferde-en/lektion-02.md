# 🚶 Lesson 2: Walk – Text

Every piece of information at the stables has a **type** – just like a horse shows one of four gaits. The four gait types:

| Gait type | Movement | Technical term | Example |
|-----------|----------|-----------------|---------|
| 🚶 Walk | calm, steady | `str` (text) | `"Thunder"` |
| 🐎 Trot | firmly timed, countable | `int` (whole number) | `7` |
| 🏇 Canter | flowing, never quite the same | `float` (decimal number) | `4.25` |
| 🦘 Jump | done or not | `bool` (truth value) | `True` / `False` |

You recognise the type with the **function `type()`**. Give it a value in the parentheses, and it tells you the type:

```python
horse_name = "Windstorm"
print(type(horse_name))   # <class 'str'>
```

## 🚶 Walk: `str`

A **string** is text – anything in quotation marks. Walk is the gait for talking and communicating.

> ⚠️ Even `"7"` is text, because it sits in quotation marks – even though it holds a digit!
