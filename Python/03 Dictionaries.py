from collections import defaultdict


print("SECTION 1: Creating a dicitonary\n-----------------")

# Option 1 for creating dictionaries
data = {"raperez": "Andie", "aaperez": "Ariel"}
print(data["raperez"])

# Option 2 for creating dictionaries
data2 = dict()
data2["raperez"] = "Andie"
data2["aaperez"] = "Ariel"
print(data["raperez"])


print("\n\nSECTION 2: Key Error\n-----------------")

print("When you refer to a key that does not exits you get KeyError")
# print(data["pepito"]) 



print("\n\nSECTION 3: values, keys and items\n-----------------")


# These are not quite lists
print(data2.values())
print(data2.keys())
print(data2.items())
print()
# But can be turned into one
values = list(data2.values())
keys = list(data2.keys())
items = list(data2.items())
print(items)
print(values)
print(keys)
print()

#Wayys to go back to a dictionary
data3 = dict(zip(keys, values))
print(data3)
print(type(data3)) # dict

data4 = dict(items)
print(data4)
print(type(data4)) # dict


print("\n\nSECTION 4: Some dict behavior\n-----------------")

dict1 = {1: "uno", 2: "dos", 3: "tres", 4: "cuatro"}

print(dict1)
print("For x in dict: takes just the keys")
for x in dict1:
	print(x)

d_items = dict1.items()

print("Reading items")
for tupla in d_items:
	print("La key es {0} y el valor es {1}".format(tupla[0], tupla[1]))

print("Alternativamente")
for x, y in d_items:
	print("La key es {0} y el valor es {1}".format(x, y))



print("\n\nSECTION 5: Default dictionary\n-----------------")


items_number = 0

def give_value():
	global items_number
	items_number += 1
	return str(items_number)

dict3 = defaultdict(give_value)
dict3["first number"] = 0
# Created "first number": 0

# When you don't give  value to a nonexistent key
# the function 
print(dict3["first number"]) # 0
print(dict3["second number"]) # "second number": 1