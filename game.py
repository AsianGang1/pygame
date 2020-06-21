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
x=0
y=0
def getcoordonclick(eventorigin):
   global x
   global y
   x=eventorigin.x
   y=eventorigin.y
   print(x,y)


root=Tk()
canvas=Canvas(root,width=700,height=500)
canvas.pack()
for i in range(0,5600):
  canvas.create_rectangle(50*(i%80)+1,50*(i//80)+1,50*(i%80)+51,50*(i//80)+51,fill="white",width=1)
canvas.update()
canvas.bind("<Button-1>",getcoordonclick)
mainloop()
