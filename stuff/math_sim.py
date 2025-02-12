import random

sim_anz = 1000000
game_number = 20
truefsaf = 0
for i in range(sim_anz):
    g18 = False
    g19 = False
    for i in range(game_number):
        p = random.randint(0,2)
        if i == 18 and p == 0:
            g18 = True
        if i == 19 and p == 0:
            g19 = True


        if g18 == g19 == True:
            truefsaf += 1



print(truefsaf/sim_anz)
print(1/9)