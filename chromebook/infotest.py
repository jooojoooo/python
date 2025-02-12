def str(variable_to_convert):
  number_int_list = [0,1,2,3,4,5,6,7,8,9,10]
  number_str_list = ["0","1","2","3","4","5","6","7","8","9","10"]
  if variable_to_convert in number_int_list:
    variable_to_convert = number_str_list[variable_to_convert]

  convertet_string = ""
  for char in variable_to_convert:
    convertet_string += char
  return convertet_string  

def strukture(variables):
  for variable in variables:
    print(str(variable)+", ", end="")
  print("")


def test():
  var1 = "Hallo"
  var2 = 10
  var3 = 0
  while var3 < var2:
    var3 += 1
    print(var1)
  strukture((var1,var2,var3))




    
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
    for current_index in range(len(string)):
        if string[current_index:current_index+len(char)] == char:
            indexes.append(current_index)
    return indexes
  
#Done
def extract(string, start_char, end_char):
    start_indexes = get_index(string,start_char)
    end_indexes = get_index(string, end_char)
    if len(start_indexes) < len(end_indexes): start_indexes.append(0)

    vars = []
    for i in range(len(start_indexes)):
        for j in range(len(end_indexes)):
            try: 
                if start_indexes[i] < end_indexes[j] and start_indexes[i+1] >= end_indexes[j]:
                    vars.append(string[start_indexes[i]+len(start_char):end_indexes[j]])
                    break
            except: pass
    return vars

def injekt(char, index, string):
  string_first_half = string[0:index]
  string_second_half = string[index:]
  new_string = string_first_half + char + string_second_half
  return new_string

vars = extract(programm, "\n", " = ")
values = extract(programm, "= ", "\n")
loop_index = get_index(programm, "while")

programm = injekt("""
vars = ["""+vars[0]+""","""+vars[1]+""","""+vars[2]+"""]                  
strukture(("""+vars[0]+""","""+vars[1]+""","""+vars[2]+"""))\n
""",loop_index[0] , programm)
programm = injekt("""
  vars = ["""+vars[0]+""","""+vars[1]+""","""+vars[2]+"""]                  
  strukture(("""+vars[0]+""","""+vars[1]+""","""+vars[2]+"""))\n
""",-1 , programm)

def code_manipulation():
  if "while" in programm:

    programm_mod = injekt("""
                                            
def str(variable_to_convert):
  number_int_list = [0,1,2,3,4,5,6,7,8,9,10]
  number_str_list = ["0","1","2","3","4","5","6","7","8","9","10"]
  if variable_to_convert in number_int_list:
    variable_to_convert = number_str_list[variable_to_convert]

  convertet_string = ""
  for char in variable_to_convert:
    convertet_string += char
  return convertet_string  

def strukture(variables):
  for variable in variables:
    print(str(variable)+", ", end="")
  print("")
                          
""",0 ,programm)
  
    print(programm_mod)

  exec(programm_mod)
code_manipulation()
#test()
