books = int(input('Please input number of books purchased: '))
points = 0

if books < 2:
    points = 0
elif books < 4:
    points = 5
elif books < 6:
    points = 15
elif books < 8:
    points = 30
else:
    points = 60

print("This customer has earned", points, "points!")
