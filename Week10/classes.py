#Object oriented programming: Focused on creating objects
#Object: entity that contains data and code (data = data attributes and procedures = methods)
#Encapsulation: combining data and code into a single object
#Data Hiding: object's data attributes are hidden from code outside the object, access restricted to the object's methods
#Object Reusability: same object can be used by different programs

import myclass

class NewClass:
    def __init__(self, name, pvtName, dept, job):
        self.name = name
        self.dept = dept
        self.job = job
        self.__privateName = pvtName #self.___name makes the attribute private

    def getPrivateName(self):
        return self.__privateName

    def getName(self):
        return self.name

    def setName(self, name):
        self.name = name

#We can pass classes (or lists of classes) as arguments
def printEmployees(employees):
    for x in employees:
        print(x.getString())

employee = NewClass('James Robinson','Jim','Materials','Senior Researcher')

print(employee.name)
employee.setName('Jim Robinson')
print(employee.getName(),'aka',employee.getPrivateName())

#We can access imported classes the same way
otherEmployee = myclass.Employee('John Lennon', 'Music','Pianist')
print(otherEmployee.getString())
print(otherEmployee) #printing a class object automatically calls the .__str__() method
print(otherEmployee.__str__())
yetAnotherEmployee = myclass.Employee('Jaco Pastorius','Music','Bassist')
print(yetAnotherEmployee.getString())

employees = {otherEmployee, yetAnotherEmployee}

printEmployees(employees)
