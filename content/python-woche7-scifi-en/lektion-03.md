# 🃏 Module Log 3: Choosing and shuffling at random

With lists from week 6, `random` can do even more:

```python
import random

modules = ["Navigation", "Communication", "Drive", "Life support", "Sensors"]
one = random.choice(modules)          # one random entry
three = random.sample(modules, 3)     # 3 different entries (no repeats)
mix = modules.copy()
random.shuffle(mix)                    # shuffles the list itself (returns nothing!)
```

- **`random.choice(list)`** – one entry
- **`random.sample(list, k)`** – `k` **different** entries
- **`random.shuffle(list)`** – **changes** the list itself; if you want to keep the original, shuffle a copy first (`list.copy()`)

> ⚠️ Do not write `list = random.shuffle(list)` – `shuffle` returns nothing, so `list` would be `None` afterwards.
