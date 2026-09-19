# 📟 System Protocol 5: Logical Operators

With **`and`**, **`or`** and **`not`** you combine several conditions:

| Operator | Meaning | True when … |
|---|---|---|
| `and` | and | **both** conditions are true |
| `or` | or | **at least one** condition is true |
| `not` | not | the condition is **false** (flips it) |

```python
has_access_code = True
has_fingerprint = True
if has_access_code and has_fingerprint:
    print("Access to the command deck granted!")
```

```python
has_emergency_key = False
has_override_code = True
if has_emergency_key or has_override_code:
    print("You can open the door manually!")
```

```python
alarm_active = False
if not alarm_active:
    print("No danger – all systems secure!")
```

You can also combine comparisons, for example `if shield > 10 and weapons > 10:`.

> 📡 **Remember:** `and` is strict (everything must be true), `or` is generous (one is enough), `not` flips.
