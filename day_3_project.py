# -*- coding: utf-8 -*-
"""Day 3 Project.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1pNcqIfGHCLr5JKUTyOCUZls0kdTGQWFc
"""

print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 
print("Danger is acound every corner")

Q1 = input('You are walking on a game trail which comes to a fork. You can go "left" or "right" , which do you choose.\n').lower()

if Q1 == "left":
  print("You went to the right and found a shelter to spend the night in")
else:
  print("You went farther into the Jungle and got lost and died")

print("The next day you find a large lake with an acient temple on the far side")

Q2 = input("Do you take the time to make a 'raft' to cross the river or do you 'swim'?\n Enter raft or swim  ").lower

if Q2 == "raft":
  print("The raft you built made it half way across the lake but came apart. You got tangled in the vines and sunk to the botton of the lake")
else:
  print("You swam across the lake and even found food to eat on the other side.")

print('You enter the temple and come to 3 doors.')

Q3 = input('One "Red", one "Blue", and one "Yellow". Which door do you go through? \n').lower()

if Q3 == "red":
  print("You step inside the door closes behind you and the room is engulfed in fire")
elif Q3 == "blue":
  print("You step in side the door closes behind you and the room fills with water. You don\'t make it out")
else:
  print("You step inside to find a room of gold. The door closes behind you and the floor gives out and you slide down and out of the temple with the gold.")

print("Thanks for playing")