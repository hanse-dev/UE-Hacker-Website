"""## 📚 Data Stream 1: File Access – The Digital Stable Book

**What it is:** File access lets you save and load data on the hard drive.

**How file access works:**
```python
# Open a file and write
with open('stable_book.txt', 'w') as f:
    f.write('Horse Protocol')

# Open a file and read
with open('stable_book.txt', 'r') as f:
    content = f.read()
```

**Step-by-step explanation:**
1. **`open()`** – function for opening files
2. **`'w'/'r'`** – mode: write / read
3. **`with`** – context manager for safe access
4. **`f.write()`/`f.read()`** – write / read

**Why it's so useful:**
- 🎯 Save data permanently
- 🔍 Process large amounts of data
- ⚡ Automatic resource management
- 🏂 Support different file formats"""
