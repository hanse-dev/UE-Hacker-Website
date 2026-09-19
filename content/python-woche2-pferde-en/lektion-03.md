# 🐴 Lesson 3: Canter and Jump – `float` and `bool`

Two more hoofbeat types are waiting for you:

- 🏇 **`float`** – decimal numbers with a **dot** (not a comma!): `550.5`, `4.25`. A canter is flowing and never quite exact – and so are decimal numbers.
- 🦘 **`bool`** – a truth value with only two states: `True` or `False`. A jump is either cleared or knocked down. Write them with a capital first letter and **without** quotation marks!

```python
weight = 550.5          # float
has_saddle = True       # bool
print(type(weight))     # <class 'float'>
print(type(has_saddle)) # <class 'bool'>
```

## 🔍 Comparisons give a bool

When you compare two values, Python answers with `True` or `False`:

```python
print(5 > 3)    # True
print(2 > 9)    # False
```

`>` means "greater than", `<` means "less than". You will use this a lot from Week 3 on!

> 🐴 **Careful:** `7` is an `int`, but `7.0` is a `float` – the dot decides! And `"7"` in quotation marks is a `str`.
