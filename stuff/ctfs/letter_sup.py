text = """
isnfnnpctitnznfmxhisnfwnxxntimjxctsnascdstushhxuhgqbinftnubfciruhgqnicichktckuxbackdurjnfqmifchimkabturjnfusmxxnkdnisntnuhgqnicichktehubtqfcgmfcxrhktrtingtmagckctifmichkebkamgnkimxtwscusmfnznfrbtnebxmkagmfonimjxntocxxtshwnznfwnjnxcnznisnqfhqnfqbfqhtnhemscdstushhxuhgqbinftnubfciruhgqnicichkctkhihkxrihinmuszmxbmjxntocxxtjbimxthihdnitibankitckinfntinackmkanpucinamjhbiuhgqbinftucnkunanenktcznuhgqnicichktmfnheinkxmjhfchbtmeemcftmkauhgnahwkihfbkkckdusnuoxctitmkanpnubickduhkecdtufcqitheenktnhkisnhisnfsmkactsnmzcxrehubtnahknpqxhfmichkmkacgqfhzctmichkmkaheinksmtnxngnkitheqxmrwnjnxcnznmuhgqnicichkihbusckdhkisnheenktcznnxngnkitheuhgqbinftnubfcirctisnfnehfnmjniinfznscuxnehfinusnzmkdnxctgihtibankitckmgnfcumkscdstushhxtebfisnfwnjnxcnznismimkbkanftimkackdheheenktczninuskcvbntctnttnkicmxehfghbkickdmkneenuicznanenktnmkaismiisnihhxtmkauhkecdbfmichkehubtnkuhbkinfnackanenktcznuhgqnicichktahntkhixnmatibankitihokhwisncfnkngrmtneenuicznxrmtinmusckdisngihmuicznxrisckoxconmkmiimuonfqcuhuiectmkheenktcznxrhfcnkinascdstushhxuhgqbinftnubfciruhgqnicichkismitnnotihdnknfminckinfntickuhgqbinftucnkunmghkdscdstushhxnftinmusckdisngnkhbdsmjhbiuhgqbinftnubfcirihqcvbnisncfubfchtcirghiczmickdisngihnpqxhfnhkisncfhwkmkankmjxckdisngihjniinfanenkaisncfgmusckntisnexmdctqcuhUIE{K6F4G_4K41R515_15_73A10B5_702E03EU} 
"""
text_dict = []
text_dict_cmp = []
unsupped = []
checked_letters = []
#checked_letters = [('e', 'f'), ('i', 't'), ('u', 'c'), ('h', 'o'), ('c', 'i'), ('q', 'p'), ('t', 's'), ('d', 'g'), ('m', 'a'), ('x', 'l'), ('s', 'h'), ('n', 'e'), ('k', 'n'), ('z', 'v'), ('f', 'r')]
missing_letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

for char in text:
    text_dict.append(char)
    text_dict_cmp.append(char)

def final(text_dict):
    final_text = ""
    for char in text_dict:
        final_text += char
    print(30*'-')
    print(final_text)
    print(30*'-')

def replacing(text_dict,text_dict_cmp,letter,rep_letter):
    unsupped.remove(letter.lower())
    missing_letters.remove(rep_letter.lower())
    for j in range(len(text_dict)):
        if text_dict[j] == text_dict_cmp[j] and text_dict[j] == letter.lower():
            text_dict[j] = rep_letter.lower()
        if text_dict[j] == text_dict_cmp[j] and text_dict[j] == letter.upper():
            text_dict[j] = rep_letter.upper()
    return text_dict

for ch in text_dict:
    if ch.lower() not in unsupped and ch.isalpha():
        unsupped.append(ch.lower())
unsupped = sorted(unsupped)

for tup in checked_letters:
    letter, rep_letter = tup[0], tup[1]
    text_dict = replacing(text_dict,text_dict_cmp,letter,rep_letter)

while True:
    final(text_dict)
    print("Unsupstituted symbols are:")
    print(unsupped)
    print("missing letters:")
    print(missing_letters)
    letter = input("Letter: ")
    rep_letter = input("Replacement: ")

    try:
        text_dict = replacing(text_dict,text_dict_cmp,letter,rep_letter)
        checked_letters.append((letter,rep_letter))
    except:
        print("This letter was already supped")
        print(checked_letters)
        



