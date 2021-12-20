from abc import ABCMeta, abstractmethod


"""
METACLASSES tips from the internet:
__new__ is called for the creation of a new class, 
while __init__ is called after the class is created, 
to perform additional initialization before the class is handed to the caller:

The primary difference is that when overriding __new__() 
you can change things like the ‘name’, ‘bases’ and ‘namespace’ arguments
before you call the super constructor and it will have an effect, 
but doing the same thing in __init__() you won’t get any results from the constructor call.

In many cases, the choice of __new__() vs __init__() is a style issue and doesn’t matter, 
but because __new__() can do everything and __init__() is slightly more limited, 
some people just start using __new__() and stick with it. 
This use can be confusing – 
I tend to hunt for the reason that __init__() has been chosen, 
and if I can’t find it wonder whether the author knew what they were doing. 
I prefer to only use __new__() when it has meaning – 
when you must in order to change things that only __new__() can change.

"""

print("SECTION 1: Basic concept\n-----------------")

class Animal (metaclass=ABCMeta):

    def __new__(cls, *args, **kwargs):
        return super().__new__(cls)

    def __init__(self, name, sex):
        self.name = name
        self.sex = sex

    @abstractmethod
    def eat(self):
        pass

    @abstractmethod
    def play(self):
        pass

class Dog (Animal):

    eating_sound = "Nomnomnonm"
    play_sound = "Bark! BarK!"

    def eat(self):
        print(Dog.eating_sound)

    def play(self):
        print(Dog.play_sound)


dog = Dog("Wafer", "M")
dog.eat()
dog.play()

try:
    animal = Animal("Apolo", "M")
except:
    print("As you see, you can't make instances of a metaclass")



print("SECTION 2: Using __new__ and __init__\n-----------------")


class Animal2 (metaclass=ABCMeta):

    def __new__(cls, *args, **kwargs): 
        # Here you can alter the class itself that inherits from Animal2

        def sleep():
            print("zzZzZZzzZ")

        setattr(cls, "sleep", sleep) # Static method added to the new class

        return super().__new__(cls) # You MUST return this line

    def __init__(self, name, sex):
        self.name = name
        self.sex = sex

        # Here on the other hand, cry is added to each instance that inherits from Animal2
        def cry():
            print("*whining*")

        self.cry = cry

    @abstractmethod
    def eat(self):
        pass

    @abstractmethod
    def play(self):
        pass

class Dog (Animal2):

    eating_sound = "Nomnomnonm"
    play_sound = "Bark! BarK!"

    def eat(self):
        print(Dog.eating_sound)

    def play(self):
        print(Dog.play_sound)


dog = Dog("Wafer", "M")
dog.eat()
dog.play()

# Added in __new__ to the whole class
Dog.sleep()

# Added in __init__ to a single instance
dog.cry()


"""
As you can see here, both cry's are different.
You are wasting memory by making a 'cry' for each instance of Dog
"""
dog2 = Dog("Bells", "F")
dog2.cry()

print(id(dog.cry))
print(id(dog2.cry))




"""
You can have abstract classes with non-abstract methods
You can have non abstract classes with abstract methods

If what you wanted to make were instances of different races of dogs
Say, Pitbull, then it would be:

Animal(metaclass=ABCMeta)
Dog(Animal, metaclass=ABCMeta)
Pitbul(Dog)

So you can't have Dog variables, only specific races 


"""
