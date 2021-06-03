#10.3 Personal Information Class
class Person:
    def __init__(self, name, address, age, phone):
        self.__name = name
        self.__address = address
        self.__age = age
        self.__phone = phone

    def getName(self):
        return self.__name

    def getAddress(self):
        return self.__address

    def getAge(self):
        return self.__age

    def getPhone(self):
        return self.__phone

    def setName(self, name):
        self.__name = name

    def setAddress(self, address):
        self.__address = address

    def setAge(self, age):
        self.__age = age

    def setPhone(self, phone):
        self.__phone = phone

    def __str__(self):
        return self.__name + ', '+ str(self.__age) + '\n' + self.__address + ' \n' + self.__phone

def main():
    me = Person('A. H.', '9739 NE Stephenson St., Portland OR', 22, '503-975-3084')
    friend1 = Person('Ben McHenry', '28720 NW Poplar Rd., Portland OR', 21, '971-555-1038')
    friend2 = Person('Matthew Traff', '909 SW Alameda Dr., Portland OR', 22, '971-222-0234')

    print(me)
    print(friend1)
    print(friend2)

main()
