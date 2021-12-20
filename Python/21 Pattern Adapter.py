class Tool:
	def __init__(self, tool):
		self.tool = tool

	def use_tool(self):
		self.tool.use_tool()

class Hammer:
	def swing_hammer(self):
		print("You swing the Hammer!")

class HammerAdapter:
	def __init__(self, hammer):
		self.hammer = hammer

	def use_tool(self):
		self.hammer.swing_hammer()

hammer = Hammer()
hammer_adapter = HammerAdapter(hammer)
my_tool = Tool(hammer_adapter)

my_tool.use_tool()