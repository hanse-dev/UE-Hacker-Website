# Loops with for

`for` iterates over a sequence. `range(start, stop, step)` generates number sequences.

```python
for i in range(0, 10, 2):
    print(i)  # 0, 2, 4, 6, 8
```

You can also iterate directly over lists or strings:

```python
playlist = ["Song A", "Song B", "Song C"]
for song in playlist:
    print(f"▶ {song}")
```
