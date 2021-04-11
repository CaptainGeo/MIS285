males = int(input("How many males are in the class? "))
females = int(input("How many females are in the class? "))

total = males+females

print('There are ', format(males/total*100,'.2f'),'% males in the class.', sep='')
print('There are ', format(females/total*100,'.2f'),'% females in the class.', sep='')
