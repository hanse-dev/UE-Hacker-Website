# 📟 System Log 4: The Letters of a Code

A for loop can also run through a **string** – letter by letter:

```python
code = "ALPHA"
for letter in code:
    print(f"  - {letter}")
```

The string is treated as a sequence of letters. On every pass `letter` holds the next letter.

You can also **count** while looping: create a variable before the loop and increase it inside:

```python
count = 0
for letter in "NEXUS":
    count += 1
print(count)   # 5
```
