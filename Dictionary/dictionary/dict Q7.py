'''Exercise 7: Check if a value 200 exists in a dictionary
sampleDict = {'a': 100, 'b': 200, 'c': 300}
Expected output:
True'''

sampleDict = {'a': 100, 'b': 200, 'c': 300}
for i in sampleDict:
    if sampleDict[i]==200:
        print('True')
'''
print(200 in sampleDict.values())'''