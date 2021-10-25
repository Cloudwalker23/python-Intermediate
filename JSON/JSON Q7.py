'''Convert the following JSON into Vehicle Object
For example, we should able to access Vehicle Object using the dot operator like this.
vehicleObj.name, vehicleObj.engine, vehicleObj.price'''
import json

class Vehicle:
    def __init__(self, name, engine, price):
        self.name = name
        self.engine = engine
        self.price = price
def vehicleDecoder(obj):
        return Vehicle(obj['name'], obj['engine'], obj['price'])
    
vehicleObj = json.loads('{ "name": "Toyota Rav4", "engine": "2.5L", "price": 32000 }',
           object_hook=vehicleDecoder)

print("Type of decoded object from JSON Data")
print(type(vehicleObj))
print("Vehicle Details")
print(vehicleObj.name, vehicleObj.engine, vehicleObj.price)
