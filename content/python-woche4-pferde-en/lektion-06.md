## 💪 Lesson 6: Training until exhaustion

The condition of a while loop can contain any comparison. The loop then runs until a value changes:

```python
stamina = 100
lap = 1

while stamina > 20:
    stamina -= 15
    print(f"Lap {lap}: {stamina}% left")
    lap += 1

print(f"Training finished after {lap-1} laps!")
```

On every pass the stamina drops by 15. As soon as it is **no longer above 20**, the loop ends.

> 🐴 **Remember:** The variable in the condition (`stamina`) has to **change inside the loop body** – otherwise you get an endless loop.
