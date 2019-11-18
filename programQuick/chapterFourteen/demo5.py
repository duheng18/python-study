stringOfJsonData = '{"name":"Zophie","isCat":true,"miceCaught":0,"felineIQ":null}'
import json

jsonDataAsPythonValue = json.loads(stringOfJsonData)
# {'name': 'Zophie', 'isCat': True, 'miceCaught': 0, 'felineIQ': None}
print(jsonDataAsPythonValue)

pythonValue = {'isCat': True, 'miceCaught': 0, 'name': 'Zophie', 'felineIQ': None}
import json
stringOfJsonData1=json.dumps(pythonValue)
print(stringOfJsonData1)
