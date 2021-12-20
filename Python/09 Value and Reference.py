print("SECTION 1: By value\n-----------------")

#  Basic types are passed by value while other objects are passed by reference

# This are two ints that start with the same value
a = 10
b = a
# They all return the same id
print(id(a))
print(id(b))
print(id(10))

print()

b = 5 # b changes value and is not longer the same as a, but is the sames as 5
print(id(a))
print(id(b))
print(id(5))


def functionA(x):
   x = 5
   return x

a = 10
print(functionA(a))
print(a)
# a does not change
# ints are value variables



print("\n\nSECTION 2: By reference\n-----------------")


array1 = [1, 2, 3]
array2 = array1
array3 = [1, 2, 3]

print(id(array1))
print(id(array2)) # array2 shares id of array1
print(id(array3))


print(array1)
array2.append(4)
print(array1) # 4 is added to both arrays


def functionB(l):
   l.append(3)
   return l

b = [1, 2]
print(functionB(b))
print(b)
# b does change
# lists go by reference