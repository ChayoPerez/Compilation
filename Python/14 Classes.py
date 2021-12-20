print("SECTION 1: Simple Classes\n-----------------")


class Student:

   # static variable
   students = []

   # constructor
   def __init__(self, name, lastname, major, laptop_name, brand):
      self.name = name
      self.lastname = lastname
      self.major = major
      self.laptop = Student.Laptop(laptop_name, brand)
      Student.students.append(self) # How to get to static variables

   # instance method
   def introduce_yourself(self):
      print("Hello, my name is " + self.name + " and my laptop is called " + self.laptop.name)

   # Static method
   def list_students():
      for i in range(0, len(Student.students)):
         print(Student.students[i].name + " " + Student.students[i].lastname )

   # Inner class
   class Laptop:

      def __init__(self, name, brand):
         self.name = name
         self.brand = brand

s1 = Student("Andie", "Perez", "Software engineering", "Artemisa", "Mac")
s2 = Student("Chayo", "Chávez", "Plastic arts", "Persefone", "HP")

s1.introduce_yourself()
Student.list_students()

# You can use the inner class outside of the normal scope
laptop = Student.Laptop("Newton", "acer")
print(laptop.name)


print("\n\nSECTION 2: __name__\n-----------------")


class Clase0:
   pass

def funcion0():
   pass

string_0 = "pass!"
objeto_0 = Clase0()

print("1) " + Clase0.__name__)
print("2) " + funcion0.__name__)

try:
   print("3) " + string_0.__name__)
except Exception:
   print("3) variables don't have names")
try:
   print("4) " + objeto0.__name__)
except Exception:
   print("4) variables don't have names")


print("\n\nSECTION 3: Creating attributes\n-----------------")

class ObjectCreator:
   pass

dog = ObjectCreator
dog1 = dog()

dog2 = dog()
dog2.name = "Wafer"

print("Does dog1 get the attribute name?")
print(hasattr(dog1, "name"))
setattr(dog1, "name", "Wafer")
print("After setattr:")
print(hasattr(dog1, "name"))

print(type(dog2))

dog.legs = 4
print("Number of legs")
print(dog1.legs)


print("\n\nSECTION 4: Creating classes\n-----------------")

class Animal:

   def sing(self):
      print("La la la la")


def class_maker(class_name, attributes_list, superclass=None):
   attr_dict = {key: None for key in attributes_list}
   # the dictionary has the attributes for keys and 'None' as value
   if superclass:
      return type(class_name, (superclass,), attr_dict)
   else:
      return type(class_name, (), attr_dict)


def func():
   print("Hello!")

attributes = ["name", "lastname", "age", "introduce_self"]
Person = class_maker("Person", attributes, Animal)

p1 = Person()
print(p1.name)
p1.name = "Melisa"
print(p1.name)
p1.sing()
print("TYPE: " + str(type(p1))) # It's Person type!
p1.introduce_self = func
p1.introduce_self()