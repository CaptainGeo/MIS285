#Dictionary is an object that stores a collection of data in keys and values which map to eachother
#Keys are immutable objects, and 'map' to values
# dictionary = {key1:val1, key2:val2}
#Retrieve w/
# dictionary[key]       throws KeyError if key is missing

dict = {'a':1, 'b':2, 'c':3, 'd':4}
key = 't'
if key in dict:
    print(dict[key])
elif key not in dict:
    print(key, 'not in dict')

dict['e'] = 5 #can change values or add new keys with dictionary[key] = val
print(dict['e'])
#delete with del dictionary[key]
del dict['e']

print('dict is', len(dict), 'keys long')

#Create new, empty, dictionaries like this
emptydict = {}
#newdict = dict('make' = 'Ford', 'model' = 'Bronco', 'year' = 1985)
#empty dictionary with dictionary.clear()
emptydict.clear()
#get method returns value for a key, if no key is found it can return default
print(emptydict.get('key','default')) #Can't raise KeyError exception

for key in dict:
    print(key, dict[key])

dictitems = dict.items() #returns a tuple of each key and its value
print(dictitems)
for x in dictitems: #iterates over tuple pairs of keys and values
    print(x)

dictkeys = dict.keys() #returns sequence of keys
print(dictkeys)

dictvalues = dict.values() #returns sequence of values
print(dictvalues)

#dictionary.pop(key, default) returns key value if it exists, then deletes it. If it doesn't exist, it returns the default value
print('Running pop on d =',dict.pop('d','default'))
print(dict)

#dictionary.popitem() returns randomly selected key value pair, then deletes it
print('Running popitem on dict = ', dict.popitem())
print(dict)
