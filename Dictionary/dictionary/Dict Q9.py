'''Exercise 9: Get the key of a minimum value from the following
dictionary

'''
sampleDict = {
 'Physics': 82,
 'Math': 65,
 'history': 75
}
count=sampleDict['Physics']
for i in sampleDict:
   var=sampleDict[i]
   if var<count:
       count=var

for i in sampleDict:
    if sampleDict[i]==count:
        print(i)
        break


