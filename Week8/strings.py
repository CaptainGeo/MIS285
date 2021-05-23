#There are many tools for examining, manipulating, and working with strings
#Strings are sequences so most those functions work on strings too

#We can iterate through all letters with a for in loop
name = "Gandalf"
for char in name:
    print(char)
#Access letters like index
print(name[2])
#length with len(string)
print("Name is",len(name),"letters long.")

#Strings are immutable, but we can reassign them
#Concat strings with + or +=
name2 = "The Grey"
newname = name + ' ' + name2
print(newname)

#We can slice strings too
#string[start:end]
#Default start is 0, default end is the index of the string (the end of it)
slice = newname[0:len(name)]
print("Slice = ",slice)

#Can use if in to see if string is contained in another
if name in newname:
    print(name,'is in', newname)
else:
    print(name,'is not in', newname)

if name not in newname:
    print(name,'is not in', newname)
else:
    print(name,'is in', newname)

#STRING METHODS
#There are a lot of built in methods for dealing with strings eg string.methods(args)

#These return true or false based on the string
if name.isalnum():
    print(name, 'is alpha numeric')
if name.isalpha():
    print(name, 'is only letters')
if name.isdigit():
    print(name, 'is only digits')
if name.islower():
    print(name, 'has only lowercase letters')
if name.isspace():
    print(name, 'is only whitespace')
if name.isupper():
    print(name, 'has only uppercase letters')

#These perform an operation, and return the resulting string
print(name.lower()) #to lowercase
print(name.upper()) #to uppercase
print(name.lstrip()) #strips all leading whitespace, as well as \t, \n, or whatever chars you pass as args
print(name.rstrip()) #strips all ending whitespace, as well as \t, \n, or whatever chars you pass as args
print(name.strip()) #strips all leading and trailing whitespace, and whatever char you pass as args

#SEARCHING STRINGS
if newname.lower().endswith('grey'):
    print(newname, 'is grey.')
if newname.startswith('Gandalf'):
    print(newname, 'is Gandalf')
print('The index of Grey is', newname.lower().find('grey')) #.find() returns the lowest index, or a negative if no index can be found
print(newname, 'more like', newname.replace('Grey','White')) #.replace() returns a string with the substring replaced

#REPETITION OPERATOR
print(name.upper() * 3) #GANDALFGANDALFGANDALF
