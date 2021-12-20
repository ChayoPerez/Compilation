print("SECTION 1: Basic catching\n-----------------")


# 1)  NameError
try:
	a = a + 1
except NameError as err:
	print(err)
print("------------------------")



# 2) ZeroDivisionError
try:
	number = 10/0
except ZeroDivisionError as err:
	print(err)
print("------------------------")

# 3) IndexError
try:
	lista = [1, 2, 3]
	print(lista[3])
except IndexError as err:
	print(err)
print("------------------------")

# 4) TypeError
try:
	n = 4
	text = "cuatro"
	new = n + text
except TypeError as err:
	print(err)
print("------------------------")

try:
	numero = 10
	lenght = len(numero)
except TypeError as err:
	print(err)
print("------------------------")

# 5) AttributeError
try:
	numero = 10
	lenght = numero.len()
except AttributeError as err:
	print(err)
print("------------------------")

# 6) KeyError
try:
	dictionary = dict()
	dictionary["a"] = "arbol"
	dictionary["c"] = "casa"
	print(dictionary["b"])
except KeyError as err:
	print(err)
print("------------------------")



print("\n\nSECTION 2: Exception Handling\n-----------------")

print("1)")
try:
	print(10/0)
except Exception as err: # If there was an exception
	print("Error")
	print(err)
	print(type(err)) # type is ZeroDivisionError, subclass of Exception
else: # If there wasn't an exception
	print("No error")
finally:
	print("Finished") # Regardless if there was or wasn't an exception
	# So if every except&else needs some code, you don't have to repeat it
	# Example: closing a file you opened in the try.s

print()
print("2)")
try:
	print(10/2)
except Exception:
	print("Error")
	print(err)
	print(type(err))
else:
	print("No error")
finally:
	print("Finished")




print("\n\nSECTION 3: Custom Exceptions\n-----------------")



class RandomError (Exception):

	locked = True


class InvalidCharacterError (Exception):

	def __init__(self, text):
		self.text = text
		super().__init__("There are invalid characters in the text: " + self.find())

	def find(self):
		invalid_chars = set()
		for x in self.text:
			if not x.isalpha():
				invalid_chars.add(x)
		return str(invalid_chars)


class EmptyResponseError (Exception):

	def __init__(self):
		super().__init__("You entered no response.")


def receive_answer(text):
	if len(text) == 0:
		raise EmptyResponseError()

	for x in text:
		if not x.isalpha():
			raise InvalidCharacterError(text)



print("\n\nSECTION 4: More than one Exception\n-----------------")

while (True):

	answer = input("only letters plz: ")
	try:
		receive_answer(answer)
	except EmptyResponseError as err:
		print("ERROR: " + str(err))
	except InvalidCharacterError as err:
		print("ERROR: " + str(err))
	else:
		print("Respuesta valida.")
	finally:
		print("-----------------\n")
