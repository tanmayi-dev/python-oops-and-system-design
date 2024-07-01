class Employee:
  numberOfWorkingHours = 40 # class attribute

employeeOne = Employee()
employeeTwo = Employee()

employeeOne.numberOfWorkingHours # 40
employeeTwo.numberOfWorkingHours # 40
Employee.numberOfWorkingHours = 45 # changing the class attribute
employeeOne.numberOfWorkingHours # 45
employeeTwo.numberOfWorkingHours # 45

# creating instance attribute

employeeOne.name = "John"
employeeOne.name # John

employeeTwo.name # attribute error
employeeTwo.name = "Mary"
employeeTwo.name # Mary

# changing the attribute using the object
employeeOne.numberOfWorkingHours = 40 # creates an instance attribute
employeeOne.numberOfWorkingHours # 40

employeeTwo.numberOfWorkingHours # 45 
# checks for instance attribute, and then checks for class attributes