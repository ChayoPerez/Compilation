print("SECTION 1: Basics\n-----------------")


def say_hi(name):
   print("Hello, " + name + "!")


say_hi("Andie")


def sum(num1, num2):
   return num2 + num1


print("The sum of 2 + 3 is " + str(sum(2, 3)))


def functionA(name, lastname=""): 
   # lastname can be skipped when calling function and take the value of "" in this case
   print("Hello " + name + " " + lastname + "!")

functionA(lastname="Pérez", name="Andie")
functionA(name="Hannah") # Here lastname takes  the value of ""




print("\n\nSECTION 2: *args\n-----------------")

# HOW TO USE * AND **

def multiply(a, *b):
   result = a
   # b is a tuple!
   for i in range(0, len(b)):
      result *= b[i]
   return result

print(multiply(2,3,4))

# This one works.
# With one * you just put all the arguments you want
def contact1(name, number, *data):
   print(name)
   print(number)
   print(data[0])

print("\ncontact1")
contact1("Andie", 66619172, "gender neutral", "asdf")
# (gender, asdf) is a tuple
# asdf is not used

def contact2(name, number, *data):
   print(name)
   print(number)
   print(data)

# contact2(name="Andrea", number=66619172, gender="gender neutral")
# ERROR TypeError: contact2() got an unexpected keyword argument 'gender'
# with * you shouldn't name the arguments



print("\n\nSECTION 3: **args\n-----------------")



def contact3(name, number, **data):
   print(name)
   print(number)
   print(data)

# contact3("Chayo", 66619172, "gender neutral")
# ERROR  TypeError: contact3() takes 2 positional arguments but 3 were given


print("contact4")
# This one  works. With ** you have to name the arguments
def contact4(name, number, **data):
   print(name)
   print(number)
   print(data) # data is a dictionary!

contact4(name="Andie", number=66619172, gender="gender neutral")
print("----")
contact4("Andie", 66619172, gender="gender neutral")
# Since name and number are explicitly part of the function they don't need names
# But can have them if you want

print("----")
contact4(name="Andie", number=66619172, gender="gender neutral", random_info="asdf")
# Here the dictionary data has two elements inside! You can put as many as you want


print("\n\nSECTION 5: Global variables\n-----------------")


# USING GLOBAL VARIABlES

a = 2

def print_a():
   print(a)
   # prints the global variable
   
print_a()

def modify_a():
   a = 14
   # Does NOT modify the global variable
   # Read only

modify_a()
print_a() # prints 2

def modify_a_correctly():
   globals()["a"] = 14

modify_a_correctly() # the global variable is now 14
print_a() # prints 14



print("\n\nSECTION 6: Function returns tuples\n-----------------")


# RETURNING TUPLES

def odd_and_even(list_of_numbers):
   odd = []
   even = []
   for number in list_of_numbers:
      if number%2 == 0:
         even.append(number)
      else:
         odd.append(number)
   return odd, even

numbers = [1, 2, 3, 4 ,5]

odd, even = odd_and_even(numbers)
print(odd)
print(even)
print(type(odd_and_even(numbers)))