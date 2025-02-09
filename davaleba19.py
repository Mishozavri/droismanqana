class Animal:
    def __init__(self, color, name,):
        self.color = color
        self.name = name

    def say_hi(self):
        print(f"Hello my name is {self.name} with color {self.color} and i am an animal")

class Dog(Animal):
    def say_hi(self):
        print(f"Hello my name is {self.name} with color {self.color} and I am a Dog")


animal = Animal("Color of the pop", "geforce")
animal.say_hi()

dog = Dog("Max", "Black")
dog.say_hi()