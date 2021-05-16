#7.6 Larger than n
def largerThanN(input, n):
    print(input)
    largerList = []
    for x in input:
        if x > n:
            print(x)
            largerList.append(x)
    print('Numbers larger than',str(n),'=')
    print(largerList)

def main():
    testlist = [1,2,3,4,5,6,7,8,9,10,20,30,40,50,60,70,80,90,100,200,300,400,500,600,700,800,900,1000]
    testn = 14
    largerThanN(testlist, testn)

main()
