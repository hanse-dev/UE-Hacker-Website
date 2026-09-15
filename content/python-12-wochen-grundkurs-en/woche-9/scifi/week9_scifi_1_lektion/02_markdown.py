"""## 📚 Data Stream 1: File Access – The Digital Gateway

**What it is:** File access lets you save and load data on disk.

**How file access works:**
```python
# Open a file and write
with open('file.txt', 'w') as f:
    f.write('Hello World')

# Open a file and read
with open('file.txt', 'r') as f:
    content = f.read()
```

**Step-by-step explanation:**
1. **`open()`** – function for opening files
2. **`'w'/'r'`** – mode: write / read
3. **`with`** – context manager for safe access
4. **`f.write()`/`f.read()`** – writing / reading

**Why it's so useful:**
- 🎯 Save data permanently
- 🔍 Process large amounts of data
- ⚡ Automatic resource management
- 🎲 Support for different file formats"""
