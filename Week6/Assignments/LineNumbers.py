def getFileName():
    name = input('Please input filename: ')
    return name

def main():
    name = getFileName()
    inputFile = open(name,'r')
    i = 1
    line = inputFile.readline()
    while line != '':
        print(str(i) + ':',line.rstrip('\n'))
        line = inputFile.readline()
        i += 1
    inputFile.close()

main()
