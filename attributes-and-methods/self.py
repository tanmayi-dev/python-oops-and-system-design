class Employee:
  def employeeDetails(self):
    self.name = "Matthew"
    print("Name : ", self.name)
    age = 30 # no error
    print("Age :", age)

  def printEmployeeDetails(self):
    print("Printing in another method")
    print("Name: ", self.name)
    print("Age: ", age) # NameError: name 'age' is not defined

employee = Employee()

# if self is not passed to the function inside the function in Employee Class
# Error : TypeError: Employee.employeeDetails() takes 0 positional arguments but 1 was given
employee.employeeDetails() # this is short hand for Employee.employeeDetails(employee)
# Employee.employeeDetails(employee)


employee.printEmployeeDetails()
# this function shows erro : NameError: name 'age' is not defined
# Since we did not use the name of the object when creating age attribute
# Life span of age is just inside the employeeDetails() method of the Employee class and is not available in other methods

# NOTE: To create instance attribute, we have to use the name of the object
# We did not use object name to create age, so its available only in the employeeDetails() method

# What if my method does not need self parameter ? If I do not use the instance attributes in the function, then should we still pass self method ?
# Answer: use static methods and not instance methods
