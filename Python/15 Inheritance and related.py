print("SECTION 1: Simple Inheritance\n-----------------")

class Pet:

   def __init__(self, name, owner):
      self.name = name
      self.owner = owner

   def print_status(self):
      print("The name of this pet is " + self.name + " and it is owned by " + self.owner)

class Dog (Pet):

   # Uses the same constructor as the parent class

   def bark(self):
      print("Guau guau!")

dog = Dog("Wafer", "Mano")
dog.print_status()
dog.bark()

# You can override but not overload
# You can also inherit from more than one class



print("\n\nSECTION 2: Multiple Inheritance\n-----------------")

class Food:

   def __init__(self, name, calories):
      self.name = name
      self.calories = calories

   def eat(self):
      print("It doesn't taste very well")

class Pizza (Food):

   def __init__(self, name, calories):       # Has own constructor
      super().__init__(name, calories)

   # You can override, but not overload
   def eat(self):
      print("I love pizza, this is great")

pizza = Pizza("Pineapple Pizz", 300)
pizza.eat()


class Clothes:

   def __init__(self, name, size):
      self.name = name
      self.size = size

   def wear(self):
      print("It fits you well")


class ChessePants (Food, Clothes):
   # Note that both have the variable name
   # Bellow when you print cheese_pants.__dict__ you can see it only appears once

   def __init__(self, name, pants_size, pants_calories):
      Food.__init__(self, name, pants_calories)
      Clothes.__init__(self, name, pants_size)


cheese_pants = ChessePants("Ultra sexy pants", "M", 500)
print(cheese_pants.calories)
print(cheese_pants.size)
cheese_pants.eat()
cheese_pants.wear()
print(cheese_pants.__dict__) 
# Note that 'name' isn't there twice
# Even though it is passed as an argument twice in the constructor



print("\n\nSECTION 3: Ducktyping\n-----------------")
# If it quacks it's a duck

class Duck:

   def make_sound(self):
      print("quack quack")

class NotADuck:

   def make_sound(self):
      print("quack quack")

a1 = Duck()
a2 = NotADuck()
a3 = Duck()

array = [a1,a2,a3]
for a in array:
   a.make_sound()
# Since they both have themethod make_sound() 
# it doesn't matter that they belong to different classes



