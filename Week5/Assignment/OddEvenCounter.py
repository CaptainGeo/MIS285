import random

def isEven(num):
    if num%2 == 0:
        return 1
    if num%2 == 1:
        return 0
    else:
        print('ERROR - unable to determine odd or even')

def getRandomNumber():
    return random.randint(0,1000)

def main():
    totalEven = 0
    totalOdd = 0
    totalRuns = 0
    for x in range(100):
        num = getRandomNumber()
        if isEven(num):
            totalEven += 1
            print(num, 'is even. Total evens = \t', totalEven)
        else:
            totalOdd += 1
            print(num, 'is odd. Total odds = \t', totalOdd)
        totalRuns += 1
    print('Total Even =\t',totalEven)
    print('Total Odd =\t',totalOdd)
    print('Total Runs =\t',totalRuns)

main()
