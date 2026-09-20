# 🎲 Module Log 2: Random numbers

The **`random`** module delivers chance – for dice, games of luck and surprises:

```python
import random

roll = random.randint(1, 6)         # whole number from 1 to 6 (both included)
decimal = random.uniform(10, 20)    # decimal between 10 and 20
number = random.random()            # decimal between 0 and 1
```

**Repeatable chance:** With `random.seed(number)` you start the chance at a fixed spot. With the same seed you always get the **same** numbers – handy for testing.

> 💡 Because chance is different on every run, the tasks check **properties** (is the roll between 1 and 6?) instead of fixed values.
