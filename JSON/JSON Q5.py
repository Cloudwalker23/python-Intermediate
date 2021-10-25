'''Access the nested key ‘salary’ from the following 
JSON
import json
sampleJson = { 
 "company":{ 
 "employee":{ 
 "name":"emma"
  "payble":{ 
 "salary":7000,
 "bonus":800
 }
 }
 }
}'''
import json
sampleJson = { 
 "company":{ 
 "employee":{ 
 "name":"emma",
  "payble":{ 
 "salary":7000,
 "bonus":800
 }
 }
 }
}
print(json.dumps(sampleJson['company']['employee']['payble']['salary']))