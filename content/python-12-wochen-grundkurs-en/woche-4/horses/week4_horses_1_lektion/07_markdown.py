"""## 🔍 The Secret of range() – The Number Rider

**range() is your most faithful companion for number sequences!**

### The three forms of range():

1. **`range(n)`** – Numbers from 0 to n-1
   ```python
   range(5) → 0, 1, 2, 3, 4
   ```

2. **`range(start, end)`** – Numbers from start to end-1
   ```python
   range(2, 7) → 2, 3, 4, 5, 6
   ```

3. **`range(start, end, step)`** – Numbers with gaps
   ```python
   range(1, 10, 2) → 1, 3, 5, 7, 9
   ```

**Important rules:**
- The **upper bound is always exclusive** (not included in the count)
- **Negative steps** are possible for counting backwards
- range() is **very memory-efficient** (generates numbers only when needed)"""
