#GENERATE TEST FILE
def genTestFile():
    filename = 'numbers.txt'
    testfile = open(filename,'w')
    i=1
    print("Creating test file on",filename)
    while i < 20:
        print('Writing...',i)
        testfile.write(str(i)+'\n')
        i += 1
    testfile.close()

def main():
#    genTestFile()
    numbers = open('numbers.txt','r')
    fromFile = numbers.read()
    print(str(fromFile).rstrip('\n'))
    numbers.close()

main()
