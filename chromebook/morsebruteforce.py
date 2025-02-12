import sys
morse =  { 
    'A':'.-', 'B':'-...',
    'C':'-.-.', 'D':'-..', 'E':'.',
    'F':'..-.', 'G':'--.', 'H':'....',
    'I':'..', 'J':'.---', 'K':'-.-',
    'L':'.-..', 'M':'--', 'N':'-.',
    'O':'---', 'P':'.--.', 'Q':'--.-',
    'R':'.-.', 'S':'...', 'T':'-',
    'U':'..-', 'V':'...-', 'W':'.--',
    'X':'-..-', 'Y':'-.--', 'Z':'--..',
    '1':'.----', '2':'..---', '3':'...--',
    '4':'....-', '5':'.....', '6':'-....',
    '7':'--...', '8':'---..', '9':'----.',
    '0':'-----'}

#.-.....-.---.....--....-.--...--.--.-....--..-.-
string = ".-...."
output = []

def bruteforce(code):
    output = []
    for char in morse:
        if code.startswith(morse[char]):
            results = bruteforce(code[len(morse[char]):])
            if results != []:
                for result in results:
                    output.append(char + result)      
            else:
                output.append(char)
    orig_stdout = sys.stdout
    f = open('morse-03.txt', 'w')
    sys.stdout = f

    print(output,end="")

    sys.stdout = orig_stdout
    f.close()

                


bruteforce(string)


print("DONE")