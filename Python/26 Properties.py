class PositiveInterger:

	def __init__(self):
		self.n = 0

	@property
	def number(self):
		return self.n

	@number.setter
	def number(self, new):
		if type(new) == int and new >= 0:
			self.n = new
		else:
			print("That is not a valid number, my friend")

	@number.deleter
	def number(self):
		print("Stored number deleted.")
		del self

b = PositiveInterger()

print(b.number)
b.number = 4
print(b.number)
b.number = -2
print(b.number)

del b
try:
	print(b)
except:
	print("Variable b does not longer exist")
