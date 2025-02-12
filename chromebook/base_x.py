base = 16
convert_number = "16"
numbers = [i for i in range(201)]
numbers = ["5b"]
base_x_digits = "0123456789abcdefghijklmnopqrstuvwxyz"
#base_x_digits = "abcdefghijklmnopqrstuvwxyz"

def to_base_x(number):
    result = ""

    while number > 0:
        digit = number % base
        result = base_x_digits[digit] + result
        number //= base

    return result or "0"

def from_base_x(base_x_number, base):
    result = 0
    power = 0

    for digit in reversed(base_x_number):
        result += base_x_digits.index(digit) * (base ** power)
        power += 1

    return result


base_x_numbers = [to_base_x(number) for number in numbers]

for base_x_number, base_10_number in zip(base_x_numbers, numbers):
    print(str(base_10_number) + " decimal: " + str(base_x_number) + " (base " + str(base) + ")")

converted_base_10 = from_base_x(convert_number, base)
print(str(convert_number)+" (base " + str(base) + "): " + str(converted_base_10)+" decimal")