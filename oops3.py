class Emp:
    def putdata(self):
        self.id=int(input("Enter Emp id : "))
        self.name=input("Enter Emp Name: ")
        self.salary=float(input("Enter employee salary:  "))
    def display(self):
        print("Employee id:",self.id)
        print("Employee Name:",self.name)
        print("Employee Salary:",self.salary)
a=Emp()
a.putdata()
a.display()