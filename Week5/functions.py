#Functions allow us to create modules of code that we can run multiple times from lots of places in our program

#Defining a function must start with 'def'
#Names have to start with a-z, A-Z, and may contain letters and underscores
def message():
    print('I am Arthur,')
    print('King of the Britons.')

#Calling a method like this
message()

#We can also use local variables, limited in scope to this function
def birds():
    birdCount = 5000
    print('California has',birdCount,'birds.')

birds()

#Arguments are variables which are passed into a function
def howmanybirds(number):
    print('There are', number, 'birds.')

howmanybirds(8000)

#We can pass in multiple values with multiple variables
def showsum(num1, num2):
    print('The sum equals',num1+num2)

showsum(5000, 8000)

#Functions can access global variables too
value = 6
def showvalue():
    print(value)

showvalue()

#We can also return data via a function
def getvalue():
    value = 6
    return value #All we need is this return

print('Value from getvalue =', getvalue())
