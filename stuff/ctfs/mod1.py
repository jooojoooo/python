nums = [268, 413, 438, 313, 426, 337, 272, 188, 392, 338, 77, 332, 139, 113, 92, 239, 247, 120, 419, 72, 295, 190, 131]
#nums = [3]
chars = " abcdefghijklmnopqrstuvwxyz0123456789_"
plaintext = ""
mod = 41
inverse = True

char = ""
for num in nums:
    if not inverse:
        plaintext += chars[num%mod]
    else:
        for i in range(mod):
            if (num * i)%mod == 1:
                plaintext += chars[i]
                break

print(plaintext)