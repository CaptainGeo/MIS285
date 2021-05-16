#7.12 Prime Number Generation
def getPrimes(inputList):
    primeList = []
    for x in inputList:
        if isPrime(x):
            primeList.append(x)
    return primeList

def isPrime(n):
    i = 2
    while i < n:
        if n%i == 0:
            #print(n, 'is not prime.')
            return 0
        else:
            i += 1
    #print(n, 'is prime.')
    return 1

def getList(limit):
    list = []
    i = 2
    while i <= limit:
        list.append(i)
        i += 1
    return list

def main():
    inLimit = int(input('Please enter an upper limit integer: '))
    lowerList = getList(inLimit)
    piList = getPrimes(lowerList)
    outString = 'Prime numbers no greater than ' + str(inLimit) + ' = '
    for x in piList:
        outString += (str(x) + ', ')
    outString = outString.rstrip(', ')
    print(outString)

main()
