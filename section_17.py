import json

with open('practice.json', 'r') as json_data:
    data  = json.load(json_data)

print(data["meta"]["owner"]["name"])