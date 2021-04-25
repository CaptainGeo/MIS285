budget = float(input("Please input the amount budgeted for the month: "))
total = 0
addmore = 'y'

while addmore == 'y' or addmore == 'yes':
    expense = float(input('Add an expense: '))
    total += expense
    addmore = input('Do you have more to add? (y/n) ').lower()

if total <= budget:
    print('You are',format(budget - total,'.2f'),'dollars under budget.')

if total > budget:
    print('You are',format(total - budget,'.2f'),'dollars over budget.')
