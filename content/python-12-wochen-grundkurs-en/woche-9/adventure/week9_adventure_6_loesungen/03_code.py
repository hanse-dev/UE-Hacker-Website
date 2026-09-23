with open("quest_log.txt", "w") as f:
    f.write("Pyralia Quest Log\n")
with open("quest_log.txt", "r") as f:
    content = f.read()
print(f"Content: {content.strip()}")
