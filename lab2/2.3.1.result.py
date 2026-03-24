import turtle as t
import math
class petal:
    def __init__(self, x, y, r1, color):
        self.x = x
        self.y = y
        self.r1 = r1
        self.color = color
    def draw(self):
        for j in range(1, 5):
            t.speed(3)
            t.pencolor(self.color)
            t.fillcolor(self.color)
            t.up()
            t.setpos(self.x, self.y - self.r1)
            t.setheading(90*(j-1))
            t.down()
            t.begin_fill()
            t.circle(self.r1)
            t.end_fill()
            t.up()
class center:
    def __init__(self, x, y, r1, r3):
        self.x = x
        self.y = y
        self.r1 = r1
        self.r3 = r3
        self.color="yellow"
        self.p1=self.x-7
        self.p2=self.y-self.r1
    def draw(self):
        t.speed(3)
        t.pencolor(self.color)
        t.fillcolor(self.color)
        t.up()
        t.setpos(self.p1, self.p2)
        t.down()
        t.begin_fill()
        t.circle(self.r3)
        t.end_fill()
        t.up()
class stem:
    def __init__(self, x, y, r1, base_x, base_y):
        self.x = x
        self.y = y
        self.r1 = r1
        self.pen_color="green"
        self.pos=self.y-self.r1
        self.base_x=base_x
        self.base_y=base_y
    def draw(self):
        t.speed(3)
        t.pencolor(self.pen_color)
        t.pensize(2)
        t.up()
        t.setpos(self.x, self.pos)
        t.down()
        t.goto(self.base_x, self.base_y)
        position = t.pos()
        t.up()
        return position
class leaf:
    def __init__(self, x, y, r1, r2, position):
        self.x = x
        self.y = y
        self.r1 = r1
        self.r2 = r2
        self.color="green"
        self.x1, self.y1 = position[0], position[1]
        self.x2, self.y2 = self.x, self.y - self.r1
        self.cx = self.x1 + 0.5 * (self.x2 - self.x1)
        self.cy = self.y1 + 0.5 * (self.y2 - self.y1)
        self.angle = math.degrees(math.atan2(self.y2 - self.y1, self.x2 - self.x1))
    def draw(self):
        t.speed(3)
        t.pencolor(self.color)
        t.fillcolor(self.color)
        t.goto(self.cx, self.cy)
        t.setheading(self.angle+180)
        t.up()
        t.goto(self.cx, self.cy)
        t.down()
        t.begin_fill()
        t.circle(self.r2)
        t.end_fill()
        t.up()
class Flower():
    def __init__(self, x, y, r1, r2, r3, color):
        self.x = x  # x - координата x центру кола
        self.y = y  # y - координата y центру кола
        self.r1= r1 # r1 - радіус кола пелюстки
        self.r2 = r2 # радіус листка
        self.r3 = r3 # радіус серединки
        self.color=color # колір пелюстки
        self.stem=stem(x, y, r1, 0, -200)
        pos = self.stem.draw()
        self.leaf=leaf(x, y, r1, r2, pos)
        self.center=center(x, y, r1, r3)
        self.petal=petal(x, y, r1, color)
    def draw(self):
        self.leaf.draw()
        self.petal.draw()
        self.center.draw()

n=int(input("enter the number of flowers: "))
k=input("enter color of flowers: ")
for i in range(n):
    flower = Flower((i - n//2)*150, 0, 30, 25,10, k)
    flower.draw()
t.mainloop()
