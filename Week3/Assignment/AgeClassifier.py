age = float(input('Please input an age (as a number): '))

if age <= 1:
    print("This person is an infant.")
elif age < 13:
    print("This person is a child.")
elif age < 20:
    print("This person is a teenager.")
else:
    print("This person is an adult.")
