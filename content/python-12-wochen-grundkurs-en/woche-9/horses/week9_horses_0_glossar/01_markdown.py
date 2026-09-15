"""# 📖 Glossary – 🐴 Week 9 – JSON Files and I/O: The Stable Archives of the Riding Ranch
> You can keep this notebook open all week.

| Term | Meaning | Example |
|------|---------|--------|
| `open()` | Open a file | `open(\"file.txt\", \"r\")` |
| `with` | Safely open a file and close it automatically | `with open(\"file.txt\") as f:` |
| `\"r\"` / `\"w\"` / `\"a\"` | Read / Write / Append mode | `open(\"f.txt\", \"w\")` |
| `.read()` | Read the entire file content as text | `content = f.read()` |
| `.readlines()` | Read all lines as a list | `lines = f.readlines()` |
| `.write()` | Write text to a file | `f.write(\"Hello\")` |
| `json` | Module for JSON data (structured text) | `import json` |
| `json.load()` | Read a JSON file → Python dictionary | `data = json.load(f)` |
| `json.dump()` | Save a Python dictionary as JSON | `json.dump(data, f)` |
| `csv.reader` | Read a CSV file line by line | `reader = csv.reader(f)` |
| `csv.writer` | Save data as a CSV file | `writer = csv.writer(f)` |
| `FileNotFoundError` | Error when a file is not found | `except FileNotFoundError:` |"""
