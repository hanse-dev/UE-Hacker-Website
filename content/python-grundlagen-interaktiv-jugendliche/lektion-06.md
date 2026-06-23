# Schleifen mit for

`for` iteriert über eine Sequenz. `range(start, stop, step)` erzeugt Zahlenfolgen.

```python
for i in range(0, 10, 2):
    print(i)  # 0, 2, 4, 6, 8
```

Du kannst auch direkt über Listen oder Strings iterieren:

```python
playlist = ["Song A", "Song B", "Song C"]
for song in playlist:
    print(f"▶ {song}")
```
