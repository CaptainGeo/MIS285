weight = float(input("Please input package weight in lbs: "))
charge = 0

#2lbs or less
if weight < 2:
    charge = weight * 1.5
#over 2lbs but not more than 6lbs
elif weight <= 6:
    charge = weight * 3
#over 6lbs but not more than 10lbs
elif weight <= 10:
    charge = weight * 4
else:
    charge = weight * 4.75

print("Total shipping charge = $", charge, ".", sep="")
