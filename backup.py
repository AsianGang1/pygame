from tkinter import *
import time
import random

root = Tk()
canvas = Canvas(root, width=930, height=630, bd=0, highlightthickness=0)
canvas.pack()
root.update()
root.resizable(False, False)



bx1 = 30
by1 = 30

bx2 = 60
by2 = 60

running = True
command_focus = False


class MyPlayer:
    def __init__(self, canvas, color):
        self.canvas = canvas
        self.id = canvas.create_rectangle(30, 30, 60, 60, fill=color)
        self.x = 0
        self.y = 0
        self.lives = 4
        self.blues = []
        self.redb = []
        self.canvas_height = self.canvas.winfo_height()
        self.canvas_width = self.canvas.winfo_width()

        self.ani = PhotoImage(file="tenor.gif", format="gif -index 2")
        canvas.create_image(0,0, anchor = NW, image = self.ani)
        #self.bag = Canvas(root, width=40, height=40, bg='brown')
        #eself.bag.place(x=600, y=600, anchor=SE)

        canvas.bind_all('<KeyPress-w>', self.act)
        canvas.bind_all('<KeyPress-s>', self.act)
        canvas.bind_all('<KeyPress-a>', self.act)
        canvas.bind_all('<KeyPress-d>', self.act)
        canvas.bind_all('<KeyPress-e>', self.act)

        canvas.bind_all('<KeyPress-Up>', self.act)
        canvas.bind_all('<KeyPress-Down>', self.act)
        canvas.bind_all('<KeyPress-Left>', self.act)
        canvas.bind_all('<KeyPress-Right>', self.act)

        canvas.bind('<Button-1>', self.callback)
        #self.bag.bind("<B1-Motion>", self.drag)

    def createblues(self, nu, de):
        r = 0
        bx1 = 30
        by1 = 30

        bx2 = 60
        by2 = 60

        for o in range(0, 10):
            for p in range(0, 15):
                r = random.randint(0, de)
                if r <= nu:
                    m = (canvas.create_rectangle(bx1, by1, bx2, by2, fill='blue'))
                    if m > 0 and len(canvas.coords(m)) > 0:
                        self.blues.append(m)
                bx1 = bx1 + 60
                bx2 = bx2 + 60

            bx1 = 30
            bx2 = 60
            by1 = by1 + 60
            by2 = by2 + 60

    def draw(self):
        self.pos = self.canvas.coords(self.id)
        self.canvas.move(self.id, self.x, self.y)

        if self.pos[1] <= 0:
            self.y = self.y
            self.canvas.move(self.id, 0, 60)
        if self.pos[3] >= 630:
            self.y = self.y
            self.canvas.move(self.id, 0, -60)
        if self.pos[0] <= 0:
            self.x = self.x
            self.canvas.move(self.id, 60, 0)
        if self.pos[2] >= self.canvas_width:
            self.x = self.x
            self.canvas.move(self.id, -60, 0)

        for b in range(len(self.redb)):
            canvas.move(self.redb[b], 0, 5)

    def act(self, event):
        if event.keysym == 'w':
            canvas.move(self.id, 0, -60)
        if event.keysym == 's':
            canvas.move(self.id, 0, 60)
        if event.keysym == 'a':
            canvas.move(self.id, -60, 0)
        if event.keysym == 'd':
            canvas.move(self.id, 60, 0)

        if event.keysym == 'Up':
            canvas.move(self.id, 0, -60)
        if event.keysym == 'Down':
            canvas.move(self.id, 0, 60)
        if event.keysym == 'Left':
            canvas.move(self.id, -60, 0)
        if event.keysym == 'Right':
            canvas.move(self.id, 60, 0)

        if event.keysym == 'e':
            m = (canvas.create_rectangle(canvas.coords(self.id)[0] + 10, canvas.coords(self.id)[1] + 10,
                                         canvas.coords(self.id)[2] - 10,
                                         canvas.coords(self.id)[3] - 10, fill='red', outline='red'))
            if m > 0 and len(canvas.coords(m)) > 0:
                self.redb.append(m)

        self.y = 0
        self.x = 0

    # def drag(self, event):
    #     widget = event.widget
    #     x = widget.winfo_x() - widget._drag_start_x + event.x
    #     y = widget.winfo_y() - widget._drag_start_y + event.y
    #     widget.place(x=x, y=y)

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
                canvas.create_text(200, 150, text="Mouse Wins!", font=('Times', 30))

        found = -1
        for j in range(0, len(self.blues)):
            if canvas.coords(self.blues[j])[0] <= mx and mx <= canvas.coords(self.blues[j])[2] and \
                    canvas.coords(self.blues[j])[1] <= my and my <= canvas.coords(self.blues[j])[3]:
                canvas.delete(self.blues[j])
                found = j
                break
        if found >= 0:
            del self.blues[found]
            self.createblues(1, 200)


player = MyPlayer(canvas, 'black')
player.createblues(35, 100)

while running == True:
    player.draw()
    root.update_idletasks()
    root.update()
    time.sleep(0.01)
