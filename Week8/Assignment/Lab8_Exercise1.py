#8.1 Initials
def getName():
    name = input('Please input a full name to find the initials of: ')
    return name

def getInitials(fullname):
    nameSegments = fullname.split(' ')
    output = ''
    for name in nameSegments:
        output += (name[0] + '. ')
    return output.rstrip()

def main():
    name = getName()
    initials = getInitials(name)
    print('The initials for', name, 'are:', initials)

main()
