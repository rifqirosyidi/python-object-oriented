# SIMPLE EXAMPLE OF PROPERTY DECORATOR - GETTER, SETTER AND DELETER


class Employee:

    def __init__(self, first, last):
        self.first = first
        self.last = last

    @property
    def email(self):
        return "{}.{}@mail.com".format(self.first, self.last).lower()

    @property
    def fullname(self):
        return "{} {}".format(self.first, self.last)

    # SETTER
    @fullname.setter
    def fullname(self, name):
        first, last = name.split(" ")
        self.first = first
        self.last = last

    # SETTER
    @fullname.setter
    def fullname(self, name):
        first, last = name.split(" ")
        self.first = first
        self.last = last

    @fullname.deleter
    def fullname(self):
        print("Deleted Name")
        self.first = None
        self.last = None


emp1 = Employee("Eric", "Smith")

emp1.first = 'Jim'
emp1.fullname = "Rief Rief"

print(emp1.first)
print(emp1.fullname)
print(emp1.email)

