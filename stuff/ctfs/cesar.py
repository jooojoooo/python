text = """
admin
"""
letters = "abcdefghijklmnopqrstuvwxyz"

try:
    rot = int(input("Rotation: "))
    use_rot = True
except:
    use_rot = False
    print("Error: Using all Rotations")

def ceasar(rot):
    plain_text = ""
    for char in text:
        up = False
        if char.isalpha():
            if char != char.lower():
                char = char.lower()
                up = True
            index = letters.index(char)
            plain_char = letters[(index + rot) % 26]
            if up: plain_char = plain_char.upper()
        else: plain_char = char
        plain_text += plain_char

    print(f"Rot {rot}: {plain_text}")

if use_rot:
    ceasar(rot)
else:
    for rot in range(26):
        ceasar(rot)

