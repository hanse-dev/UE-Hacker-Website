import json
data = {"name": "Test"}
text = json.dumps(data)
result = json.loads(text)
print("Name:", result["name"])
