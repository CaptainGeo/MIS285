def getFileName():
    name = 'numbers.txt'
    return name

def main():
    name = getFileName()
    inputFile = open(name,'r')
    i = 0
    line = inputFile.readline()
    total = 0
    while line != '':
        i += 1
        print('Grabbing number',str(i) + ':',int(line.rstrip('\n')))
        total += int(line)
        print(total)
        line = inputFile.readline()
    inputFile.close()
    average = total/i
    print('AVERAGE =',format(average,'.2f'))
    
main()
