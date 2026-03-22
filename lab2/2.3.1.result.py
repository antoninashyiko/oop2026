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
    def draw(self):
        t.speed(3)
        t.pencolor("yellow")
        t.fillcolor("yellow")
        t.up()
        t.setpos(self.x - 7, self.y - self.r1)
        t.down()
        t.begin_fill()
        t.circle(self.r3)
        t.end_fill()
        t.up()
class stem:
    def __init__(self, x, y, r1):
        self.x = x
        self.y = y
        self.r1 = r1
    def draw(self, base_x, base_y):
        t.speed(3)
        t.pencolor("green")
        t.pensize(2)
        t.up()
        t.setpos(self.x, self.y - self.r1)
        t.down()
        t.goto(base_x, base_y)
        position = t.pos()
        t.up()
        return position
class leaf:
    def __init__(self, x, y, r1, r2):
        self.x = x
        self.y = y
        self.r1 = r1
        self.r2 = r2
    def draw(self, position):
        t.speed(3)
        t.pencolor("black")
        t.fillcolor("green")
        x1, y1 = position[0], position[1]
        x2, y2 = self.x, self.y - self.r1
        cx = x1 + 0.5 * (x2 - x1)
        cy = y1 + 0.5 * (y2 - y1)
        angle = math.degrees(math.atan2(y2 - y1, x2 - x1))
        t.goto(cx, cy)
        t.setheading(angle+180)
        t.up()
        t.goto(cx, cy)
        t.down()
        t.begin_fill()
        t.circle(self.r2)
        t.end_fill()
        t.up()
class Flower:
    def __init__(self, x, y, r1, r2, r3, color):
        self.x = x  # x - координата x центру кола
        self.y = y  # y - координата y центру кола
        self.r1= r1 # r1 - радіус кола пелюстки
        self.r2 = r2 # радіус листка
        self.r3 = r3 # радіус серединки
        self.color=color # колір пелюстки
        self.stem=stem(x, y, r1)
        self.leaf=leaf(x, y, r1, r2)
        self.center=center(x, y, r1, r3)
        self.petal=petal(x, y, r1, color)
    def draw(self):
        pos = self.stem.draw(0, -200)
        self.leaf.draw(pos)
        self.petal.draw()
        self.center.draw()

n=int(input("enter the number of flowers: "))
k=input("enter color of flowers: ")
for i in range(n):
    flower = Flower((i - n//2)*150, 0, 30, 25,10, k)
    flower.draw()
t.mainloop()