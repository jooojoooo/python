from random import randint
import sys


def generator(g, x, p):
    return pow(g, x) % p


def encrypt(plaintext, key):
    cipher = []
    for char in plaintext:
        cipher.append(((ord(char) * key*311)))
    return cipher


def is_prime(p):
    v = 0
    for i in range(2, p + 1):
        if p % i == 0:
            v = v + 1
    if v > 1:
        return False
    else:
        return True


def dynamic_xor_encrypt(plaintext, text_key):
    cipher_text = ""
    key_length = len(text_key)
    for i, char in enumerate(plaintext[::-1]):
        key_char = text_key[i % key_length]
        encrypted_char = chr(ord(char) ^ ord(key_char))
        cipher_text += encrypted_char
    return cipher_text


def test(plain_text, text_key):
    p = 97
    g = 31

    a = 94
    b = 29
    u = generator(g, a, p)
    print(f"u = {u}")
    v = generator(g, b, p)
    print(f"v = {v}")
    key = generator(v, a, p)
    print(f"key = {key}")
    b_key = generator(u, b, p)
    print(f"b_key = {b_key}")
    shared_key = None
    if key == b_key:
        shared_key = key
        print(key)
    else:
        print("Invalid key")
        return
    semi_cipher = dynamic_xor_encrypt(plain_text, text_key)
    print(semi_cipher)
    cipher = encrypt(semi_cipher, shared_key)
    print(f'cipher is: {cipher}')


if __name__ == "__main__":
    message = "p" #sys.argv[1]
    test(message, "trudeau")