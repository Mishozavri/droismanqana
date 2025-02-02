import math

class Triangle:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def get_perimeter(self):
        return self.a + self.b + self.c

    def get_area(self):
        s = self.get_perimeter() / 2
        return math.sqrt(s * (s-self.a) * (s-self.b) * (s-self.c))

    def get_sides(self):
        return self.a, self.b, self.c


triangle = Triangle(3, 4, 5)
print("Sides:", triangle.get_sides())
print("Perimeter:", triangle.get_perimeter())
print("Area:", triangle.get_area())