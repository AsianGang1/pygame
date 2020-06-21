"""
2 players: virus and medic
virus player abilities:
  invest in symptom hiding so the hosts get more turns before they show symptoms and can be detected by medic
  invest in infections per turn (auto infect). each infected person will spread to 1 person next to them which can be increased to 4
  invest in manual infections where he can choose (manual infect). can increase manual infections from 1 up to 4. *supposed to simulate*
  spends virus points for in
"""
from tkinter import *
root=Tk()
canvas=Canvas(root,width=800,height=700)
canvas.pack()
for i in range(0,5600):
  canvas.create_rectangle(10*(i%80),10*(i//80),10*(i%80)+10,10*(i//80)+10,fill="white")
canvas.update()
mainloop()
