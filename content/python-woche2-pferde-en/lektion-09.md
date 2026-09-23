# 🎤 Lesson 9: Processing Input

You know `input()` from Week 1: the **function** hands you back the user's answer – **always as text (`str`)**, even if they type a number! To calculate with it, you have to convert it:

```python
answer = input("How many kg of hay? ")   # text, e.g. "15"
number = int(answer)                     # now a number: 15
print(f"{number} kg of hay will last {number * 2} days.")
```

> 💡 In the input box, type only a **whole number** – otherwise `int()` can't convert it.
