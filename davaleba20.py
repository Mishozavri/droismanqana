#1
class People:
    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname

    def get_email(self):
        return f"{self.firstname}, {self.lastname}.mshobeli@gmail.com"

    class Lecturer(people):
        def __init__(self, firstname, lastname, salay):
            super().__init__(firstname, lastname)

            self.salay = salay

    def get_email(self):
        return f"{self.firstname}, {self.lastname}, {self.salay}.@svili1@gmail.com"

    class Student(people):
        def __init__(self, firstname, lastname, courses):
            super().__init__(firstname, lastname)

            self.courses = courses

        def get_email(self):
            return f"{self.firstname}, {self.lastname}, {self.courses}.shvili2@gmail.com"

lecturer = Lecturer("misho", "abu", 5000)
student = Student("gio", "abu", ["Math", "Physics"])

print(lecturer.get_email())
print(student.get_email())

#2
class LibraryItem:
    def __init__(self, title, status="available"):
        self.title = title
        self.status = status

    def booking(self):
        if self.status = "available":
            self.status = "occupied"
            return f"{self.title} has been booked."
        return f"{self.title} is already occupied."

class Book(LibraryItem):
    def __init__(self, title, authors, ISBN, status="available"):
        super().__init__(title, status)
        self.authors = authors
        self.ISBN = ISBN

class Magazine(LibraryItem):
    def __init__(self, title, journalName, volume, status="available"):
        super().__init__(title, status)
        self.journalName = journalName
        self.volume = volume

class CD(LibraryItem):
    def __init__(self, title, status="available"):
        super().__init__(title, status)

book = Book("Python junior", "Author Name", "123456")
cd = CD("classic Music")

print(book.booking())
print(cd.booking())

#3
class Contacts:
    def __init__(self, name, phone):
        self.name = name
        self.phone = phone

class Mail_Sender:
    def send_mail(self, email):
        print(f"ტექსტი ჩემი გაგზავნა ამ მისამართზე: {email}")

class Friend(Contacts, Mail_Sender):
    def __init__(self, name, phone, email):
        super().__init__(name, phone)

        self.email = email

class Family(Contacts, Mail_Sender):
    def __init__(self, name, phone, email, birthdate):
        super().__init__(name, phone)

        self.email = email
        self.birthdate = birthdate

friend = Friend("saba", "112", "saba.artkmeladze@mziuri.ge")
family = Family("Nino", "911", "nino@deda@gmail.com", "07/09/1976")

friend.send_mail(friend.email)
family.send_mail(family.email)


