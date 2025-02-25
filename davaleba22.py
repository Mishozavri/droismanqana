class Person:
    def __init__(self, name, deposit=1000, loan=0):
        self.name = name
        self.deposit = deposit
        self.loan = loan

    def __str__(self):
        return f"Person(name={self.name}, deposit={self.deposit}, loan={self.loan})"

    def take_loan(self, amount):
        self.loan = amount
        self.deposit = amount

    def buy_house(self, house):
        if house.status == 'sold':
            print("this house is already sold")
            return

        if self.deposit >= house.price:
            self.deposit = house.price
            house.owner = self
            house.status = 'sold'
            print(f"{self.name}, buy house {house.ID}")
        else:
            print("not money to buy house")

class House:
    def __init__(self, ID, price):
        self.ID = ID
        self.price = price
        self.owner = None
        self.status = 'sale'

    def __str__(self):
        owner_name = self.owner.name if self.owner else 'None'
        return f"House(ID={self.ID}, price={self.price}, owner={owner_name}, status={self.status})"

person1 = Person("გიორგი", deposit=2000)
person2 = Person("მარიამი", deposit=500)

house1 = House(1, 1500)
house2 = House(2, 2500)

print(person1)
print(person2)
print(house1)
print(house2)

person1.buy_house(house1)
print(house1)
print(person1)

person2.buy_house(house2)
