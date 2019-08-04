import datetime


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

    @classmethod
    def set_amount(cls, amount):
        cls.raise_amount = amount

    @classmethod
    def from_string(cls, emp_str):
        first, last, pay = emp_str.split('-')
        return cls(first, last, pay)

    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True


emp1 = Employee("Test", "User", 50000)
emp2 = Employee("Another", "Instance", 60000)

# THIS IS CALLED INSTANCE VARIABLE
# print(emp1.full_name())

# THIS ONE IS CLASS VARIABLE
# print(Employee.full_name(emp1)) # this also works

# CLASS METHOD
# Employee.set_amount(1.05)
#
# print(Employee.raise_amount)
# print(emp1.raise_amount)
# print(emp2.raise_amount)
#
# print(Employee.num_of_employee)

emp_str_4 = "John-Doe-60000"
emp_str_5 = "Another-User-50000"
emp_str_6 = "User-Three-30000"

emp4 = Employee.from_string(emp_str_4)
print(emp4.first)

my_date = datetime.date(2019, 8, 2)
print(Employee.is_workday(my_date))
