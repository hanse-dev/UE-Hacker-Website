"""## 🛡️ Stage 5: Catching wrong input

*Knowledge from Week 8: try/except*

Players sometimes type nonsense. The command `go north` consists of two words, which `split()` (Week 2) splits into `action` and `target`. With `hello` or `go to north` the number does not fit, and Python raises a `ValueError`.

Instead of crashing, `try/except` catches the error and shows a friendly message. That keeps the game stable!"""