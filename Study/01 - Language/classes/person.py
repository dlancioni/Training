import os

class Person:

    # Class documentation goes here
    ''' Use __doc__ to get above value '''

    # Private members
    __salary = 100.99

    # Public members
    fullName = ""

    # Constructor
    def __init__(self, firstName = "", lastName = ""):
        print(self.__class__.__name__, " initialized")
        self.firstName = firstName
        self.lastName = lastName
        self.fullName = self.firstName + " " + self.lastName

    # Destructor
    def __del__(self):
        print(self.__class__.__name__, " destroyed")

    # Methods
    def getSalary(self):
        return self.__salary

    def getFullName(self):
        return self.fullName


class Customer(Person):

    # Class documentation goes here
    ''' Use __doc__ to get above value '''

    # Constructor
    def __init__(self, firstName = "", lastName = ""):
        super().__init__(firstName, lastName)

    # Methods with same name are not allowed, consider using * param
    def calculate(self, *args):

        if len(args) == 2:
            if isinstance(args[0], int) and isinstance(args[1], int):
                return args[0] + args[1]

        if len(args) == 3:
            return args[0] + args[1] + args[2]
 



###############################################################
# Clear console
os.system("cls")

# Print class related info
p1 = Customer("David", "Lancioni")

#print(p1.__dict__)              # Class to json
#print(p1.__doc__)               # Class documentation
#print(p1.__module__)            # Class module
#print(p1.__class__.__name__)    # Class name
#print(p1.getFullName())
#print(p1.getSalary())
#print(p1.calculate(1, 1))
#print(p1.calculate(1, 1, 1))


#########################################################
# Overriding: Just write method with same name (...)

class Parent:        # define parent class
   def myMethod(self):
      print('Calling parent method')

class Child(Parent): # define child class
   def myMethod(self):
      print('Calling child method')

c = Child()
c.myMethod()
c.sup