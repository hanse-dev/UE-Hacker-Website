"""## 🪞 Why `self`? – The Key to Your Objects

**What is `self`?** `self` is the reference to **the concrete object** that is currently being addressed. When you call `enterprise.launch()`, `self` inside the method is exactly the object `enterprise`.

**Why do we need it at all?** A class can create many objects. Python needs to know: *which* of these objects is meant? With 10 spaceships the method needs to know: \"I am working for THIS ship here.\"

**In the constructor `__init__`:**
- `self.name = name` means: **Save** the passed `name` on THIS object.
- Without `self` Python would not know where the variable belongs – it would only exist locally and disappear after the call.

**In methods:**
- `self.name` means: **Read the name** from THIS object.
- Without `self` the method could not access the object's attributes – it would not know whether it's Enterprise, Millennium or another ship.

**How the call works in the background:**
- `enterprise.launch()` is translated by Python to `Spaceship.launch(enterprise)`.
- The first argument is always the object itself – that's why the parameter is called `self`."""
