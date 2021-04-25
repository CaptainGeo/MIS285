weight = float(input('Please input the starting weight: '))
month = 1
rate = 4

print('Month:','Expected Weight:',sep = '\t')
while month <= 6:
    weight = weight - rate
    print(month,weight,sep = '\t')
    month += 1
