#10.1 Pet Class
class Pet:
    def __init__(self, name, type, age):
        self.__name = name
        self.__animal_type = type
        self.__age = age

    def setName(self, name):
        self.__name = name

    def setAnimalType(self, type):
        self.__animal_type = type

    def setAge(self, age):
        self.__age = age

    def getName(self):
        return self.__name

    def getAnimalType(self):
        return self.__animal_type

    def getAge(self):
        return self.__age

def main():
    name = input("Please enter the pet's name: ")
    type = input("Please enter the pet's type: ")
    age = input("Please enter the pet's age: ")

    pet = Pet(name,type,age)
    print(pet.getName(),'is a',pet.getAnimalType(),'that is',pet.getAge(),'years old.')

main()
