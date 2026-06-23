# f-Strings

f-Strings are the most modern way to embed variables in strings (since Python 3.6). Easier to read than concatenation with `+`.

```python
name = "Alex"
followers = 1200
print(f"{name} has {followers} followers.")
```

You can also put expressions inside `{}`:

```python
price = 29.99
print(f"Price with tax: {price * 1.19:.2f} €")
```
