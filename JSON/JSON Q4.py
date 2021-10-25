'''Sort JSON keys in and write them into a file
Sort following JSON data alphabetical order of keys
sampleJson = {"id" : 1, "name" : "value2", "age" : 29}'''
import json
sampleJson = {"id" : 1, "name" : "value2", "age" : 29}
print(json.dumps(sampleJson))