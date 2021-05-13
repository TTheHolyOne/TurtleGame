"""
Made in Python 3.8.2

Developers: Jacob and Sam

This is a test not a real thing just for now. 

This could become a real program day but for now this is 
what you get. 

Looks pretty messy but it works

"""

# Import Modules

# This is our main module for the program

import turtle as t
from turtle import *

# This is so we can make random art
import random as ran

# this is just time
import time

# Important
import os
from PIL import Image
import sys


# all colors it can give

collist = ['red', 'orange', 'yellow', 'black', 'blue', 'purple', 'gold', 'magenta']



# random color gen

rancolor = ran.choice(collist)
rancolor1 = ran.choice(collist)
ranint = ran.randint(100,250)
ranwidth = ran.randint(5,45)



# Clear Function

def clear():
    print('\n'*100)



# Boot Message
print('TURTLE GAME BOOTING...')
time.sleep(1)
clear()




# random turtle game mode

def randomturtle():
    color(rancolor, rancolor1)
    begin_fill()
    while True:
       t.width(ranwidth)
       t.title("Random Turtle")
       forward(ranint)
       left(100)
       if abs(pos()) < 1:
           break
    end_fill()
    done()
    program()

   # Name 
def turtlename():
    name = input("Hey! I heard you want me \nto write your name..!\nPlease enter your name: \n")
    print("Writing...")
    time.sleep(1)
    color(rancolor, rancolor1)
    begin_fill()
    while True:
        t.title("Name Turtle")
        t.color(rancolor)
        style = ('Courier', 20, 'normal')
        t.write(f'{name}', font=style, align='center')
        t.hideturtle()	   

        


# Main Menu

def program():
    options = int(input("""
Welcome To Turtle Game!
Developers:
TTheHolyOne(Jacob) and Sam

Short Description:
Turtle Game is a fun game where you can
see art made and it can make fun colors!


OPTIONS:

1: Randomly Generated Art
2: Write Your Name
3: About
4: Quit
"""))

    # Options

    if options == 1:
        randomturtle()
    
    # Name
    elif options == 2:
        turtlename()

    # About
    elif options == 3:
        print("""
About Turtle Game:

This game is developed by Jacob and Sam

It is mainly just testing of turtle game..!
""")    
        options()

    # Quit
    elif options == 4:
        clear() 
        print('Sad to see you go.. goodbye..')
        time.sleep(1)
        sys.exit()

program()





# hopefully almost never shows

print("Shutting down...")




