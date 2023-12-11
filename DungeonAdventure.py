"""
Minna Chae
TCSS 501 and 502
Dungeon Adventure
"""

"""contains main logic on playing the game"""
from Adventurer import Adventurer
from Dungeon_Minna import Dungeon
import random
import sys, time


class DungeonAdventure:

    def __init__(self):
        self.menu = {"Action Menu": "m", "Go up": "w", "Go down": "s", "Go Left": "a", "Go Right": "d",
                     "Use Health Potion": "h", "Use Vision": "v", "View current status": "stats", "Quit": "q"}
        self.hidden_menu_option = "map" #prints dungeon
        self.dungeon = Dungeon(5,5)
        self.adventurer = Adventurer()
        self.player_loc_col = 3
        self.player_loc_row = 3


    def play_whole_game(self):
        """
        Plays full game from top to bottom
        :return: None
        """
        self.print_introduction()
        play = "y"
        while play.lower() == "y":
            self.set_play_mode()
            # print(play_game.menu_str())
            self.set_up_player()
            self.player_command()
            self.dungeon.print_dungeon()
            self.player_results()
            play = input("Would you like to play again? \"y\" to keep playing or any key to exit. ")

        # self.print_end()

    def print_introduction(self):
        """
        Prints Introduction and game play
        """
        print("Welcome to Dungeon Adventure where you may traverse the dangerous dungeons to find the 4 pillars of OO -"
              " Abstraction, Encapsulation, Inheritance, and Polymorphism. \n"
              "To travel, use keys Up (w), down (s), left (a), right (d). "
              "Within the dungeons you will find a multiple of surprises in each room such as a healing potion, "
              "vision potion, or fall into a pit. "
              "\nThe healing potion can be stored and used to heal your HP. The Vision potion and be stored"
              "and allows you to look at surrounding rooms. \n The pit will take away HP. Be careful not to lose all"
              "health and die. The goal of this game is to "
              "survive and find all 4 pillars of OO. Use \"m\" to look at menu options for information.\n")

    def set_play_mode(self):
        """
        Setting up play mode level based on user input. Adventure attributes health, health potion count,
        vision potion count, dungeon dimension are set up in this module
        :return: None
        """
        input_play_mode = input(f"Choose: Easy, Medium, or Hard? Default will be Easy. ")
        # print("Choose: Easy, Medium, or Hard? Default will be Easy. ") #for debugging purposes
        # input_play_mode = "hard" #for debugging purposes
        if input_play_mode.lower() == "medium":
            HP = random.randint(75, 100)
            healing_potion_count = random.randint(0, 2)
            vision_potion_count = random.randint(0, 1)
            self.dungeon = Dungeon(15, 15) #static number
            print(f"Play mode is Medium")
        elif input_play_mode.lower() == "hard":
            HP = random.randint(75, 90)
            healing_potion_count = 0
            vision_potion_count = 0
            self.dungeon = Dungeon(10, 10) #static number
            print(f"Play mode is Hard")
        else:
            HP = 100
            healing_potion_count = 3
            vision_potion_count = random.randint(100, 200)
            self.dungeon = Dungeon(5, 5) #static number
            print(f"Play mode is Easy")

        # name = input("What is your name? ")

        # ----------------debug--------------------------------------------------
        name = "Minna"#for debugging purposes
        # ----------------debug--------------------------------------------------

        self.adventurer.__init__(name, HP, healing_potion_count, vision_potion_count)


    def menu_str(self):
        """Hidden menu option "map" prints dugeon -- specify what the menu option is in your documentation
        for the DungeonAdventure class
        Creates the menu string to be printed
        :return: menu str
        """
        formatted_list = [item + " : " + values for item, values in self.menu.items()]
        return "\n" + "\n".join(formatted_list) + "\n"


    def set_up_player(self):
        """
        Sets up the game by creating the dungeon maze and locating the starting coordinates
        """
        # self.dungeon.build_dungeon()
        self.player_str = self.dungeon.get_entrance()

        #better to use code to find the entrance coordinates _______________------------------
        self.player_loc_col = 0
        self.player_loc_row = 0

    def player_command(self):
        """
        Execute player's menu inputs
        :return: None - maybe return menu_command?
        """
        menu_command = ""
        item = ""
        while item != "O" or menu_command.lower() != "q":
            menu_command = input("What is your next move? Enter \"m\" for menu: ")
            # while still in maze and not quit
            if menu_command.lower() == "q":
                return "q"
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
                #use vision potion
                if self.adventurer.__get_vision_potion_count__() > 0:
                    self.adventurer.dec_vision_potion()
                    self.use_vision()
                else:
                    print("You don't have any vision potions left")

            elif str(menu_command).lower() == "stats":
                print(self.adventurer)
            elif menu_command.lower() == "w" or menu_command.lower() == "a" or menu_command.lower() == "s" or menu_command.lower() == "d":
                #moving character
                item = self.move_adventurer(menu_command)

                #if the player reaches an exit or dies, break out of the game
                if item == "O" or self.adventurer.get_HP() <= 0: #or self.adventurer.get_pillar() == 4:
                    break
            elif str(menu_command).lower() == "map":
                self.dungeon.print_dungeon()
                # self.dungeon.print_dictionary()

            else:
                print("Not a valid command")


        # ask if player wants to use potion or vision
    def move_adventurer(self, menu_command):
        """
        Player's input is a direction, check to see if that direction is possible and move that direction.
        If moving to next room is possible, collect items and make traveled rooms empty unless pit
        :return: any collected items
        """

        #change input to be direction
        if menu_command == "w":
            direction = "W" #go up
            real_direction = "N"
        elif menu_command == "s":
            direction = "E" #go down
            real_direction = "S"
        elif menu_command == "d":
            direction = "S" #go right
            real_direction = "E"
        elif menu_command == "a":
            direction = "N" #go left
            real_direction = "W"
        else:

            # ---------- testing, delete later-------------------
            print(f"How did I get in move? {menu_command}")
            # ---------- testing, delete later-------------------

            return menu_command

        #get coordinates for next move
        new_row, new_col = self.dungeon._get_neighbor_coords(self.player_loc_row, self.player_loc_col,
                                                             direction)
        # ---------- testing, delete later-------------------
        # print(f"this is real_direction: {real_direction}")
        # ---------- testing, delete later-------------------

        #check if door is available to go into coordinates
        if self.dungeon.is_valid_room(new_row, new_col):
            new_key = self.dungeon._get_neighbor_coords(self.player_loc_row, self.player_loc_col,
                                                             direction)
            current_key = self.player_loc_row, self.player_loc_col
            # ---------- testing, delete later-------------------
            # print(f"this is new coors row: {new_row} col: {new_col}")
            # print(self.dungeon.get_room_str((new_row, new_col)))
            # print(f"this is door boolean: {self.dungeon.get_doors(current_key, new_key, real_direction)}")
            # ---------- testing, delete later-------------------
            #check if door is available to go into coordinates


            # if self.dungeon.get_doors(current_key, new_key, real_direction): #able to move into the room
            # ---------- testing, delete later-------------------
            if True:
                # ---------- testing, delete later-------------------

                self.player_loc_row, self.player_loc_col = new_row, new_col

                # ---------- testing, delete later-------------------
                print(f"this is new coors row: {self.player_loc_row} col: {self.player_loc_col}")
                print(self.dungeon.get_room_str((new_row, new_col)))
                print(f"{self.dungeon.get_room_contents((self.player_loc_row, self.player_loc_col))}")
                # ---------- testing, delete later-------------------

                item = self.dungeon.get_room_contents((self.player_loc_row, self.player_loc_col))
                item = self.collect_item(item)
                if item == "O":
                    print("You found the exit to the dungeon")
                    return item
                if self.adventurer.get_HP() <= 0:
                    print("You have died and lost the game!")
                    return item

                # Collecting Item code

            else:
                print("Cannot move that direction because there is no door")

        else:
            print("Not valid direction")
            print(f"Current location: row: {self.player_loc_row} col: {self.player_loc_col}")
            return

    def collect_item(self, item):
        """
        Items in room affects the player
        :return: any collected
        """
        if item == "H":
            self.adventurer.inc_healing_potion_count()
            print(f"Increased healing: {self.adventurer.__get_health_potion_count__()}")
            self.dungeon.set_room_empty((self.player_loc_row, self.player_loc_col), False)

        elif item == "V":  # vision
            self.adventurer.inc_vision_potion_count()
            print(f"Increased vision: {self.adventurer.__get_vision_potion_count__()}")
            self.dungeon.set_room_empty((self.player_loc_row,self.player_loc_col),False)
        elif item == "X":  # pit- come back to it ----------------------------------------------
            self.adventurer.dec_HP()
            print(f"Pit! Decreased HP: {self.adventurer.get_HP()}")
        elif item == "O":  # exit
            return item
        elif item == "M":  # get multiple items- come back to it----------------------------
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
        # print(f"this is self.adventurer after update{self.adventurer}")

    def multi_items(self):
        items = ["V", "H", "P", ""]
        results = random.sample(items, 3)
        pit = False
        for value in results:
            if value == "V":
                self.adventurer.inc_vision_potion_count()
                print(f"Increased vision: {self.adventurer.__get_vision_potion_count__()}")
            if value == "H":
                self.adventurer.inc_healing_potion_count()
                print(f"Increased healing: {self.adventurer.__get_health_potion_count__()}")
            if value == "P":
                self.adventurer.dec_HP()
                print(f"Pit! Decreased HP: {self.adventurer.get_HP()}")
                pit = True
        self.dungeon.set_room_empty((self.player_loc_row, self.player_loc_col), pit)




    def get_vision_rm_corner(self, row, col):
        """
        Retrieves and returns column and row for corner rooms
        :return: New column and row
        """
        #Grab new column
        temp, north_col = self.dungeon._get_neighbor_coords(self.player_loc_row, self.player_loc_col,
                                                            col)
        # Grab new row
        west_row, temp = self.dungeon._get_neighbor_coords(self.player_loc_row, self.player_loc_col,
                                                           row)
        #If it is a true room, return the
        if self.dungeon.is_valid_room(west_row, north_col):
            return self.dungeon.get_room_str((west_row, north_col))
        return ""

    def get_vision_rm_one(self, direction):
        """
        Retrieves and returns column and row for directly touching rooms
        :return: New column and row
        """
        # row, col = self.dungeon._get_neighbor_coords(self.player_loc_row, self.player_loc_col,
        #                                                     direction)
        row, col = self.dungeon._get_neighbor_coords(self.player_loc_row, self.player_loc_col,
                                                            direction)

        # print(f"valid? {self.dungeon.is_valid_room(row, col)}")
        if self.dungeon.is_valid_room(row, col):
            # print("I am printing?")
            return self.dungeon.get_room_str((row, col))
        return ""

    def use_vision(self):
        """
        Prints a 3x3 view of the surrounding rooms at current location. Used for Vision Potion
        :return: None
        """
        vision_rooms = []
        #
        # if menu_command == "w":
        #     direction = "W" #go up
        #     real_direction = "N"
        # elif menu_command == "s":
        #     direction = "E" #go down
        #     real_direction = "S"
        # elif menu_command == "d":
        #     direction = "S" #go right
        #     real_direction = "E"
        # elif menu_command == "a":
        #     direction = "N" #go left
        #     real_direction = "W"

        #NW - W/N
        vision_rooms.append(self.get_vision_rm_corner("W", "N"))
        #N - W
        vision_rooms.append(self.get_vision_rm_one("W"))
        #NE - WS
        vision_rooms.append(self.get_vision_rm_corner("W", "S"))
        #new line
        #W = N
        vision_rooms.append(self.get_vision_rm_one("N"))
        #self
        vision_rooms.append(self.dungeon.get_room_str((self.player_loc_row, self.player_loc_col)))
        #E - S
        vision_rooms.append(self.get_vision_rm_one("S"))
        #/n
        #SW - E/N
        vision_rooms.append(self.get_vision_rm_corner("E", "N"))
        #S - E
        vision_rooms.append(self.get_vision_rm_one("E"))
        #SE - ES
        vision_rooms.append(self.get_vision_rm_corner("E", "S"))

        # Splitting room view by top, middle, bottom
        # top string
        top = []
        for rooms in vision_rooms:
            top.append(str(rooms)[0:3] + "  ")

        # mid
        mid = []
        for rooms in vision_rooms:
            if len(str(rooms)) == 10:
                mid.append(str(rooms)[4:6] + "   ")
            else:
                mid.append(str(rooms)[4:7] + "  ")
        print(end="\n")

        # bottom
        bottom = []
        for rooms in vision_rooms:
            if len(str(rooms)) == 10:
                bottom.append(str(rooms)[7:10] + "  ")
            else:
                bottom.append(str(rooms)[8:11] + "  ")

        #Printing View
        for i in range(3):
            print(top[i], end="")
        print(end="\n")
        for i in range(3):
            print(mid[i], end="")
        print(end="\n")
        for i in range(3):
            print(bottom[i], end="")
        print(end="\n")
        for i in range(3, 6):
            print(top[i], end="")
        print(end="\n")
        for i in range(3, 6):
            print(mid[i], end="")
        print(end="\n")
        for i in range(3, 6):
            print(bottom[i], end="")
        print(end="\n")
        for i in range(6,9):
            print(top[i], end="")
        print(end="\n")
        for i in range(6, 9):
            print(mid[i], end="")
        print(end="\n")
        for i in range(6, 9):
            print(bottom[i], end="")
        print("\n")

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
        # see_stats = input("\nDo you want to see your stats? y/n ")
        # if see_stats.lower() == "y" or see_stats.lower() == "yes":
        print(self.adventurer)
        # else:
        #     print("I guess you'll never know")

    def print_end(self):
        """
        Prints closing title slides
        """
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
game_play.play_whole_game()
# game_play.use_vision()

# game_play.player_command()