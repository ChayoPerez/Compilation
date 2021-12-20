# VARIABLES AND BASIC TYPES
print("SECTION 1: Basic types\n-----------------")


number1 = 1
float1 = 1.5
string1 = "Hello"
bool1 = True
bool2 = False
print(type(number1))
print(type(float1))
print(type(string1))
print(type(bool1))

# variables are written in snakecase
# No ; at the end of statements

print("\n\nSECTION 2: interacions between types\n-----------------")

# Declaring and initializing are done in the same line
random_string = "Hello world"
print(2 * random_string)

random_number = 4
# print("The number is " + random_number)
# This doesn't work ^^^
# You can't put a string and an int together


# This does work
print("The number is " + str(random_number))
# This works too
random_number_now_string = str(random_number)
print(2 + int(random_number_now_string))

# ints and floats can be used together
print(0.4 + 3)
print(type(0.4 + 3)) # converts to float


print("\n\nSECTION 3: using \\ in strings \n-----------------")

# Strings:
# Both of this things print the same

print("c:\\docs\\navin")
print(r'c:\docs\navin')


# while positive numbers start in 0 from the begining, negative numbers start from -1 from the end
print(random_string[0]) # -> "H"
print(random_string[-1]) # -> "d"
print()
# To exemplify this:

random_string2 = "Abcd";

print(random_string2[0]) # A
print(random_string2[1]) # b
print(random_string2[2]) # c
print(random_string2[3]) # d

print()
# print(random_string2[4]) 
# What happens here? IndexError: string index out of range


print(random_string2[-1]) # d
print(random_string2[-2]) # c
print(random_string2[-3]) # b
print(random_string2[-4]) # A

# print(random_string2[-5]) 
# WHat happens here? IndexError: string index out of range


print("\n\nSECTION 4: Playing with strings\n-----------------")

# random_string = "Hello world"

print(random_string[1:4]) # -> "ell" Starts in 1 and ends at 3
print(random_string[1:400]) # Doesn't throw error! Just prints to the end
print(random_string[0:len(random_string)]) #  Prints it all
print(random_string[0:len(random_string):2]) # Prints all with steps of two. Hlowrd

# Constants are written in all uppercase
PI = 3.14
