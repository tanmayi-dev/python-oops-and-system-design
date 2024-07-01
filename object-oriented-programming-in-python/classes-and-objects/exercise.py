## Exercise Solution

class Employee:
  # Define an attribute called name
  name = "Ben"

  def changeName(self):
    # Change the value of the attribute within a method
    Employee.name = "Mark" # self.name = "Mark" gives same result

employee = Employee()
print(employee.name) # Ben
employee.changeName()
print(employee.name) # Mark