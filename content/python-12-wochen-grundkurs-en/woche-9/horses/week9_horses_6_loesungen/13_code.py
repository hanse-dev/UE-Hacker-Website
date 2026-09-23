try:
    with open("missing.txt", "r") as f:
        print(f.read())
except FileNotFoundError:
    print("No file: missing.txt")
