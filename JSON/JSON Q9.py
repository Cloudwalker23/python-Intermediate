import json
list1=[ 
 { 
 "id":1,
 "name":"name1",
 "color":[ 
 "red",
 "green"
 ]
 },
 { 
 "id":2,
 "name":"name2",
 "color":[ 
 "pink",
 "yellow"
 ]
 }
]
container=[]
for i in list1:
    container.append(i['name'])
print(json.dumps(container))

