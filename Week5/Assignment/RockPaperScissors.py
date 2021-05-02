import random

def setPlayerMove():
    global player
    player = input("Please enter your choice ('rock', 'paper', or 'scissors'): ")
    player = player.lower()

def setCompterMove():
    global computer
    rand = random.randint(0,2)
    if rand == 0:
        computer = 'rock'
    elif rand == 1:
        computer = 'paper'
    elif rand == 2:
        computer = 'scissors'
    else:
        print('ERROR: Unable to assign computer move.')

def determineWinner():
    if player == 'rock':
        if computer == 'paper':
            winner = 'Computer'
        if computer == 'scissors':
            winner = 'Player'
    elif player == 'paper':
        if computer == 'rock':
            winner = 'Player'
        if computer == 'scissors':
            winner = 'Computer'
    elif player == 'scissors':
        if computer == 'rock':
            winner = 'Computer'
        if computer == 'paper':
            winner = 'Player'
    else:
        print('ERROR: Unable to determine winner')
        winner = 'ERROR: Unable to determine winner'
    return winner

def main():
    winner = 'n'
    while winner != 'y':
        setPlayerMove()
        print('Player chose:', player)
        setCompterMove()
        print('Computer chose:', computer)
        if player != computer:
            winner = 'y'
            print(determineWinner(), 'wins!')
        else:
            print('A tie! Play again.')

main()
