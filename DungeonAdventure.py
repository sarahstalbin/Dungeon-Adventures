"""
Minna Chae
TCSS 501 and 502
Dungeon Adventure
"""

"contains main logic on playing the game"
from Adventurer import Adventurer
from Dungeon import Dungeon
import random

class DungeonAdventure:

    def __init__(self):
        self.menu = {"Action Menu": "m", "Go North": "n", "Go South": "s", "Go East": "e", "Go West": "w",
                     "Use Potion": "p", "Use Vision": "v", "View current status": "stats"}
        self.hidden_menu_option = "map"
        self.dungeon = Dungeon(20,20)
        self.adventurer = Adventurer()
        self.player_location = [0,0]
        #creating dungeon and adventure (initializing them)


    # def __str__(self): #menu?
    #     """Printing in string form"""
    #     formatted_list = [str(item) + " : " + str(values) for item, values in self.adventurer_dict.items()]
    #     return "\n" + "\n".join(formatted_list) + "\n"

    # def game_play(self):
    #     """Plays the game"""
    #     game = DungeonAdventure()
    #     game.print_introduction()
    #     # input_play_mode = input(f"Choose: Easy, Medium, or Hard? Default will be Easy. ")
    #     game.set_play_mode()
    #
    #     print(f"Hello {self.adventurer.__get_name__()}. Welcome to the Dungeon Adventurer game.")
    #     print(f"Here are your current details: {self.adventurer}")
    def print_introduction(self):
        """Prints Introduction and game background"""
        print("Welcome to Dungeon Adventure where you may traverse the dangerous dungeons to find the secret exit. \n"
              "In this game, you will find a multiple of surprises in each room such as a healing potion, vision potion, or"
              " fall into a pit. \nThe healing potion can be stored and used to heal your HP. The Vision potion and be stored"
              "and allows you to look at the rooms \naround you. The pit will take away HP. The goal of this game is to "
              "survive and find all 4 pillars of OO: Abstraction, \nEncapsulation, Inheritance, and Polymorphism to win. If "
              "you die before you find the 4 pillars, you lose. \n")

    def set_play_mode(self):
        """Setting Play mode based on user input and setting attributes to Adventurer"""
        input_play_mode = input(f"Choose: Easy, Medium, or Hard? Default will be Easy. ")
        # print("Choose: Easy, Medium, or Hard? Default will be Easy. ") #for debugging purposes
        # input_play_mode = "easy" #for debugging purposes
        if input_play_mode.lower() == "medium":
            HP = random.randint(75, 100)
            healing_potion_count = random.randint(0, 2)
            vision_potion_count = random.randint(0, 1)
            print(f"Play mode is Medium")
        elif input_play_mode.lower() == "hard":
            HP = random.randint(75, 90)
            healing_potion_count = 0
            vision_potion_count = 0
            print(f"Play mode is Hard")
        else:
            HP = 100
            healing_potion_count = 3
            vision_potion_count = random.randint(0, 2)
            print(f"Play mode is Easy")
        name = input("What is your name? ")
        # name = "Minna"#for debugging purposes
        self.adventurer.__init__(name, HP, healing_potion_count, vision_potion_count)
        print(self.adventurer) #for debugging purposes

    def menu_str(self):
        """Return menu display for player moves NOTE: Include a hidden menu option for testing that prints out the
        entire Dungeon -- specify what the menu option"""
        formatted_list = [item + " : " + values for item, values in self.menu.items()]
        return "\n" + "\n".join(formatted_list) + "\n"


    def set_up_player(self):
        #Prints the current room (this is based on the Adventurer's current location)
        #Determines the Adventurer's options (Move, Use a Potion)
        #Continues this process until the Adventurer wins or dies
        #NOTE: Include a hidden menu option for testing that prints out the entire Dungeon -- specify what the menu
        #   option is in your documentation for the DungeonAdventure class
        #At the conclusion of the game, display the entire Dungeon
        # dungeon = Dungeon(5,5) I should create dungeon eventually
        self.dungeon.build_dungeon()
        self.player_str = self.dungeon.__get_entrance__()
        self.player_location = [0,0]
        print(self.player_location)

        #print action menu option
        #n, s, e, w, p: potion, v:vision

    def get_input_player(self):
        menu_command = input("What is your next move? Enter \"m\" for menu: ")
        if str(menu_command).lower() == "m":
            print(self.menu_str())
        elif str(menu_command).lower() == "p":
            if self.adventurer.__get_health_potion_count__() >0:
                #increase healing
                pass
        elif str(menu_command).lower() == "e":
            input_row = 0
            input_col = 0
            print(f"this is str(menu_command).upper {str(menu_command).upper()}")
            row, col = self.dungeon._get_neighbor_coords(input_row, input_col, str(menu_command).upper())
            print(f"this is get neighbor row {row} col {col}")
            print(f"this is self.dungeon.is_valid_room(row, col) {self.dungeon.is_valid_room(row, col)}")
            if self.dungeon.is_valid_room(row, col):
                print(self.dungeon.next_move(row, col))
                # self.dungeon.get_item_in_room(row, col)
        elif str(menu_command).lower() == "map":
            self.dungeon.print_dungeon()
            self.dungeon.print_dictionary()
        # while still in maze
        # next_move = input("What would you like to do next? M for action menu"
        # if next_move.lower = "m":
        # print
        # ask if player wants to use potion or vision

    def __traverse_maze__(self):




            #ask to go N,S,E,W
            #if direction is possible
                #move
            #else
                #request new direction
                #maybe look at dungeon and give options?
            #print room
            #if room has poition
                #adventurer potion+1 & potion value?
            #if room has vision
                #vision +1
            #if pit
                #-HP
            #if pillar
                #pillar +=1

            #grab necessary objects and values of object and pass into adventurer
            #adventurer
        person = self.dungeon.next_move(0,1)
        print(person)
        # dungeon.print_dictionary()



    # Prints the current room(this is based on the Adventurer 's current location)
    # Determines the Adventurer 's options (Move, Use a Potion)
    # Continues this process until the Adventurer wins or dies
game_play = DungeonAdventure()
