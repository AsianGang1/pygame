"""
2 players: virus and medic
virus player abilities:
  invest in symptom hiding so the hosts get more turns before they show symptoms and can be detected by medic (max 6 turns, randomly so its not guaranteed that maxed out will grant 6 turn symptom hiding)
  invest in infections per turn (auto infect). each infected person will spread to 1 person next to them which can be increased to 4
  invest in manual infections where he can choose (manual infect). can increase manual infections from 1 up to 4. *supposed to simulate transportation*
  spends virus points for investments which are gained every turn for each infected individual which isn't caught by the medic
medic player abilities:
  invest in more test kids per turn.
  look at people with high symptoms (takes 3 turns to show by default) and isolate them with the cost of 1 med kit
  invest in hospital capacity so that there can be more infected people before the game is over
  invest in vaccine speed so that the turns before winning as medic is reduced by 1 turn (starts at 50)
  invest in social distancing: the next turn most people are separated by 1 grid unit to prevent spread (doesn't work if there are too many people)
winning as medic:
  vaccine is developed or all infected people are isolated
winning as virus:
  pass hospital capacity
*every turn the people on the board will move 1 square unless social distancing is used that turn
"""
from tkinter import *
import random
import time

root = Tk()
root.resizable(False, False)
canvas = Canvas(root, width=480, height=420)
root.title("Game")
canvas.pack()
canvas2 = Canvas(root, width=480, height=420)
turn = "virus"
people = []
xglobal=0
yglobal=0


def get_location():
    rand_x = random.randrange(1, 14)
    rand_y = random.randrange(1, 16)
    for person in people:
        if rand_x == person.x and rand_y == person.y:
            get_location()
            break
    return [rand_x, rand_y]


def check_surroundings(self):
    available = ["up", "down", "left", "right"]
    for person in people:
        if person == self:
            continue
        if self.x + 1 == person.x and self.x + 1 < 14:
            available[3] = 0
        if self.x - 1 == person.x and self.x - 1 > 0:
            available[2] = 0
        if self.y + 1 == person.y and self.y + 1 < 16:
            available[1] = 0
        if self.y - 1 == person.y and self.y - 1 > 0:
            available[0] = 0
    for x in available:
        if x == 0:
            available.remove(x)
    print(available)
    return available


class Person:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.infected = False
        self.turns_symptoms = 3
        self.turns_death = 3 + random.randrange(1, 3)

    def draw(self):
        canvas.create_rectangle(self.x * 30, self.y * 30, self.x * 30 + 30, self.y * 30 + 30, fill="black")

    def move(self):
        available = check_surroundings(self)
        move = available[random.randrange(0, len(available))]
        if move == "up":
            self.y -= 1
        elif move == "down":
            self.y += 1
        elif move == "right":
            self.x += 1
        elif move == "left":
            self.x -= 1


def a():  # remove this later when people move properly
    for x in people:
        x.move()
        x.draw()


def openshop():
    canvas.pack_forget()
    button.pack_forget()
    button2.pack_forget()
    root.title("Shop")
    canvas2.pack()
    button3.pack()


def closeshop():
    canvas2.pack_forget()
    button3.pack_forget()
    root.title("Game")
    canvas.pack()
    button.pack()
    button2.pack()

def getorigin(eventorigin):
    global xglobal,yglobal
    xglobal=eventorigin.x
    yglobal=eventorigin.y
    print(xglobal,yglobal)
    for i in range(0,14*16):
        if 30*(i%16)<xglobal and xglobal<30*(i%16)+30:
            if 30*(i//16)<yglobal and yglobal<30*(i//16)+30:
                canvas.create_rectangle(30 * (i % 16), 30 * (i // 16), 30 * (i % 16) + 30, 30 * (i // 16) + 30, fill="blue")

for i in range(0, 14 * 16):
    canvas.create_rectangle(30 * (i % 16), 30 * (i // 16), 30 * (i % 16) + 30, 30 * (i // 16) + 30, fill="white")
for x in range(0, 30):
    location = get_location()
    people.append(Person(location[0], location[1]))
canvas.update()
for person in people:
    person.draw()
button = Button(text="p", command=a)
button2 = Button(text="shop", command=openshop)
button3 = Button(text="go back", command=closeshop)
if not canvas.winfo_manager()=="":
    canvas.bind("<Button-1>",getorigin)
button.pack()
button2.pack()
root.mainloop()
