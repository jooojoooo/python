import turtle
import random
import time

objects = 1000
screen_hight = 100
screen_widht = 100
spacing = screen_hight/objects

screen = turtle.Screen()
screen.setworldcoordinates(0,0,screen_widht,screen_hight)
screen.bgcolor(0,0,0)
pen = turtle.Turtle()
pen.penup()
pen.goto(0,0)
pen.pendown()
pen.speed(10)
pen.left(90)


class rect:
  
  def __init__(self,r,g,b,hight,x_pos):
    self.r = r
    self.g = g
    self.b = b
    self.hight = hight
    self.x_pos = x_pos
    
  def draw(self):
    pen.color(self.r,self.g,self.b)
    pen.begin_fill()
    for i in range(2):
      pen.forward(self.hight)
      pen.right(90)
      pen.forward(spacing)
      pen.right(90)
    pen.right(90)
    pen.forward(spacing)
    pen.left(90)
    pen.end_fill()
      
rects = []
for i in range(objects):
  rects.append(rect(i*(255/objects),i*(255/objects),250,i*(screen_hight/objects)+screen_hight/objects,i))

def clear():
  pen.penup()
  pen.goto(0,0)
  pen.pendown()
  pen.color(0,0,0)
  pen.begin_fill()
  pen.goto(0,screen_hight)
  pen.goto(screen_widht,screen_hight)
  pen.goto(screen_widht,0)
  pen.goto(0,0)
  pen.end_fill()
  
def draw_rects(list):
  pen.tracer(0)
  clear()
  for item in list:
    item.draw()
  pen.tracer(1)

draw_rects(rects)
x = input()

random.shuffle(rects)
draw_rects(rects)

def swapitem(lst, idx1, idx2):
    global swap
    lst[idx1], lst[idx2] = lst[idx2], lst[idx1]
    #time.sleep(0.01)
    draw_rects(rects)
    swap += 1
    
def quicksort(left, right):
  if left < right:
    split = split_list(left, right)
    quicksort(left, split-1)
    quicksort(split+1, right)

def split_list(left, right):
  global comparison
  i = left
  j = right -1
  pivot = list1[right]
  
  while i < j:
    while i < j and list1[i] <= pivot:
      i += 1
      comparison += 1
    
    while j > i and list1[j] > pivot:
      j -= 1
      comparison += 1
    
    if list1[i] > list1[j]:
      swapitem(list1, i, j)
      swapitem(rects, i, j)
      comparison += 1
    
  if list1[i] > pivot:
    swapitem(list1, i, right)
    swapitem(rects, i, right)
    comparison += 1
  else: i = right
  return i
  
def bubblesort():
  global comparison
  for i in range(len(list1)-1):
    for j in range(len(list1)-1):
      if list1[j] > list1[j+1]:
        swapitem(list1, j, j+1)
        swapitem(rects, j, j+1)
        comparison += 1

global comparison, swap
comparison = 0
swap = 0
list1 = [rects[i].hight for i in range(len(rects))]
st = time.time()
#bubblesort()
quicksort(0, len(list1)-1)
et = time.time()
ft = et -st
print(comparison)
print(swap/2)
print(ft)
