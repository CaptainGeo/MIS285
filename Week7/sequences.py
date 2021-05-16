#A sequence is a data object that contains multiple items of data
#they are stores IN SEQUENCE, one after another
#Lists and tuples are sequences
#A list is mutable (changable), a tuple is immutable

#List is an object that contains multiple data items (even diff types)
newlist = ["item1", "item2", "item3"]
print(newlist) #we can print lists with print
#the list() funciton can be used to convert other objects into lists
newerlist = newlist * 2 #we can multiply lists to mult and join them
for x in newerlist: #can iterate through lists with for
    print(x)

print("First item (index 0):", newerlist[0]) #indexing starts at 0
print("Last item (index -1):", newerlist[-1]) #we can go from the end starting with -1

print("List size =", len(newerlist)) #get length with len()
print("Last index =", len(newerlist) - 1) #get last index len(list)-1

listtoadd = ["item4","item5","item6"]
finallist = newlist + listtoadd #we can concatenate lists too using +
finallist += ["item7","item8"] #can add with +
finallist.append("item9") #append with append

print("Final list:",finallist)

#we can slice lists too. Starts at the start index, doesn't include end index
listslice = finallist[3:6] #start:end. defaults are start at 0, end at the end
#Finding items in lists
if "item5" in listslice:
    index = listslice.index("item5")
    print("item5 is in the slice at position:",index)
    listslice.remove("item5") #remove with .remove()
    listslice.insert(index,"item5.1")
else:
    print("item5 is not in the slice")
if "item8" not in listslice:
    print("item 8 is not in the slice")
print(listslice)
#Can also use .reverse() and .sort to reverse and sort the order of items
#max(sequence) and min(sequence) return max and min values in a sequence

#can delete objects by index with del list[i]
del listslice[2]
print(listslice)



#Tuples are like lists, but immutable, and cannot be changed
newtuple = ("item1", "item2", "item3")
#support same operators, len, max, min, index, slice, etc

#Can convert between them with list() and tuple()
tuplelist = list(newtuple)
