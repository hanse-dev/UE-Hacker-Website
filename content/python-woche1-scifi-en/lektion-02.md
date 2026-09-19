# 💾 System Protocol 2: Data Storage

A variable is like a **labelled data storage unit**: you give it a name and can store something inside – and retrieve it again later.

```python
ship_name = "Enterprise"   # the storage is called 'ship_name', inside is the text "Enterprise"
crew = 150                 # the storage is called 'crew', inside is the number 150
```

**The two most common types of values:**

| Type | Technical term | Example | How to recognise |
|------|---------------|---------|------------------|
| Text | **String** | `"Enterprise"` | Quotation marks |
| Whole number | **Integer** | `150` | No quotation marks |

Variables can **change**: if you write a new value into the storage, the old one is overwritten.

```python
energy = 80
energy = 45    # after the jump
print(energy)
```
