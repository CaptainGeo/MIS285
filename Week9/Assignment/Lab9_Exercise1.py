#9.2 Capitol Quiz
import random

def getCaps():
    capitals = {
        'Alabama': 'Montgomery', 'Alaska': 'Juneau', 'Arizona': 'Phoenix',
        'Arkansas': 'Little Rock', 'California': 'Sacramento', 'Colorado': 'Denver',
        'Connecticut': 'Hartford', 'Delaware': 'Dover', 'Florida': 'Tallahassee',
        'Georgia': 'Atlanta', 'Hawaii': 'Honolulu', 'Idaho': 'Boise',
        'Illinois': 'Springfield', 'Indiana': 'Indianapolis', 'Iowa': 'Des Monies',
        'Kansas': 'Topeka', 'Kentucky': 'Frankfort', 'Louisiana': 'Baton Rouge',
        'Maine': 'Augusta', 'Maryland': 'Annapolis', 'Massachusetts': 'Boston',
        'Michigan': 'Lansing', 'Minnesota': 'St. Paul', 'Mississippi': 'Jackson',
        'Missouri': 'Jefferson City', 'Montana': 'Helena', 'Nebraska': 'Lincoln',
        'Nevada': 'Carson City', 'New Hampshire': 'Concord', 'New Jersey': 'Trenton',
        'New Mexico': 'Santa Fe', 'New York': 'Albany', 'North Carolina': 'Raleigh',
        'North Dakota': 'Bismarck', 'Ohio': 'Columbus', 'Oklahoma': 'Oklahoma City',
        'Oregon': 'Salem', 'Pennsylvania': 'Harrisburg', 'Rhoda Island': 'Providence',
        'South Carolina': 'Columbia', 'South Dakota': 'Pierre', 'Tennessee': 'Nashville',
        'Texas': 'Austin', 'Utah': 'Salt Lake City', 'Vermont': 'Montpelier',
        'Virginia': 'Richmond', 'Washington': 'Olympia', 'West Virginia': 'Charleston',
        'Wisconsin': 'Madison', 'Wyoming': 'Cheyenne'}
    return capitals

def main():
    print('Welcome to the State Capitals Quiz! Enter the capital of each state, or press "q" to quit.')
    caps = getCaps()
    quit = False
    length = len(caps)
    correct = 0
    incorrect = 0
    while quit == False and len(caps) > 0:
        state = random.choice(list(caps.keys()))
        cap = caps[state]
        prompt = "What city is the capital of " + state + "? \n"
        guess = input(prompt).lower()
        if guess == 'q':
            quit = True
        elif guess == cap.lower():
            correct += 1
            print("CORRECT")
        elif guess != cap.lower():
            incorrect += 1
            print("INCORRECT - The capital of ",state, " is ",cap,'.',sep='')
        print(correct,"Correct \t",incorrect,"Incorrect\n")
        del caps[state]
    print("Final Score =",correct,"Correct, and",incorrect,"Incorrect.")

main()
