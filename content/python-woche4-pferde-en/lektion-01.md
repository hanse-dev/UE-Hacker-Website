# 🐴 Week 4: The Rhythm of Riding

Welcome to the **Endurance Training Ground**! Here movements repeat, and rhythm leads to perfection. This week you will learn how Python repeats code **automatically** – with **loops**:

1. 🔁 The **for loop** with `range()`
2. 🎯 `range()` with a start and an end
3. 🏇 Step size and counting backwards
4. 🔤 Loops over **text**
5. ⏳ The **while loop**
6. 💪 while with conditions
7. 🌀 **Nested** loops

## 🔁 Lesson 1: Loop – The Dressage Circle

A **for loop** repeats code for every item in a sequence.

```python
for i in range(5):
    print(f"Lap {i+1}: The horse trots elegantly")
```

1. **`for`** starts the repetition.
2. **`i`** is a placeholder that holds the current number on each pass.
3. **`in range(5)`** produces the numbers 0, 1, 2, 3, 4 – that is **5** passes.
4. The **colon `:`** ends the first line.
5. Everything **indented** below it is run on every pass.

> 🐴 **Important:** `range(5)` starts at **0** and stops **before** 5. That is why we write `i+1` to count from 1 to 5.
