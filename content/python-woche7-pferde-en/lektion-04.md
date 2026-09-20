# 🔤 Lesson 4: The string module

The **`string`** module provides ready-made **character collections**:

```python
import string

print(string.ascii_letters)   # all letters a–z and A–Z (52)
print(string.ascii_uppercase) # capital letters only
print(string.digits)          # 0123456789
```

Together with `random.choice()` you forge a **key** (password) from them:

```python
import random, string

alphabet = string.ascii_letters + string.digits          # 62 characters
key = "".join([random.choice(alphabet) for _ in range(8)])
```

- **`"".join(list)`** glues the entries of a list into **one text** (between the quotes goes whatever should stand between the parts – here nothing)
- The list comprehension `[... for _ in range(8)]` repeats `random.choice` **8 times**
