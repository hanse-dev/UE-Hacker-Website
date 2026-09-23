# 🚀 Data Log 3: Safe access with get() and in

If a key is missing, `dict[key]` raises a **KeyError**. Two safe ways:

```python
print(member.get("name"))         # Nova
print(member.get("shield"))       # None – no error
print(member.get("shield", 0))    # 0 – your own default value

print("name" in member)           # True – checks the KEYS
print("shield" in member)         # False
```

**`in`** always checks the **keys** of a dictionary, never the values.
