def getFileName():
    name = 'numbers.txt'
    return name

def main():
    try:
        name = getFileName()
        inputFile = open(name,'r')
        i = 0
        line = inputFile.readline()
        total = 0
        while line != '':
            i += 1
            try:
                print('Grabbing number',str(i) + ':',int(line.rstrip('\n')))
                total += int(line)
            except ValueError as err:
                print('Value Error:', err)
            print(total)
            line = inputFile.readline()
            average = total/i
        print('AVERAGE =',format(average,'.2f'))
        inputFile.close()
    except IOError as err:
        print('IO ERROR:',err)

main()
