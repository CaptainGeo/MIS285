#9.3 File Encryption and Decryption
def getCypher():
    code = {
    'A':'~', 'a':'n',
    'B':'z', 'b':'N',
    'C':'@', 'c':'o',
    'D':'#', 'd':'O',
    'E':'$', 'e':'r',
    'F':'%', 'f':'R',
    'G':'^', 'g':'S',
    'H':'&', 'h':'s',
    'I':'*', 'i':'t',
    'J':'I', 'j':'T',
    'K':'i', 'k':'x',
    'L':'m', 'l':'_',
    'M':'+', 'm':'=',
    'N':'[', 'n':'{',
    'O':']', 'o':'}',
    'P':'a', 'p':'|',
    'Q':'X', 'q':'y',
    'R':'<', 'r':'M',
    'S':'>', 's':'q',
    'T':'Q', 't':'A',
    'U':'B', 'u':'c',
    'V':'C', 'v':'D',
    'W':'d', 'w':'e',
    'X':'G', 'x':'f',
    'Y':'p', 'y':'g',
    'Z':'P', 'z':'b'
    }
    return code

def main():
    pathin = input("Please specify default filepath (default = outputfile.txt)... ")
    if pathin == '':
        pathin = 'outputfile.txt'

    code = getCypher()
    print(" -> Input:",pathin)

    filein = open(pathin, 'r')
    print(" -> Importing",pathin,'...')
    text = filein.read()
    length = len(text)
    print(" -> Text imported. Length =",length,"characters.")
    out = ''

    keys = list(code.keys())
    vals = list(code.values())

    for x in text:
        if x in vals:
            y = keys[vals.index(x)]
        else:
            y = x
        out += y
    print("-----------------------------<DECRYPTED TEXT>-----------------------------\n",out,sep='')
    filein.close()

main()
