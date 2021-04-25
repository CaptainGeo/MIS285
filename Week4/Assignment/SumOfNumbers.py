number = float(input('Please input a string of positive numbers to add: '))
sum = 0
while number >= 0:
    sum = sum + number
    number = float(input('Enter another number (or a negative number to exit): '))
print('The sum is:', sum)
