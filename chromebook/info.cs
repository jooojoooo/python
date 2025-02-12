

def strukture(variables):
  variables = str(variables)
  print(variables)


def test():
  var1 = "Hallo"
  var2 = 10
  var3 = 0
  strukture((var1, var2, var3))
  while var3 < var2:
    var3 += 1
    print(var1)
    strukture((var1, var2, var3))


    
programm = """

text = "Hallo"
anzahl = 10
i = 0
while i < anzahl:
  i += 1
  print(text)

"""
#Done
def get_index(string, char):
  indexes = []
  for current_index in range(len(programm)):
    if programm[current_index:current_index+len(char)] == char:
      indexes.append(current_index)
  return indexes
  
    
def extract_var(programm):
  start_indexes = get_index(programm,"\n")
  end_indexes = get_index(programm," = ")
    
  for i in range(len(start_indexes)):
    for j in range(len(end_indexes)):
      if start_indexes[i] < end_indexes[j] and start_indexes[i+1] >= end_indexes[j]:
        print(programm[i:j])  
  var = []
  for i in range(2):
    var.append("ubib")

extract_var(programm)

