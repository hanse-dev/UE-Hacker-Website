# Schleifen mit for

`for` iteriert über eine Sequenz. `range(start, stop, step)` erzeugt Zahlenfolgen.

```python
for i in range(0, 10, 2):
    print(i)  # 0, 2, 4, 6, 8
```

`range()` schließt den `stop`-Wert dabei **nicht** mit ein – `range(0, 10, 2)` endet also bei 8, nicht bei 10. Lässt du `step` weg, wird automatisch 1 verwendet (`range(0, 5)` → 0, 1, 2, 3, 4); lässt du auch `start` weg, beginnt die Zählung bei 0 (`range(5)` entspricht `range(0, 5)`).

Du kannst auch direkt über Listen oder Strings iterieren, ohne den Umweg über `range()` und Indizes zu gehen:

```python
playlist = ["Song A", "Song B", "Song C"]
for song in playlist:
    print(f"▶ {song}")
```

Das ist in der Praxis der häufigere Fall: statt "gib mir die Zahlen von 0 bis Listenlänge und greife jeweils auf `playlist[i]` zu" schreibst du direkt "gib mir jedes Element". Brauchst du zusätzlich den Index, gibt es `enumerate()`:

```python
for index, song in enumerate(playlist):
    print(f"{index + 1}. {song}")
```
