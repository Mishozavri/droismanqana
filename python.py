class Rectangle:
    def __init__(self, width, length, color):
        self.width = width
        self.length = length
        self.color = color

    def perimeter(self):
        result = (self.width + self.length) + (self.width + self.length)
        return result

    def area(self):
        result = 0
        count = self.length
        while count > 0:
            result += self.width
            count -= 1

    def __str__(self):
        return f"Rectangle(width={self.width}, length={self.length}, color={self.color})"


# Creating objects
obj1 = Rectangle(1, 5, "blue")
obj2 = Rectangle(3, 3, "green")
obj3 = Rectangle(3, 7, "purple")

# Printing the results
print(obj1)
print(f"Perimeter: {obj1.perimeter()}, Area: {obj1.area()}\n")

print(obj2)
print(f"Perimeter: {obj2.perimeter()}, Area: {obj2.area()}\n")

print(obj3)
print(f"Perimeter: {obj3.perimeter()}, Area: {obj3.area()}\n")