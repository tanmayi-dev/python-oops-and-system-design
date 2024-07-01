# Attributes and Methods

- [Instance Attributes and Class attributes](#instance-attributes)
- [Understanding the 'self' parameter](#self-parameter)
- [Static Methods and Instance Methods](#static-methods-and-instance-methods)
- [init() method - create a fully initialised object](#init-method)
- [Questions](#questions)
- [Exercise](#exercise)

## Instance Attributes and Class Attributes <a id="instance-attributes"></a>

- [Code](./class-and-instance-attributes.py)

```py
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
```

---

## Understanding the 'self' parameter <a id="self-parameter"></a>

- [Code](./self.py)

```py
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
```

---

## Static Methods and Instance Methods <a id="static-methods-and-instance-methods"></a>

- [Code](./methods.py)

- Instance Methods : These are the methods of the class that make use of "self" parameter to access and modify the instance attributes of the class.

```py
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
```

- static method do not take the default "self" parameter as argument

- We can differenciate instance method from static method by using a decorator @staticmethod

- Decorators are functions that takes other functions and extends their functionality (similar to HOC in react), they are denoted by starting them with @ symbol

- static method takes the function and extends its functionality and ignores binding of the obect , python understand the binding has been ignored and executes without any errors

---

## init() method - Create a fully initialised object <a id="init-method"></a>

- [Code](./init.py)

## Questions <a id="questions"></a>

## Exercise <a id="exercise"></a>
