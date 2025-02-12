import turtle
import time
import random

screen_size = 200
space = 15
bat_size = 20
screen = turtle.Screen()
screen.setworldcoordinates(0,0,screen_size,screen_size)
screen.bgcolor(0,0,0)
pen = turtle.Turtle()
pen.ht()
pen.speed(screen_size/2)
pen.penup()
pen.right(90)
delay = 0.01
random_faktor = 20
tolerance = 5

class objekts:
  
  def __init__(self, shape, color, size):
    self.shape = shape
    self.color = color
    self.size = size
    
  def draw(self, position):
    pen.goto(position)
    
    if self.shape == "bat":
      pen.pendown()
      pen.color(self.color)
      pen.begin_fill()
      pen.forward(self.size/2)
      pen.right(90)
      pen.forward(2)
      pen.right(90)
      pen.forward(self.size)
      pen.right(90)
      pen.forward(2)
      pen.right(90)
      pen.forward(self.size)
      pen.end_fill()
      pen.penup()
      
    if self.shape == "ball":
      pen.forward(self.size)
      pen.right(90)
      pen.forward(self.size)
      pen.color(self.color)
      pen.begin_fill()
      pen.circle(self.size)
      pen.end_fill()
      pen.penup()
      pen.back(self.size)
      pen.left(90)  
      pen.back(self.size)
      
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
  
pen.tracer(0)
obj1 = objekts("bat","red",bat_size)
obj1_cord = (space,screen_size/2)
obj1.draw(obj1_cord)

obj2 = objekts("bat","red", bat_size)
obj2_cord = (screen_size-space,screen_size/2)
obj2.draw(obj2_cord)

obj3 = objekts("ball","red", 2)
obj3_cord = (screen_size/2,screen_size/2)
obj3.draw(obj3_cord)
pen.tracer(1)

move_direction = 0

def up():
  global move_direction
  move_direction = 1
  
def down():
  global move_direction
  move_direction = -1

def stop():
  global move_direction
  move_direction = 0
  
def vector_length(vector):
  length = (vector[0]**2+vector[1]**2)**.5
  vector = (vector[0]*(1/length),vector[1]*(1/length))
  return vector

def bounce(wall, last_vector):
  if wall == "wall":
    move_vector = (last_vector[0],last_vector[1]*(-1))
  elif wall == "bat":
    move_vector = ((last_vector[0]+random.randint(-10,10)/random_faktor)*(-1),last_vector[1]+random.randint(-10,10)/random_faktor)
  else:
    move_vector = (2,0)
  move_vector = vector_length(move_vector)
  return move_vector

move_vector = bounce(False, (0,0))

while True:
  time.sleep(delay)
  pen.tracer(0)
  screen.listen()
  x1, y1 = obj1_cord
  x2, y2 = obj2_cord
  
  screen.onkey(up,"w")
  screen.onkey(down,"s")
  screen.onkey(stop,"x")
  
  clear()
  y1 += move_direction
  obj1_cord = x1, y1
  obj1.draw(obj1_cord)
  
  y2 += move_direction
  obj2_cord = x2, y2
  obj2.draw(obj2_cord)
    
  if y1 >= screen_size-space or y1 <= space:
    move_direction = 0
  
  obj3_cord = (obj3_cord[0]+move_vector[0],obj3_cord[1]+move_vector[1])
  obj3.draw(obj3_cord)
  
  if (obj3_cord[0] <= space or obj3_cord[0] >= screen_size-space) and (y1-bat_size+tolerance < obj3_cord[1] < y1+bat_size+tolerance or y2-bat_size+tolerance < obj3_cord[1] < y2+bat_size+tolerance):
    move_vector = bounce("bat", move_vector)
    print("Block")
  
  if (obj3_cord[0] <= space or obj3_cord[0] >= screen_size-space) and not (y1-bat_size+tolerance < obj3_cord[1] < y1+bat_size+tolerance or y2-bat_size+tolerance < obj3_cord[1] < y2+bat_size+tolerance):
    print("score")
    obj3_cord = (screen_size/2,screen_size/2)
    
  if obj3_cord[1] <= 0 or obj3_cord[1] >= screen_size:
    move_vector = bounce("wall", move_vector)

  
  pen.tracer(1)