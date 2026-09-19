## 🌀 Lesson 7: The Training-Plan Circuit

A loop can **contain** another loop. The inner loop then runs all the way through on **every** pass of the outer one:

```python
for week in range(1, 4):
    print(f"Training week {week}:")
    for session in range(1, 3):
        print(f"  Session {session} is being completed...")
```

3 weeks × 2 sessions = 6 session messages.

This is how patterns of hoof prints are made:

```python
for row in range(3):
    for col in range(4):
        print("🐴", end=" ")
    print()
```

- `end=" "` adds a space instead of a line break.
- `end=""` adds nothing at all, so the next `print` continues right on the same line.
- The empty `print()` at the end of each row makes the line break.

> 🐴 **Important:** Every additional level of nesting needs **another indent**!
