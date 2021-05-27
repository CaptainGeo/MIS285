#9.9 Blackjack Simulation
# This program uses a dictionary as a deck of cards.

# The create_deck function returns a dictionary
# representing a deck of cards.
def getDeck():
    # Create a dictionary with each card and its value stored as key-value pairs.
    deck = {'Ace of Spades':1, '2 of Spades':2, '3 of Spades':3,
            '4 of Spades':4, '5 of Spades':5, '6 of Spades':6,
            '7 of Spades':7, '8 of Spades':8, '9 of Spades':9,
            '10 of Spades':10, 'Jack of Spades':10,
            'Queen of Spades':10, 'King of Spades': 10,

            'Ace of Hearts':1, '2 of Hearts':2, '3 of Hearts':3,
            '4 of Hearts':4, '5 of Hearts':5, '6 of Hearts':6,
            '7 of Hearts':7, '8 of Hearts':8, '9 of Hearts':9,
            '10 of Hearts':10, 'Jack of Hearts':10,
            'Queen of Hearts':10, 'King of Hearts': 10,

            'Ace of Clubs':1, '2 of Clubs':2, '3 of Clubs':3,
            '4 of Clubs':4, '5 of Clubs':5, '6 of Clubs':6,
            '7 of Clubs':7, '8 of Clubs':8, '9 of Clubs':9,
            '10 of Clubs':10, 'Jack of Clubs':10,
            'Queen of Clubs':10, 'King of Clubs': 10,

            'Ace of Diamonds':1, '2 of Diamonds':2, '3 of Diamonds':3,
            '4 of Diamonds':4, '5 of Diamonds':5, '6 of Diamonds':6,
            '7 of Diamonds':7, '8 of Diamonds':8, '9 of Diamonds':9,
            '10 of Diamonds':10, 'Jack of Diamonds':10,
            'Queen of Diamonds':10, 'King of Diamonds': 10}

    return deck

# The deal_cards function deals a specified number of cards
# from the deck.

def getHand(deck, number):
    # Make sure the number of cards to deal is not
    # greater than the number of cards in the deck.
    hand = []
    score = 0
    if number > len(deck):
        number = len(deck)

    # Deal the cards and accumulate their values.
    for count in range(number):
        card, value = deck.popitem()
        score += value
        hand.append(card)
        #print(card)

    # Display the value of the hand.
    #print('Hand:', hand)
    return deck, hand, score

def getScoreString(score1, score2, handsScore1, handsScore2):
    out ='Hand Score:\n'
    out += 'Player 1: ' + str(score1) + '\nPlayer 2: ' + str(score2) + '\n'
    out += 'Game Score:\n'
    out += 'Player 1: ' + str(handsScore1) + '\nPlayer 2: ' + str(handsScore2)
    return out

def decideHit(score):
    if score < 14: #rounded avg card value (mean and median)
        return True
    return False

def decideAce(score):
    if score > 10:
        return 1
    return 11

def main():
    # Create a deck of cards.
    deck = getDeck()
    #Initial deal number
    initDeal = 2

    #These track number of hands won per player
    handsScore1 = 0
    handsScore2 = 0
    hands = 0

    #Hand loop
    while len(deck) > 0:
        # Deal the cards.
        deck, hand1, score1 = getHand(deck, initDeal)
        deck, hand2, score2 = getHand(deck, initDeal)
        for x in hand1:
            if 'Ace' in x:
                score1 +=10
        for x in hand2:
            if 'Ace' in x:
                score2 +=10

        while score1 <= 21 and score2 <= 21 and len(deck) > 0:
            deck, newhand1, newscore1 = getHand(deck, 1)
            deck, newhand2, newscore2 = getHand(deck, 1)

            score1 += newscore1
            score2 += newscore2
            hand1.append(newhand1)
            hand2.append(newhand2)

        if score1 > 21 and score2 <= 21:
            handsScore2 += 1
            print('-------- HAND',hands,'--------')
            print('Player 2 Wins Hand', str(hands))
            print(getScoreString(score1,score2,handsScore1,handsScore2))
        if score2 > 21 and score1 <= 21:
            handsScore1 += 1
            print('-------- HAND',hands,'--------')
            print('Player 1 Wins Hand', str(hands))
            print(getScoreString(score1,score2,handsScore1,handsScore2))
        if score1 > 21 and score2 > 21:
            print('-------- HAND',hands,'--------')
            print('Both players scored above 21. No points for hand', str(hands),':(')
            print(getScoreString(score1,score2,handsScore1,handsScore2))

        hands += 1

main()
