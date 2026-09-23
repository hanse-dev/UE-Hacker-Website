# 🐴 Stage 6: Catching Wrong Input

*Knowledge from week 8: try/except*

Players sometimes type nonsense. A command like `go north` consists of two words that `split()` splits into `action` and `target`. With `hello` the count does not fit and Python raises a `ValueError`. `try/except` catches it:

```python
def execute(player, text):
    try:
        action, target = text.split()
    except ValueError:
        print("🤔 I only understand commands of two words, e.g. 'go north' or 'take Flashlight'.")
        return
    if action == "go":
        player.go(target)
        check_enemy(player)
    elif action == "take":
        player.take(target)
    else:
        print(f"🤔 '{action}' I don't know that. Try 'go' or 'take'.")
```

That keeps the game stable.
