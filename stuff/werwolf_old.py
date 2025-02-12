
from turtle import *

 

import playsound

import time

delay = 1

delay1 = 4

 

ts = Screen()

ts.setworldcoordinates(-400,-400,400,400)

ts.bgcolor("#C9C9C9")

tracer(0)

font_color = "red"

 

player = ["Spieler Namen: "]

ts.bgpic("C:\\Users\Jenni\OneDrive\Desktop\Phython.py\WerwolfTag2.gif")

 

player_name = "none"

start = "false"

 

while start != "true":

    player_name = input("Spieler Name: ")

    if not player_name.isnumeric() and player_name != "s" and player_name != "set1" and player_name != "del":

      player.append(player_name)

    elif player_name.isnumeric():

      player = ["Spieler Namen: "]

      for i in range(int(player_name)):

        player.append(str(i+1))

      start = "true"

    elif player_name == "set1":

      player = ["Spieler Namen: ","Katrin","Enni","Jonas","Steffen","Tommy"]

      start = "true"

    elif player_name == "del":

      player.pop()

    elif player_name == "s":

      start = "true"

r = range(1,len(player))

 

event = "none"

special_events = input("ja/enter")

if special_events == "ja":

  event = "true"

   

 

def werewolf_game():

 

  def touch_setup():

    tracer(0)

    penup()

    goto(-400,-200)

    for i in range(1,len(player)):

      color("grey")

      begin_fill()

      for j in range(4):

        forward(100)

        right(90)

      forward(50)

      right(90)

      forward(50)

      end_fill()

      color(font_color)

      write(player[i] + "/" + str(i), align="center", font=("Courier", 10, "bold"))

      right(180)

      forward(50)

      right(90)

      forward(70)

    tracer(1)

     

  touch_setup()

 

  def input_control(v):

    if v.isnumeric() and int(v) in r:

        input_control.goon = "true"

    elif v in player:

        input_control.goon = "true"

    elif v == "" or v == "s":

      input_control.goon = "true"

    elif v[0] == "n":

      input_control.goon = "true"

    else:

        print("Falsche Schreibweise oder Nummer")

        input_control.goon = "false"

 

  input_control.goon = "false"

 

  needs_a_role=[]

  alive_role = []

  dead_role = ["Tote Rollen: "]

  role_in_game = []

  player_role = ["Spieler Rollen: "]

 

  #Getestete Rollen: Dorfbewohner, Magischer Seher, Magischer Werwolf, Amor, Ritter der Nacht, Normaler Werwolf, Gebildeter Henker, Hexe, Dorfmatratze, Harter Bursche

  #nicht Getestete Rollen:

  #Geplante / Defekte Rollen: Alter Mann,

  if len(player) - 1 == 4:

    important_role = ["Magischer Werwolf","Hexe"]

    possible_role = ["Harter Bursche","Dorfbewohner","Gerber"]

  if len(player) - 1 == 5:

    important_role = ["Magischer Werwolf","Hexe"]

    possible_role = ["Normaler Werwolf","Amor","Gerber","Harter Bursche","Magischer Seher","Dorfbewohner"]

  if len(player) - 1 == 6:

    important_role = ["Magischer Werwolf","Hexe"]

    possible_role = ["Normaler Werwolf","Magischer Seher","Ritter der Nacht","Gerber","Dorfmatratze"]

  if len(player) - 1 == 7:

    important_role = ["Magischer Werwolf","Normaler Werwolf","Hexe"]

    possible_role = ["Normaler Werwolf","Magischer Seher","Ritter der Nacht","Dorfbewohner","Dorfbewohner"]

  if len(player) - 1 == 8:

    important_role = ["Magischer Werwolf","Normaler Werwolf","Hexe"]

    possible_role = ["Normaler Werwolf","Magischer Seher","Ritter der Nacht","Dorfbewohner","Dorfbewohner"]

  if len(player) - 1 == 9:

    important_role = ["Magischer Werwolf","Normaler Werwolf","Hexe"]

    possible_role = ["Normaler Werwolf","Magischer Seher","Ritter der Nacht","Dorfmatratze","Betrunkener Richter","Gerber","Dorfbewohner","Dorfbewohner"]

  if len(player) - 1 == 10:

    important_role = ["Magischer Werwolf","Normaler Werwolf A","Hexe"]

    possible_role = ["Normaler Werwolf B","Magischer Seher","Ritter der Nacht","Dorfmatratze","Amor","Gerber","Dorfbewohner A","Dorfbewohner B","Harter Bursche"]

 

  for i in range(1,len(player)):  

    player_role.append("none")

    needs_a_role.append(player[i])

 

  role_in_game = important_role + possible_role

 

  import random

 

  c = len(needs_a_role)

 

  while len(needs_a_role) !=0:

    major = "none"

   

    random_player = random.randint(1,c)

    if len(important_role) != 0:

      random_role = random.randint(0,len(important_role)-1)

    if len(important_role) == 0:

      random_role = random.randint(0,len(possible_role)-1)

   

    if player_role[random_player] == "none":

      if len(important_role) > 0:

        player_role[random_player] = important_role[random_role]

        important_role.remove(important_role[random_role])

      else:

        player_role[random_player] = possible_role[random_role]

        possible_role.remove(possible_role[random_role])

      needs_a_role.remove(player[random_player])

      alive_role.append(player_role[random_player])

     

  role_not_in_game = possible_role  

  global validation_num

  validation_num = 0

 

  start = "false"

  while start != "true":

 

    while input_control.goon != "true":

      validation = input("Spieler Nummer: ")

      input_control(validation)

    input_control.goon = "false"

    if not validation.isnumeric() and validation != "s":

      validation = str(player.index(validation))

 

    if validation != "s" and len(player) >= int(validation):

      tracer(0)

      ht()

      penup()

      goto(0,300)

      color(font_color)

      write(player[int(validation)] + ": " + player_role[int(validation)], align="center", font=("Courier", 40, "bold"))

      tracer(1)

      time.sleep(delay)

      clear()

   

    if validation == "s":

      start = "true"    

 

  werewolf_number = alive_role.count("Normaler Werwolf") + alive_role.count("Magischer Werwolf")

  innocent_number = len(alive_role) - werewolf_number

  heal_potion = 1

  kill_potion = 1

  gerber_win = "false"

  liebespaar_win = "false"

  night_num = 0

  couple1 = "none"

  couple2 = "none"

  dead_night = "none"

  haertester_bursche = "false"

  koks = "false"

  nachwuchs = "false"

 

  while werewolf_number > 0 and innocent_number > 1 and gerber_win == "false":

   

    ran_delay = random.randint(4,8)

    delay1 = ran_delay

    night_num = night_num + 1

   

    #Wählen des Liebespaares (Working)

    if night_num == 1 and "Amor" in role_in_game:

      playsound.playsound("C:\\Users\Jenni\OneDrive\Desktop\Phython.py\Sound\Mittagsschlaf_einschalfen.mp3")

      playsound.playsound("C:\\Users\Jenni\OneDrive\Desktop\Phython.py\Sound\Amor_aufwachen.mp3")

      if "Amor" in alive_role:

 

        while input_control.goon != "true":

          couple1_ = input("Ersten Spierler: (Name/Nummer) ")

          input_control(couple1_)

        input_control.goon = "false"

        if not couple1_.isnumeric():

          couple1_ = str(player.index(couple1_))

         

        while input_control.goon != "true":

          couple2_ = input("Zweiten Spierler: (Name/Nummer) ")

          input_control(couple2_)

        input_control.goon = "false"

        if not couple2_.isnumeric():

          couple2_ = str(player.index(couple2_))

 

        couple1 = couple1_.replace(couple1_,player_role[int(couple1_)])

        couple2 = couple2_.replace(couple2_,player_role[int(couple2_)])

      else:

        time.sleep(delay1)

      playsound.playsound("C:\\Users\Jenni\OneDrive\Desktop\Phython.py\Sound\Amor_einschlafen.mp3")

    #Anschauen des Liebespaares (Working)

    if night_num == 1 and "Amor" in role_in_game:

      start = "false"

 

      while start != "true":

        while input_control.goon != "true":

          validation = input("Spieler Nummer: ")

          input_control(validation)

        input_control.goon = "false"

        if not validation.isnumeric() and validation != "s":

          validation = str(player.index(validation))

 

        if validation != "s" and len(player) >= int(validation):

          ht()

          penup()

          goto(0,300)

          color(font_color)

          if validation != "s" and len(player) >= int(validation):

            if couple1 == player_role[int(validation)]:

              write(player[int(validation)]+ " <3 " + player[int(couple2_)], align="center", font=("Courier", 40, "bold"))

            elif couple2 == player_role[int(validation)]:

              write(player[int(validation)] + " <3 " + player[int(couple1_)], align="center", font=("Courier", 40, "bold"))

            else:

              write("Du liebst nur dich Selbst!", align="center", font=("Courier", 40, "bold"))

 

          tracer(1)

          time.sleep(delay)

          clear()

          validation_num = validation_num + 1

 

        if validation == "s":

          start = "true"

      playsound.playsound("C:\\Users\Jenni\OneDrive\Desktop\Phython.py\Sound\Mittagsschlaf_aufwachen.mp3")

    #Buergermeisterwhal (Working)

    if major not in alive_role:

      playsound.playsound("C:\\Users\Jenni\OneDrive\Desktop\Phython.py\Sound\Buergermeisterwahl.mp3")

      if major not in dead_role:

        major = "Buergermeister"

        dead_role.append("Buergermeister")

      while input_control.goon != "true":

          major_ = input("Spieler Nummer des Buergermeisters: ")

          input_control(major_)

      input_control.goon = "false"

      if not major_.isnumeric():

          major_ = str(player.index(major_))

      major = major_.replace(major_,player_role[int(major_)])

      dead_role.remove("Buergermeister")

      alive_role.append(major)

   

    protecting = "none"

    visiting = "none"

    playsound.playsound("C:\\Users\Jenni\OneDrive\Desktop\Phython.py\Sound\Alle_schlafen_ein.mp3")

    ts.clear()

    ts.bgpic("C:\\Users\Jenni\OneDrive\Desktop\Phython.py\Werwolf_Nacht2.gif")

    tracer(1)

    tracer(0)

     

    if "Dorfmatratze" in role_in_game:

      playsound.playsound("C:\\Users\Jenni\OneDrive\Desktop\Phython.py\Sound\Dorfmatratze_aufwachen.mp3")

      if "Dorfmatratze" in alive_role:

        visiting = input("Bei welchem Spieler moechstest du uebernachten? : ")

        visiting = visiting.replace(visiting,player_role[int(visiting)])

 

      else:

        time.sleep(delay1)

      playsound.playsound("C:\\Users\Jenni\OneDrive\Desktop\Phython.py\Sound\Dorfmatratze_einschlafen.mp3")

    #Ritter beschützen (Working)

    if "Ritter der Nacht" in role_in_game:

      playsound.playsound("C:\\Users\Jenni\OneDrive\Desktop\Phython.py\Sound\Ritter_derNacht_erwachen.mp3")

      if "Ritter der Nacht" in alive_role:

        while input_control.goon != "true":

          protecting = input("Welchen Spieler moechtests du beschuetzen? :")

          input_control(protecting)

        input_control.goon = "false"

 

        if not protecting.isnumeric():

          protecting = str(player.index(protecting))

        protecting = protecting.replace(protecting,player_role[int(protecting)])

     

      else:

        time.sleep(delay1)

      playsound.playsound("C:\\Users\Jenni\OneDrive\Desktop\Phython.py\Sound\Ritter_der_Nacht_einschlafen.mp3")

    #Seher Ueberprüfen der Rolle (Working)

    if "Magischer Seher" in role_in_game:

      playsound.playsound("C:\\Users\Jenni\OneDrive\Desktop\Phython.py\Sound\Seher_erwachen.mp3")

      if "Magischer Seher" in alive_role:

        x = 1

        if koks == "true":

          x = 2

          koks = "false"

        for i in range(x):

 

          while input_control.goon != "true":

            viewing = input("Welchen Spieler moechter der Seher ueberpruefen? : ")

            input_control(viewing)

          input_control.goon = "false"

          if not viewing.isnumeric():

            viewing = str(player.index(viewing))

         

          tracer(0)

          ht()

          penup()

          goto(0,300)

          color(font_color)

          write(player_role[int(viewing)], align="center", font=("Courier", 40, "bold"))

          tracer(1)

          x = input("Drücke Enter um fortzufahren ")

          clear()

        else:

          time.sleep(delay1)

        playsound.playsound("C:\\Users\Jenni\OneDrive\Desktop\Phython.py\Sound\Seher_einschalfen.mp3")

    #Werwolf Ueberprüfen der Rolle (defekt)

    if "Magischer Werwolf" in role_in_game:

      playsound.playsound("C:\\Users\Jenni\OneDrive\Desktop\Phython.py\Sound\Magischer_Werwolf_erwachen.mp3")

      if "Magischer Werwolf" in alive_role:

        while input_control.goon != "true":

          stalking = input("Welchen Spieler moechtest du ueberpruefen? : ")

          input_control(stalking)

        input_control.goon = "false"

 

        if not stalking.isnumeric():

          stalking = str(player.index(stalking))

         

        tracer(0)

        ht()

        penup()

        goto(0,300)

        color(font_color)

        write(player_role[int(stalking)], align="center", font=("Courier", 40, "bold"))

        tracer(1)

       

        if stalking == "n1":

          print(role_not_in_game[0])

        if stalking == "n2":

          print(role_not_in_game[1])

        if stalking == "n3":

          print(role_not_in_game[2])

        if stalking == "n4":

          print(role_not_in_game[3])

        x = input("Drücke Enter um fortzufahren ")

        clear()

      else:

        time.sleep(delay1)

      playsound.playsound("C:\\Users\Jenni\OneDrive\Desktop\Phython.py\Sound\Magischer_Werwolf_einschalfen.mp3")

    #Werwolf Toeten (Working)

    if "Normaler Werwolf" in role_in_game or "Magischer Werwolf" in role_in_game:

      playsound.playsound("C:\\Users\Jenni\OneDrive\Desktop\Phython.py\Sound\Werwolf_erwachen.mp3")

      if "Normaler Werwolf" in alive_role or "Magischer Werwolf" in alive_role:

        x = 1

        if nachwuchs == "true":

          x = 2

          nachwuchs = "false"

        for i in range(x):

          while input_control.goon != "true":

            kill1_ = input("Welchen Spieler moechtest du toeten? : ")

            input_control(kill1_)

          input_control.goon = "false"

 

          if not kill1_.isnumeric():

            kill1_ = str(player.index(kill1_))

       

          kill1 = kill1_.replace(kill1_,player_role[int(kill1_)])

       

          if kill1 == visiting:

            alive_role.remove("Dorfmatratze")

            dead_role.append("Dorfmatratze")

     

          if kill1 != protecting and kill1 != "Dorfmatratze":

            if kill1 == "Harter Bursche" and haertester_bursche != "ture":

              if dead_night == "none":

                dead_night = night_num + 1

            elif kill1 == "Harter Bursche" and haertester_bursche == "ture":

              if dead_night == "none":

                dead_night = night_num + 1

            else:

              alive_role.remove(kill1)

              dead_role.append(kill1)

       

 

      else:

        time.sleep(delay1)

      playsound.playsound("C:\\Users\Jenni\OneDrive\Desktop\Phython.py\Sound\Werwolf_einschlafen.mp3")

    #Hexe (Working)

    if "Hexe" in role_in_game:

      playsound.playsound("C:\\Users\Jenni\OneDrive\Desktop\Phython.py\Sound\Hexe_aufwachen_retten.mp3")

      #Hexe Opfer anzeigen (Working)

      if "Hexe" in alive_role or "Hexe" == dead_role[-1]:

          tracer(0)

          ht()

          penup()

          goto(0,300)

          color(font_color)

          write("Opfer: " + player[int(kill1_)], align="center", font=("Courier", 40, "bold"))

          tracer(1)

      #Hexe Heilen (Working)

      if "Hexe" in alive_role and heal_potion == 1 or "Hexe" == dead_role[-1] and heal_potion == 1:

        heal = input("Moechtest du das Opfer retten? (ja/Enter) ")

        if heal == "ja" and heal_potion == 1 and protecting != kill1 and kill1 != "Harter Bursche":

          dead_role.remove(kill1)

          alive_role.append(kill1)

        if heal == "ja":

          heal_potion = 0

          if kill1 == "Harter Bursche":

            dead_night == "none"

      else:

        time.sleep(delay1)

      #Hexe Toeten (Working)

      playsound.playsound("C:\\Users\Jenni\OneDrive\Desktop\Phython.py\Sound\Hexe_handlung.mp3")

      if "Hexe" in alive_role or "Hexe" in dead_role[-1] and kill_potion == 1:

        while input_control.goon != "true":

          kill2_ = input("Welchen Spieler moechtest du toeten? (Spieler/Enter) : ")

          input_control(kill2_)

        input_control.goon = "false"

        kill2 = "none"

        if not kill2_.isnumeric() and kill2_ != "":

          kill2_ = str(player.index(kill2_))

        if kill2_ != "":

          kill_potion = 0

          kill2 = kill2_.replace(kill2_,player_role[int(kill2_)])

         

          if kill2 == visiting:

            alive_role.remove("Dorfmatratze")

            dead_role.append("Dorfmatratze")

           

          if kill2 != protecting and kill2 != "Dorfmatratze":

            if kill2 == "Harter Bursche" and haertester_bursche != "ture":

              if dead_night == "none":

                dead_night = night_num + 1

            elif kill2 == "Harter Bursche" and haertester_bursche == "ture":

              if dead_night == "none":

                dead_night = night_num + 1

            else:

              alive_role.remove(kill2)

              dead_role.append(kill2)

 

       

      else:

        time.sleep(delay1)

 

    if event == "true":

      events = ["Events: ","Wiederbelebung","Testament","Haertester Bursche","Trank","Trennung","Alter","Koffein","Verschlafen","Alpha Wolf","Nachwuchs"]

      random_event = random.randint(1,len(events)-1)

 

      if random_event == 1:

          x = len(dead_role)

          playsound.playsound("C:\\Users\Jenni\OneDrive\Desktop\Phython.py\Sound\Events\Wiederbeleben_start.mp3")

          while len(dead_role) == x:

            event_player = random.randint(1,len(dead_role)-1)

            m = player_role.index(dead_role[event_player])

            if player_role[m] in dead_role:

              playsound.playsound("C:\\Users\Jenni\OneDrive\Desktop\Phython.py\Sound\Spieler" + str(m) + ".mp3")

              playsound.playsound("C:\\Users\Jenni\OneDrive\Desktop\Phython.py\Sound\Events\Wiederbeleben_ende.mp3")

              alive_role.append(dead_role[event_player])

              dead_role.remove(dead_role[event_player])

         

      if random_event == 2:

          event_player = random.randint(1,len(player_role))

          m = player_role.index(player_role[event_player])

          if major in alive_role:

            alive_role.remove(major)

          if major not in alive_role:

            dead_role.remove(major)

          major = player_role[event_player]

          alive_role.append(player_role[event_player])

          playsound.playsound("C:\\Users\Jenni\OneDrive\Desktop\Phython.py\Sound\Events\Testament_start.mp3")

          playsound.playsound("C:\\Users\Jenni\OneDrive\Desktop\Phython.py\Sound\Spieler" + str(m) + ".mp3")

          playsound.playsound("C:\\Users\Jenni\OneDrive\Desktop\Phython.py\Sound\Events\Testament_ende.mp3")

       

      if random_event == 3:

        haertester_bursche = "true"

             

      if random_event == 4:

        random_event = random.randint(1,5)

        if random_event == 1:

          heal_potion = heal_potion + 1

        if random_event == 2:

          kill_potion = kill_potion + 1

        if random_event == 3:

          heal_potion = heal_potion - 1

        if random_event == 4:

          kill_potion = kill_potion - 1

 

      if random_event == 5:

        couple1 = "none"

        couple2 = "nome"

 

      if random_event == 6:

        event_player = random.randint(1,len(player_role))

        m = player_role.index(player_role[event_player])

        if player_role[m] in alive_role:

          alive_role.remove(player_role[m])

          dead_role.append(player_role[m])

        else:

          pass

 

      if random_event == 7:

        koks = "true"

 

      if random_event == 8:

        print("Event 8")

      if random_event == 9:

        print("Event 9")

      if random_event == 10:

        nachwuchs = "true"

 

    if "Amor" in role_in_game:

      if couple1 in dead_role and couple2 not in dead_role:

        alive_role.remove(couple2)

        dead_role.append(couple2)

      if couple2 in dead_role and couple1 not in dead_role:

        alive_role.remove(couple1)

        dead_role.append(couple1)

   

    if "Harter Bursche" in role_in_game and dead_night == night_num:

      alive_role.remove("Harter Bursche")

      dead_role.append("Harter Bursche")

 

    if werewolf_number == 0 or innocent_number <= 1 or gerber_win == "true" or liebespaar_win == "true":

      if werewolf_number == 0:

        playsound.playsound("C:\\Users\Jenni\OneDrive\Desktop\Phython.py\Sound\Dorfbewohner_sieg.mp3")

      if innocent_number == 1:

        playsound.playsound("C:\\Users\Jenni\OneDrive\Desktop\Phython.py\Sound\Werwolf_sieg.mp3")

      if gerber_win == "true":

        playsound.playsound("C:\\Users\Jenni\OneDrive\Desktop\Phython.py\Sound\Gerber_sieg.mp3")

      if liebespaar_win == "true":

        print("Das Liebespaar hat Gewonnen!")

      x = input("Drücke Enter um fortzufahren ")

      werewolf_game()

 

    ts.clear()

    ts.bgpic("C:\\Users\Jenni\OneDrive\Desktop\Phython.py\WerwolfTag2.gif")

    tracer(1)

    tracer(0)

 

    playsound.playsound("C:\\Users\Jenni\OneDrive\Desktop\Phython.py\Sound\Alle_wachen_auf.mp3")

    if len(dead_role) != 0:

      playsound.playsound("C:\\Users\Jenni\OneDrive\Desktop\Phython.py\Sound\Ausser.mp3")

 

      for i in range(1, len(player_role)):

        if player_role[i] in dead_role:

          playsound.playsound("C:\\Users\Jenni\OneDrive\Desktop\Phython.py\Sound\Spieler" + str(i) + ".mp3")

    #Vote (Working)

    vote = "true"

    if vote == "true":

      while input_control.goon != "true":

          vote_kill_ = input("Spieler Nummer des verdaechtigen Spielers (Spieler Nummer/enter) ")

          input_control(vote_kill_)

      input_control.goon = "false"

      if not vote_kill_.isnumeric() and vote_kill_ != "":

        vote_kill_ = str(player.index(vote_kill_))

      if vote_kill_ != "":

        vote_kill = vote_kill_.replace(vote_kill_,player_role[int(vote_kill_)])

     

        if vote_kill in alive_role:

          alive_role.remove(vote_kill)

          dead_role.append(vote_kill)

          if vote_kill == "Gerber":

            gerber_win = "true"

        if vote_kill_ != "":

          playsound.playsound("C:\\Users\Jenni\OneDrive\Desktop\Phython.py\Sound\Beginn_Hinrichtung.mp3")

          playsound.playsound("C:\\Users\Jenni\OneDrive\Desktop\Phython.py\Sound\Spieler" + vote_kill_ + ".mp3")

          playsound.playsound("C:\\Users\Jenni\OneDrive\Desktop\Phython.py\Sound\Ende_Hinrichtung.mp3")

       

        if "Amor" in role_in_game:

          if couple1 in dead_role and couple2 not in dead_role:

            alive_role.remove(couple2)

            dead_role.append(couple2)

          if couple2 in dead_role and couple1 not in dead_role:

            alive_role.remove(couple1)

            dead_role.append(couple1)

     

    #Buergermeister tot (working)

    if major in dead_role:

      alive_role.remove(major)

      dead_role.append("Buergermeister")

   

    werewolf_number = alive_role.count("Normaler Werwolf") + alive_role.count("Magischer Werwolf")

    innocent_number = len(alive_role) - werewolf_number

 

    if  couple1 in alive_role and couple2 in alive_role and len(alive_role) <= 2:

      liebespaar_win = "true"

 

    #Gewinnnen (Liebespaar fehlt)

 

    if werewolf_number == 0 or innocent_number <= 1 or gerber_win == "true" or liebespaar_win == "true":

      if werewolf_number == 0:

        playsound.playsound("C:\\Users\Jenni\OneDrive\Desktop\Phython.py\Sound\Dorfbewohner_sieg.mp3")

      if innocent_number == 1:

        playsound.playsound("C:\\Users\Jenni\OneDrive\Desktop\Phython.py\Sound\Werwolf_sieg.mp3")

      if gerber_win == "true":

        playsound.playsound("C:\\Users\Jenni\OneDrive\Desktop\Phython.py\Sound\Gerber_sieg.mp3")

      if liebespaar_win == "true":

        print("Das Liebespaar hat Gewonnen!")

      x = input("Drücke Enter um fortzufahren ")

      werewolf_game()




werewolf_game()

 

#Paar nach Vote umbringe