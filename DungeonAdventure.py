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

""" 
Dungeon Adventure contains the main logic of playing the game. 
Game play must be initiated by creating an instance of the class and calling the module 
play_whole_game. This file
will have the set up created after the class.

This game provides 4 levels, Easy, Medium, Hard, and Player's Choice.
Easy provides a 5x5 dungeon maze with the player at 100 HP, 3 healing potions, random vision
potions between 1 and 3. Medium provides a 10x10 dungeon maze with the player at random 
generated HP of 75 to 100, random healing potions of 0 to 2, and random vision potions 
of 0 to 1. Hard provides a 15x15 dungeon maze with the player at random 
generated HP of 75 to 90, 0 healing potions, and 0 vision potions. Player's choice allows
the player to choose any HP, healing potion, vision potion, and dungeon size as long as the
dungeon size is equal to or larger than 3x3. HP can be negative but player will instantly die.
Healing and vision potions can be negative but that will count against player.

Players can use the Action menu option to view keyboard inserts "Action Menu": "m", "Go Up": 
"w", "Go Down": "s", "Go Left": "a", "Go Right": "d", "Use Health Potion": "h", "Use Vision": 
"v", "View current status": "stats", "Quit Game": "q". The hidden/secret menu option is "map"
which will print the whole map and item layout.

Each time a player moves, the output will be a display of the map. Traveled Rooms will be 
indicated by the notation --- and not yet traveled rooms will be indicated by the notation ^^^.
Player's current location will display the current layout of the room. There is also a print
of only the current room after the map layout.

If a player picks up items or falls into a pit, a print statement will indicate these added or
negative points.

"""
class DungeonAdventure:

    def __init__(self):
        self.menu = {"Action Menu": "m", "Go Up": "w", "Go Down": "s", "Go Left": "a", "Go Right": "d",
                     "Use Health Potion": "h", "Use Vision": "v", "View current status": "stats", "Quit Game": "q"}
        self.hidden_menu_option = "map" #prints dungeon
        self.dungeon = Dungeon(5, 5)
        self.adventurer = Adventurer()
        self.player_loc_col = 0
        self.player_loc_row = 0
        self.original_dungeon = copy.deepcopy(self.dungeon)
        self.item = DungeonItemsFactory()

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
            play = input("Would you like to play again? \"y\" to keep playing or enter any key to exit. ")
        self.print_end()

    def print_introduction(self):
        """
        Prints Introduction and game play
        """
        print("\nWelcome to the Dungeon Adventure Game, where you may traverse a dangerous maze in hopes \nof finding "
              "the 4 pillars of Object Oriented Programing (OOP) - Abstraction, Encapsulation, \nInheritance, "
              "and Polymorphism. Within the dungeon's maze you will find surprises, such \nas healing potions, "
              "vision potions, or pits. Items will be stored and healing potions \ncan be used to increase your HP, "
              "or health points. The Vision potion allows you to see \nthrough the walls of surrounding rooms. Falling "
              "into a pit will lower your HP. Be careful \nnot to die and lose the game. Survive and find all pillars of OOP to win. "
              "\n \nTo travel, press keys w for Up, s for Down, a for Left, and d for Right. "
              "\nPress \"m\" to view menu options for legend key.\n")

    def set_play_mode(self):
        """
        Setting up play mode level based on user input. Adventure attributes health, health potion count,
        vision potion count, dungeon dimension are set up in this module
        :return: None
        """
        input_play_mode = input(f"Choose: Easy/e, Medium/m, Hard/h, or players choice (c/choice)? Default will be Easy. ")
        if input_play_mode.lower() == "medium" or input_play_mode.lower() == "m":
            HP = random.randint(75, 100)
            healing_potion_count = random.randint(0, 2)
            vision_potion_count = random.randint(0, 1)
            self.dungeon = Dungeon(10, 10)
            self.original_dungeon = copy.deepcopy(self.dungeon)
            print(f"Play mode is Medium with dungeon dimension of 10x10")
        elif input_play_mode.lower() == "hard" or input_play_mode.lower() == "h":
            HP = random.randint(75, 90)
            healing_potion_count = 0
            vision_potion_count = 0
            self.dungeon = Dungeon(15, 15)
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

            self.dungeon = Dungeon(int(row), int(col))
            self.original_dungeon = copy.deepcopy(self.dungeon)
            print(f"Play mode is Player's Choice with dungeon dimension of {row}x{col}")

        else:
            HP = 100
            healing_potion_count = 3
            vision_potion_count = random.randint(1, 3)
            self.dungeon = Dungeon(5, 5)
            self.original_dungeon = copy.deepcopy(self.dungeon)
            print(f"Play mode is Easy with dungeon dimension of 5x5")

        name = input("What is your name? ")

        self.adventurer.__init__(name, HP, healing_potion_count, vision_potion_count)
        print(f"Your stats: {self.adventurer}")


    def menu_str(self):
        """
        Creates and returns the menu string. Hidden menu option "map" prints dungeon map
        :return: str
        """
        formatted_list = ["    " + item + " : " + values for item, values in self.menu.items()]
        return "\n".join(formatted_list) + "\n"

    def set_up_player(self):
        """
        Sets up the game by creating the dungeon maze and locating the starting coordinates
        :return: None
        """
        self.player_str = self.dungeon.get_entrance()

        self.player_loc_col = 0
        self.player_loc_row = 0
        self.dungeon.set_player_traveled((self.player_loc_row,self.player_loc_col))

    def player_command(self):
        """
        Execute player's menu inputs
        :return: None
        """
        response = ""
        if self.adventurer.get_HP() > 0:
            self.dungeon.print_play_dungeon(self.player_loc_row, self.player_loc_col)

        while self.adventurer.get_HP() > 0:
            menu_command = input("What is your next move? Enter \"m\" for menu: ")
            # while still in maze and not quit
            # quits game
            if menu_command.lower() == "q":
                break
            # prints menu
            elif str(menu_command).lower() == "m":
                print(self.menu_str())
            # use health potion
            elif str(menu_command).lower() == "h":
                if self.adventurer.get_health_potion_count__() > 0:
                    health_points = self.item.create_item("H", 1, 10).use_item()
                    self.adventurer.set_HP(health_points)
                    print(f"You gained {health_points} health points! Your health is now "
                          f"{self.adventurer.get_HP()} and you have "
                          f"{self.adventurer.get_health_potion_count__()} left.")
                else:
                    print("You don't have any health potions left")
            # use vision potion
            elif str(menu_command).lower() == "v":
                if self.adventurer.get_vision_potion_count__() > 0:
                    self.adventurer.dec_vision_potion()
                    self.item.create_item("V").use_vision(self.player_loc_row, self.player_loc_col, self.dungeon.get_col_length(),
                                           self.dungeon.get_row_length(), self.dungeon)
                else:
                    print("You don't have any vision potions left")
            # print adventurer statistics
            elif str(menu_command).lower() == "stats":
                print(self.adventurer)
            # move adventurer in dungeon
            elif (menu_command.lower() == "w" or menu_command.lower() == "a" or menu_command.lower() == "s" or
                  menu_command.lower() == "d"):
                #moving character
                item = self.move_adventurer(menu_command)

                #if the player dies end  game
                if self.adventurer.get_HP() <= 0:
                    break
                #reached exit, ask to leave game
                elif item == "O":
                    while True:
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
                if response.lower() == "y" or response.lower() == "yes":
                    break
            elif str(menu_command).lower() == "map":
                # Secret menu prints map and uses @ for player location
                self.dungeon.print_dungeon(self.player_loc_row, self.player_loc_col)
            else:
                print("Not a valid command")

    def move_adventurer(self, menu_command="g"):
        """
        Player's input is a direction, check to see if that direction is possible and move that direction.
        If moving to next room is possible, collect items and make traveled rooms empty unless pit
        :return: str
        """
        #Getting direction
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
        # checking to see if next move is going to an actual room
        if self.dungeon.is_valid_room(new_row, new_col):
            new_key = self.dungeon._get_neighbor_coords(self.player_loc_row, self.player_loc_col, real_direction)
            current_key = self.player_loc_row, self.player_loc_col

            #If there is a door to enter into the next room
            if self.dungeon.get_doors(current_key, new_key, real_direction):
                self.player_loc_row, self.player_loc_col = new_row, new_col
                self.dungeon.print_play_dungeon(self.player_loc_row, self.player_loc_col)
                print(self.dungeon.get_room_str((new_row, new_col)))
                self.dungeon.set_player_traveled((self.player_loc_row, self.player_loc_col))
                item = self.dungeon.get_room_contents((self.player_loc_row, self.player_loc_col)) #item = get room content, str
                item = self.collect_item(item)  #item = get room content, str
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
            return

    def collect_item(self, item="a"):
        """
        Items in room affects the player and returns item str if needed
        :return: str
        """
        # Collect Health potion
        if item == "H":
            self.adventurer.inc_healing_potion_count()
            print(f"Picked up Healing Potion. Total Healing Potions: {self.adventurer.get_health_potion_count__()}")
            self.dungeon.set_room_empty((self.player_loc_row, self.player_loc_col), False) #removing item from dungeon
        # Collect Vision potion
        elif item == "V":
            self.adventurer.inc_vision_potion_count()
            print(f"Picked up Vision Potion. Total Vision Potions: {self.adventurer.get_vision_potion_count__()}")
            self.dungeon.set_room_empty((self.player_loc_row,self.player_loc_col),False)
        # Encounter Pit
        elif item == "X":
            pit_points = self.item.create_item("X", 1, 15)
            self.adventurer.set_HP(pit_points.use_item())
            print(f"You fell into a Pit! You lost {pit_points.use_item()} points. Current HP: {self.adventurer.get_HP()}.")
        # find exit
        elif item == "O":
            return item
        # Collect multiple items
        elif item == "M":
            self.multi_items()
        # collect Abstraction pillar
        elif item == "A":  # abstraction
            self.adventurer.inc_pillar()
            self.dungeon.set_room_empty((self.player_loc_row, self.player_loc_col),False)
            print(f"You found the Abstraction pillar! Total Pillars: {self.adventurer.get_pillar()}")
        # collect polymorphism pillar
        elif item == "P":
            self.adventurer.inc_pillar()
            self.dungeon.set_room_empty((self.player_loc_row, self.player_loc_col),False)
            print(f"You found the Polymorphism pillar! Total Pillars: {self.adventurer.get_pillar()}")
        # collect inheritance pillar
        elif item == "I":  # inheritance
            self.adventurer.inc_pillar()
            self.dungeon.set_room_empty((self.player_loc_row, self.player_loc_col),False)
            print(f"You found the Inheritance pillar! Total Pillars: {self.adventurer.get_pillar()}")
        # collect encapsulation pillar
        elif item == "E":  # encapsulation
            self.adventurer.inc_pillar()
            self.dungeon.set_room_empty((self.player_loc_row, self.player_loc_col),False)
            print(f"You found the Encapsulation pillar! Total Pillars: {self.adventurer.get_pillar()}")
        else:
            return item

    def multi_items(self):
        """
        When player encounters multi item room
        :return: None
        """
        items = ["V", "H", "X", ""]
        results = random.sample(items, 3)
        pit = False
        for value in results:
            if value == "V":
                self.adventurer.inc_vision_potion_count()
                print(f"Gained 1 Vision Potion. Total Vision Potion count: {self.adventurer.get_vision_potion_count__()}")
            if value == "H":
                self.adventurer.inc_healing_potion_count()
                print(f"Gained 1 Healing Potion. Total Healing Potion count: {self.adventurer.get_health_potion_count__()}")
            if value == "X":
                pit_points = self.item.create_item("X", 1, 15)
                self.adventurer.set_HP(pit_points.use_item())
                print(
                    f"You fell into a Pit! You lost {pit_points.use_item()} points. Current HP: {self.adventurer.get_HP()}.")
        self.dungeon.set_room_empty((self.player_loc_row, self.player_loc_col), pit)

    def player_results(self):
        """
        Game has ended and prints Adventurer results
        :return: None
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
        time.sleep(.1)
        group_names = ("Aqueno Nirasmi Amalraj \nMinna Chae \nSarah St. Albin \n")
        teacher_names = ("Varik Hoang \nRobert Cordingly \nAshutosh Engavle")
        print("\n")
        print("Thank you for playing Dungeon Adventure. \nThis game was created by\n")
        for character in group_names:
            sys.stdout.write(character)
            sys.stdout.flush()
            time.sleep(.05)
        print("\nA special thanks to our instructors \n")
        for character in teacher_names:
            sys.stdout.write(character)
            sys.stdout.flush()
            time.sleep(.05)
        print("\n\nWe could not have done it without you.")


game_play = DungeonAdventure()
game_play.play_whole_game()
