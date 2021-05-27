#9.5 Word Frequency
def getDict(stringIn):
    print(" -> Building dictionary...")
    dict = {}
    alpha = ''
    for x in stringIn:
        if x.isalpha() or x == ' ' or x == "'":
            alpha += x
        elif x == '.' or x == '—' or x == '\n':
            alpha += ' '

    wordsList = alpha.split(' ')
    lowerList = []
    for x in wordsList:
        if x == '':
            wordsList.remove('')
        else:
            lowerList.append(x.lower())

    for x in lowerList:
        dictkeys = dict.keys()
        if x in dictkeys:
            dict[x] += 1
        else:
            dict[x] = 1

    print(" -> Building complete.")
    return dict

def main():
    pathin = input("Please specify input filepath (default = inputfile.txt)... ")
    if pathin == '':
        pathin = 'inputfile.txt'
    print(" -> Input:",pathin)
    filein = open(pathin, 'r')

    text = filein.read()
    dict = getDict(text)

    print('Word Frequencies:')
    for word in dict:
        print(dict[word],'\t', word)

    filein.close()

main()
