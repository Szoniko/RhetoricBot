import json

def append_json(json_data, filename='test.json'):
    with open(filename, "r+") as file:
        data = json.load(file)
        data.update(json_data)
        file.seek(0)
        json.dump(data, file, indent=4)

def create_json(filename):
    with open(filename, 'w') as file:
        file.write('{}')
        file.close()

def getKeyValue(json, key):
    return json.get(key)

def readJson(filename):
    with open(filename, 'r') as file:
        return json.load(file)
