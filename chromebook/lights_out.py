import turtle 
import random
import time

witdh = 200
hight = 200

s = turtle.Screen()
s.setworldcoordinates(0, -hight, witdh,0)
pen = turtle.Turtle()
pen.ht()

rects = []

points = []
move = 0

difficulty = 3
sim = True
delay = .04
xnum = ynum = difficulty


class rect:
  
    def __init__(self, r, g, b, on):
        self.r = r
        self.g = g
        self.b = b
        self.on = on
        
    def rec(self, points):
        points.append((pen.xcor(),pen.ycor()))
        if (self.on % 2) == 0: pen.color(0, 0, 0)
        else: pen.color(self.r, self.g, self.b)
        pen.begin_fill()
        for i in range(2):
            pen.forward(witdh/xnum)
            pen.right(90)
            pen.forward(hight/ynum)
            pen.right(90)
        pen.end_fill()
        return points
    
    def next_rect(self, x, y):
        pen.penup()
        pen.goto(x, y)
        pen.pendown()
        
for i in range(xnum):
    for j in range(ynum):
        #random_solid = random.randint(1,2)
        random_solid = 2
        if random_solid == 1: solid = True
        else: solid = False
        rects.append(rect(i*(255/xnum), j*(255/ynum),255, 0))
              
def draw(list1, anim):
    pen.tracer(0)
    for i in range(xnum):
        for j in range(ynum):
            if anim: pen.tracer(0)
            list1[i*ynum+j].next_rect(i*(witdh/xnum), j*(-hight/ynum))
            list1[i*ynum+j].rec(points)
            if anim: pen.tracer(1)
    pen.tracer(1)
          
draw(rects, False)

def check():
    if all((rects[i].on % 2) != 0 for i in range(len(rects))):
        print("Finished in " + str(move) + " moves!")
        exit()
        
def swaptest(rect):
    if rect is not None:
        rect.on += 1


def swap(lst, i):
    x, y = points[i]
    if y != 0: swaptest(rects[i-1])
    rects[i].on += 1
    if int(y) != int(-hight+hight/ynum): swaptest(rects[i+1])
    if int(x) != int(witdh+witdh/xnum): 
      try: swaptest(rects[i+xnum])
      except: pass
    if x != 0: 
      try: swaptest(rects[i-xnum])
      except: pass
    
    draw(rects, False)
    check()

rec1 = rec2 = 0

if not sim:
  def onclick(x, y):
      global move, rec1, rec2
      move += 1
      for i in range(len(rects)):
          x1, y1 = points[i]
          if x1 < x < x1+witdh/xnum and y1 > y > y1-hight/ynum:
              swap(rects, i)
    
  s.onclick(onclick)
  
else:
    while True:
        move += 1
        time.sleep(delay)
        i = random.randint(0, len(rects)-1)
        swap(rects, i)
    
