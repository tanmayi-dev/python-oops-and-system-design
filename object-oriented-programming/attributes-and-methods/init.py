class Employee:
  def enterEmployeeDetails(self):
    self.name = "Mark"
  
  def displayEmployeeDetails(self):
    print(self.name)

employee = Employee()
employee.displayEmployeeDetails() # calling the second method before the first one which initializes the data
# AttributeError: 'Employee' object has no attribute 'name'

# Since initialization happens in the first method, which was not called, we see attribute error when calling second method (displayEmployeeDetails)
# We need to have a mechanism, in which we can initialize all the attributes of our objects or of our class before they are being used
# We can do this by using init method which is similar to constructor in java or c++


class Employee1:
  def __init__(self):
    self.name = name
  
  def displayEmployeeDetails(self):
    print(self.name)

employee = Employee()
employee.displayEmployeeDetails() 