"""
Minna Chae
TCSS 501 and 502
Dungeon Adventure
"""

"contains main logic on playing the game"
from Adventurer import Adventurer
from Dungeon_Minna import Dungeon
import random
import sys, time

class DungeonAdventure:

    def __init__(self):
        self.menu = {"Action Menu": "m", "Go North": "n", "Go South": "s", "Go East": "e", "Go West": "w",
                     "Use Health Potion": "h", "Use Vision": "v", "View current status": "stats", "Quit": "q"}
        self.hidden_menu_option = "map"
        self.dungeon = Dungeon(5,5)
        self.adventurer = Adventurer()
        self.player_loc_col = 0
        self.player_loc_row = 0
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
        """
        Prints Introduction and game background
        """
        print("Welcome to Dungeon Adventure where you may traverse the dangerous dungeons to find the secret exit. \n"
              "In this game, you will find a multiple of surprises in each room such as a healing potion, vision potion, or"
              " fall into a pit. \nThe healing potion can be stored and used to heal your HP. The Vision potion and be stored"
              "and allows you to look at the rooms \naround you. The pit will take away HP. The goal of this game is to "
              "survive and find all 4 pillars of OO: Abstraction, \nEncapsulation, Inheritance, and Polymorphism to win. If "
              "you die before you find the 4 pillars, you lose. \n")

    def set_play_mode(self):
        """
        Setting up play mode level based on user input and setting attributes to Adventurer
        :return: None
        """
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
        print(f"this is self.adventurer {self.adventurer}") #for debugging purposes

    def menu_str(self):
        """Reminder: Include a hidden menu option for testing that prints out the
        entire Dungeon -- specify what the menu option is in your documentation for the DungeonAdventure class
        :return: menu str display for player moves
        """
        formatted_list = [item + " : " + values for item, values in self.menu.items()]
        return "\n" + "\n".join(formatted_list) + "\n"


    def set_up_player(self):
        #Prints the current room (this is based on the Adventurer's current location)
        #Determines the Adventurer's options (Move, Use a Potion)
        #Continues this process until the Adventurer wins or dies
        #At the conclusion of the game, display the entire Dungeon
        # dungeon = Dungeon(5,5) I should create dungeon eventually
        """
        Sets up the game by creating the dungeon maze and locating the starting coordinates
        """
        self.dungeon.build_dungeon()
        self.player_str = self.dungeon.get_entrance()
        self.player_loc_col = 0
        self.player_loc_row = 0
        #create better code for ths

    def get_input_player(self):
        menu_command = ""
        item = ""
        while item != "O" or menu_command.lower() != "q":
            menu_command = input("What is your next move? Enter \"m\" for menu: ")
            # while still in maze and not quit
            if menu_command.lower() == "q":
                break
            elif str(menu_command).lower() == "m":
                #call for menu
                print(self.menu_str())
            elif str(menu_command).lower() == "h":
                #use health potion
                if self.adventurer.__get_health_potion_count__() >0:
                    self.adventurer.inc_HP()
                    print(f"Your health is now {self.adventurer.get_HP()}")
                else:
                    print("You don't have any health potions left")
            elif str(menu_command).lower() == "v":
                if self.adventurer.__get_vision_potion_count__() > 0:
                    self.adventurer.dec_vision_potion()

                    #do the vision code
                else:
                    print("You don't have any vision potions left")

            elif menu_command.lower() == "e" or menu_command.lower() == "w" or menu_command.lower() == "s" or menu_command.lower() == "n":
                #moving character
                item = self.move_adventurer(menu_command)

                #if the player reaches an exit or dies, break out of the game
                if item == "O" or self.adventurer.get_HP() < 0 or self.adventurer.get_pillar() == 4:
                    break
            elif str(menu_command).lower() == "map":
                self.dungeon.print_dungeon()
                self.dungeon.print_dictionary()
            else:
                print("Not a valid command")


        # ask if player wants to use potion or vision
    def move_adventurer(self, menu_command):
        """
        If player input is a director, move to that direction if possible
        :return: item in next room
        """
        new_row, new_col = self.dungeon._get_neighbor_coords(self.player_loc_row, self.player_loc_col,
                                                             str(menu_command).upper())
        # print(f"is valid coords? {self.dungeon.is_valid_room(new_row, new_col)}")
        if self.dungeon.is_valid_room(new_row, new_col):
            self.player_loc_row, self.player_loc_col = new_row, new_col
            print(f"this is new coors row: {self.player_loc_row} col: {self.player_loc_col}")
            print(self.dungeon.get_room_str((new_row, new_col)))
            print(f"{self.dungeon.get_room_contents((self.player_loc_row, self.player_loc_col))}")
            item = self.dungeon.get_room_contents((self.player_loc_row, self.player_loc_col))
            if item == "H":
                self.adventurer.inc_healing_potion_count()
                print(f"Increased healing: {self.adventurer.__get_health_potion_count__()}")
            elif item == "V":  # vision
                self.adventurer.inc_vision_potion_count()
                print(f"Increased vision: {self.adventurer.__get_vision_potion_count__()}")
            elif item == "X":  # pit- come back to it
                self.adventurer.dec_HP()
                print(f"Pit! Decreased HP: {self.adventurer.get_HP()}")
                if self.adventurer.get_HP() < 0:
                    print("You have died and lost the game!")
                    return item
            elif item == "O":  # exit
                print("You found the exit to the dungeon")
                return item
            elif item == "M":  # get multiple items- come back to it
                self.adventurer.inc_healing_potion_count()
                print(f"You got a pillar! Total Pillars: {self.adventurer.get_pillar()}")
            elif item == "A":  # abstraction
                self.adventurer.inc_pillar()
                print(f"You got a pillar! Total Pillars: {self.adventurer.get_pillar()}")
            elif item == "P":  # polymorphism
                self.adventurer.inc_pillar()
                print(f"You got a pillar! Total Pillars: {self.adventurer.get_pillar()}")
            elif item == "I":  # inheritance
                self.adventurer.inc_pillar()
                print(f"You got a pillar! Total Pillars: {self.adventurer.get_pillar()}")
            elif item == "E":  # encapsulation
                self.adventurer.inc_pillar()
                print(f"You got a pillar! Total Pillars: {self.adventurer.get_pillar()}")
            # print(f"this is self.adventurer after update{self.adventurer}")
        else:
            print("Not valid direction")
            print(f"Current location: row: {self.player_loc_row} col: {self.player_loc_col}")
            return

    def player_results(self):
        if self.adventurer.get_pillar() == 4:
            print(f"You won the game and found all {self.adventurer.get_pillar()} pillars!")

        else:
            print(f"Sorry, you have lost the game")
        see_stats = input("Do you want to see your stats? y/n ")
        if see_stats.lower() == "y" or see_stats.lower() == "yes":
            print(self.adventurer)
        else:
            print("I guess you'll never know")

    def print_end(self):
        time.sleep(1)
        group_names = ("\nSarah St. Albin\nAqueno Amalraj  \nMinna Chae \n")
        teacher_names = ("Varik Hoang \nRobert Cordingly \nAshutosh Engavle")
        print("Thank you for playing Dungeon Adventure. \nThis game was created by")
        for character in group_names:
            sys.stdout.write(character)
            sys.stdout.flush()
            time.sleep(.05)
        print("\nA special thanks to our instructors ")
        for character in teacher_names:
            sys.stdout.write(character)
            sys.stdout.flush()
            time.sleep(.05)
        print("\nWe could not have done it without you.")



    # Prints the current room(this is based on the Adventurer 's current location)
    # Determines the Adventurer 's options (Move, Use a Potion)
    # Continues this process until the Adventurer wins or dies
game_play = DungeonAdventure()
