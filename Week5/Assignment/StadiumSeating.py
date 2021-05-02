def getSeats(numOfSeats, seatClass):
    if seatClass == 'A':
        return numOfSeats * 20
    if seatClass == 'B':
        return numOfSeats * 15
    if seatClass == 'C':
        return numOfSeats * 10
    else:
        print('ERROR: INVALID SEAT CLASS')

def main():
    a = int(input('How many class A seats do you want?: '))
    b = int(input('How many class B seats do you want?: '))
    c = int(input('How many class C seats do you want?: '))

    totalCost = getSeats(a,'A') + getSeats(b,'B') + getSeats(c,'C')
    print('Your total cost is: $',format(totalCost,'.2f'),sep = '')

main()
