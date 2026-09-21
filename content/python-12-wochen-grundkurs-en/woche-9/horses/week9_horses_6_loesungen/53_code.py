with open("stable_book.txt", "w") as f:
    f.write("Stable book of the farm\n")
    f.write("Status: Open\n")
    f.write("Ride planned\n")
def count_lines(name):
    try:
        with open(name, "r") as f:
            return len(f.readlines())
    except FileNotFoundError:
        return 0

print(f"stable_book.txt: {count_lines('stable_book.txt')}")
print(f"missing.txt: {count_lines('missing.txt')}")
