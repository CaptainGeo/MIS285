def display(lineIn):
    line = lineIn.split(' ')
    fName = line[0]
    lName = line[1]
    score = line[2]
    print('Name: ',fName + ' ' + lName + '\tScore: '+ score)

def main():
    filename = 'golf.txt'
    golf = open(filename, 'r')
    line = golf.readline()
    while line != '':
        display(line.rstrip('\n'))
        line = golf.readline()

main()
