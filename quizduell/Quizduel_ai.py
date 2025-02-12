from PIL import Image 
import pytesseract as tess

import numpy as np 
import cv2 
import pyautogui, sys
import time
import random

from Bard import Chatbot

region_question = (700, 230, 500, 270)
regions_awnser = ((690, 610, 240, 120),(970, 610, 240, 120),(690, 760, 240, 120),(970, 760, 240, 120))

def anwser_question():
    time.sleep(2)
    question = screen_shot_text(region_question, "screenshot.png")

    awnser0 = screen_shot_text(regions_awnser[0],"awnser"+str(0)+".png")
    awnser1 = screen_shot_text(regions_awnser[1],"awnser"+str(1)+".png")
    awnser2 = screen_shot_text(regions_awnser[2],"awnser"+str(2)+".png")
    awnser3 = screen_shot_text(regions_awnser[3],"awnser"+str(3)+".png")


    Secure_1PSID  = "dQgGmMzJjMDrMXsAoovMN1vhsoSvYjjZ7GkjD5ieViDwiKwqEQgUh1yENF9x8LzwiLNweQ."
    Secure_1PSIDTS = "sidts-CjEBNiGH7i5l0VOFBlQKozjSljHalSsFpg_w8Xqrr6Vylh01hO-qstUg4cZv1zXjaoYrEAA"

    chatbot = Chatbot(Secure_1PSID, Secure_1PSIDTS)
    output = chatbot.ask(f"Frage: {question} , Antwort Möglichkeiten: A: {awnser0}, B: {awnser1}, C: {awnser2}, D: {awnser3}. Bitte Wiederhohle nur die richtige Antwort Möglichkeit.")
    bard_awnser = list(output.values())[0]
    start_index = bard_awnser.find("**")
    string = bard_awnser[start_index+2:start_index+3]

    print(string)

    if string == "A": pyautogui.click(x=820, y=670)
    elif string == "B": pyautogui.click(x=1100, y=670)
    elif string == "C": pyautogui.click(x=820, y=820)
    elif string == "D": pyautogui.click(x=1100, y=820)
    else: pyautogui.click(x=820, y=670)

def screen_shot_text(region, file_name):
    image = pyautogui.screenshot(region=(region))
    image = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR) 
    cv2.imwrite(file_name, image) 


    tess.pytesseract.tesseract_cmd = r"C:\Users\lecke\AppData\Local\Programs\Tesseract-OCR\tesseract.exe"
    image_path = file_name

    img = Image.open(image_path) 
    text = tess.image_to_string(img) 
    text = text[:-1]
    return text

#anwser_question()

def cursor():
    try:
        while True:
            time.sleep(1)
            x, y = pyautogui.position()
            positionStr = 'X: ' + str(x).rjust(4) + ' Y: ' + str(y).rjust(4)
            print(positionStr, end='')
            print('\b' * len(positionStr), end='', flush=True)
    except KeyboardInterrupt:
        print('\n')

def scroll_down():
    pyautogui.moveTo(970, 600)
    pyautogui.dragTo(970, 415, 0.5, button='left')
    time.sleep(3)

def play_game(coordinates):
    pyautogui.click(x=coordinates[0]+0.5*coordinates[2], y=coordinates[1]+0.5*coordinates[3])
    time.sleep(1)

def accept_game():
    pyautogui.click(x=970, y=680)
    time.sleep(1)

def select_category():
    time.sleep(4)
    category = random.randint(0,2)
    pyautogui.click(x=970, y=350+200*category)

def press_go_on():
    time.sleep(2)
    pyautogui.click(x=970, y=970)

def setup_game():
    time.sleep(2)
    pyautogui.click(x=50, y=830)
    time.sleep(0.2)
    pyautogui.click(x=50, y=830)
    time.sleep(15)
    for _ in range(2):
        if check_for("quizduell", (750,400, 110, 30)):
            pyautogui.click(x=800, y=350)
            time.sleep(0.2)
            pyautogui.click(x=800, y=350)
            time.sleep(10)
    time.sleep(15)
    check_for_annoying_windows()

def check_for_annoying_windows():
    if check_for("belohnung",(900,450,120,40)):
        pyautogui.click(x=970, y=470)
    time.sleep(2)

def reset_game():
    time.sleep(3)
    pyautogui.keyDown('alt')
    pyautogui.press('f4')
    pyautogui.keyUp('alt')
    time.sleep(2)
    pyautogui.click(x=1000, y=580)
    time.sleep(5)

def end_current_game():
    time.sleep(2)
    pyautogui.click(x=730, y=140)

def turn():
    press_go_on()
    for _ in range(3):
        anwser_question()
        press_go_on()

def first_turn():
    press_go_on()
    select_category()
    turn()

def game_loop():
    time.sleep(5)        
    press_go_on()
    time.sleep(2)
    #Check for category selection
    if not check_for("spielen", (850, 930, 200, 70)):
        first_turn()
        #reset_game()
        #auto_play_game()
    else: 
        turn()
    time.sleep(10)    
    game_loop()

def wait_for_check(string, coordinates, state, delay=60):
    if check_for(string, coordinates, 2) != state:
        print("waiting...")
        time.sleep(delay)
        wait_for_check(string, coordinates, state)

def check_for(string, coordinates, hard_check=1):
    text = screen_shot_text(coordinates, "setup_control.png")
    if hard_check == 1: return text.lower() == string.lower()
    elif hard_check == 2: return string.lower() in text.lower()

def search_for(string, coordinates, direction):
    x, y, x1, y1 = coordinates
    if not check_for(string, coordinates, 2):
        if direction == "x": x += 5
        else:  y += 5
        return search_for(string, (x, y, x1, y1), direction)
    else: 
        return (x, y, x1, y1)
    
def wait_for_god_damm_ads(start_coordinates = (0, 0), offset = 160, screen_range = 20):
    # time.sleep(20)
    found = False
    x, y = start_coordinates
    print(offset)
    for i in range(screen_range):
        for j in range(screen_range//2): 
            if check_for("xxxx",(x+j*offset, y+i*offset, offset, offset), hard_check=2):
                found = True
                break
        if found: break
    if offset != 40: wait_for_god_damm_ads((int(x+j*offset),int(y+i*offset)), int(offset/2), screen_range//2)
    else: pyautogui.click(x=x+j*offset+offset*0.5, y=y+i*offset+offset*0.5)
                

def auto_play_game():
    setup_game()
    scroll_down()
    time.sleep(3)
    play_game_coordinates = search_for("spiel", (720, 300, 100,40), "y")
    wait_for_check("spielen", play_game_coordinates, True, delay=60)
    play_game(play_game_coordinates)
    time.sleep(2)
    #Accept and Play Game
    if check_for("spielen", (820, 640, 280, 60)):
        accept_game()
game_loop()

#auto_play_game()

#cursor()

# Quizduell: 850 20 1070 70
#Middle 970
#Spielen bei herausforderung (720, 620, 100, 40) Mitte 750 720
#Weiter 970 970
#Frage 700 230 500 270
# awnser0 = (690, 610, 240, 120) 
# awnser0_middle = (820, 670)
# awnser1 = (970, 610, 240, 120) 
# awnser1_middle = (1100, 670)
# awnser2 = (690, 760, 240, 120) 
# awnser2_middle = (820, 820)
# awnser2 = (970, 760, 240, 120) 
# awnser2_middle = (1100, 820)
#Spielen2 850 930 200 70 Mitte 970 970
#Spiel Akzeptieren 820 640 280 60 Mitte 970 680
