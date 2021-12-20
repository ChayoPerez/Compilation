print("SECTION 1: Functions creating functions\n-----------------")

# This function returns the function greeting with the name already specified
def greetings_generator(name):
	print("Creating generator for name " + name)
	def greeting():
		print("Hello " + name + "!")
	return greeting

# We generated two functions which come from an edited greeting
say_hello_to_ana = greetings_generator("Ana")
say_hello_to_john = greetings_generator("John")

say_hello_to_ana()
say_hello_to_john()


print("\n\nSECTION 2: Manually decorating fuctions with functions\n-----------------")

# I'll add to this example some prints so we see what
# executes first

# Simple function
def division(a, b):
	print("division(a,b)")
	print(a / b)


# This function makes sure you always make the division so 
# the largest number is the one being divided
def smart_div(func): # func = original function
	print("smart_div(func)")
	def inner_function(a, b):
		print("inner_function")
		if a < b:
			a, b = b, a
		return func(a, b)
	return inner_function 
	# smart_div returns inner_function, which uses the original func inside it


div = smart_div(division)
# using the function as a variable 
# Both print the same:
div(4, 2)
div(2, 4)

# What is printed?

# smart_div(func) 	--> Decorator is read only once
# inner_function 	--> While inner function is read every time
# division(a,b) 	--> If valid, the initial function runs too
# 2.0 				--> This is just the result of div(4,2)
# inner_function
# division(a,b)
# 2.0

print("-----")

# Simple function
def multiply(a, b):
	print(a * b)

# smart_mult makes sure the types are correct
def smart_mult(func):

	def inner_function(a, b):
		if (type(a) == int or type(a) == float) and (type(b) == int or type(b) == float):
			return func(a, b) # calls func because variables are valid
		else:
			print("The numbers are not valid") # Does not call func as the variables are not valid
	return inner_function

mult = smart_mult(multiply)
mult(2, 5)
mult("Hello", 4)



print("\n\nSECTION 3: How to properly decorate a function with a function\n-----------------")

# There is another way to write this:


@smart_mult
def multiply2(a, b):
	print(a * b)
# What happens here?
# First we read the decorator
# The decorator receives multiply2 as func
# The decorator checks the numbers are valid
# The decorator chooses to use or not the func you passed
# aka, multiply2 with its parameters a, b

multiply2(2,5)
multiply2("Hello", 3)

print("------")

def protection_function(f):
	def inner_function():
		if RandomClass.permission_granted:
			f()
		else:
			print("Permission was not granted")
	return inner_function

class RandomClass:

	permission_granted = False

	@protection_function
	def dangerous_action():
		print("So much dangerous stuff right here")

	def grant_permission():
		RandomClass.permission_granted = True

RandomClass.dangerous_action()
RandomClass.grant_permission()
RandomClass.dangerous_action()



print("\n\nSECTION 4: Class decorating function\n-----------------")
class Power:
	def __init__(self, func):
		print("__init__ Power")
		self._func = func

	def __call__(self, a, b):
		print("Power called") #(3)
		return_val = self._func(a, b)
		return return_val ** 2


@Power # (1)__init__ Power is printed
def multiply_together(a, b):
	print("multiply_together called") # (4)
	return a * b


print(multiply_together) # (2) Object is printed
print(multiply_together(2, 2)) # (5) --> print(16)



print("\n\nSECTION 5: Function decorating Class\n-----------------")

def decorator_function(target): # Target is the class

    def decorator_init(self):
        print("Decorator running") # This is what is printed because __init__ got replaced

    target.__init__ = decorator_init # decorator_init replaces RandomClass.__init__
    return target # You have to return the class 

@decorator_function
class RandomClass:
    def __init__():
        print("RandomClass running") # This does not run

RandomClass() # Prints "Decorator running"



print("\n\nSECTION 6: Function decorator with parameters\n-----------------")

""" When you mean to pass arguments to the decorated function
you have to make a third function, which is the one that
receives the arguments you later use in wrapper
wrapper is the new, decorated fuction """

def box_decorator(lock_class): # When you need to add parameters
	def opener(function): # The one that receives the function
		def wrapper(): # What will be called in place of open()
			if lock_class.locked:
				print("Function locked!")
			else:
				return function()
		return wrapper
	return opener

"""Code explanation:
Class Lock has a static variable called locked
locked can be changed by using unlock() and lock(), static methods
SecretBox can only be opened when Lock.locked is False
So we pass to the decorator the whole Lock class
Which gives it permanent access to Lock.locked
even if the value of Lock.locked changes """


class Lock:

	locked = True

	def unlock():
		Lock.locked = False

	def lock():
		Lock.locked = True


class SecretBox:

	@box_decorator(Lock)
	def open():
		print("Box opened!")

SecretBox.open() # Function locked!
Lock.unlock()
SecretBox.open() # Box openes!



# Something to be noted: This was my original code:

# def box_decorator(locked):
# 	def opener(function):
# 		def wrapper():
# 			if locked:
# 				print("Function locked!")
# 			else:
# 				return function()
# 		return wrapper
# 	return opener


# class SecretBox:

# 	@box_decorator(Lock.locked)
# 	def open():
# 		print("Box opened!")


# What is wrong here?
# Lock.locked is the argument we pass to box_decorator
# Since its a boolean, the value in 'if locked' is set once 
# when making the function and never again
# Even if you change Lock.locked later, the bool is set
# Since locked starts as True, you will never be able to execute open()


print("\n\nSECTION 7: Double decorators\n-----------------")


def decoratorA(original_function):
	print("DecoratorA creates wrapper")
	def wrapper_function(*args, **kwargs):
		print("DecoratorA's wrapper is called")
		return original_function(*args, **kwargs)
	return wrapper_function

def decoratorB(original_function):
	print("DecoratorB creates wrapper")
	def wrapper_function(*args, **kwargs):
		print("DecoratorB's wrapper is called")
		return original_function(*args, **kwargs)
	return wrapper_function

@decoratorB
@decoratorA
def plus(a, b):
	return a + b

# Order:
# DecoratorA creates wrapper
# DecoratorB creates wrapper
# DecoratorB's wrapper is called
# DecoratorA's wrapper is called

print(plus(1, 2))

