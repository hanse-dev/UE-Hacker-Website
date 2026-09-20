# 🧮 Lesson 6: math and calculation operators

The **`math`** module has number tools:

```python
import math

print(math.pi)          # 3.141592653589793
print(math.sqrt(16))    # square root: 4.0
print(math.ceil(3.2))   # round up: 4
print(math.floor(3.8))  # round down: 3
print(round(3.14159, 2))  # round to 2 places: 3.14
print(abs(-5.5))        # absolute value: 5.5
```

Plus three **operators** that need no module:

```python
print(2 ** 3)    # power: 8
print(17 // 5)   # whole-number division: 3
print(17 % 5)    # remainder (modulo): 2
```

**`%`** is especially useful: `number % 2 == 0` means "`number` is **even**", and `number % 5 == 0` means "divisible by 5".
