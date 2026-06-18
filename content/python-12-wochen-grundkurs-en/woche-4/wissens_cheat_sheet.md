# Knowledge Cheat Sheet: Week 4

_Summary of all topics from Weeks 1–3_

## Week 1: Introduction and your first program

### print()
Outputs text on the screen. Text goes in quotes.

```python
print("Hello World!")
```

### Variables
Store information for later use. A name is assigned a value.

```python
name = "Python"
count = 3
```

### Combining strings with + and str()
Connect text with `+`. Convert numbers with `str()` to include them in text.

```python
print("My name is " + name)
print("Count: " + str(count))
```

### Comments
Lines starting with `#` are ignored – for explanations in the code.

```python
# This is a comment
x = 5  # x has the value 5
```

---

## Week 2: Data types and variables

### f-Strings
Modern text formatting: insert variables in curly braces.

```python
print(f"Name: {name}, Count: {count}")
```

### The four data types
- **String** (str): Text in quotes
- **Integer** (int): Whole numbers
- **Float** (float): Decimal numbers
- **Boolean** (bool): `True` or `False`

```python
text = "Hello"
number = 42
decimal = 3.14
is_true = True
```

### Operations
Maths with numbers, string concatenation with `+`, repetition with `*`.

```python
result = 10 + 5
long_text = "A" * 3  # "AAA"
```

### Type conversions
`int()`, `float()`, `str()` convert between data types.

```python
x = int("42")
text = str(3.14)
```

---

## Week 3: Conditions (if-else)

### if, if-else, if-elif-else
Decisions: only certain code runs when the condition is met.

```python
if age >= 18:
    print("Adult")
elif age >= 16:
    print("Almost an adult")
else:
    print("Minor")
```

### Comparison operators
`==` (equal), `!=` (not equal), `<`, `>`, `<=`, `>=`

```python
x == 5
name != ""
```

### Logical operators
`and` (both true), `or` (at least one true), `not` (negate)

```python
if age >= 18 and valid:
    print("OK")
```

### Nested conditions
if-blocks inside if-blocks – indentation with 4 spaces is essential.
