"""# 📖 Glossary – ⚔️ Week 8 – Dictionaries and Tuples: Profiles and Artifacts
> You can keep this notebook open all week.

| Term | Meaning | Example |
|------|---------|-------|
| **Dictionary** `{}` | Collection of key-value pairs | `{\"name\": \"Aria\", \"level\": 5}` |
| **Key** | Name of an entry in the dictionary | `hero[\"name\"]` |
| **Value** | Content of an entry | `hero[\"level\"]` → `5` |
| `.get()` | Safe access – no error if key is missing | `hero.get(\"xp\", 0)` |
| `.pop()` | Delete an entry and return its value | `hero.pop(\"level\")` |
| `.keys()` | All keys as a list | `hero.keys()` |
| `.values()` | All values as a list | `hero.values()` |
| `.items()` | All key-value pairs – useful for loops | `for k, v in hero.items():` |
| **Tuple** `()` | Immutable ordered collection | `point = (3, 5)` |
| **Tuple Unpacking** | Split tuple values directly into variables | `x, y = (3, 5)` |
| `try` / `except` | Catch errors, e.g. when trying to change a tuple | `try: ... except TypeError:` |
| **List Comprehension** | Short syntax to build a new list from an existing one | `[x for x in list_ if x > 5]` |"""
