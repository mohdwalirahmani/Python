class Employee:
    start_time = "9 AM"
    end_time = "5 PM"

class Teachers(Employee):
    def __init__(self,name, subject):
        self.name = name
        self.subject = subject

class Guest_Teacher(Teachers):
    def __init__(self,salary, name, subject):
        super().__init__(name, subject)                     # call parent class constructor
        self.salary = salary

emp1 = Guest_Teacher(40_000, "Arjun", "Maths")

print(emp1.name, emp1.subject, emp1.salary)