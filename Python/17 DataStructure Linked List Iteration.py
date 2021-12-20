class Node:

	def __init__(self, value):
		self.value = value
		self.next = None


class LinkedList:

	def __init__(self):
		self.first = None
		self.actual = None
		self.is_iterating = False # Important, don't touch

	def append(self, element):
		new = Node(element)
		if self.first:
			current = self.first
			while current.next:
				current = current.next
			current.next = new
		else:
			self.first = new

	def __iter__(self): # Important, don't touch
		return self

	def __next__(self): 
		if len(self) == 0: # The iteration doesn't start if the list is empty
			raise StopIteration
		if not self.is_iterating: # Starts iterating since list is not empty
			self.is_iterating = True
			self.actual = self.first.next
			return self.first.value
		elif self.is_iterating and not self.actual: # If it reaches the end it stops
			self.is_iterating = False
			raise StopIteration
		else:
			value = self.actual.value # Otherwise it returns the next value
			self.actual = self.actual.next
			return value

	def __len__(self):
		n = 0
		current = self.first
		while current:
			n += 1
			current = current.next
		return n

	def __getitem__(self, item):
		if len(self) == 0:
			raise IndexError
		n = 0
		current = self.first
		while n != item:
			current = current.next
			n += 1
			if current == None:
				raise IndexError
		return current.value

	def __str__(self):
		elements = []
		for element in self:
			elements.append(element)
		return str(elements)

l = LinkedList()
l.append(1)
l.append(2)
l.append(4)

for element in l:
	print(element)