#8.9 Sentence Capitalizer
def getString():
    return input('Please enter a string to capitalize: ')

def capitalizeSentences(textInput):
    punc = []
    for char in range(len(textInput)):
        if textInput[char] == '.':
            punc.append('.')
        elif textInput[char] == '!':
            punc.append('!')
        elif textInput[char] == '?':
            punc.append('?')
    textInput = textInput.replace('!','.')
    textInput = textInput.replace('?','.')

    sentences = textInput.split('.')
    for x in sentences:
        if x == '':
            sentences.remove('')
    if len(punc) != len(sentences):
        print("ERROR")
        return "ERROR: Unsupported punctuation."
    i = 0
    output = ''
    while i < len(sentences):
        sentences[i] = sentences[i].strip()
        sentences[i] = sentences[i][0].upper() + sentences[i][1:]
        output += sentences[i] + punc[i] + ' '
        i += 1
    output.strip()
    return output

def main():
    textIn = getString()
    print(capitalizeSentences(textIn))

main()
