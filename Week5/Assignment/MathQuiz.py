import random

max = 1000

def showQuestion():
    varA = random.randrange(0, max)
    varB = random.randrange(0, max)
    print('\t    ', varA, sep = '')
    print('\t+   ', varB, sep = '')
    print('________________')
    correct = varA + varB
    answer = int(input('\t    '))
    if answer == correct:
        print('Congratulations! You are correct!')
    else:
        print('Oops, that was incorrect. The correct answer was:', correct, '\nBetter luck next time!')

def main():
    print('Welcome to the math quiz! Solve problem below.')
    again = 'y'
    while again == 'y' or again == 'yes':
        showQuestion()
        again = input('Do you want to go again? (y/n) ').lower()

main()
