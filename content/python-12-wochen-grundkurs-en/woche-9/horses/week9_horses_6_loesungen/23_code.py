import json

text = json.dumps({"pos": (3, 4)})
back = json.loads(text)
print(f"List: {back['pos'] == [3, 4]}")
print(f"Tuple: {back['pos'] == (3, 4)}")
