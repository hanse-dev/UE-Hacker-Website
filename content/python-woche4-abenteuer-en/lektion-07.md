# 🌀 Spell Formula 3: Nested Loops

On the top floor of the tower waits the **Double Spiral of Power**. A loop can contain another loop – this is called **nesting**. The **inner** loop runs through completely on **every single** run of the outer loop.

```python
for outer in range(3):
    for inner in range(2):
        print(f"outer {outer}, inner {inner}")
```

This `print` code runs **3 × 2 = 6 times**.

**Important:** Every additional level of nesting needs another **indentation**!

```python
for tower in range(1, 4):
    print(f"Tower {tower}:")
    for floor in range(1, 3):
        print(f"  Floor {floor} is being searched...")
```
