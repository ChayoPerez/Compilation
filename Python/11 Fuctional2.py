from functools import reduce


print("SECTION 1: Functions as variables\n-----------------")

def random_function():
	print("La la la")

random_variable = random_function
random_variable()



print("\n\nSECTION 2: lambda\n-----------------")

another_function1 = lambda a, b: a*b
print(another_function1(3, 4))

another_function2 = lambda a: print(a)
another_function2("hello")



print("\n\nSECTION 3: filter\n-----------------")

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# array = list(filter(function, iterable))

def is_even(number):
	if number % 2 == 0:
		return True
	else:
		return False

evens = list(filter(is_even, numbers))
print(evens)

# using lambda it prints the same
evens2 = list(filter(lambda num: num%2==0, numbers))
print(evens2)




print("\n\nSECTION 4: Map\n-----------------")

# array = list(map(function, iterable))
doubles = list(map(lambda num: num * 2, evens))
print(doubles) # 
print(evens) # evens is not modified





print("\n\nSECTION 5: Reduce\n-----------------")

sum_variable = reduce(lambda a,b: a + b, doubles)
print(sum_variable)


print("\n\nSECTION 6: Enumerate\n-----------------")

name_list = ["Cero", "Uno", "Dos", "Tres", "Cuatro"]
enumeration = enumerate(name_list)
print(enumeration)
print(type(enumeration))
print(list(enumeration))


print("\n\nSECTION 7: Zip\n-----------------")

data = ["name", "lastname", "gender"]
person1 = ["Maya", "Hyde", "F"]
person2 = ["Ruth", "Bell", "X"]
person3 = ["John", "Rogers", "M"]

for p in person1, person2, person3:
	contacto = zip(data, p)
	print(contacto) # This is a zip object
	print(tuple(contacto)) # This is a tuple object

print("--------")

# You use zip to go back and forth
zipped = list(zip(data, person1))
print(zipped)
unzipped = list(zip(*zipped))
print(unzipped[0])
print(unzipped[1])

print("--------")
# You can also make it into a dictionary
keys = data
dictionary_zip1 = dict(zip(keys, person1))
print(dictionary_zip1)


print("\n\nSECTION 8: Lists\n-----------------")

base_list = ["0", "1", "2", "3", "4", "5"]
nums = [int(x) + 1 for x in base_list]
print(nums)