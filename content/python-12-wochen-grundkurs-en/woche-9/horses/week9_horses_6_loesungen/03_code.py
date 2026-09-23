with open("stable_book.txt", "w") as f:
    f.write("Stable book of the farm\n")
with open("stable_book.txt", "r") as f:
    content = f.read()
print(f"Content: {content.strip()}")
