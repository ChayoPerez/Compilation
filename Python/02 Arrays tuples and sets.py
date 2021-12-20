from array import *
# We use the array() method from this library
from collections import deque
from collections import namedtuple


print("SECTION 1: Arrays\n-----------------")

array1 = [1, 2, 3, 4, 5]
print(array1)
print(array1[0])
print(array1[0:2]) # [1,2] Starting from 0 up to 1



print("\n\nSECTION 2: Basic methods\n-----------------")

# Arrays can have different kinds of variables/objects
array2 = [1, 2, "random_string", False]
print(array2)
array2.append(0.5) # Adds in the end of the array
print(array2)
array2.insert(4, 6) # Inserts in a given index. In this case, inserts 6 in position 5

print(array2) 
# [1, 2, 'random_string', False, 6, 0.5]
# The element originally in index 4 is not removed
# just moved one space to the right

array2.remove(2) # 2 is the element to remove, not the index of it
print(array2)

# What happens if there is more than one element with that value?
array_with_repetition = [1,2,2,3]
array_with_repetition.remove(2)
print(array_with_repetition) 
# Only removes the first one it encounters


element = array2.pop(2) # index of element to remove: In this case, False
print(array2)
print(element) # with pop you can get the element you removed

array2.pop() # If you don't specify, the element you remove is the last one
print(array2)

index_found = array2.index("random_string")
print("The index of 'random_string' is " + str(index_found))

# This prints ValueError since what is searched for doesn't exist:
# index_found2 = array2.index("hello world!")
# print("Not found: " + str(index_found2))



print("\n\nSECTION 3: Using del\n-----------------")

array3 = ["apple", "banana", "orange", "Watermelon", "Pear"]
print(array3)
del array3[0] # Deletes idex 0 => apple
print(array3)
del array3[2:] # deletes from index 2 onward, including index 2
print(array3)


print("\n\nSECTION 4: Extend\n-----------------")

array3.extend(["melon", "kiwi"])
print(array3) # elements are added to the array at the end



print("\n\nSECTION 5: String to list conversion\n-----------------")


random_string2 = "This is a sentence"
print(random_string2)
print(list(random_string2))


print("\n\nSECTION 6: Using array method\n-----------------")

# Another way to create an array
array4 = array("i", [1, 2, 3, 4, 5, 6, 7]) # This comes from the module we imported in the first line
print(array4)


print("\n\nSECTION 7: Using copy\n-----------------")

# With copy you have equal but separate instances of the list
array5 = array3.copy()
print(id(array3))
print(id(array5))


#----------------------------

print("\n\nSECTION 8: Tuples\n-----------------")


tup = (1, 2, 3, 4)
print(tup) # (1, 2, 3, 4)

# Unpacking tuple
x, y, z, w = tup
print("x: " + str(x))
print("y: " + str(y))
print("z: " + str(z))
print("w: {0}".format(str(w))) # Otra forma de imprimir


# Values can't be changes
# tup[0] = 5 ERROR
print(tup[0:2]) # (1,2)


print("Named tuples")
# You can create something similar to an object with parameters


# This is how it isn't node:
# -------------------
person = namedtuple("name", "age")

try:
	u1 = person("Kai", 15)
	print(u1.name)
	print(type(u1))
except TypeError:
	print("A namedtuple needs as first argument the name of the 'class'")
	print("In this case, 'name' would be the  name of the 'class'")
	u1 = person(15)
	print(u1.age)
	print(type(u1))
# -------------------

# This is the correct way to make a namedtuple
user = namedtuple("UserType", ["name", "age"])
u2 = user("May", 13)
print(u2.name)
print(u2.age)
print(type(u2))


print("\n\nSECTION 9: Sets\n-----------------")

# Sets  DO NOT have order, so you can index them: set[]
set1 = {1, 2, 3, 4}
set1.add(100)
print(set1)
set2 = {3, 4, 5, 6}

print(set1.union(set2)) # Order  does not matter
print(set2.intersection(set1)) # Order does not matter

# Elements that are not present in both. Order does not matter
print(set1.symmetric_difference(set2))

# From here on, orther DOES matter:
set3 = {1, 2, 3}
set4 = {2, 3}
print("\nSubset")
print(set3.issubset(set4))
print(set4.issubset(set3))
print("\nSuperset")
print(set3.issuperset(set4))
print(set4.issuperset(set3))

print("\nDifference")
print(set3.difference(set4))
print(set4.difference(set3))



print("\n\nSECTION 10: Deque\n-----------------")

queue = deque()
queue.append(1)
queue.append(2)
queue.append(3)
queue.append(4)
print(queue)

print("----------")
print("POPLEFT(): " + str(queue.popleft()))
print(queue)

print("----------")
print("POP(): " + str(queue.pop()))
print(queue)

print("----------")
print("APPENDLEFT(1)")
queue.appendleft(1)
print(queue)

print("----------")
print("APPENDRIGHT(5)")
queue.append(5)
print(queue)

print("----------")
print("REMOVE(3)")
queue.remove(3)
print(queue)

print("----------")
print("CLEAR")
queue.clear()
print(queue)