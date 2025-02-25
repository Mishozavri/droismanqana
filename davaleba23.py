class Bank_Account:
    def __init__(self, account_name, balance=0):
        self.__account_name = account_name
        self.__balance = balance

    @property
    def account_name(self):
        return self.__account_name

    @account_name.setter
    def account_name(self, name):
        self.__account_name = name

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited {amount} currency units into the account")
        else:
            print("The deposit amount must be a positive number")

    def withdraw(self, amount):
        if amount > self.__balance:
            print("Insufficient funds in the account")
        elif amount < 0:
            print("The withdrawal amount must be a positive number")
        else:
            self.__balance -= amount
            print(f"Withdrew {amount} currency units from the account")

    def display_balance(self):
        print(f"Account Holder: {self.__account_name}")
        print(f"Remaining Balance: {self.__balance} currency units")

account = Bank_Account("Giorgi Abashidze", 100)
account.display_balance()
account.deposit(200)
account.display_balance()
account.withdraw(300)
account.display_balance()
