print("SECTION 1: Operation overloading\n-----------------")

class Number:

	def __init__(self, num):
		self.num = num

	def __add__(self, other_num):
		return self.num + other_num.num

	def __sub__(self, other_num):
		return self.num - other_num.num

	def __mul__(self, other_num):
		return self.num * other_num.num

	def __str__(self):
		return "This number's value is " + str(self.num)

n1 = Number(3)
n2 = Number(5)

print(n1 + n2)
print(n1 - n2)
print(n1 * n2)
print(n1)
