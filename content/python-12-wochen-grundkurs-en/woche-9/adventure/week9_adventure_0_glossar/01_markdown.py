"""# 📖 Glossary – ⚔️ Week 9 – JSON Files and I/O: The Scrolls of Data
> You can keep this notebook open all week.

| Term | Meaning | Example |
|------|---------|--------|
| `open()` | Open a file | `open(\"file.txt\", \"r\")` |
| `with` | Safely open and automatically close a file | `with open(\"file.txt\") as f:` |
| `\"r\"` / `\"w\"` / `\"a\"` | Read / Write / Append mode | `open(\"f.txt\", \"w\")` |
| `.read()` | Read entire file content as text | `content = f.read()` |
| `.readlines()` | Read all lines as a list | `lines = f.readlines()` |
| `.write()` | Write text to a file | `f.write(\"Hello\")` |
| `json` | Module for JSON data (structured text) | `import json` |
| `json.load()` | Read JSON file → Python dictionary | `data = json.load(f)` |
| `json.dump()` | Save Python dictionary as JSON | `json.dump(data, f)` |
| `csv.reader` | Read a CSV file line by line | `reader = csv.reader(f)` |
| `csv.writer` | Save data as a CSV file | `writer = csv.writer(f)` |
| `FileNotFoundError` | Error when a file cannot be found | `except FileNotFoundError:` |"""
