# 📟 System Protocol 9: Processing Input

You know `input()` from Week 1: the **function** hands you back the crew's answer – **always as text (`str`)**, even if a number is typed! To calculate with it, you have to convert it:

```python
answer = input("Energy level? ")     # text, e.g. "70"
energy = int(answer)                 # now a number: 70
print(f"After charging: {energy + 10}%")
```

For decimal numbers use `float()` instead of `int()`.

> 💡 In the input box, type only a **whole number** – otherwise `int()` can't convert it.
