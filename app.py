class Employee:

    raise_amount = 1.04
    num_of_employee = 0

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = f'{first}.{last}@mail.com'.lower()

        Employee.num_of_employee += 1

    def full_name(self):
        return "{} {}".format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)


emp1 = Employee("Test", "User", 50000)
emp2 = Employee("Another", "Instance", 60000)

# THIS IS CALLED INSTANCE VARIABLE
# print(emp1.full_name())

# THIS ONE IS CLASS VARIABLE
# print(Employee.full_name(emp1)) # this also works

print(emp2.pay)
emp2.apply_raise()
print(emp2.pay)

print(Employee.num_of_employee)

