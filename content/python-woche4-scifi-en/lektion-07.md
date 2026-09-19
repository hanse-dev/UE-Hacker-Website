# 📟 System Log 7: Nested Loops – The Time-Within-Time Cycle

A loop can contain **another loop** – this is called nesting. The inner loop runs completely through on **every single pass** of the outer loop.

```python
for deck in range(1, 4):
    print(f"Deck {deck}:")
    for room in range(1, 3):
        print(f"  Room {room} is being scanned...")
```

Here the inner code runs 3 × 2 = 6 times. Every additional nesting level needs **one more level of indentation**.

A nice trick for patterns: `print("✨", end="")` prints without a line break (`end=" "` adds a space instead) – and an empty `print()` at the end of each row starts a new line.
