#Serializing an object converts it to a stream of bytes which can be easily stored in a file
#Pickling = serializing an object
import pickle

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

#Open a file for binary writing
binarywritefile = open('pickling.txt','wb') #wb for writing binary

#Use pickle.dump(object,file) to pickle an object. Can pickle multiple onjects before closing.
pickle.dump(capitals,binarywritefile)

#After pickling as many objects as we want, close the file
binarywritefile.close()

#READING
#Open file for binary reading
storedbinaryfile = open('pickling.txt','rb') #rb for reading binary

#use pickle.load(file) to load pickled objects in
newcaps = pickle.load(storedbinaryfile)

print(newcaps)

#Close when done
storedbinaryfile.close()
