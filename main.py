import json
'''code to compare apple prices '''
with open("resources/apples.json", 'r') as file:
    info = json.load(file)
    print(info)