#This is really bad code
#My bad virus game shop
#If there is a ! at the beginning of a variable, it's likely it's a variable you already have, but in a different name
#PLS HELP WRITING THE FUNCTIONS/COMMANDS, I DON'T KNOW HOW TO WRITE MOST OF THEM
#I USED SOME VARIABLES THAT I DON'T THINK YOU GUYS USED
#IF YOU HAVE THE TIME, PLEASE CHECK EACH LINE!!!
#Thanks guys, couldn't have asked for a better team ;)
#My bad virus game shop
from tkinter import *
from random import *
root = Tk()

!virus_points = 20
!medic_points = 20


#Labels
shop_label = Label(root, text = "SHOP", font = ("Times New Roman", 20), padx = 300)
virus_label = Label(root, text = "VIRUS UPGRADES", font = ("Times New Roman", 16), padx = 100)
medic_label = Label(root, text = "MEDICAL UPGRADES", font = ("Times New Roman", 16), padx = 150)
virus_points_label = Label(root, text = f"Virus points: {str(virus_points)}")
medic_points_label = Label(root, text = f"Medic points: {str(medic_points)}")
virus_upgrade_1_label = Label(root, text = "Symptom Hiding")
virus_upgrade_2_label = Label(root, text = "Automatic Infection")
virus_upgrade_3_label = Label(root, text = "Manual Infection")
virus_upgrade_4_label = Label(root, text = "Investments")
virus_upgrade_5_label = Label(root, text = "Currency Rate")
medic_upgrade_1_label = Label(root, text = "More Test Kits")
medic_upgrade_2_label = Label(root, text = "Hospital Capacity")
medic_upgrade_3_label = Label(root, text = "Vaccine Speed")
medic_upgrade_4_label = Label(root, text = "Social Distancing")
medic_upgrade_5_label = Label(root, text = "Currency Rate")

shop_label.grid(row = 0, column = 0, columnspan = 10)
virus_label.grid(row = 1, column = 0, columnspan = 5)
medic_label.grid(row = 1, column = 4, columnspan = 5)
virus_points_label.grid(row = 2, column = 0, columnspan = 5)
medic_points_label.grid(row = 2, column = 4, columnspan = 5)
virus_upgrade_1_label.grid(row = 3, column = 0)
virus_upgrade_2_label.grid(row = 3, column = 1)
virus_upgrade_3_label.grid(row = 3, column = 2)
virus_upgrade_4_label.grid(row = 3, column = 3)
virus_upgrade_5_label.grid(row = 3, column = 4)
medic_upgrade_1_label.grid(row = 3, column = 6, sticky = E)
medic_upgrade_2_label.grid(row = 3, column = 7, sticky = E)
medic_upgrade_3_label.grid(row = 3, column = 8, sticky = E)
medic_upgrade_4_label.grid(row = 3, column = 9, sticky = E)
medic_upgrade_5_label.grid(row = 3, column = 10, sticky = E)

#Defining Button Functions
def symptom_hiding():
    random_number = randint(1, 6)
    !days_left += random_number

def auto_infection():
    return


def manual_infection():
    return


def investments():
    return


def more_test_kits():
    random_number = randint(2, 3)
    !test_kits += random_number


def currency_increase():
    !rate_of_currency += 2


def increase_hospital_capacity():
    !hospital_capacity += 10


def increase_vaccine_speed():
    !turns_left -= 10


def social_distancing():
    return


def go_back():
    return


#Adding the Buttons
virus_button_upgrade_1 = Button(root, text = "Purchase Cost 10", command = symptom_hiding)
virus_button_upgrade_2 = Button(root, text = "Purchase Cost 7", command = auto_infection)
virus_button_upgrade_3 = Button(root, text = "Purchase Cost 7", command = manual_infection)
virus_button_upgrade_4 = Button(root, text = "Purchase Cost 7", command = investments)
virus_button_upgrade_5 = Button(root, text = "Purchase Cost 5", command = currency_increase)
medic_button_upgrade_1 = Button(root, text = "Purchase Cost 5", command = more_test_kits)
medic_button_upgrade_2 = Button(root, text = "Purchase Cost 3", command = increase_hospital_capacity)
medic_button_upgrade_3 = Button(root, text = "Purchase Cost 5", command = increase_vaccine_speed)
medic_button_upgrade_4 = Button(root, text = "Purchase Cost 10", command = social_distancing)
medic_button_upgrade_5 = Button(root, text = "Purchase Cost 5", command = currency_increase)
back_button = Button(root, text = "BACK", command = go_back)
virus_button_1_cost = 10
virus_button_2_cost = 7
virus_button_3_cost = 7
virus_button_4_cost = 7
virus_button_5_cost = 5

medic_button_1_cost = 5
medic_button_2_cost = 3
medic_button_3_cost = 5
medic_button_4_cost = 10
medic_button_5_cost = 5


virus_button_upgrade_1.grid(row = 4, column = 0)
virus_button_upgrade_2.grid(row = 4, column = 1)
virus_button_upgrade_3.grid(row = 4, column = 2)
virus_button_upgrade_4.grid(row = 4, column = 3)
virus_button_upgrade_5.grid(row = 4, column = 4)
medic_button_upgrade_1.grid(row = 4, column = 6)
medic_button_upgrade_2.grid(row = 4, column = 7)
medic_button_upgrade_3.grid(row = 4, column = 8)
medic_button_upgrade_4.grid(row = 4, column = 9)
medic_button_upgrade_5.grid(row = 4, column = 10)
back_button.grid(row = 0, column = 0)

!player_1_turn = True
!player_2_turn = not player_1_turn
#If Conditions
if player_1_turn:
    medic_button_upgrade_1["state"] = "disabled"
    medic_button_upgrade_2["state"] = "disabled"
    medic_button_upgrade_3["state"] = "disabled"
    medic_button_upgrade_4["state"] = "disabled"
    medic_button_upgrade_5["state"] = "disabled"
    virus_button_upgrade_1["state"] = "active"
    virus_button_upgrade_2["state"] = "active"
    virus_button_upgrade_3["state"] = "active"
    virus_button_upgrade_4["state"] = "active"
    virus_button_upgrade_5["state"] = "active"

elif player_2_turn:
    medic_button_upgrade_1["state"] = "active"
    medic_button_upgrade_2["state"] = "active"
    medic_button_upgrade_3["state"] = "active"
    medic_button_upgrade_4["state"] = "active"
    medic_button_upgrade_5["state"] = "active"
    virus_button_upgrade_1["state"] = "disabled"
    virus_button_upgrade_2["state"] = "disabled"
    virus_button_upgrade_3["state"] = "disabled"
    virus_button_upgrade_4["state"] = "disabled"
    virus_button_upgrade_5["state"] = "disabled"

if virus_button_1_cost > virus_points:
    virus_button_upgrade_1["state"] = "disabled"
else:
    virus_button_upgrade_1["state"] = "active"

if virus_button_2_cost > virus_points:
    virus_button_upgrade_2["state"] = "disabled"
else:
    virus_button_upgrade_2["state"] = "active"

if virus_button_3_cost > virus_points:
    virus_button_upgrade_3["state"] = "disabled"
else:
    virus_button_upgrade_3["state"] = "active"

if virus_button_4_cost > virus_points:
    virus_button_upgrade_4["state"] = "disabled"
else:
    virus_button_upgrade_4["state"] = "active"
    
if virus_button_5_cost > virus_points:
    virus_button_upgrade_5["state"] = "disabled"
else:
    virus_button_upgrade_5["state"] = "active"

if medic_button_1_cost > medic_points:
    medic_button_upgrade_1["state"] = "disabled"
else:
    medic_button_upgrade_1["state"] = "active"

if medic_button_2_cost > medic_points:
    medic_button_upgrade_2["state"] = "disabled"
else:
    medic_button_upgrade_2["state"] = "active"

if medic_button_3_cost > medic_points:
    medic_button_upgrade_3["state"] = "disabled"
else:
    medic_button_upgrade_3["state"] = "active"

if medic_button_4_cost > medic_points:
    medic_button_upgrade_4["state"] = "disabled"
else:
    medic_button_upgrade_4["state"] = "active"
    
if medic_button_5_cost > medic_points:
    medic_button_upgrade_5["state"] = "disabled"
else:
    medic_button_upgrade_5["state"] = "active"


root.mainloop()
