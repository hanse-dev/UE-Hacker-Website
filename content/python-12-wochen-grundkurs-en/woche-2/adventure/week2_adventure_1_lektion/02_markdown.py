"""## 🗣️ Chapter 1: The Common Tongue – f-strings

Before you combine elements, you need a language to talk about them. An **f-string** is the **more modern and readable** way to embed variables in text. The `f` before the quotation marks tells Python: *\"Look inside the curly braces!\"*

**f-string vs. `+` concatenation – which should I use?**

| Method | Example | Recommendation |
|--------|---------|-----------------|
| `+` concatenation | `\"Hello \" + name` | works, needs `str()` for numbers |
| f-string | `f\"Hello {name}\"` | more modern, shorter, numbers work directly |

> ✅ Use f-strings – they're clearer to read and less error-prone.
> The `+` method from Week 1 still works, though."""
