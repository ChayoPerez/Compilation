import math as m
# import math
# from math import sqrt, pow
import ImportedModule # What we are importing to see the printing order and the result of __name__ in each file

print("SECTION 1: Note the order")


x = m.sqrt(25)
print(x)

y = m.pow(2, 3)
print(y)
ImportedModule.a_random_function()

print("14 Module")
print(__name__) # When opened, it prints "__main__"


