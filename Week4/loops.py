#while loops
print('While Loop:')
i = 1
while i < 6:
    print(i)
    i += 1

#In this case we can use use 3 as a 'Sentinel' - when we see that value in the loop we know to stop
print('While Break:')
i = 1
while i < 6:
    print(i)
    i += 1
    if i == 3:
        break
print('Stopped at 3')

print('While else loop:')
i = 1
while i < 6:
    print(i)
    i += 1
else:
    print('6 or more')


#For loops
for num in [1,2,3,4,5,6]:
    print('Num in for loop:', num)

cars = ["honda","hyundai","ford"]
for x in cars:
    print("I drive a",x)

for num in range(6):
    print(num, "in range.")

for rangeval in range(2,6):
    print(rangeval, "in range.")

#We can also skip through a loop with 'pass', and it does nothing
for x in range(6):
    pass
