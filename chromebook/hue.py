import turtle 
import random

witdh = 200
hight = 200

s = turtle.Screen()
s.setworldcoordinates(0, -hight, witdh,0)
pen = turtle.Turtle()
pen.ht()

rects = []
rects_copy = []

points = []
move = 0

difficulty = 4
xnum = ynum = difficulty


class rect:
  
    def __init__(self, r, g, b, solid):
        self.r = r
        self.g = g
        self.b = b
        self.solid = solid
        
    def rec(self, points):
        points.append((pen.xcor(),pen.ycor()))
        pen.color(self.r, self.g, self.b)
        pen.begin_fill()
        for i in range(2):
            pen.forward(witdh/xnum)
            pen.right(90)
            pen.forward(hight/ynum)
            pen.right(90)
        pen.end_fill()
        
        if self.solid:
            pen.forward(witdh/xnum/2-1)
            pen.right(90)
            pen.forward(hight/ynum/2-1)
            pen.color("black")
            pen.begin_fill()
            pen.circle(2)
            pen.end_fill()
            pen.penup()
            pen.back(hight/ynum/2-1)
            pen.left(90)
            pen.back(witdh/xnum/2-1)
        return points
    
    def next_rect(self, x, y):
        pen.penup()
        pen.goto(x, y)
        pen.pendown()
        
for i in range(xnum):
    for j in range(ynum):
        random_solid = random.randint(1,difficulty)
        #random_solid = 2
        if random_solid == 1: solid = True
        else: solid = False
        rects.append(rect(i*(255/difficulty), j*(255/difficulty),255-i*(255/difficulty), solid))
        rects_copy.append(rect(i*(255/difficulty), j*(255/difficulty),255-i*(255/difficulty), solid))
        #rects.append(rect(i*10, j*10,255, solid))
        #rects_copy.append(rect(i*10,j*10,255,solid))
              
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
cut_part = []
cut_index = []

for i, rect in enumerate(rects_copy):
    if rect.solid:
        cut_part.append(rect)
        cut_index.append(i)

cut_index.reverse()
for index in cut_index:
    rects_copy.pop(index)
cut_index.reverse()

random.shuffle(rects_copy)

for i, value in enumerate(cut_part):
    rects_copy.insert(cut_index[i], value)

x = input()
draw(rects_copy, True)


def check():
    if all(rects_copy[i].r == rects[i].r and rects_copy[i].g == rects[i].g and rects_copy[i].b == rects[i].b for i in range(len(rects))):
        print("Finished in " + str(move) + " moves!")
        exit()

def swapitem(lst, idx1, idx2):
    lst[idx1], lst[idx2] = lst[idx2], lst[idx1]
    draw(rects_copy, False)
    check()

rec1 = rec2 = 0

def onclick(x, y):
    global move, rec1, rec2
    move += 1
    for i in range(len(rects_copy)):
        x1, y1 = points[i]
        if x1 < x < x1+witdh/xnum and y1 > y > y1-hight/ynum and not rects_copy[i].solid:
            if (move % 2) != 0:
                rec1 = i
            else:
                rec2 = i
                swapitem(rects_copy, rec1, rec2)
    
s.onclick(onclick)

    
