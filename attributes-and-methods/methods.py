## Instance Methods : These are the methods of the class that make use of "self" parameter to access and modify the instance attributes of the class.

class Employee:
  def employeeDetails(self):
    self.name = "Ben"
  
  @staticmethod
  def welcomeMessage():
    print("Welcome to the Organization")

employee = Employee()
employee.employeeDetails()
print(employee.name)
employee.welcomeMessage()

# static method do not take the default "self" parameter as argument

# We can differenciate instance method from static method by using a decorator @staticmethod
# Decorators are functions that takes other functions and extends their functionality (similar to HOC in react), they are denoted by starting them with @ symbol
# static method takes the function and extends its functionality and ignores binding of the obect , python understand the binding has been ignored and executes without any errors