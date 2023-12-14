"""
Name: Aqueno Nirasmi, Minna Chae, Sarah St. Albin
TCSS 501 and 502
Dungeon Adventure
"""


from Adventurer import Adventurer
from Dungeon import Dungeon
from DungeonItemsFactory import DungeonItemsFactory
import random
import sys, time
import copy

""" Dungeon Adventure contains the main logic of playing the game."""
class DungeonAdventure:

    def __init__(self):
        self.menu = {"Action Menu": "m", "Go up": "w", "Go down": "s", "Go Left": "a", "Go Right": "d",
                     "Use Health Potion": "h", "Use Vision": "v", "View current status": "stats", "Quit": "q"}
        self.hidden_menu_option = "map" #prints dungeon
        self.dungeon = Dungeon(5,5)
        self.adventurer = Adventurer()
        self.player_loc_col = 0
        self.player_loc_row = 0
        self.original_dungeon = ""
        self.vision_potion = DungeonItemsFactory.create_item("V")
        self.healing_potion = DungeonItemsFactory.create_item("H", 1, 5)
        self.pit = DungeonItemsFactory.create_item("X", 1, 15)




    def play_whole_game(self):
        """
        Plays full game from top to bottom
        :return: None
        """
        self.print_introduction()
        play = "y"
        while play.lower() == "y" or play.lower() == "yes":
            self.set_play_mode()
            print(self.menu_str())
            self.set_up_player()
            self.player_command()
            print("\nOriginal maze:\n")
            self.original_dungeon.print_dungeon()
            print("Your maze:\n")
            self.dungeon.print_dungeon()
            self.player_results()
            play = input("Would you like to play again? \"y\" to keep playing or press any key to exit. ")
        self.print_end()

    def print_introduction(self):
        """
        Prints Introduction and game play
        """
        print("Welcome to the Dungeon Adventure Game, where you will traverse a dangerous maze to "
              "find the 4 pillars of Object Oriented Programming (OOP) -"
              " Abstraction, Encapsulation, Inheritance, and Polymorphism. \n"
              "To travel, use keys Up (w), down (s), left (a), and right (d). "
              "Within the dungeon's maze you will find many surprises, such as healing potions and "
              "vision potions. Or you may fall into a pit! "
              "\nHealing potions can be stored and used to increase your HP, or health points. The Vision potion "
              "can be stored and allows you to see through the walls of surrounding rooms. \n Falling into a pit will "
              "lower your HP. Be careful not to lose all your HP and die! The goal of this game is to "
              "survive and find all 4 pillars of OOP. Use \"m\" to look at menu options for information.\n")

    def set_play_mode(self):
        """
        Setting up play mode level based on user input. Adventure attributes health, health potion count,
        vision potion count, dungeon dimension are set up in this module
        :return: None
        """
        input_play_mode = input(f"Choose: Easy/e, Medium/m, Hard/h, or players choice (c/choice)? Default will be Easy. ")

        # ----------------------------------Delete for debugging ------------------------------------------
        if input_play_mode.lower() == "medium" or input_play_mode.lower() == "m":
            HP = random.randint(75, 100)
            healing_potion_count = random.randint(0, 2)
            vision_potion_count = random.randint(0, 1)
            self.dungeon = Dungeon(10, 10) #static number
            self.healing_potion = DungeonItemsFactory.create_item("H", 1, 5)
            self.pit = DungeonItemsFactory.create_item("X", 1, 15)
            self.original_dungeon = copy.deepcopy(self.dungeon)
            print(f"Play mode is Medium with dungeon dimension of 10x10")
        elif input_play_mode.lower() == "hard" or input_play_mode.lower() == "h":
            HP = random.randint(75, 90)
            healing_potion_count = 0
            vision_potion_count = 0
            self.dungeon = Dungeon(15, 15) #static number
            self.healing_potion = DungeonItemsFactory.create_item("H", 1, 5)
            self.pit = DungeonItemsFactory.create_item("X", 1, 20)
            self.original_dungeon = copy.deepcopy(self.dungeon)
            print(f"Play mode is Hard with dungeon dimension of 15x15")
        elif input_play_mode.lower() == "choice" or input_play_mode.lower() == "c":
            while True:
                choice = input("Desired health points? ")
                try:
                    HP = int(choice)
                    break
                except ValueError:
                    print("\nMust be a number")
            while True:
                choice = input("Healing Potion count? ")
                try:
                    healing_potion_count = int(choice)
                    break
                except ValueError:
                    print("\nMust be a number.")
            while True:
                choice = input("Vision Potion count? ")
                try:
                    vision_potion_count = int(choice)
                    break
                except ValueError:
                    print("\nMust be a number.")
            while True:
                row = input("Row Dimension? Must be larger than 2. ")
                try:
                    row = int(row)
                    if row >= 3:
                        break
                    else:
                        print("\nRow dimension must not be smaller than 2")
                except ValueError:
                    print("\nMust be a number")

            while True:
                col = input("Column Dimension? Must be larger than 2 ")
                try:
                    col = int(col)
                    if col >= 3:
                        break
                    else:
                        print("\nRow dimension must not be smaller than 2.")
                except ValueError:
                    print("\nMust be a number")

            self.dungeon = Dungeon(int(row), int(col)) #static number
            self.original_dungeon = copy.deepcopy(self.dungeon)
            print(f"Play mode is Player's Choice with dungeon dimension of {row}x{col}")

        else:
            HP = 100
            healing_potion_count = 3
            vision_potion_count = random.randint(1, 3)
            self.dungeon = Dungeon(5, 5) #static number
            self.original_dungeon = copy.deepcopy(self.dungeon)
            self.healing_potion = DungeonItemsFactory.create_item("H", 5, 10)
            self.pit = DungeonItemsFactory.create_item("X", 1, 5)
            print(f"Play mode is Easy with dungeon dimension of 5x5")

        name = input("What is your name? ")

        self.adventurer.__init__(name, HP, healing_potion_count, vision_potion_count)
        print(f"Your stats: {self.adventurer}")


    def menu_str(self):
        """Hidden menu option "map" prints dugeon -- specify what the menu option is in your documentation
        for the DungeonAdventure class
        Creates the menu string to be printed
        :return: menu str
        """
        formatted_list = ["    " + item + " : " + values for item, values in self.menu.items()]
        return "\n".join(formatted_list) + "\n"


    def set_up_player(self):
        """
        Sets up the game by creating the dungeon maze and locating the starting coordinates
        """
        self.player_str = self.dungeon.get_entrance()

        self.player_loc_col = 0
        self.player_loc_row = 0
        self.dungeon.set_player_traveled((self.player_loc_row,self.player_loc_col))

    def player_command(self):
        """
        Execute player's menu inputs
        :return: None - maybe return menu_command?
        """
        menu_command = ""
        item = ""
        response = ""
        if self.adventurer.get_HP() > 0:
            self.dungeon.print_play_dungeon(self.player_loc_row, self.player_loc_col)
        while self.adventurer.get_HP() > 0:
            menu_command = input("What is your next move? Enter \"m\" for menu: ")
            # while still in maze and not quit
            if menu_command.lower() == "q":
                break
            # if self.adventurer.get_HP() <= 0:
            #     break
            elif str(menu_command).lower() == "m":
                #call for menu
                print(self.menu_str())
            elif str(menu_command).lower() == "h":
                #use health potion
                if self.adventurer.__get_health_potion_count__() >0:
                    print(self.healing_potion.use_item())
                    self.adventurer.set_HP(self.healing_potion.use_item())
                    print(f"You gained {self.healing_potion.use_item()} health points! Your health is now "
                          f"{self.adventurer.get_HP()} and you have "
                          f"{self.adventurer.__get_health_potion_count__()} left.")
                else:
                    print("You don't have any health potions left")
            elif str(menu_command).lower() == "v":
                #use vision potion
                if self.adventurer.__get_vision_potion_count__() > 0:
                    self.adventurer.dec_vision_potion()
                    self.vision_potion.use_vision(self.player_loc_row, self.player_loc_col, self.dungeon.get_col_length(),
                                           self.dungeon.get_row_length(), self.dungeon)
                else:
                    print("You don't have any vision potions left")

            elif str(menu_command).lower() == "stats":
                print(self.adventurer)
            elif (menu_command.lower() == "w" or menu_command.lower() == "a" or menu_command.lower() == "s" or
                  menu_command.lower() == "d"):
                #moving character
                item = self.move_adventurer(menu_command)

                #if the player reaches an exit or dies, break out of the game
                if self.adventurer.get_HP() <= 0:
                    break
                #reached exit
                elif item == "O":
                    while(True):
                        response = input("You have reached the exit. Would you like to leave the maze? (y to leave, "
                                         "pillar to view pillar count, or n to stay: ")
                        if response.lower() == "y" or response.lower() == "yes":
                            break
                        elif response.lower() == "pillar":
                            if self.adventurer.get_pillar() == 1:
                                print(f"You have found {self.adventurer.get_pillar()} pillar so far.")
                            else:
                                print(f"You have found {self.adventurer.get_pillar()} pillars so far.")
                        elif response.lower() == "n" or response.lower() == "no":
                            break
                        else:
                            response = input("Please enter y to leave, pillar to view pillar count, or n to stay: ")
                if response.lower() == "y" or response.lower() == "yes":
                    break
            elif str(menu_command).lower() == "map":
                self.dungeon.print_dungeon(self.player_loc_row, self.player_loc_col)
            else:
                print("Not a valid command")

    def move_adventurer(self, menu_command="g"):
        """
        Player's input is a direction, check to see if that direction is possible and move that direction.
        If moving to next room is possible, collect items and make traveled rooms empty unless pit
        :return: any collected items
        """

        #change input to be direction
        if menu_command == "w":
            real_direction = "N"
        elif menu_command == "s":
            real_direction = "S"
        elif menu_command == "d":
            real_direction = "E"
        elif menu_command == "a":
            real_direction = "W"
        else:
            return menu_command
        #get coordinates for next move
        new_row, new_col = self.dungeon._get_neighbor_coords(self.player_loc_row, self.player_loc_col,
                                                             real_direction)
        if self.dungeon.is_valid_room(new_row, new_col):
            new_key = self.dungeon._get_neighbor_coords(self.player_loc_row, self.player_loc_col, real_direction)
            current_key = self.player_loc_row, self.player_loc_col

            if self.dungeon.get_doors(current_key, new_key, real_direction): #able to move into the room - DO NOT DELETE

                self.player_loc_row, self.player_loc_col = new_row, new_col
                self.dungeon.print_play_dungeon(self.player_loc_row, self.player_loc_col)
                print(self.dungeon.get_room_str((new_row, new_col)))
                self.dungeon.set_player_traveled((self.player_loc_row, self.player_loc_col))
                item = self.dungeon.get_room_contents((self.player_loc_row, self.player_loc_col))
                item = self.collect_item(item)
                if item == "O":
                    print("You found the exit to the dungeon")
                    return item
                if self.adventurer.get_HP() <= 0:
                    print("You have died and lost the game!")
                    return item

            else:
                print("Cannot move that direction because there is no door")

        else:
            print("Not valid direction")
            # print(f"Current location: row: {self.player_loc_row} col: {self.player_loc_col}")
            return

    def collect_item(self, item="g"):
        """
        Items in room affects the player
        :return: any collected
        """
        if item == "H":

            self.adventurer.inc_healing_potion_count()
            print(f"Picked up Healing Potion: {self.adventurer.__get_health_potion_count__()}")
            self.dungeon.set_room_empty((self.player_loc_row, self.player_loc_col), False) #removing item from dungeon

        elif item == "V":  # vision
            self.adventurer.inc_vision_potion_count()
            print(f"Picked up Vision Potion: {self.adventurer.__get_vision_potion_count__()}")
            self.dungeon.set_room_empty((self.player_loc_row,self.player_loc_col),False)
        elif item == "X":  # pit-
            self.adventurer.set_HP(self.pit.use_item())
            print(f"You fell into a Pit! You lost {self.pit.use_item()} points. Current HP: {self.adventurer.get_HP()}.")
        elif item == "O":  # exit
            return item
        elif item == "M":  # get multiple items
            self.multi_items()
        elif item == "A":  # abstraction
            self.adventurer.inc_pillar()
            self.dungeon.set_room_empty((self.player_loc_row, self.player_loc_col),False)
            print(f"You found the Abstraction pillar! Total Pillars: {self.adventurer.get_pillar()}")
        elif item == "P":  # polymorphism
            self.adventurer.inc_pillar()
            self.dungeon.set_room_empty((self.player_loc_row, self.player_loc_col),False)
            print(f"You found the Polymorphism pillar! Total Pillars: {self.adventurer.get_pillar()}")
        elif item == "I":  # inheritance
            self.adventurer.inc_pillar()
            self.dungeon.set_room_empty((self.player_loc_row, self.player_loc_col),False)
            print(f"You found the Inheritance pillar! Total Pillars: {self.adventurer.get_pillar()}")
        elif item == "E":  # encapsulation
            self.adventurer.inc_pillar()
            self.dungeon.set_room_empty((self.player_loc_row, self.player_loc_col),False)
            print(f"You found the Encapsulation pillar! Total Pillars: {self.adventurer.get_pillar()}")
        else:
            return item


    def multi_items(self):
        items = ["V", "H", "X", ""]
        results = random.sample(items, 3)
        pit = False
        print_string = ""
        for value in results:
            if value == "V":
                self.adventurer.inc_vision_potion_count() #should be Factory
                print(f"Increased vision: {self.adventurer.__get_vision_potion_count__()}")
            if value == "H":
                self.adventurer.inc_healing_potion_count()
                print(f"Increased healing: {self.adventurer.__get_health_potion_count__()}")
            if value == "X":
                self.adventurer.set_HP(self.pit.use_item())
                print(f"You fell into a Pit! You lost {self.pit.use_item()} points. Current HP: {self.adventurer.get_HP()}.")
                pit = True
        self.dungeon.set_room_empty((self.player_loc_row, self.player_loc_col), pit)

    def player_results(self):
        """
        Game has ended and prints Adventurer results
        """
        if self.adventurer.get_pillar() == 4:
            print(f"You won the game and found all {self.adventurer.get_pillar()} pillars!")

        elif self.adventurer.get_pillar() == 1:
                print(f"Sorry, you only found {self.adventurer.get_pillar()} pillar. You have lost the game")
        else:
            print(f"Sorry, you only found {self.adventurer.get_pillar()} pillars. You have lost the game")
        see_stats = input("\nDo you want to see your stats? y/n ")
        if see_stats.lower() == "y" or see_stats.lower() == "yes":
            print(self.adventurer)
        else:
            print("I guess you'll never know")

    def print_end(self):
        """
        Prints closing title slides
        """
        time.sleep(1)
        group_names = ("\nAqueno Amalraj \nSarah St. Albin \nMinna Chae \n")
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

    # Determines the Adventurer 's options (Move, Use a Potion)
    # Continues this process until the Adventurer wins or dies
game_play = DungeonAdventure()
game_play.play_whole_game()
