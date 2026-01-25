class Employee:
    # class variables
    company_name = 'ABC Company'

    # constructor to initialize the object
    def __init__(self, name, salary):
        # instance variables
        self.name = name
        self.__salary = salary

    # instance method
    def show(self):
        print('Employee:', self.name, self.__salary, self.company_name)

# create first object
emp1 = Employee("Harry", 12000)
emp1.show()

#this will reflect only for emp1 instance not other instance of Employee class
emp1.company_name = 'XYZ Company'  # change class variable value
# this will change the class variable for all instances of Employee class
Employee.company_name = 'XYZ Company'  # change class variable value

# add new instance variable 'marks' to stud
emp1.address = "123 Main St";

# can't access private variable directly,  emp1.__salary  # This will raise an AttributeError
# Instead, we can access it through a public method
#print(emp1.name, emp1.__salary, emp1.company_name) 
print(emp1.name, ":", emp1.company_name, ":", emp1.address) 

# create second object
emp2 = Employee("Emma", 10000)
emp2.show()

# Use the __dict__ function of an object to get all instance variables along with their value.
print('Instance variable object has')
print(emp2.__dict__); #{'name': 'Emma', '_Employee__salary': 10000}