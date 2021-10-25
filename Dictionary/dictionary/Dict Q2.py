''': Merge following two Python dictionaries into one
dict1 = {'Ten': 10, 'Twenty': 20, 'Thirty': 30}
dict2 = {'Thirty': 30, 'Forty': 40, 'Fifty': 50'''
dict1 = {'Ten': 10, 'Twenty': 20, 'Thirty': 30}
dict2 = {'Thirty': 30, 'Forty': 40, 'Fifty': 50}

dict1.update(dict2)
print(dict1)

'''
def Merge(dict1, dict2):
    res = {**dict1, **dict2}
    return res
dict3=merge(dict1, dict2)
'''