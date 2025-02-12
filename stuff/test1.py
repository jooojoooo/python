import time
import sys

morse =  { 'A':'.-', 'B':'-...',
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


string = "....-.--"

def FindCombinations(code):
    out = []
    for char in morse:
        if code.startswith(morse[char]):
            results = FindCombinations(code[len(morse[char]):])
            
            if results != []:
                for result in results:
                    out.append(char + result) 
                    
            else:
                out.append(char)

    return out


# start = time.asctime(time.localtime(time.time()))
# end = 0
# print(f"start: {start}, end: {end}")

# print("Starting brute force")
sys.stdout = open('output_last_01.txt','wt')
print(FindCombinations(string))
sys.stdout.close()

# end = time.asctime(time.localtime(time.time()))
# print(f"start: {start}, end: {end}")
