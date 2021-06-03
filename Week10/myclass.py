#Classes can be stored in modules (.py files) and imported like any other module

class Employee:
    def __init__(self, name, dept, job):
        self.__name = name
        self.__dept = dept
        self.__job = job

    #Mutator Methods: store or change a data attribute
    def setName(self, name):
        self.__name = name

    #Accessor Methods: return a value from the class' attributes w/o changing it
    def getName(self):
        return self.__name
        
    def getString(self):
        out = self.__name + ' is a ' + self.__job + ' in the ' + self.__dept + ' department.'
        return out
