print("===== INFOSYS =====")


class Employee:
    employee_count = 0

    def __init__(self, name, age, employee_id, department, salary):
        self.name = name
        self.age = age
        self.employee_id = employee_id
        self.department = department
        self.salary = salary

        Employee.employee_count += 1

    def display(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Employee ID: {self.employee_id}")
        print(f"Department: {self.department}")
        print(f"Salary: {self.salary}")


class Manager(Employee):

    def __init__(self, name, age, employee_id, department, salary, team_size):
        super().__init__(name, age, employee_id, department, salary)
        self.team_size = team_size

    # Polymorphism
    def display_manager(self):
        self.display()
        print(f"Team Size: {self.team_size}")
        print()


class Developer(Employee):

    def __init__(self, name, age, employee_id, department, salary, programming_language):
        super().__init__(name, age, employee_id, department, salary)
        self.programming_language = programming_language

    # Polymorphism
    def display_developer(self):
        self.display()
        print(f"Programming Language: {self.programming_language}")
        print()


# Creating Manager objects
manager1 = Manager(
    'Yaswanth', 30, 1001, 'Management', 70000, 5
)

manager2 = Manager(
    'Jahnavi', 35, 1002, 'Management', 75000, 8
)


# Creating Developer objects
developer1 = Developer(
    'Jaswanth', 22, 1003, 'CSE', 50000, 'Python'
)

developer2 = Developer(
    'Charan', 23, 1004, 'CSD', 55000, 'Java'
)

developer3 = Developer(
    'Bharath', 22, 1005, 'CSE', 60000, 'JavaScript'
)


# Display Manager Details
print("\n----- MANAGER DETAILS -----")

manager1.display_manager()
manager2.display_manager()


# Display Developer Details
print("----- DEVELOPER DETAILS -----")

developer1.display_developer()
developer2.display_developer()
developer3.display_developer()


# Total Employees
print("Total Employees:", Employee.employee_count)
