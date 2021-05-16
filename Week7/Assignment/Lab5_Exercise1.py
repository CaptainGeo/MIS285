#7.3 Rainfall Statistics
def getList():
    month = 1
    rainfall = []
    while month <=12:
        try:
            monthstring = "Please enter rainfall statistic for month " + str(month) +": "
            data = float(input(monthstring))
            rainfall.append(data)
            month += 1
        except ValueError as err:
            print('Value Error:', err)
            print("Please try again. Be sure to input a number.")
    return rainfall

def main():
    rainfall = getList()
    total = 0
    for x in rainfall:
        total += x
    print("Total Rainfall =", total)
    average = total/12
    print("Average Rainfall =", average)
    maxvalue = max(rainfall)
    maxmonth = rainfall.index(maxvalue) + 1
    print("Wettest month was month", maxmonth, "with",maxvalue, "rain.")
    minvalue = min(rainfall)
    minmonth = rainfall.index(minvalue) + 1
    print("Dryest month was month", minmonth, "with", minvalue, "rain.")


main()
