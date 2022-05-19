import json
# while True:
with open('data.json', 'r') as infile:
    data = json.load(infile)
    print(data)