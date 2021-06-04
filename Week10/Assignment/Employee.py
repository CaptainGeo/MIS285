class Employee:
    def __init__(self, name, ID, department, job):
        self.__name = name
        self.__id = ID
        self.__dept = department
        self.__job = job

    def getName(self):
        return self.__name

    def getID(self):
        return self.__id

    def getDept(self):
        return self.__dept

    def getJob(self):
        return self.__job

    def setName(self, name):
        self.__name = name

    def setID(self, id):
        self.__id = id

    def setDept(self, department):
        self.__dept = department

    def setJob(self, job):
        self.__job = job

    def __str__(self):
        return self.__name + ', #'+ str(self.__id) + ', ' + self.__dept + ', ' + self.__job
