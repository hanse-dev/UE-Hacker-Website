# 🚀 Module Log 1: Importing modules

Welcome to the **Module Banks of space station Nebula-7**! The ship's AI manages thousands of ready-made software modules. It reports: *"Whoever builds every program alone misses the launch. Whoever loads the right modules flies at once."*

You do not have to write everything yourself. Python comes with many ready-made **modules** – collections of functions you fetch with `import`:

```python
import math                 # load the whole module
print(math.sqrt(16))        # function with module name in front: 4.0

import math as m            # with a nickname
print(m.sqrt(25))           # 5.0

from math import sqrt       # fetch just one function
print(sqrt(36))             # 6.0 – without the module name in front
```

**Step by step:**
1. **`import module`** loads the module – you use it with **`module.function()`**
2. **`import module as short`** gives it a short **nickname**
3. **`from module import function`** fetches a single function – then you write **no** module name in front any more

> ⚠️ Without `import` Python does not know the module: `math.sqrt(16)` gives a **NameError**.
