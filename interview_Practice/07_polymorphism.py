class Employee:
    def get_designation(self):
        print("Designation = Employee")

class Teacher(Employee):
    def get_designation(self):
        print("Designation = Teacher")

emp1 = Teacher()
emp1.get_designation()              

# Method Overriding, although Teacher is a child class but still parent class wala method use nhi ho rha