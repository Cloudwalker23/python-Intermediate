'''Exercise 4: Initialize dictionary with default values
Given:
employees = ['Kelly', 'Emma', ‘George’]
defaults = {"designation": 'Application Developer', "salary": 8000'''

employees = ['Kelly', 'Emma','George']
defaults = {"designation": 'Application Developer', "salary": 8000}

resDict = dict.fromkeys(employees, defaults)
print(resDict)

# Individual data
print(resDict["Kelly"])