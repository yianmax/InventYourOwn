# Adapted from Invent Your Own Computer Games with Python,
# 2nd edition, Al Steigwart

import random
import time
from os import system, name

INTRO_TEXT = ["You are on a planet full of dragons.",
              "In front of you, you see two caves.",
              "In one cave, the dragon is friendly\nand will share his treasure with you.",
              "The other dragon is greedy and hungry,\nand will eat you on sight.\n"]


def displayIntro(text):
    for line in text:
        print line
        time.sleep(2)
    


def chooseCave():
    cave = ''
    while cave != '1' and cave != '2':
        print('Which cave will you go into? (1 or 2)')
        cave = raw_input()
    return cave

def checkCave(chosenCave):
    print('You approach the cave...')
    time.sleep(2)
    print('It is dark and spooky...')
    time.sleep(2)
    print('A large dragon jumps out in front of you! He opens his jaws and...\n')
    time.sleep(3)
    friendlyCave = random.randint(1,2)

    if chosenCave == str(friendlyCave):
        print('Gives you his treasure!')
    else:
        print('Gobbles you down in one bite!')


def clear():

    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')


#--- Main body ---
clear()
playAgain = 'yes'
while playAgain[0].lower() == 'y':

    displayIntro(INTRO_TEXT)

    caveNumber = chooseCave()

    checkCave(caveNumber)
    
    time.sleep(2)
    print('\nDo you want to play again? (yes or no)')
    playAgain = raw_input()
