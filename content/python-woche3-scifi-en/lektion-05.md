# 📟 System Protocol 4: Logical Operators

With `and`, `or` and `not` you combine several conditions:

| Operator | Meaning | True when … |
|---|---|---|
| `and` | both | **both** conditions are true |
| `or` | either | **at least one** condition is true |
| `not` | flips | the condition is **false** |

```python
has_access_code = True
has_fingerprint = True
if has_access_code and has_fingerprint:
    print("Access to the command deck granted!")
```
