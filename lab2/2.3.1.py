import turtle as t
import math
class Flower:
    def __init__(self, x, y, r1, r2, r3, color):
        self._x = x  # _x - координата x центру кола
        self._y = y  # _y - координата y центру кола
        self._r1= r1 # _r1 - радіус кола пелюстки
        self._r2 = r2 # радіус листка
        self._r3 = r3 # радіус серединки
        self._color=color # колір пелюстки
    def petal(self):
        for j in range(1, 5):
            t.speed(3)
            t.pencolor(self._color)
            t.fillcolor(self._color)
            t.up()
            t.setpos(self._x, self._y - self._r1)
            t.setheading(90*(j-1))
            t.down()
            t.begin_fill()
            t.circle(self._r1)
            t.end_fill()
            t.up()
    def center(self):
        t.speed(3)
        t.pencolor("yellow")
        t.fillcolor("yellow")
        t.up()
        t.setpos(self._x-7, self._y - self._r1)
        t.down()
        t.begin_fill()
        t.circle(self._r3)
        t.end_fill()
        t.up()
    def stem(self, base_x, base_y):
        t.speed(3)
        t.pencolor("green")
        t.pensize(2)
        t.up()
        t.setpos(self._x, self._y - self._r1)
        t.down()
        t.goto(base_x, base_y)
        position=t.pos()
        t.up()
        return position
    def leaf(self, position):
        t.speed(3)
        t.pencolor("black")
        t.fillcolor("green")
        x1, y1 = position[0], position[1]
        x2, y2 = self._x, self._y - self._r1
        cx = x1 + 0.5 * (x2 - x1)
        cy = y1 + 0.5 * (y2 - y1)
        angle = math.degrees(math.atan2(y2 - y1, x2 - x1))
        t.goto(cx, cy)
        t.setheading(angle + 180)
        t.up()
        t.goto(cx, cy)
        t.down()
        t.begin_fill()
        t.circle(self._r2)
        t.end_fill()
        t.up()

n=int(input("enter the number of flowers: "))
k=input("enter color of flowers: ")
for i in range(n):
    flower = Flower((i - n//2)*150, 0, 30, 25,10, k)
    pos=flower.stem(0, -200)
    flower.leaf(pos)
    flower.petal()
    flower.center()
t.mainloop()