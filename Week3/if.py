#Comparing values
#Operators
# >  - greater than
# <  - lesser than
# >= - greater than or equal to
# <= - less than or equal to
# == - equal to
# != - not equal to

a = 4
b = 5

if a == 0:
    print('a is equal to 0')
else:
    print('a is not equal to 0')

if a < b:
    print(a,'is less than',b)
    pass

#Comparing Strings
#Strings can be compared with !!, ==, !=, <, >, <=, >=
#<> etc compares ASCII value of each character
CAPS = 'ABC'
lowercase = 'abc'
if CAPS > lowercase:
    print(CAPS,'is greater than',lowercase)
else:
    print(lowercase,'is greater than',CAPS)

value1 = int(input('Enter first integer to compare: '))
value2 = int(input('Enter second integer to compare: '))
#BOOLEAN EXPRESSIONS - aka true/false
if value1 > value2:
    print(value1, 'is greater than', value2)
if value1 < value2:
    print(value2, 'is greater than', value1)
if value1 == value2:
    print(value1, 'is equal to', value2)

#Alternative decision structure - if the condition is met, this, else, this
if value1 > value2:
    print(value1, 'is greater than', value2)
else:
    print(value1, 'is not greater than', value2)

#We can also nest statements just my doing more indentation
if value1 != value2:
    print(value1, 'is not equal to', value2)
    if value1 > value2:
        print(value1, 'is greater than', value2)
    if value1 < value2:
        print(value2, 'is greater than', value1)
elif value1 == value2: #Else if
    print(value1, 'is equal to', value2)
else:
    print('error! values are caught by conditions')
