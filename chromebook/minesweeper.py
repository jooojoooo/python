import turtle 
import random

difficulty = 10

witdh = difficulty/2*100
hight = difficulty/2*100

s = turtle.Screen()
s.setworldcoordinates(0, -hight, witdh,0)
pen = turtle.Turtle()
pen.ht()

rects = []
rects_copy = []

points = []
move = 0


class rect:
  
    def __init__(self, r, g, b, mine, on):
        self.r = r
        self.g = g
        self.b = b
        self.mine = mine
        self.on = on
        
    def rec(self, points, mine_num):
        points.append((pen.xcor(),pen.ycor()))
        
        if self.on or mine_num == 0 and not self.mine: pen.color(self.r, self.g, self.b)
        else: pen.color(0,0,0)
        pen.begin_fill()
        for i in range(2):
            pen.forward(witdh/difficulty)
            pen.right(90)
            pen.forward(hight/difficulty)
            pen.right(90)
        pen.end_fill()
        
        if self.mine:
            pen.forward(witdh/difficulty/2-1)
            pen.right(90)
            pen.forward(hight/difficulty/2-1)
            pen.color("black")
            pen.begin_fill()
            pen.circle(2)
            pen.end_fill()
            pen.penup()
            pen.back(hight/difficulty/2-1)
            pen.left(90)
            pen.back(witdh/difficulty/2-1)
        
        elif mine_num != 0:
            pen.forward(witdh/difficulty/2-1)
            pen.right(90)
            pen.forward(hight/difficulty/2-1)
            pen.color("black")
            pen.write(mine_num)
            pen.penup()
            pen.back(hight/difficulty/2-1)
            pen.left(90)
            pen.back(witdh/difficulty/2-1)
            
        return points
    
    def next_rect(self, x, y):
        pen.penup()
        pen.goto(x, y)
        pen.pendown()
        
def color_transition(number):
    color = 0
    if number == 0: color = 0
    elif number == difficulty - 1: color = 255
    else: color = number*(255/difficulty)+(255/difficulty/2) 
    return color
    
        
for i in range(difficulty):
    for j in range(difficulty):
        random_mine = random.randint(1,6)
        if random_mine == 1: mine = True
        else: mine = False
        r = color_transition(i)
        g = color_transition(j)
        b = 255-i*(255/difficulty)
        rects.append(rect(r, g, b, mine, False))
        rects_copy.append(rect(r, g, b, mine, False))
              
def draw(list1, anim):
    pen.tracer(0)
    for i in range(difficulty):
        for j in range(difficulty):
            if anim: pen.tracer(0)
            list1[i*difficulty+j].next_rect(i*(witdh/difficulty), j*(-hight/difficulty))
            list1[i*difficulty+j].rec(points, change[i*difficulty+j])
            if anim: pen.tracer(1)
    pen.tracer(1)

def mine_num(lst):
    change = []
    for i in range(len(rects)):
        neighbor_offsets = [-difficulty-1, -difficulty, -difficulty+1, -1, 1, difficulty-1, difficulty, difficulty+1]
        if (i % difficulty) == 0:
            neighbor_offsets.remove(-difficulty-1)
            neighbor_offsets.remove(-1)
            neighbor_offsets.remove(difficulty-1)
        if ((1+i) % difficulty) == 0:
            neighbor_offsets.remove(-difficulty+1)
            neighbor_offsets.remove(+1)
            neighbor_offsets.remove(difficulty+1)
        
        mines = 0

        for offset in neighbor_offsets:
            neighbor_index = i + offset
            if 0 <= neighbor_index < len(rects) and rects[neighbor_index].mine:
                mines += 1
            
        change.append(mines)
    return change

change = mine_num(i)

draw(rects, False)

def reveal(lst, idx):
    lst[idx].on = True
    draw(rects, False)

def onclick(x, y):
    global move
    move += 1
    for i in range(len(rects)):
        x1, y1 = points[i]
        if x1 < x < x1+witdh/difficulty and y1 > y > y1-hight/difficulty:
            reveal(rects, i)
            
    
s.onclick(onclick)

    
