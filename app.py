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

    def __repr__(self):
        return "Employee('{}', '{}', '{}')".format(self.first, self.last, self.email)

    def __str__(self):
        return "{} - {}".format(self.full_name(), self.email)

    def __add__(self, other):
        return self.pay + other.pay

    def __len__(self):
        return len(self.full_name())

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


# =============================================
# ============== INHERITANCE ==================
# =============================================


class Developer(Employee):
    raise_amount = 1.10

    def __init__(self, first, last, pay, prog_lang):
        super().__init__(first, last, pay)
        self.prog_lang = prog_lang


class Manager(Employee):

    def __init__(self, first, last, pay, employees=None):
        super().__init__(first, last, pay)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees

    def add_emp(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)

    def remove_emp(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)

    def print_emps(self):
        for emp in self.employees:
            print("-> ", emp.full_name())


# emp1 = Employee("Test", "User", 50000)
# emp2 = Employee("Another", "Instance", 60000)

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
#
# emp_str_4 = "John-Doe-60000"
# emp_str_5 = "Another-User-50000"
# emp_str_6 = "User-Three-30000"
#
# emp4 = Employee.from_string(emp_str_4)
# print(emp4.first)
#
# my_date = datetime.date(2019, 8, 2)
# print(Employee.is_workday(my_date))


dev1 = Developer("Rifqi", "Ros", 90000, "Java")
dev2 = Developer("Neuron", "Sie", 90000, "Python")
# print(dev1.email, dev1.prog_lang)
# print(dev2.email, dev2.prog_lang)

mg1 = Manager("Test", "Manager", 10000, [dev1])
print(mg1.email)
mg1.add_emp(dev2)  # Add Employees
mg1.remove_emp(dev1)  # Remove Employees
mg1.print_emps()  # List Employees

# CHECK AN INSTANCE
# print(isinstance(mg1, Manager))  # true
# print(isinstance(mg1, Employee))  # true
# print(isinstance(mg1, Developer))  # false

# CHECK A SUB CLASS
# print(issubclass(Manager, Employee))  # true
# print(issubclass(Developer, Employee))  # true
# print(issubclass(Developer, Manager))  # false

# print(repr(mg1))
# print(str(mg1))

# print(mg1.__repr__())
# print(mg1.__str__())

# Dunder Add
# print((dev1 + dev2))

# Dunder Len
# print(len(mg1))

