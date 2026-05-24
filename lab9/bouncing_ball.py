import tkinter as tk
import random
class Ball:
    def __init__(self, canvas, x, y):
        self.canvas = canvas
        self.x = x
        self.y = y
        colors = ["red", "blue", "green", "yellow", "purple", "cyan", "pink"]
        self.color = random.choice(colors)
        self.ball=canvas.create_oval(x-20, y-20, x+20, y+20, fill=self.color, outline=self.color)
        self.dx=3
        self.dy=2
        self.WIDTH = 500
        self.HEIGHT = 400
    def move(self): # movement of tha ball
        self.canvas.move(self.ball, self.dx, self.dy)
        x1, y1, x2, y2 = self.canvas.coords(self.ball)
        if x1 <= 0 or x2 >= self.WIDTH: # verification for borders
            self.dx = -self.dx
        if y1 <= 0 or y2 >= self.HEIGHT:
            self.dy = -self.dy

class Game:
    def __init__(self):
        self.WIDTH = 500
        self.HEIGHT = 400
        self.root = tk.Tk() # create window
        self.root.title("Bouncing Ball")
        self.canvas = tk.Canvas(self.root, width=self.WIDTH, height=self.HEIGHT, bg="white")
        self.canvas.pack() # create canvas
        self.balls_list=[]
        self.canvas.bind("<Button-1>", self.ball_list) # creation of bouncing ball; "<Button-1>" - left click
    def ball_list(self, event):
        ball = Ball(self.canvas, event.x, event.y) # event.x, event.y - click of the mouse
        self.balls_list.append(ball)
        return self.balls_list
    def animate(self):
        for ball in self.balls_list:
            ball.move()
        self.root.after(20, self.animate)
    def play(self):
        self.animate()
        self.root.mainloop()

g=Game()
g.play()
