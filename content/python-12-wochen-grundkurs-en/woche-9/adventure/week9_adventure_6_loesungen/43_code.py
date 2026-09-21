with open("test.txt", "w") as f:
    f.write("Hello")
with open("test.txt", "r") as f:
    content = f.read()
print(content)
