class Employee:
  name = "Ben"
  designation = "Sales Executive"
  salesMadeThisWeek = 6
  def hasAchievedTarget(self):
    if self.salesMadeThisWeek >= 5:
      print("Target has been achieved")
    else:
      print("Target has not been achieved")

employeeOne = Employee() # object instantiation

print(employeeOne.name) # Ben

employeeOne.hasAchievedTarget() # Target has been achieved

employeeTwo = Employee() # new object
print(employeeTwo.name) # Ben

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