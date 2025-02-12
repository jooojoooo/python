cipher = [260307, 491691, 491691, 2487378, 2516301, 0, 1966764, 1879995, 1995687, 1214766, 0, 2400609, 607383, 144615, 1966764, 0, 636306, 2487378, 28923, 1793226, 694152, 780921, 173538, 173538, 491691, 173538, 751998, 1475073, 925536, 1417227, 751998, 202461, 347076, 491691]
#cipher1 = [491691]
#cipher1 = [491691,347076,202461,751998,1417227,925536,1475073,751998]
#cipher = cipher1[::-1]
key = 93
text_keys = "trudeau"
text_keys = "abcdefghijklmnopqrstuvwxyz"
safe_key = "aedurtu"

def encrypt(cipher, key):
    cipher_text = ""
    for char in cipher:
        cipher_text += (chr(char//311//key))
    return cipher_text

def dynamic_xor_encrypt(semi_cipher, text_key):
    key_length = len(text_key)
    plain_text = ""
    for i, char in enumerate(semi_cipher[::-1]):
        key_char = text_key[i % key_length]
        decrypted_char = chr(ord(char) ^ ord(key_char))
        plain_text += decrypted_char
    return plain_text

# for text_key in text_keys:
if 1==1:
    current_key = safe_key# + text_key
    semi_cipher = encrypt(cipher, key)
    plain_text = dynamic_xor_encrypt(semi_cipher, current_key)
    print(plain_text)

    # if plain_text == "picoCTF{":
    #     print(current_key)


message = 30*"a" + "pico" #sys.argv[1]