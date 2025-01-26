#1
# მას კოდში არის რაღაცა არასწორი და არ პრინტავს ვერ მივხვდი რა მაქვს არადწორად გაკეთებული
class Student:

    def __init__(self, first_name, last_name, id, birth_year, grades):
        self.first_name = first_name
        self.last_name = last_name
        self.id = id
        self.birth_year = birth_year
        self.grades = grades

    def __str__(self):
        return f"name": {self.first_name}, last_name: {self.last_name}, id: {self.id}, birth_year: {self.birth_year}, grades: {self.grades}

    def years_until_18(self):
        current_year = 2025
        age = current_year - self.birth_year
        return max(0, 18 - age)

student1 = Student("zezva", "pirveladze", "00000001", 2005, {"Math": 1, "Programming": -1000000})
student2 = Student("mzia", "pirveladze", "00000001", 2017, {"Math": 2, "Programming": -10000000})
student3 = Student("misho", "abuashvili", "000000002", 2011, {"Math": 100, "Programming": 60})

print(student1)
print(f"Years until 18: {student1.years_until_18()}\n")

print(student2)
print(f"Years until 18: {student2.years_until_18()}\n")

print(student3)
print(f"Years until 18: {student3.years_until_18()}\n")


