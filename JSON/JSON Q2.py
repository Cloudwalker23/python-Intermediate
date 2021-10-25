'''Access the value of key2 from the following JSON'''
import json
sampleJson ={"key1": "value1", "key2": "value2"}
print(json.dumps(sampleJson['key2']))
