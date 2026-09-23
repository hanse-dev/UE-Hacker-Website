def parse(text):
    try:
        action, target = text.split()
    except ValueError:
        return None
    return (action, target)

print(parse("go north"))
print(parse("hallo"))
