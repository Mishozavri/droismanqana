#1
class Cat:
    def __init__(self, eat, talk, walk):
        self.eat = eat
        self.talk = talk
        self.walk = walk

    def eat(self):
        print(f"Cat eats {self.eat}")

    def talk(self):
        print(f"Cat says {self.talk}")

    def walk(self):
        print(f"Cat can run {self.walk}km/h")

class Dog:
    def __init__(self, eat, talk, walk):
        self.eat = eat
        self.talk = talk
        self.walk = walk

    def eat(self):
        print(f"Dog eats {self.eat}")

    def talk(self):
        print(f"Dog says {self.talk}")

    def walk(self):
        print(f"Dog can run {self.walk}km/h")

cat = Cat("milk", "miaww", 20)
dog = Dog("bone", "Aww", 40)

print(Cat.eat,)
print(Cat.talk)
print(Cat.walk)

print(Dog.eat)
print(Dog.talk)
print(Dog.walk)

