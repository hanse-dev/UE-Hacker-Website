# Problem: load() expects a file, not a string
import json
data = {'name': 'Test'}
json_string = json.dumps(data)
result = json.loads(json_string)  # loads() for string
print(f'Result: {result}')