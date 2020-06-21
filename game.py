# the real game. changes to make: more squares to hide under instead of controlling 1 square, you control any of the squares you infect. 
from tkinter import *
import time
import random

root = Tk()
root.title("Game")
canvas = Canvas(root, width=500, height=400, bd=0, highlightthickness=0)
canvas.pack()
root.update()

running = True
command = [['zizz', 'zizz', 'zizz', 'zizz', 'zizz', 'zizz', 'zizz', 'zizz', 'zizzle', 'zizzle'],
           ['zizzle', 'zizzle', 'zizzle', 'zizzle', 'zizzle', 'zizzle', 'boom', 'boom', 'boom', 'boom'],
           ['boom', 'boom', 'boom', 'boom', 'kabang', 'kabang', 'kabang', 'kabang', 'kabang', 'kabang'],
           ['kabang', 'kabang', 'kabang', 'kabang', 'freeze', 'freeze', 'freeze', 'freeze', 'freeze', 'freeze'],
           ['kamikazee', 'call for aid', 'fire slash', 'fire slash', 'karacaracle slash', 'karacaracle slash',
            'metal blade', 'metal blade', 'hatchet throw', 'hatchet throw'],
           ['hatchet throw', 'hatchet throw', 'whack', 'whack', 'whack', 'whack', 'thwack', 'thwack', 'thwack',
            'thwack'],
           ['magic burst', 'magic burst', 'magic burst', 'magic burst', 'karacaracle slash', 'metal blade',
            'metal blade', 'fire slash', 'call for aid', 'kamikazee', ],
           ['kamikazee', 'psyche up', 'psyche up', 'psyche up', 'psyche up', 'psyche up', 'speed up', 'speed up',
            'speed up', ],
           ['speed up', 'call of aid', 'Socialism', 'reflect', 'reflect', 'reflect', 'reflect', 'reflect', 'reflect',
            'reflect'],
           ['rejuvenate', 'rejuvenate', 'rejuvenate', 'rejuvenate', 'rejuvenate', 'rejuvenate', 'rejuvenate',
            'rejuvenate', 'wind circle', 'wind circle', 'wind circle', 'wind circle']]

command_list = []
command_focus = False


class Player:
    def __init__(self, canvas, color):
        self.canvas = canvas
        self.id = canvas.create_rectangle(20, 20, 50, 50, fill=color)
        self.x = 0
        self.y = 0
        self.lives = 4
        self.canvas_height = self.canvas.winfo_height()
        self.canvas_width = self.canvas.winfo_width()
        canvas.bind_all('<KeyPress-w>', self.act)
        canvas.bind_all('<KeyPress-s>', self.act)
        canvas.bind_all('<KeyPress-a>', self.act)
        canvas.bind_all('<KeyPress-d>', self.act)
        canvas.bind_all('<KeyPress-e>', self.act)

        canvas.bind_all('<KeyPress-Up>', self.act)
        canvas.bind_all('<KeyPress-Down>', self.act)
        canvas.bind_all('<KeyPress-Left>', self.act)
        canvas.bind_all('<KeyPress-Right>', self.act)

        canvas.bind_all('<Button-1>', self.callback)

        canvas.create_rectangle(20, 20, 50, 50, fill='blue')
        canvas.create_rectangle(80, 80, 110, 110, fill='blue')
        canvas.create_rectangle(140, 140, 170, 170, fill='blue')
        canvas.create_rectangle(200, 200, 230, 230, fill='blue')
        canvas.create_rectangle(260, 260, 290, 290, fill='blue')
        canvas.create_rectangle(320, 320, 350, 350, fill='blue')

        canvas.create_rectangle(450, 20, 470, 40, fill='red')
        canvas.create_rectangle(450, 330, 470, 350, fill='red')
        canvas.create_rectangle(40, 330, 20, 350, fill='red')

    def draw(self):
        self.pos = self.canvas.coords(self.id)
        self.canvas.move(self.id, self.x, self.y)

        if self.pos[1] <= 0:
            self.y = self.y
            self.canvas.move(self.id, 0, 60)
        if self.pos[3] >= self.canvas_height:
            self.y = self.y
            self.canvas.move(self.id, 0, -60)
        if self.pos[0] <= 0:
            self.x = self.x
            self.canvas.move(self.id, 60, 0)
        if self.pos[2] >= self.canvas_width:
            self.x = self.x
            self.canvas.move(self.id, -60, 0)

    def act(self, event):
        if event.keysym == 'w':
            canvas.move(self.id, 0, -60)
        if event.keysym == 's':
            canvas.move(self.id, 0, 60)
        if event.keysym == 'a':
            canvas.move(self.id, -60, 0)
        if event.keysym == 'd':
            canvas.move(self.id, 60, 0)
        if event.keysym == 'e':
            canvas.create_rectangle()

        if event.keysym == '<KeyPress-Up>':
            canvas.move(self.id, 0, -60)
        if event.keysym == '<KeyPress-Down>':
            canvas.move(self.id, 0, 60)
        if event.keysym == '<KeyPress-Left>':
            canvas.move(self.id, -60, 0)
        if event.keysym == '<KeyPress-Right>':
            canvas.move(self.id, 60, 0)

        self.y = 0
        self.x = 0

    def callback(self, event):
        pos = self.canvas.coords(self.id)
        global mx
        global my
        global running
        mx = event.x
        my = event.y

        print("clicked at", event.x, event.y)
        if mx >= pos[0] and mx <= pos[2] and my >= pos[1] and my <= pos[3]:
            print("collision")
            self.lives = self.lives - 1
            if self.lives == 3:
                canvas.itemconfig(self.id, fill='green', outline='green')
            if self.lives == 2:
                canvas.itemconfig(self.id, fill='yellow', outline='yellow')
            if self.lives == 1:
                canvas.itemconfig(self.id, fill='red', outline='red')
            if self.lives == 0:
                canvas.itemconfig(self.id, fill='orange', outline='orange')
                running = False
                canvas.create_text(200, 150, text="Mouse Wins!", font=('Times', 30))


player = Player(canvas, 'black')

while running == True:
    player.draw()
    root.update_idletasks()
    root.update()
    time.sleep(0.01)

