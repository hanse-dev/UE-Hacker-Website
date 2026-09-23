def read_or_empty(name):
    try:
        with open(name, "r") as f:
            return f.read()
    except FileNotFoundError:
        return ""

print(f"Empty: {read_or_empty('missing.txt') == ''}")
with open("stable_book.txt", "w") as f:
    f.write("Stable book of the farm\n")
print(f"Content: {read_or_empty('stable_book.txt').strip()}")
