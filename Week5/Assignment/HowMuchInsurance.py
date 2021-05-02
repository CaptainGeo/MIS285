def getValue():
    costOfStructure = int(input('Please input total replacement cost of the structure($): '))
    return costOfStructure

def main():
    totalCost = 0
    addmore = 'y'
    while addmore == 'y' or addmore == 'yes':
        totalCost += getValue()
        addmore = input('Do you have more to add? (y/n) ').lower()
    insuranceAmount = totalCost * .8
    print('You should insure the property for at least $',insuranceAmount, sep = '')

main()
