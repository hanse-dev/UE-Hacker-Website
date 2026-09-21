with open("ship_log.txt", "w") as f:
    f.write("Ship log Nebula-7\n")
with open("ship_log.txt", "r") as f:
    content = f.read()
print(f"Content: {content.strip()}")
