from abc import ABC, abstractmethod

class Animal(ABC):                          # Abstract Class
    @abstractmethod
    def make_sound(self):                       # Abstract Method
        pass

class Dog(Animal):
    def make_sound(self):
        print("Bow!")

class Cat(Animal):
    def make_sound(self):
        print("Meau!")

dog = Dog()
dog.make_sound()
cat = Cat()
cat.make_sound()