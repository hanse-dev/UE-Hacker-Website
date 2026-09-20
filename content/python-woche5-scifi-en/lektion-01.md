# 🚀 System Log 1: Defining a protocol

Welcome to the **Headquarters of Reusability** aboard space station Nebula-7! The ship's AI reports: *"A system protocol is written once – and runs on every mission."*

That is exactly what a **function** does: a piece of code with a name that you can call again and again.

```python
def start_scan():
    print("Scan started...")
    print("Checking sector!")

start_scan()
start_scan()
```

**Step by step:**
1. **`def`** starts the definition – here you only *define* the protocol
2. **`start_scan`** is the name of the protocol
3. **`()`** and the **colon `:`** always belong there
4. The **indented** code (4 spaces) is the protocol itself
5. **`start_scan()`** – with parentheses – *runs* it

> ⚠️ Defining does not run anything yet! Only the **call with parentheses** runs the code. Without parentheses (`start_scan`) nothing starts.

Every call runs the code again – so you save yourself copy & paste.
