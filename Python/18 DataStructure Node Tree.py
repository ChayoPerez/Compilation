from collections import deque


class TreeNode:

	def __init__(self, node_id, value, parent_id,):
		self.node_id = node_id
		self.child = []
		self.parent = parent_id
		self.value = value

	def append(self, new_node):
		self.child.append(new_node)



class Tree:

	def __init__(self):
		self.root = TreeNode(0, "Root", None)

	def add_node(self, value, node_id, parent_id=0):
		node = self.search_id(parent_id)
		if node:
			node.append(TreeNode(node_id, value, node))
			print("Nodo [id" + str(node_id) + ": " + str(value) + "] agregado a nodo id" + str(node.node_id))
		else:
			print("El arbol no tiene nodos con ese id.")

	def search_id(self, node_id, start_node=None):
		if start_node == None:
			node = self.root
		else:
			node =  start_node

		if node.node_id == node_id:
			return node
		else:
			for child in node.child:
				node = self.search_id(node_id, child)
				if node:
					return node
		return None


	# Non recursive reading of the tree
	def print_tree(self):
		nodes = [] # Here we  store tuples with the nodes' info
		thread = deque()
		thread.append(self.root) # The first element is the root
		visited_ids = []

		while len(thread) > 0:
			node = thread.pop() # You get the nod and if it's not visited, store info in 'nodes' and mark as visited
			if not (node.node_id in visited_ids):
				nodes.append((node.value, node.node_id, node.parent))
				visited_ids.append(node.node_id)
				for child in node.child: # Append all the children of that node
					thread.append(child)

		# Every tuple in nodes is stored in three  variables
		for value, node_id, parent in nodes:
			if parent:
				print("Nodo [" + str(node_id) + " :" + str(value) + "], parent " + str(parent.node_id))
			else:
				print("Root [" + str(node_id) + "]")





tree = Tree()
tree.add_node("A", 1)
tree.add_node("B", 2)
tree.add_node("AA", 3, 1)
tree.add_node("AAA", 4, 3)
tree.add_node("X", 5, 100)

tree.print_tree()