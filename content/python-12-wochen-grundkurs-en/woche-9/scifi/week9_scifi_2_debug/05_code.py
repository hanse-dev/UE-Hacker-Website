import json
data = {'name': 'Test'}
json_string = json.dumps(data)
result = json.load(json_string)