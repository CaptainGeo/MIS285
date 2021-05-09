#We can access, write, and edit files within python as well
#file_object = open(<filename>,<mode>)
#mode can be 'r' for read, 'w' for create or overwrite an existing file, or 'a' for appending an existing file

#Opening
testfile = open('testtext.txt','w')

#Writing
#writes values as strings by default
testfile.write('123456789\n1011121314151617181920\n')

#Closing
testfile.close()

#You can only read when it was specifically opened for reading
readfile = open('testtext.txt','r')
linetext = readfile.read() #reads next line in the file
print(linetext)
text = readfile.read() #reads the whole file
print(text)
readfile.close()
#values are read as strings, can use int() and float() to convert

#Concatinating new line and stripping it
#To write and access variables we probably want to have them on different lines
#but don't want '\n' to be part of our variables
a = 'red'
b = 'red'
c = 'yellow'
d = 'green'

testfile = open('testtext.txt','w')
testfile.write(a + '\n' + b + '\n' + c + '\n' + d + '\n')
testfile.close()

#Appending
appendfile = open('testtext.txt','a')
appendfile.write('blue'+'\n')
appendfile.close()

testfile = open('testtext.txt','r')
text = testfile.read()
#Using the .rstrip method allows you to take off characters from the end of a string
print('TEST STRIP: ',text.rstrip('\n'),'end of read') #removing \n for the file read
testfile.close()

testfile = open('testtext.txt','r')
print('Reading in loooooooop:')
for line in testfile:
    print(line.rstrip('\n'))
testfile.close()
