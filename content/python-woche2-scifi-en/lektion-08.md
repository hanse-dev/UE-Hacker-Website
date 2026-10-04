# 📟 System Protocol 7: Calculating with Text

**With text** two operations work:

- `+` **joins** texts: `"Neo" + "tron"` → `"Neotron"`
- `*` **repeats** text: `"Ping" * 3` → `"PingPingPing"`

```python
prefix = "Neo"
suffix = "tron"
system_name = prefix + suffix
print(system_name)      # Neotron
```

> ⚠️ Not everything can be combined: `"Crew: " + 5` causes an error – text and number don't mix. More on that in the next protocol!
