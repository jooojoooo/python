numbers = [0,1]
i = 1
while i < 100:
  number1 = numbers[i]
  number2 = numbers[i-1]
  new_number = number1 + number2
  numbers.append(new_number)
  i = i + 1
print(numbers)