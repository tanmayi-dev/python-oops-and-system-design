# Classes and Objects

- [Creating a Class and Object](#creating-class-and-object)
- [Questions](#questions)
- [Exercise](#exercise)

## Creating a Class and Object <a id="creating-class-and-object"></a>

```py

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

employeeOne.name # "Ben"

employeeOne.hasAchievedTarget() # "Target has been achieved"


employeeTwo = Employee() # new object

employeeTwo.name # "Ben"
```

## Basic Questions <a id="questions"></a>

### What is a class ?

A class is logical grouping of attributes (variables) and methods (functions).

**Syntax :**

```py
class ClassName:
  # class body
```

**Example :**

```py
class Employee:
  # class body
```

### What is an object ?

Object is an instance of a class that has access to all the attributes and methods of that class.

**Syntax :**

```py
objectName = ClassName()
```

**Example :**

```py
employee = Employee()
# The object employee now has access to all the attributes and methods of the class Employee.
# You will be learning more about attributes and methods in the next section.
```

### What is Object Instantiation ?

The process of creation of an object of a class is called instantiation

---

## Exercise - Classes and Objects <a id="exercise"></a>

### Define a class called "Employee" and create an instance of that class. Create an attribute called name and assign it with a value. Change the name you previously defined within a method and call this method by making use of the object you created.

```py

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

```
