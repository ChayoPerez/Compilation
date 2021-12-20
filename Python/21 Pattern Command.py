class MyVariable:

	my_variable = None

	def __init__(self, value):
		self.value = value
		MyVariable.my_variable = self

	def move(self, move_value):
		self.value += move_value

class Command:
	def execute(self):
		pass

	def undo(self):
		pass

class ButtonCommand (Command):
	def execute(self):
		MyVariable.my_variable.move(1)

	def undo(self):
		MyVariable.my_variable.move(-1)

class Button:
	def __init__(self, command):
		self.command = command

	def press_button(self):
		self.command.execute()

	def controlZ(self):
		self.command.undo()


myVariable = MyVariable(10)

myCommand = ButtonCommand()
button1 = Button(myCommand)

print(myVariable.value)
button1.press_button()
print(myVariable.value)
button1.controlZ()
print(myVariable.value)
