import pygame
import random
import time

# Initialize Pygame
pygame.init()


# Constants
global screen_history
screen_info = pygame.display.Info()
screen_width, screen_height = screen_info.current_w, screen_info.current_h
resolution = (screen_width, screen_height)
font_basic = pygame.font.SysFont('Corbel', 20)
screen = pygame.display.set_mode(resolution)
caption = pygame.display.set_caption("Werewolf")
click_method = pygame.MOUSEBUTTONUP
font_color_basic = (255, 255, 255)

# __________________________________________________________________________________________________________________________________________________________________________#

#Getestete Rollen: Dorfbewohner, Magischer Seher, Magischer Werwolf, Amor, Ritter der Nacht, Normaler Werwolf, Gebildeter Henker, Hexe, Dorfmatratze, Harter Bursche
#Geplante / Defekte Rollen: Alter Mann      Max 9 spierler (ansonsten villeicht noch Dorfbewohner hinzufügen, weiß aber nicht ob das Funktioiert)
player_number = 4
important_role = ["Magischer Werwolf","Hexe"]
possible_role = ["Harter Bursche","Dorfbewohner","Gerber","Magischer Seher","Dorfmatratze","Ritter der Nacht","Amor"]

# __________________________________________________________________________________________________________________________________________________________________________#

# Load and scale images
def load_and_scale_image(filename):
    original_image = pygame.image.load(filename)
    return pygame.transform.scale(original_image, resolution)

background_images_folder = "background_images"
main_folder = "werewolf_game"
menu_screen = load_and_scale_image(background_images_folder+"/menu_screen.png")
game_screen1 = load_and_scale_image(background_images_folder+"/game_screen1.png")
role_selection1 = load_and_scale_image(background_images_folder+"/role_selection.png")
bg_image_day = load_and_scale_image(background_images_folder+"/Werwolf_Tag.gif")
bg_image_night = load_and_scale_image(background_images_folder+"/Werwolf_Nacht.gif")
music_folder = "Music"

# Define a Button class
class Button:
    def __init__(self, text, coordinates, offset):
        self.text = text
        self.coordinates = coordinates
        self.rect = pygame.Rect(
            coordinates[0] - offset[0] / 2,
            coordinates[1] - offset[1] / 2,
            offset[0],
            offset[1],
        )
             
    def draw_button(self, screen, is_active):
        color = button_colors[0] if is_active else button_colors[1]
        pygame.draw.rect(screen, color, self.rect)
        text_surface = font_basic.render(self.text, True, font_color_basic)
        text_rect = text_surface.get_rect(center=self.rect.center)
        screen.blit(text_surface, text_rect)

# Create button objects
button_offsets_rectangle = (100, 30)
button_offsets_square = (30, 30)
button_offsets_player = (100, 50)
button_colors = ((170, 170, 170), (100, 100, 100))
buttons_ui = ["Play", "Settings", "Roles", "Main"]
buttons_ui_coordinates = [[resolution[0]/2, resolution[1]/2 + i*resolution[1]*0.06] for i in range(len(buttons_ui))]
buttons_players = [f"{i}" for i in range(player_number)]
buttons_players_coordinates = [[resolution[0]*.5-(len(buttons_players)-1)/2*button_offsets_player[0]+i* button_offsets_player[0], resolution[1]*.9] for i in range(len(buttons_players))]
button_ui_objects = [Button(text, coord, button_offsets_rectangle) for text, coord in zip(buttons_ui, buttons_ui_coordinates)]
button_permanent_objects = [
    Button("x", (resolution[0]*.99,resolution[1]*.01), button_offsets_square), 
    Button("<", (resolution[0]*.01,resolution[1]*.01), button_offsets_square), 
    Button("->", (resolution[0]*.9,resolution[1]*.9), button_offsets_rectangle)
    ]
button_player_objects = [Button(text, coord, button_offsets_player) for text, coord in zip(buttons_players, buttons_players_coordinates)]
buttons_role = ["Magischer Werwolf","Hexe","Amor","Harter Bursche","Dorfbewohner","Gerber","Magischer Seher","Dorfmatratze","Ritter der Nacht"] + ["Delete"]
buttons_role_coordinates = [[resolution[0]/2, resolution[1]*.2 + i*resolution[1]*0.06] for i in range(len(buttons_role))]
buttons_role_objects = [Button(text, coord, button_offsets_rectangle) for text, coord in zip(buttons_role, buttons_role_coordinates)]

def create_label(text, title):
    if title:
        coordinates = (screen_width*.5, screen_height*.1)
        offset = (300,60)
    else:
        coordinates =  (screen_width*.5, screen_height*.5)
        offset = (200,50)
    label = Button(text, coordinates, offset)
    label.draw_button(screen, False)

# Define functions for button actions
def player_selection(title, bg_image, button_players=True, label=None):
    if button_players: screen_buttons = button_player_objects + button_permanent_objects
    else: screen_buttons = button_permanent_objects

    action = None
    while not action:
        mouse_position = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == click_method:
                for button in screen_buttons:
                    if button.rect.collidepoint(mouse_position):
                        if button.text in button_functions:
                            button_functions[button.text]()
                        else: action = button.text
                        if action == "->": action = "quit"

        screen.blit(bg_image, (0, 0)) 
        if label != None:
            create_label(label, False)                 
        create_label(title, True)
        for button in screen_buttons:
            button.draw_button(screen, button.rect.collidepoint(mouse_position))
        pygame.display.update()
    return action

def settings():
    if screen_history [-1] != settings:
        screen_history.append(settings)
    while True:
        mouse_position = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == click_method:
                for button in button_ui_objects:
                    if button.rect.collidepoint(mouse_position):
                        if button.text in button_functions:
                            button_functions[button.text]()
        screen.blit(game_screen1, (0, 0))
        pygame.display.update()

def role_selection():
    screen_buttons = buttons_role_objects + button_permanent_objects
    if screen_history [-1] != role_selection:
        screen_history.append(role_selection)
    
    while True:
        mouse_position = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == click_method:
                for button in screen_buttons:
                    if button.rect.collidepoint(mouse_position):
                        if button.text in button_functions:
                            button_functions[button.text]()

        screen.blit(role_selection1, (0, 0))
        for button in screen_buttons:
            button.draw_button(screen, button.rect.collidepoint(mouse_position))
        pygame.display.update()

def main_menu():
    screen_buttons = button_ui_objects + button_permanent_objects
    if (screen_history [-1] != main_menu): screen_history.append(main_menu)
    while True:
        mouse_position = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT: pygame.quit()
            if event.type == click_method:
                for button in screen_buttons:
                    if button.rect.collidepoint(mouse_position):
                        if button.text in button_functions:
                            button_functions[button.text]()

        screen.blit(menu_screen, (0, 0))
        for button in screen_buttons:
            button.draw_button(screen, button.rect.collidepoint(mouse_position))
        
        pygame.display.update()

def exit():
    pygame.quit()

def screen_back():
    global screen_history
    if len(screen_history) > 1:
        screen_history.pop()
        if screen_history:
            screen_history[-1]()

def role_distibution(important_role, possible_role):

    role_in_game = important_role + possible_role
    dead_role = []

    player_role = {str(i):None for i in range(player_number)}
    needs_a_role = [str(i) for i in range(player_number)]

    length_needs_a_role = len(needs_a_role)-1
    while len(needs_a_role) !=0:

        random_player = random.randint(0,length_needs_a_role)
        random_role = random.randint(0,len(important_role)-1) if len(important_role) != 0 else random.randint(0,len(possible_role)-1)

        if player_role.get(str(random_player)) is None:
            if len(important_role) > 0:
                player_role[str(random_player)] = important_role[random_role]
                important_role.remove(important_role[random_role])
            else:
                player_role[str(random_player)] = possible_role[random_role]
                possible_role.remove(possible_role[random_role])
            needs_a_role.remove(str(random_player))
        
    alive_role = [player_role[str(i)] for i in range(len(player_role))]
    return player_role, alive_role, dead_role, role_in_game

def show_roles(player_role, title, max_reveals=1, specific_palyer=None, bg_image = bg_image_night):
    reveals = 0
    while True and reveals < max_reveals:
        if specific_palyer == None:
            player = player_selection(title, bg_image)
            if player == "quit": break
            create_label(player_role.get(str(player)), False)
            pygame.display.update()
            time.sleep(1)
        else: 

            player = player_selection(title, bg_image, False, specific_palyer)
            pygame.display.update()
        reveals += 1

def show_couple(lovers, title, max_reveals=1):
    reveals = 0
    while True and reveals < max_reveals:
        player = player_selection(title, bg_image_day)
        if player == "quit": break
        if str(player) == lovers[0]: create_label(lovers[1], False)
        elif str(player) == lovers[1]: create_label(lovers[0], False)
        else: create_label("Yourself! You narcissist!", False)
        pygame.display.update()
        time.sleep(1)
        reveals += 1

def play_music(file, bg_image=bg_image_night):
    screen.blit(bg_image, (0, 0))
    pygame.display.update()
    pygame.mixer.music.load(f"{music_folder}\{file}.mp3")
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(5)

def game_loop():
    win_villager = win_werewolf = win_gerber = win_couple = False

    day = 1
    healpotion = 1
    killpotion = 1
    tuff_man_kill = False

    player_role, alive_role, dead_role, role_in_game = role_distibution(important_role, possible_role)
    show_roles(player_role, "Your Role is:", 100, None, bg_image = bg_image_day)

    while win_villager == win_werewolf == win_gerber == win_couple == False:
        delay = random.randint(3,8)
        visited = protected = attacked = None
        print(len(alive_role) - alive_role.count("Magischer Werwolf") - alive_role.count("Werwolf"))
        print(alive_role)

        if day == 1:
            lover1 = lover2 = None
            if ("Amor" in role_in_game and day ==1):
                play_music("Mittagsschlaf_Einschlafen", bg_image_day)
                play_music("Amor_Aufwachen", bg_image_day)
                if "Amor" in alive_role: lover1, lover2 = player_selection("Select first player", bg_image_day), player_selection("Select second player", bg_image_day)
                else: time.sleep(delay)
                play_music("Amor_Einschlafen", bg_image_day)
                show_couple((lover1,lover2), "You are in love with", 100)
                play_music("Mittagsschlaf_Aufwachen", bg_image_day)
                

        if "major" not in alive_role:
            play_music("Bürgermeister_Wahl", bg_image_day)
            major = player_selection("Select a major", bg_image_day)
            alive_role.append("major")
        
        play_music("Einschlafen_alle")
        
        if "Dorfmatratze" in role_in_game:
            play_music("Dorfmatratze_Aufwachen")
            if "Dorfmatratze" in alive_role: visited = player_selection("Who do you want to visit?", bg_image_night)
            else: time.sleep(delay)
            play_music("Dorfmatratze_Einschlafen")

        if "Ritter der Nacht" in role_in_game:
            play_music("Ritter_Erwachen")
            if "Ritter der Nacht" in alive_role: protected = player_selection("Who do you want to protect?", bg_image_night)
            else: time.sleep(delay)
            play_music("Ritter_Einschlafen")
        
        if "Magischer Seher" in role_in_game:
            play_music("Seher_Erwachen")
            if "Magischer Seher" in alive_role: show_roles(player_role, "Which role do you want to see?")
            else: time.sleep(delay)
            play_music("Seher_Einschlafen")

        if "Magischer Werwolf" in role_in_game:
            play_music("Magischer_Werwolf_Erwachen")
            if "Magischer Werwolf" in alive_role: show_roles(player_role, "Which role do you want to see?")
            else: time.sleep(delay)
            play_music("Magischer_Werwolf_Einschlafen")

        if "Magischer Werwolf" in alive_role or "Werwolf" in alive_role:
            play_music("Werwolf_Erwachen")
            if "Magischer Werwolf" in alive_role or "Werwolf" in alive_role: attacked = player_selection("Who do you want to eat?", bg_image_night)
            else: time.sleep(delay)
            play_music("Werwolf_Einschlafen")

        if "Hexe" in role_in_game:
            play_music("Hexe_Erwachen")
            if "Hexe" in alive_role:
                show_roles(player_role, "The attacked player is:", 1, attacked)
                if healpotion != 0: healed = player_selection("Do you want to heal a player?", bg_image_night)
                if healed != "quit": healpotion -= 1
                if killpotion != 0: poisened = player_selection("Who do you want to kill?", bg_image_night)
                if poisened != "quit": killpotion -= 1
            else: time.sleep(delay)
            play_music("Hexe_Einschlafen")
        
        for _ in range(2):
            for player in player_role:
                if (attacked == player or poisened == player) and (protected != player or healed != player) or (player_role[player] in dead_role) or (player_role[player] == "Harter Bursche" and tuff_man_kill == True):
                    if (player_role[player] != "Harter Bursche") or (player_role[player] == "Harter Bursche" and tuff_man_kill):
                        if (player_role[player] == "Harter Bursche" and tuff_man_kill): tuff_man_kill = False
                        if player_role[player] != "Dorfmatratze": dead_role.append(player_role[player])
                        if (visited == player): dead_role.append("Dorfmatratze")
                        if (lover1 == player): dead_role.append(player_role[lover2])
                        if (lover2 == player): dead_role.append(player_role[lover1])
                        if (major in dead_role): dead_role.append("Bürgermeister")
                    else: tuff_man_kill = True

        play_music("Aufwachen_alle", bg_image_day)
        play_music("Ausser", bg_image_day)
        for player in player_role:
            if player_role[player] in dead_role:
                play_music("Spieler"+str(int(player)+1), bg_image_day)
        
        screen.blit(game_screen1, (0, 0))
        vote = player_selection("Who should be executed?", bg_image_day)
        if vote:
            play_music("Hinrichtung_Beginn", bg_image_day)
            dead_role.append(player_role[vote])
            if (lover1 == vote): dead_role.append(player_role[vote])
            if (lover2 == vote): dead_role.append(player_role[vote])
            if (major == vote): dead_role.append("Bürgermeister")
            play_music("Spieler"+str(int(vote)+1), bg_image_day)
            play_music("Hinrichtung_Ende", bg_image_day)

        day += 1

        if ("Magischer Werwolf" not in alive_role and "Werwolf" not in alive_role): 
            win_villager = True
            play_music("Sieg_Dorfbewohner", bg_image_day)
        if (len(alive_role) == 2 and player_role[lover1] in alive_role and player_role[lover1] in alive_role):
            win_couple = True
            play_music("Sieg_Dorfbewohner", bg_image_day)
        if (player_role[vote] == "Gerber"): 
            win_gerber = True
            play_music("Sieg_Gerber", bg_image_day)
        if (len(alive_role) - alive_role.count("Magischer Werwolf") - alive_role.count("Werwolf") <= alive_role.count("Magischer Werwolf") + alive_role.count("Werwolf")): 
            win_werewolf = True
            play_music("Sieg_Werwolf", bg_image_day)
    
    game_loop()

screen_history = [main_menu] 
button_functions = {
    "Play": game_loop,
    "Settings": settings,
    "Roles": role_selection,
    "Main": main_menu,
    "x": exit,
    "<": screen_back,
}

if __name__ == "__main__": main_menu()
