# 🐴 Lesson 4: Calculating with Numbers

With `int` and `float` you can calculate just like with a calculator:

| Sign | Meaning | Example | Result |
|------|---------|---------|--------|
| `+` | add | `12 + 8` | `20` |
| `-` | subtract | `12 - 8` | `4` |
| `*` | multiply | `12 * 2` | `24` |
| `/` | divide | `12 / 4` | `3.0` |

**Watch out:** the division `/` **always** gives a `float`, even if it comes out evenly: `12 / 4` is `3.0`, not `3`.

```python
horses_a = 12
horses_b = 8
print(f"Total horses: {horses_a + horses_b}")
```

You can put calculations right inside the braces of an f-string – or store the result in a new variable first.
