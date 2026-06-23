# Curriculum – Python 12-Week Beginner Course

Overview of all concepts per week. Each week has three parallel courses with identical learning content but different theme settings (Adventure / Horses / SciFi).

---

## Week 1 – Basics

**New concepts:**
- `print()` – output text on the screen
- Variables – store values under a name
- Data types (overview): `String`, `Integer`, `Boolean`
- String concatenation with `+`
- `str()` – convert a number to text
- Comments with `#`
- `input()` – first input from the user

**Learning goals:** Write simple interactive programs, create and output variables, find and fix first errors.

---

## Week 2 – Data Types & Strings

**New concepts:**
- f-Strings – modern text formatting (`f"Hello {name}"`)
- f-Strings vs. `+` concatenation – when to use which
- `Float` – decimal numbers
- `type()` – check the data type of a variable
- `len()` – determine the length of a text
- Type conversions: `int()`, `float()`, `str()`, `bool()`
- String methods: `.upper()`, `.lower()`, `.strip()`, `.split()`, `.replace()`
- Deepening `input()` – convert inputs to other types (`int(input(...))`)

**Deepening:** Variables (from Week 1), String and Integer

**Learning goals:** Know and convert all four basic types, edit text, write programs with user input.

---

## Week 3 – Conditions

**New concepts:**
- `if`, `elif`, `else` – make decisions
- Comparison operators: `==`, `!=`, `<`, `>`, `<=`, `>=`
- Logical operators: `and`, `or`, `not`

**Deepening:** Variables, data types, f-Strings, `input()`

**Learning goals:** Write programs with branching, validate user input.

---

## Week 4 – Loops & List Basics

**New concepts:**

- `for` loop – iterate over a collection (`for item in list`)
- `range()` – generate a number sequence (`for i in range(10)`)
- `while` loop – repeat as long as a condition holds
- Lists `[]` – basics: create, add elements (`append()`), access by index

**Deepening:** Conditions, variables

> 💡 Lists are introduced here only as a foundation for meaningful `for` loops.
> All list methods come in Week 6.

**Learning goals:** Automate repetitive tasks, write `for` loops over real collections.

---

## Week 5 – Functions

**New concepts:**
- `def` – define a function
- Parameters & arguments
- `return` – return a result
- Docstrings – document functions
- Naming conventions (`snake_case`)
- `try` / `except` – catch errors (basics)

**Deepening:** `len()`, `type()` (from Week 2) in function context, lists from Week 4

**Learning goals:** Write reusable code, split programs into sub-tasks, basic error handling.

---

## Week 6 – Lists (complete)

**New concepts:**

- List methods: `insert()`, `remove()`, `pop()`, `index()`, `count()`
- `in` – check if element is in list
- `sort()`, `sorted()`, `reverse()`
- `enumerate()` – index and value simultaneously in a loop
- `break` – exit loop early
- `continue` – skip current round
- `set` – remove duplicates (short introduction)

**Deepening:** List basics (Week 4), loops, functions

> 💡 **OOP foreshadowing:** Methods like `.append()` or `.sort()` are a first example
> of OOP – the list is an object, and these methods belong to it. In Week 10 we build
> our own objects with our own methods.

**Learning goals:** Fully manage collections, search and sort lists, fine-control loops.

---

## Week 7 – Modules & Libraries

**New concepts:**
- `import` – load modules
- `from … import …` and `import … as …`
- `math` – mathematical functions (`sqrt`, `floor`, `ceil`, `pi`)
- `random` – random numbers (`randint`, `choice`, `shuffle`)

**Deepening:** Functions, lists, data types

> 💡 JSON is deliberately left out here – it is introduced in Week 9 together with
> file I/O, where it fits more naturally.

**Learning goals:** Use existing libraries, add random elements.

---

## Week 8 – Dictionaries & Tuples

**New concepts:**
- Dictionaries `{}` – key-value pairs
- Access with `[]` and `.get()`
- Add, change, delete entries (`.pop()`, `.update()`)
- Iteration: `.keys()`, `.values()`, `.items()`
- Tuples `()` – immutable ordered collection
- Tuple unpacking

**Deepening:** Lists, loops, functions

> 💡 **OOP foreshadowing:** A dictionary with fixed fields (`{"name": "Aria", "level": 5}`)
> is the precursor of a class. In Week 10 we replace such dictionaries with real objects.

**Learning goals:** Manage structured data with named fields.

---

## Week 9 – Files & I/O

**New concepts:**
- `open()` and `with` – open and close files
- Reading and writing text files
- `json` – read (`json.load`) and write (`json.dump`) JSON files
- Read (`csv.reader`) and write (`csv.writer`) CSV files
- `try` / `except` for file errors (`FileNotFoundError`)

**Deepening:** Dictionaries, lists, try/except (from Week 5)

**Learning goals:** Save and load data permanently.

---

## Week 10 – OOP Basics

**New concepts:**
- `class` – define your own class
- `__init__` – constructor / initialisation
- `self` – reference to the own instance
- Attributes – properties of an object
- Methods – functions of an object
- Creating instances

**Deepening:** Functions, dictionaries

> 💡 Building a bridge: *"Remember the hero dictionary from Week 8?
> Now we turn it into a proper hero class."*

**Learning goals:** Model your own data structures with behaviour.

---

## Week 11 – Advanced OOP

**New concepts:**
- Inheritance – derive a class from another
- `super()` – access the parent class
- Polymorphism – same method, different behaviour
- Magic Methods: `__str__`, `__repr__`, `__add__`, `__len__`, `__eq__`

**Deepening:** OOP Basics (Week 10)

**Learning goals:** Build class hierarchies, compare and output objects.

---

## Week 12 – Graphics with Turtle

**New concepts:**
- `turtle` module – graphical output
- Basic commands: `forward()`, `backward()`, `left()`, `right()`
- `color()`, `fillcolor()`, `begin_fill()`, `end_fill()`
- `circle()`, `speed()`
- Loops for patterns and animations

**Deepening:** Loops, functions, OOP (Turtle as an object)

> 💡 **OOP connection:** The `turtle` object is itself a class – `t = turtle.Turtle()`
> creates an instance. Week 12 thus rounds off the OOP knowledge from Weeks 10–11.
> **Note:** Turtle requires a local Python installation with `tkinter` –
> may not work in pure browser environments (JupyterHub etc.).

**Learning goals:** Write graphical programs with Turtle, experience OOP in practice.

---

## Not in the Course (deliberate omissions)

The following topics are too advanced for a beginner course and are not taught:

- List Comprehensions
- Decorators / `@property`
- Abstract classes (`abc.ABC`, `@abstractmethod`)
- Generators and iterators
- Type Hints (`typing`)
- `os`, `shutil`, `pathlib`
- Regular expressions
- Virtual environments / Package Management
- Testing frameworks
