
import sys 

sys.stdout = open('clean_output_last_03.txt','wt')
with open("clean_output_last_01.txt") as file1:
    for line in file1:
        #if "NEUN" in line:
            #print(line,end="")
        if not "E" in line and not "A" in line and not "I" in line and not "O" in line and not "U" in line: pass
        else: print(line, end="")
sys.stdout.close()

