def parse(text):
    try:
        action, target = text.split()
    except ValueError:
        return None
    return (action, target)

print(parse("gehe norden"))
print(parse("hallo"))
