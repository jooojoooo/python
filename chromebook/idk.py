import turtle
import random
import time

global player_coord

screen_size = 200

screen = turtle.Screen()
screen.setworldcoordinates(0,0,screen_size,screen_size)
screen.bgcolor(0,0,0)

pen = turtle.Turtle()
pen.ht()
pen.speed(100)
pen.penup()

delay = 0.01
speed = 0.50

move_direction = 0

player_size = 5
bonus_size = 0

    
class player:
  def __init__(self, color, size):
    self.color = color
    self.size = size
    
  def draw(self, start_position, bonus_size):
    pen.goto(start_position)
    pen.pendown()
    pen.color(self.color)
    pen.begin_fill()
    pen.circle(self.size+bonus_size)
    pen.end_fill()
    pen.penup()

def clear():
  pen.penup()
  pen.goto(0,0)
  pen.pendown()
  pen.color(0,0,0)
  pen.begin_fill()
  pen.goto(0,screen_size)
  pen.goto(screen_size,screen_size)
  pen.goto(screen_size,0)
  pen.goto(0,0)
  pen.end_fill()

player1 = player("lime",player_size)

def left():
  global player_coord
  move_direction = -1
  
def right():
  global player_coord
  move_direction = 1
  
while True:
  pen.tracer(0)
  time.sleep(delay)
  clear()
  
  screen.listen()
  screen.onkey(left,"a")
  screen.onkey(right,"d")
  screen.onkey(left,"Left")
  screen.onkey(right,"Right")
  
  player1.draw(player_coord)
  
  if (loop % 200) == 0:
    speed += speed_buff
  
  if (loop % round(20/speed)) == 0:
    obstacles.append(obstacle("red",1))
    random_lane = random.randint(0,lane_number-1)
    obstacle_coordinates.append((lane_coordinates[random_lane][0],lane_coordinates[random_lane][1]))
  
  for i in range(len(obstacle_coordinates)):
    x, y = obstacle_coordinates[i]
    y -= speed
    obstacle_coordinates[i] = (x,y)
    obstacles[i].draw(obstacle_coordinates[i])
  
  if obstacle_coordinates[0][1] < -20:
      obstacles.pop(0)
      obstacle_coordinates.pop(0)
  
  if any(player_coord[1]-player_size > obstacle_coordinates[i][1]-obstacle_size > player_coord[1]-player_size*2 and obstacle_coordinates[i][0] == player_coord[0] for i in range(len(obstacles))):
    pen.penup()
    pen.goto(screen_size/2,screen_size-20)
    pen.color("white")
    pen.pendown()
    pen.write("Score: "+str(loop*delay*2),font=("arial",10),align="center")
    pen.tracer(1)
    exit()

  loop += 1
  pen.tracer(1)