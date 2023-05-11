class Employee:


    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def print_info(self):
        print(
            'Name: {} \nSalary: {}'.format(self.name, self.salary)
        )


emp_1 = Employee('Tom', 10000)
emp_2 = Employee('bob', 20000)
emp_1.print_info()
emp_2.print_info()