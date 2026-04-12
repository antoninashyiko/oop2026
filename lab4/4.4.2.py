import turtle as t
class Figure:
    def __init__(self, x, y, color):
        self._x=x
        self._y=y
        self._visible=False
        self._color=color
    def setPosition(self):
        def click(x, y):
            self._x = x
            self._y = y
        t.onscreenclick(click)
        t.listen()
    def draw(self, color):
        t.up()
        t.goto(self._x, self._y)
        t.down()
        t.forward(25)
        t.up()
    def show(self):
        if not self._visible:
            self._visible = True
            self.draw(self._color)
    def hide(self):
        if self._visible:
            self._visible = False
            self.draw(t.bgcolor())

class Circle(Figure):
    def __init__(self, x, y):
        super().__init__(x, y, 'black')
        self._r=50
    def draw(self, color):
        t.pencolor(color)
        t.up()
        t.setpos(self._x, self._y - self._r)
        t.down()
        t.circle(self._r)
        t.up()

class Cross(Figure):
    def __init__(self, x, y):
        super().__init__(x, y, 'black')
        self._angle=90
    def draw(self, color):
        t.pencolor(color)
        for i in range(4):
            t.up()
            t.setpos(self._x, self._y)
            t.down()
            t.setheading(self._angle*i+45)
            t.forward(50)

class Game_field():
    def __init__(self):
        self._visible=False
    def draw(self):
        for i in range(2):
            t.speed(0)
            t.up()
            t.setpos(-100 + i * 200, 200)
            t.setheading(-90)
            t.down()
            t.pencolor('black')
            t.forward(500)
        for i in range(2):
            t.speed(0)
            t.up()
            t.setpos(-300, 50 - i * 200)
            t.setheading(0)
            t.down()
            t.pencolor('black')
            t.forward(600)
    def show(self):
        if not self._visible:
            self._visible = True
            self.draw()
    def hide(self):
        if self._visible:
            self._visible = False
            self.draw(t.bgcolor())

print("welcome to the game of tic tac toe")
k=input("who goes first: circles or crosses? ")
print(" ")
g=Game_field()
g.show()

def click(x, y):
    global k
    if k=="circles":
        f=Circle(x, y)
        f.show()
        k="crosses"
    elif k=="crosses":
        f=Cross(x, y)
        f.show()
        k="circles"
    else:
        print("input circles or crosses to start the game: ")

t.onscreenclick(click)
t.mainloop()
