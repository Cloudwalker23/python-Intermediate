'''
Create a new dictionary by extracting the following
keys from a below dictionary
Given dictionary
'''
sampleDict = {
    "name": "Kelly",
    "age": 25,
    "salary": 8000,
    "city": "New york"

}
dict=sampleDict.copy()
dict.pop("age")
dict.pop("city")
print(dict)