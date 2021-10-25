'''Exercise 1: Below are the two lists convert it into the dictionary'''
keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]
'''dict1= {
    'ten':10,
    'Twenty':20,
    'thirty':30
}
print(dict1)
'''
dict2={keys[i]:values[i] for i in range(len(keys))}
print(dict2)
dict3=dict(zip(keys,values))

print(dict(zip(keys,values)))