class Employee:
    start_time = "9 AM"
    end_time = "5 PM"

    def change_time(self, new_time):
        self.end_time = new_time

class Teachers(Employee):
    def __init__(self,name, subject):
        self.name = name
        self.subject = subject

class Staffs (Employee):
    def __init__(self, name, role):
        self.name = name
        self.role = role

emp1 = Teachers("Wali", "Maths")
emp2 = Staffs("kk", "Manager")
emp2.change_time("6 PM")

print (emp1.name, emp1.subject, emp1.start_time, emp1.end_time)
print (emp2.name, emp2.role, emp2.start_time, emp2.end_time)