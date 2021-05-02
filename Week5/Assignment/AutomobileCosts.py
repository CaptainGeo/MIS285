def main():
    loan = float(input('Please input your monthly loan payment ($): '))
    insurance = float(input('Please input your monthly insurance cost ($): '))
    gas = float(input('Please input your monthly gas cost ($): '))
    oil = float(input('Please input your monthly oil cost ($): '))
    tires = float(input('Please input your monthly tire cost ($): '))
    maintenance = float(input('Please input your monthly maintenance cost ($): '))
    totalMonthly = loan + insurance + gas + oil + tires + maintenance
    print('Your total monthly cost is: $',format(totalMonthly,'.2f'), sep = '')
    print('Your estimated annual cost is: $',format(totalMonthly*12,'.2f'), sep = '')

main()
