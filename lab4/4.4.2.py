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

b=[[0, 0, 0], [0, 0, 0], [0, 0, 0]]
n=0
def fill_board(x, y):
    global k, b
    print(f"{k}: click [{x}, {y}]") # виведення координат ходів
    if -300<x<-100 and 100<y<300:
        if k=="circles":
            b[0][0]=1
        else:
            b[0][0]=2
    elif -300<x<-100 and -100<y<100:
        if k == "circles":
            b[1][0] = 1
        else:
            b[1][0] = 2
    elif -300<x<-100 and -300<y<-100:
        if k == "circles":
            b[2][0] = 1
        else:
            b[2][0] = 2
    elif -100<x<100 and 100<y<300:
        if k == "circles":
            b[0][1] = 1
        else:
            b[0][1] = 2
    elif -100<x<100 and -100<y<100:
        if k == "circles":
            b[1][1] = 1
        else:
            b[1][1] = 2
    elif -100<x<100 and -300<y<-100:
        if k == "circles":
            b[2][1] = 1
        else:
            b[2][1] = 2
    elif 100<x<300 and 100<y<300:
        if k == "circles":
            b[0][2] = 1
        else:
            b[0][2] = 2
    elif 100<x<300 and -100<y<100:
        if k == "circles":
            b[1][2] = 1
        else:
            b[1][2] = 2
    elif 100<x<300 and -300<y<-100:
        if k == "circles":
            b[2][2] = 1
        else:
            b[2][2] = 2
    return b
def click(x, y):
    global k, b, n
    b=fill_board(x, y)
    win=False
    p=k
    if k=="circles":
        f=Circle(x, y)
        f.show()
        k="crosses"
        n+=1
    elif k=="crosses":
        f=Cross(x, y)
        f.show()
        k="circles"
        n+=1
    else:
        print("input circles or crosses to start the game: ")

    for i in range(3):
        if b[i][0] == b[i][1] == b[i][2] != 0:
            win = True
    for i in range(3):
        if b[0][i] == b[1][i] == b[2][i] != 0:
            win = True
    if b[0][0] == b[1][1] == b[2][2] != 0:
        win = True
    if b[2][0] == b[1][1] == b[0][2] != 0:
        win = True
    if win:
        t.ontimer(t.bye, 2000)
        print("game over")
        if p=="circles":
            print("circles won")
        else:
            print("crosses won")
    if n==9 and not win:
        t.ontimer(t.bye, 3000)
        print("game over")
        print("it's a tie")

t.onscreenclick(click)
t.mainloop()
