# Knowledge Cheat Sheet: Week 7

_Summary of all topics from Weeks 1–6_

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

### Logical operators
`and` (both true), `or` (at least one true), `not` (negate)

### Nested conditions
if-blocks inside if-blocks – indentation with 4 spaces is essential.

---

## Week 4: Loops (for, while)

### for with range()
Repeats code a fixed number of times – `range(n)` gives 0 to n-1.

```python
for i in range(5):
    print(i)  # 0, 1, 2, 3, 4
```

### while loop
Runs as long as the condition is true.

```python
while counter < 10:
    counter += 1
```

### Loops over sequences
Iterate over strings or lists – go through each element.

```python
for char in "Hello":
    print(char)
```

### break and continue
`break` ends the loop immediately. `continue` skips the rest.

### Nested loops
A loop inside a loop – e.g. for patterns or tables.

---

## Week 5: Functions

### Calling functions
A function must be called with parentheses to run it.
- **With parentheses `function()`:** Runs the function – the code is executed
- **Without parentheses `function`:** Just a reference to the function object – does NOT run it (useful e.g. for passing as a parameter)

```python
def greet():
    print("Hello!")
greet()   # Is executed
greet     # Is NOT executed – just a reference
```

### def and parameters
Reuse code blocks. Parameters are placeholders for values when called.

```python
def greet_name(name):
    print(f"Hello, {name}!")
greet_name("Anna")
```

### return
Returns a value – the function becomes that value.

```python
def double(x):
    return x * 2
result = double(5)
```

### Docstrings
Explain the function in triple quotes directly under `def`.

```python
def add(a, b):
    """Adds two numbers."""
    return a + b
```

### Default values
Parameters can have a default value.

```python
def say(text, end="."):
    print(text + end)
say("Hello")  # end is "."
```

---

## Week 6: Lists

### Creating lists
Multiple values in an ordered collection. Square brackets `[]`.

```python
animals = ["Dog", "Cat", "Mouse"]
```

### append() and insert()
Add new elements – at the end or at a position.

```python
animals.append("Bird")
animals.insert(1, "Fish")
```

### remove() and pop()
Remove elements – `remove()` by value, `pop()` by index (returns the value).

```python
animals.remove("Cat")
last = animals.pop()
```

### index() and in
Find position or check if an element is present.

```python
pos = animals.index("Mouse")
if "Dog" in animals:
    print("found")
```

### sort() and sorted()
`sort()` changes the list in place. `sorted()` creates a new sorted list.

```python
animals.sort()
new_list = sorted(animals)
```
