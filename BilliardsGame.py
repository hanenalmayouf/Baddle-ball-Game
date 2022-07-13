import random
import time
from tkinter import *


#  generate small balls


class Ball:
    def __init__(self, canvas, paddle, color):
        self.canvas = canvas
        self.paddle = paddle
        self.id = canvas.create_oval(10, 10, 25, 25, fill=color)  # draw a circle with two numbers in the lower left corner and two in the upper right corner
        self.canvas.move(self.id, 245, 100)  # move the picture to the specified location
        starts = [-3, -2, -1, 1, 2, 3]
        # shuffle() method to randomly sort all elements of the sequence
        random.shuffle(starts)
        self.x = starts[0]
        self.y = -3
        self.canvas_height = self.canvas.winfo_height()  # get high
        self.canvas_width = self.canvas.winfo_width()  # get width
        self.hit_bottom = False  # set the flag bit to see if the ball touches the bottom of the screen

    def draw(self):
        self.canvas.move(self.id, self.x, self.y)
        pos = self.canvas.coords(
            self.id)  # coord = coordinates, returns the coordinates of the ball frame ， the upper left corner x1, y1    lower right corner x2, y2
        if pos[1] <= 0:
            self.y = 3
        if pos[3] >= self.canvas_height:  # when you hit the bottom of the screen, you fail.
            self.y = -3
        if self.hit_paddle(pos) == True:  # the ball collided with the racket
            self.y = -3
            label0["text"] = "score：" + str(score.score())
            if score.x % 100 == 0:
                paddle.length /= 2
                canvas.coords(paddle.id, (0, 0, paddle.length, 10))
                paddle.canvas.move(paddle.id, 200, 300)

        if pos[3] >= self.canvas_height:
            self.hit_bottom = True
        if pos[0] <= 0:
            self.x = 3
        if pos[2] >= self.canvas_width:
            self.x = -3

    def hit_paddle(self, pos):
        paddle_pos = self.canvas.coords(self.paddle.id)
        if pos[2] >= paddle_pos[0] and pos[0] <= paddle_pos[2]:
            if pos[3] >= paddle_pos[1] and pos[3] <= paddle_pos[3]:
                return True
        return False


class Paddle:
    def __init__(self, canvas, length, color):
        self.length = length
        self.canvas = canvas
        self.id = canvas.create_rectangle(0, 0, length, 10, fill=color)
        self.canvas.move(self.id, 200, 300)
        self.x = 0
        self.canvas_width = self.canvas.winfo_width()
        self.canvas.bind_all('<KeyPress-Left>', self.turn_left)
        self.canvas.bind_all('<KeyPress-Right>', self.turn_right)

    def turn_left(self, evt):
        self.x = -2

    def turn_right(self, evt):
        self.x = 2

    def draw(self):
        self.canvas.move(self.id, self.x, 0)
        pos = self.canvas.coords(self.id)
        if pos[0] <= 0:
            self.x = 0
        elif pos[2] >= self.canvas_width:
            self.x = 0


#  memorize and classify


class Scoreboard:
    def __init__(self):
        self.x = 0

    def score(self):
        self.x += 10
        return self.x


#  life class

class Die:
    def __init__(self):
        self.life = 2  # number of life of small ball

    def balldie(self):  # if you die once, your life will be reduced. 1
        if self.life >= 0:
            self.life -= 1


#  game form

tk = Tk()
tk.title(" Billiards Game ")
tk.config(background="powder blue")
tk.resizable(False, True)  # whether the window is variable ( long 、 width ), you can also use 0, 1 express
tk.wm_attributes("-topmost", 1)  # the window is always in front.
canvas = Canvas(tk, width=500, height=400, bd=0, highlightthickness=0)  # there is no border outside the canvas
canvas.pack()
label0 = Label(tk, text='score: 0', background="powder blue")  # scoreboard
label0.pack()  # if you don't add this sentence, you can't show it. label come on.
tk.update()  # refresh window
# instantiation
paddle = Paddle(canvas, 200, 'red')
ball = Ball(canvas, paddle, 'green')
score = Scoreboard()
balldie = Die()

# the game continues to cycle
while 1:
    if ball.hit_bottom == False:
        ball.draw()
        paddle.draw()
        label0["text"] = "score: " + str(score.x) + ", life: " + str(balldie.life)
    else:  # if you touch the bottom, the life of the ball decreases. 1
        if balldie.life > 0:
            balldie.balldie()
            del ball
            ball = Ball(canvas, paddle, 'blue')
            label0["text"] = label0["text"] + ", life: " + str(balldie.life)
        else:
            label0["text"] = "score: " + str(score.x) + ", life: " + str(balldie.life) + ", GAME OVER !!"

    tk.update_idletasks()
    tk.update()
    time.sleep(0.01)
