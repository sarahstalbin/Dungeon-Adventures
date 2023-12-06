"""
Minna Chae
TCSS 501 and 502
Dungeon Adventure
"""

"contains main logic on playing the game"
from Adventurer import Adventurer
# from dungeon import Dungeon
import random

class DungeonAdventure:

    #easy, medium , hard
    play_mode = input(f"Choose: Easy, Medium, or Hard? Default will be Easy. ")
    print(f"this is play_mode {play_mode.lower()}")
    if play_mode.lower() == "medium":
        HP = random.randint(75, 100)
        healing_potion_count = random.randint(0, 2)
        vision_potion_count = random.randint(0, 1)
    elif play_mode.lower() == "hard":
        HP = random.randint(75, 90)
        healing_potion_count = 0
        vision_potion_count = 0
    else:
        HP = 100
        healing_potion_count = 3
        vision_potion_count = random.randint(0, 2)
    print("Welcome to Dungeon Adventure where you may traverse the dangerous dungeons to find the secret exit. \n"
          "In this game, you will find a multiple of surprises in each room such as a healing potion, vision potion, or"
          " fall into a pit. \nThe healing potion can be stored and used to heal your HP. The Vision potion and be stored"
          "and allows you to look at the rooms \naround you. The pit will take away HP. The goal of this game is to "
          "survive and find all 4 pillars of OO: Abstraction, \nEncapsulation, Inheritance, and Polymorphism to win. If "
          "you die before you find the 4 pillars, you lose. \n")
    name = input("What is your name? ")
    adventurer = Adventurer(HP, name, healing_potion_count, vision_potion_count)
    print(f"Hello {adventurer.get_name()}. Welcome to the Dungeon Adventurer game.")
    print(f"Here are your current details: {adventurer}")
    #Prints the current room (this is based on the Adventurer's current location)
    #Determines the Adventurer's options (Move, Use a Potion)
    #Continues this process until the Adventurer wins or dies
    #NOTE: Include a hidden menu option for testing that prints out the entire Dungeon -- specify what the menu
    #   option is in your documentation for the DungeonAdventure class
    #At the conclusion of the game, display the entire Dungeon
    # dungeon = Dungeon()