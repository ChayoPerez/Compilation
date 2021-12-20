import json


print("SECTION 1: Basics JSON\n-----------------")

dictionary = {"name": "Andie", "lastname": "Perez", "age":24}
print(dictionary)
print(type(dictionary))

print("-----")

json_string = json.dumps(dictionary)
print(json_string)
print(type(json_string))

print("-----")

dictionary2 = json.loads(json_string)
print(dictionary2)
print(type(dictionary2))



print("\n\nSECTION 2: JSONEncoder\n-----------------")


class Person:
    
    def __init__(self, name):
        self.name = name
        
class PersonEncoder(json.JSONEncoder):
    
    def default(self, obj):
        if isinstance(obj, Person):
            print("We are dumping a Persona object")
            new_name = obj.name[0].upper() + obj.name[1::].lower()
            return {"name": new_name}
        else:
            print("This is not a Persona object, PersonEncoder can't dump")
            super().default(obj)

    
person = Person("sAm")
dumped_person = json.dumps(person, cls=PersonEncoder)
undumped_person = json.loads(dumped_person)
print(undumped_person)
