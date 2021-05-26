#Sets are objects which store a collection of data in the same way as a mathematical set
#All unique items, unordered, may be of different datatypes
#create with set() for empty
#create and populate with set(arguments) where arguments are iterable objects (list, string, tuple, sequence)
args = {'a','b','c','d','e'}
newset = set(args)
print(newset)
args = 'alphabet'
alphabetset = set(args) #If there are dupes, only one appears in the set
print(alphabetset)
print('alphabetset is =',len(alphabetset),'items long')

newset.add('f') #.add adds just one more item into the set
updateargs = {'g','h','i','j'}
newset.update(updateargs) #.update adds a whole new iterable object
print(newset)

#Remove with:
newset.remove('j') #Raises a KeyError exception if item is not found
newset.discard('i') #Doesn't raise an exception if not found
print(newset)
alphabetset.clear() #Clears all elements in the set
print(alphabetset)

#Can use if in and if not in to determine if an item is in a set
if 'g' in newset:
    print('g is in newset')
elif 'g' not in newset:
    print('g is not in newset')

#Can use for loops to iterate through the set
print("Looping!....")
for x in newset:
    print(x)

#Can combine sets in two ways:     (both ways delete dupes)
newerset = set('abcdefghijklmnopqrstuvwxyz')
combinedset = newset.union(newerset)
print(combinedset)
combinedset2 = newset | newerset
print (combinedset2)

#find "intesections", or overlap, or sets
overlapset = newset.intersection(newerset)
print(overlapset)
overlapset2 = newset & newerset
print(overlapset2)

#find differences in sets
diffset = newset.difference(newerset)
print(diffset)
diffset2 = newerset - newset
print(diffset2)

#Symmetric difference (set which contains elements not shared by the two sets)
symmdiffset = newset.symmetric_difference(newerset)
print(symmdiffset)
symmdiffset2 = newset ^ newerset
print(symmdiffset2)

#Finding Subsets (all it's elements are contained also in the superset)
if newset.issubset(newerset):
    print('newset is a subset of newerset')
if newset <= newerset:
    print('newset is a subset of newerset')

#Finding supersets (they contain all items of their subsets)
if newerset.issuperset(newset):
    print('newerset is a superset of newset')
if newerset >= newset:
    print('newerset is a superset of newset')
