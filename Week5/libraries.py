#Libraries provide a lot of prebuild useful functions
#we import them with 'import <library>'
#We can also import our own 'modules' this way, referring to their filepath without the .py at the end
import random
import math
import myModule #This is the one we made

def showRandomNumber():
    number = myModule.getRandomNumber() #Calling our own function in a diff module
    print('Out number is', number)

def main():
    #There are a number of functions within random that are handy
    print(random.randrange(0, 101, 10)) #selects 0-100 counting by 10s
    print(random.random()) #if you don't pass anything in you get a float 0-.99
    print(random.uniform(0,10)) #returns a float within a range
    howmany = int(input('How many numbers do you want? '))
    for x in range(howmany):
        print(x,'/',howmany)
        showRandomNumber()

main()

#The math library allows us to do a lot too
number = 5
value = math.sqrt(number)
sideA = 3
sideB = 4
hypotnuse = math.hypot(sideA, sideB)
