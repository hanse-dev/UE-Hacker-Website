# 💀 The Game Loop

Almost every game uses a `while` loop: it keeps going **as long as** the hero still has health.

```python
health = 100
round_number = 1

while health > 0:
    damage = 20
    health -= damage
    print(f"Round {round_number}: -{damage} health, left: {health}")
    round_number += 1
```

The condition `health > 0` eventually becomes false through `health -= damage` – so the loop ends by itself.

You can also join conditions with `and`, for example `while health > 0 and mana > 0:` – then the loop only continues if **both** are still true.
