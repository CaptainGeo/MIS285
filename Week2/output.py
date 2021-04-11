#There are a lot of different kinds of ouputs we can user
print('Basic output','with a basic default seperator')
print('Concatinated','output',sep = '')
print('Fancy','seperator',sep = '---')

#Escape Characters
print('One\nTwo\nThree') # \n gives us a new line
print('One\tTwo\tThree') # \t gives us a tab
print('Test\\') # \\ gives us a single backslash
print('Test\'') # \\ gives us a single quote
print('Test\"') # \\ gives us a double quote

print('We can add strings together' + ' using the addition operator')

#We can also do some formatting using the format() function
print(format(12345.6789,'.2f')) #the '.2' indicates the precision, the f indicates that we are formatting a floating point number
print(format(12345.6789,'e')) #the 'e' gives us Scientific formatting
print(format(12345.6789,',.2f')) #the ',' gives us commas in our number,'.2' indicates the precision, the f indicates that we are formatting a floating point number
