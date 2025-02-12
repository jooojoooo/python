decipher = False
encrypt = False
charset = "abcdefghijklmnopqrstuvwxyz"
charset_u = charset.upper()
numset = "1234567890"
result = ""

str1 = input("String to encrypt/decipher ")
#str1 = str1.lower()
#str1 = "-t abz -k -1 -e "
str1 += " "
if "--help" in str1:
    print("""
          
please specify:
    -t (text to use)
    -e (encrypt text)
    -d (decipher text (default))
    -k (key (number 0-26, -1 if key unknown))
          
    """)
    exit()

if "-k " in str1: 
    key = int(str1[str1.index("-k ")+3 : str1.index("-k ")+5])
    str1 = str1.replace(str1[str1.index("-k ") : str1.index("-k ")+5], "")


if "-e " in str1: 
    encrypt = True
    str1 = str1.replace("-e ", "")

if "-d " in str1: 
    decipher = True
    key = -key
    str1 = str1.replace("-d ", "")

if "-t " in str1:
    str1 = str1.replace("-t ", "")

print(str1)

if key !=-1:
    for letter in str1:

        if letter in charset:
            if encrypt:
                if charset.index(letter) + key > 26: result += charset[charset.index(letter) + key]
                else: result += charset[charset.index(letter)+ key - 26]
            if decipher:
                if charset.index(letter) + key >= 0: result += charset[charset.index(letter) + key]
                else: result += charset[charset.index(letter) + key + 26]

        if letter in charset_u:
            if encrypt:
                if charset_u.index(letter) + key > 26: result += charset_u[charset_u.index(letter) + key]
                else: result += charset_u[charset_u.index(letter)+ key - 26]
            if decipher:
                if charset_u.index(letter) + key >= 0: result += charset_u[charset_u.index(letter) + key]
                else: result += charset_u[charset_u.index(letter) + key + 26]


        elif letter in numset:
            if encrypt:
                if numset.index(letter) + key > 10: result += numset[numset.index(letter) + key]
                else: result += numset[numset.index(letter)+ key - 10]
            if decipher:
                if numset.index(letter) + key >= 0: result += numset[numset.index(letter) + key]
                else: result += numset[numset.index(letter)+ key + 10]

        else: result += letter
    if key != -1:
        print(f"Result: {result}")

if key == -1:
    for i in range(25):
        for letter in str1:
            if letter in charset:
                if encrypt:
                    key = i
                    if charset.index(letter) + key > 26: result += charset[charset.index(letter) + key]
                    else: result += charset[charset.index(letter)+ key - 26]
                if decipher:
                    key = -i
                    if charset.index(letter) + key >= 0: result += charset[charset.index(letter) + key]
                    else: result += charset[charset.index(letter) + key + 26]
            else: result += letter
        print(f"Result: {result}")

