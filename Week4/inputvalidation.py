#Validates input by checking the input everytime through a loop.
#Loop only proceeds when the data isn't bad

#Get a test score:
score = int(input('Please input a test score: '))
#Make sure it's not less than zero
while score < 0 or score > 100:
    print('ERROR: Score cannot be negative or greater than 100')
    score = int(input('Please input the correct score: '))

print('The score is:',score)
