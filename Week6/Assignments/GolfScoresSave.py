def main():
    filename = 'golf.txt'
    golf = open(filename, 'w')
    addmore = 'y'
    while addmore == 'y' or addmore == 'yes':
        fName = input("Please enter player's first name: ")
        lName = input("Please enter player's last name: ")
        score = int(input("Please enter player's score: "))
        golf.write(fName + ' ' + lName + ' ' + str(score) + '\n')

        addmore = input('Do you have another player to save? (Y/N): ').lower()
    golf.close()


main()
