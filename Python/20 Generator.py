print("SECTION 1: Simple generator\n-----------------")


def generador():
	value = 1
	while True:
		yield value
		value += 1

gen = generador()
print(next(gen))
print(next(gen))


print("\n\nSECTION 2: Error\n-----------------")


# def countdown_error(start):
#	n = start
# 	print("Counting from " + str(n) + " to 1")
# 	active = True
# 	while active:
# 		if n == 1:
# 			active = False
# 		yield n
# 		n -= 1

# a = countdown_error(5)
# for i in range(0,10):
# 	print(next(a))


# There is a point in which the generator stops yielding numbers


print("\n\nSECTION 3: Fixing Error\n-----------------")

def countdown(start):
	n = start
	print("Counting from " + str(n) + " to 1") 
	active = True
	while True:  # There is always iteration
		if n == 0: # active is only true until you reach 0
			active = False
		if not active: # now n is equals or lower than 0
			yield "No quedan numeros"
		else:
			yield n # If you haven't reached 0 yet you yield a number
		n -= 1 # Countdown

a = countdown(5)
print(a)
for i in range(0,10):
	print(next(a))