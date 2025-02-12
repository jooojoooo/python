
word = input()
letters = "abcdefghijklmnopqrstuvwxyz"

swapped_letters = {"a":"a","b":"b","c":"c"}

wheels = ["qaywsxedcrfvtgbzhnujmikolp","poiuztrewqlkjhgfdsamnbvcxy","qwsayxcdertgfvbnhzuikjmlop"]
wheel_change = ["g","w","y"]

def change_letter(wheel, current_letter_index):
  return letters.index(wheel[current_letter_index])
  
def rotate_wheel(wheel):
  return wheel[-1] + wheel[:-1]

result = ""
for letter in word:
  current_letter_index = letters.index(letter)
  
  for i in range(len(wheels)):
    current_letter_index = change_letter(wheels[i], current_letter_index)
    
    wheels[0] = rotate_wheel(wheels[0])
    if wheels[0][0] == wheel_change[0]:
      wheels[1] = rotate_wheel(wheels[1])
      if wheels[1][0] == wheel_change[1]:
        wheels[2] = rotate_wheel(wheels[2])
        
  for i in range(len(wheels)-2):
    current_letter_index = change_letter(wheels[i], current_letter_index)
    
    wheels[0] = rotate_wheel(wheels[0])
    if wheels[0][0] == wheel_change[0]:
      wheels[1] = rotate_wheel(wheels[1])
      if wheels[1][0] == wheel_change[1]:
        wheels[2] = rotate_wheel(wheels[2])
        
  
  result += letters[current_letter_index]
  
print(result)