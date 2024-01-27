import json
path = r'C:\Users\Yurgenich\Desktop\PYTHON\Python_in\Task_8\sample4.json'

with open(path, 'r', encoding='Utf-8') as file:
    json_file = json.load(file)


print(json_file[1]['firstName'])

