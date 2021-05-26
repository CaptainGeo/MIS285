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
    pathin = input("Please specify input filepath (default = inputfile.txt)... ")
    if pathin == '':
        pathin = 'inputfile.txt'
    pathout = input("Please specify output filepath (default = outputfile.txt)... ")
    if pathout == '':
        pathout = 'outputfile.txt'
    code = getCypher()
    print(" -> Input:",pathin,'\n -> Output:', pathout)

    filein = open(pathin, 'r')
    fileout = open(pathout, 'w')
    print(" -> Importing",pathin,'...')
    text = filein.read()

    length = len(text)
    print(" -> Text imported. Length =",length,"characters.")
    out = ''
    for x in text:
        if x in code:
            y = code[x]
        else:
            y = x
        out += y
    print("-----------------------------<ENCRYPTED TEXT>-----------------------------\n",out,sep='')

    fileout.write(out)
    filein.close()
    fileout.close()

main()
