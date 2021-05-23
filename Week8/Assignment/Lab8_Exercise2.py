#8.3 Date Printer
def getDate():
    return input('Please enter a date in mm/dd/yyyy format: ')

def getMonth(date):
    monthList = ['January', 'February', 'March',
                'April', 'May', 'June',
                'July', 'August', 'September',
                'October', 'November', 'December']
    dateSplit = date.split('/')
    monthNum = int(dateSplit[0])
    return str(monthList[monthNum-1])

def getDay(date):
    dateSplit = date.split('/')
    date = int(dateSplit[1])
    return str(date)

def getYear(date):
    dateSplit = date.split('/')
    year = int(dateSplit[2])
    return str(year)

def main():
    date = getDate()
    print(getMonth(date),getDay(date) + ',', getYear(date))

main()
