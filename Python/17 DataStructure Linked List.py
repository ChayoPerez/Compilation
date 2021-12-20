class Node:

	def __init__(self, value):
		self.next = None
		self.value = value


class LinkedList:

	def __init__(self):
		self.head = None
		self.tail = None

	def add(self, value):
		new = Node(value)
		if not self.tail:
			self.head = new
			self.tail = new
		else:
			self.tail.next = new
			self.tail = new

	def __getitem__(self, position): # So you can list[1] = second value
		node = self.head
		for i in range(position):
			if node != None:
				node = node.next
		if node:
			return node.value
		else:
			return "Not found."

	def __repr__(self): # So you can print it
		rep = ""
		node = self.head
		while node != None:
			rep += str(node.value) + " "
			node = node.next
		return rep

l = LinkedList()
l.add(1)
l.add(4)
l.add(7)
l.add(10)
l.add(0)

print(l[1])
print(l[4])
print(l)