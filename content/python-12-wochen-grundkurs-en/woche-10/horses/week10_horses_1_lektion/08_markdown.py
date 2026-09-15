"""## 🪞 Why `self`? – The Key to Your Horses

**What is `self`?** `self` is the reference to **the concrete horse** that is currently being addressed. When you call `lucky.neigh()`, `self` inside the method is exactly the object `lucky`.

**Why do we need it at all?** A class can create many horses. Python needs to know: *which* of these horses is meant? With 10 horses the method needs to know: \"I am working for THIS horse here.\"

**In the constructor `__init__`:**
- `self.name = name` means: **Save** the passed `name` on THIS horse.
- Without `self` Python would not know where the variable belongs – it would only exist locally and disappear after the call.

**In methods:**
- `self.name` means: **Read the name** from THIS horse.
- Without `self` the method could not access the object's attributes – it would not know whether it's Lucky, Spirit or another horse.

**How the call works in the background:**
- `lucky.neigh()` is translated by Python to `Pony.neigh(lucky)`.
- The first argument is always the object itself – that's why the parameter is called `self`."""
