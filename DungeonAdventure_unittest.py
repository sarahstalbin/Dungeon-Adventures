"""
Name: Aqueno Nirasmi, Minna Chae, Sarah St. Albin
TCSS 501 and 502
Dungeon Adventure
"""

from room import Room
from DungeonItemsFactory import DungeonItemsFactory
import random


class Dungeon:
    """
    Creates a Dungeon for the DungeonAdventure Game.
    """

    def __init__(self, rows, cols):
        self.__rows = rows
        self.__cols = cols
        self.__items = {}
        self.__maze = []

        for r in range(0, self.__rows):
            self.__maze.append([Room() for c in range(0, self.__cols)])

        self.build_dungeon()

    # External methods

    def build_dungeon(self):
        """
        Generates a maze for the Dungeon.
        :return: None
        """
        # Randomly select a starting Room
        start_row = random.randint(0, self.__rows - 1)
        start_col = random.randint(0, self.__cols - 1)
        start_room = self.__maze[start_row][start_col]

        # Generate the maze
        self._create_maze(start_room, start_row, start_col)

        # Set entrance and exit
        self._set_entrance_exit()

        # Make some Rooms impassable
        self._make_impassable()

        # Verify that the maze is still traversable from entrance to exit
        if self._is_traversable(0, 0):  # If it's traversable
            self.__items = {(row, col): self.__maze[row][col] for row in range(self.__rows) for col
                            in range(self.__cols)}
            self._place_pillars()  # Randomly add pillars
            self._place_items()  # Randomly add pillars, potions, and other objects to it
        else:
            self._create_maze(start_room, start_row, start_col)  # Otherwise generate a new maze if not passable

    def get_entrance(self):
        """
        Gets the entrance Room coordinates of the Dungeon's maze.
        :return: Room
        """
        return self.__maze[0][0]

    def get_maze_array(self):
        return self.__maze

    def _get_maze_dictionary(self):
        """
        Internal getter method that returns the dictionary.
        :return: the dictionary instantiated in the class constructor.
        """
        return self.__items

    def get_room_str(self, key):
        """
        Gets the entrance Room coordinates of the Dungeon's maze.
        :return: Room
        """
        return self.__items.get(key)

    def get_col_length(self):
        return self.__cols

    def get_row_length(self):
        return self.__rows

    def get_doors(self, current_key, new_key, direction="N"):
        """
        Get attributes of room
        :return: attributes
        """
        attributes_current = self.__items.get(current_key)  # grabbing room attributes
        attributes_new = self.__items.get(new_key)  # grabbing room attributes

        if direction == "N":
            boo_results = attributes_current.get_north_door() and attributes_new.get_south_door()
            return boo_results

        if direction == "S":
            boo_results = attributes_current.get_south_door() and attributes_new.get_north_door()
            return boo_results

        if direction == "E":
            boo_results = attributes_current.get_east_door() and attributes_new.get_west_door()
            return boo_results

        if direction == "W":
            boo_results = attributes_current.get_west_door() and attributes_new.get_east_door()
            return boo_results

    def set_current_room(self, room):
        """
        Sets player's current coordinates as current room. Used in vision potion
        """
        room.set_healing_potion(False)
        room.set_vision_potion(False)
        room.set_pit(False)
        room.set_multiple_items(False)
        room.set_entrance(False)
        room.set_empty_room(False)
        room.set_abstraction_pillar(False)
        room.set_polymorphism_pillar(False)
        room.set_inheritance_pillar(False)
        room.set_encapsulation_pillar(False)
        room.set_current_room(True)

    def set_room_empty(self, key=(0, 0), pit=False):
        """
        If room traveled, removes items but leaves pit
        """
        item = self.__items.get(key)
        if item.get_healing_potion():
            item.set_healing_potion(False)
            item.set_empty_room(True)
        elif item.get_vision_potion():
            item.set_vision_potion(False)
            item.set_empty_room(True)
        elif item.get_multiple_items():
            item.set_multiple_items(False)
            if pit:
                item.set_pit(True)
            else:
                item.set_empty_room(True)
        elif item.get_abstraction_pillar():
            item.set_abstraction_pillar(False)
            item.set_empty_room(True)
        elif item.get_polymorphism_pillar():
            item.set_polymorphism_pillar(False)
            item.set_empty_room(True)
        elif item.get_inheritance_pillar():
            item.set_inheritance_pillar(False)
            item.set_empty_room(True)
        elif item.get_encapsulation_pillar():
            item.set_encapsulation_pillar(False)
            item.set_empty_room(True)

    def get_room_contents(self, key):
        """
       Gets the contents of a Room in the dungeon.
       :param key: a tuple representation of the row, column Room coordinates (0, 0)
       :return: the contents of the specified Room, in the format specified in the __str__() method in Room class.
       """

        item = self.__items.get(key)
        symbols = ""
        if item.get_healing_potion():
            symbols += "H"
        elif item.get_vision_potion():
            symbols += "V"
        elif item.get_pit():
            symbols += "X"
        elif item.get_entrance():
            symbols += "i"
        elif item.get_exit():
            symbols += "O"
        elif item.get_multiple_items():
            symbols += "M"
        elif item.get_empty_room():
            symbols += " "
        elif item.get_abstraction_pillar():
            symbols += "A"
        elif item.get_polymorphism_pillar():
            symbols += "P"
        elif item.get_inheritance_pillar():
            symbols += "I"
        elif item.get_encapsulation_pillar():
            symbols += "E"
        return symbols

    def print_dictionary(self):
        """
        Prints the contents of each Room without the symbols from Room's __str__() method.
        Uses the format (row, col) : contents.
        :return: None
        """
        symbols_dict = self._get_object_symbols()
        for key, value in symbols_dict.items():
            print(f"Room at ({key[0]}, {key[1]}): {value}")

    def is_valid_room(self, row, col):
        """
        Checks whether a Room is valid or not.
        :param row: row coordinate
        :param col: column coordinate
        :return: boolean
        """
        return 0 <= row < self.__rows and 0 <= col < self.__cols

    def __str__(self):
        """
        External method that builds a string containing information about the entire Dungeon.
        :return: String
        """
        dungeon_info = ""
        for row in range(self.__rows):
            for col in range(self.__cols):
                room = self.__maze[row][col]
                dungeon_info += f"Room at ({row}, {col}):"
                dungeon_info += f"\n  - North Door: {room.get_north_door()}"
                dungeon_info += f"\n  - South Door: {room.get_south_door()}"
                dungeon_info += f"\n  - East Door: {room.get_east_door()}"
                dungeon_info += f"\n  - West Door: {room.get_west_door()}"
                dungeon_info += f"\n  - Visited: {room.get_visited()}"
                dungeon_info += f"\n  - Entrance: {room.get_entrance()}"
                dungeon_info += f"\n  - Exit: {room.get_exit()}"
                dungeon_info += f"\n  - Impasse: {room.get_impasse()}"
                dungeon_info += f"\n  - Empty Room: {room.get_empty_room()}"
                dungeon_info += f"\n  - Abstraction Pillar: {room.set_abstraction_pillar(True)}"
                dungeon_info += f"\n  - Encapsulation Pillar: {room.set_encapsulation_pillar(True)}"
                dungeon_info += f"\n  - Inheritance Pillar: {room.set_inheritance_pillar(True)}"
                dungeon_info += f"\n  - Polymorphism Pillar: {room.set_polymorphism_pillar(True)}"
                dungeon_info += f"\n  - Healing Potion: {room.set_healing_potion(True)}"
                dungeon_info += f"\n  - Vision Potion: {room.set_vision_potion(True)}"
                dungeon_info += f"\n  - Pit: {room.set_pit(True)}"
                dungeon_info += "\n\n"

        return dungeon_info

    def print_play_dungeon(self, current_row=-1, current_col=-1):
        """
        Prints a simple visual representation of the Dungeon's maze as player is playing
        :return: None.
        """
        top = []
        for row in range(self.__rows):
            for col in range(self.__cols):
                if row == current_row and col == current_col:
                    top.append(str(self.__maze[row][col])[0:3] + "  ")
                else:
                    if self.__items.get((row, col)).get_player_traveled():
                        top.append("---  ")
                    else:
                        top.append("^^^  ")

        # saves mid string of all rooms in dungeon
        mid = []
        for row in range(self.__rows):
            for col in range(self.__cols):
                if row == current_row and col == current_col:
                    if len(str(self.__maze[row][col])) == 10:
                        mid.append(str(self.__maze[row][col])[4:6] + "   ")
                    else:
                        mid.append(str(self.__maze[row][col])[4:7] + "  ")
                else:
                    if self.__items.get((row, col)).get_player_traveled():
                        mid.append("---  ")
                    else:
                        mid.append("^^^  ")

        # Saves bottom strings of all rooms in dungeon
        bottom = []
        for row in range(self.__rows):
            for col in range(self.__cols):
                if row == current_row and col == current_col:
                    if len(str(self.__maze[row][col])) == 10:
                        bottom.append(str(self.__maze[row][col])[7:10] + "  ")
                    else:
                        bottom.append(str(self.__maze[row][col])[8:11] + "  ")
                else:
                    if self.__items.get((row, col)).get_player_traveled():
                        bottom.append("---  ")
                    else:
                        bottom.append("^^^  ")

        # prints dungeon according to the dimensons
        for i in range(0, self.__rows):
            # print(end="\n")
            for room in range(i * self.__cols, (i + 1) * self.__cols):
                print(top[room], end="")
            print(end="\n")
            for room in range(i * self.__cols, (i + 1) * self.__cols):
                print(mid[room], end="")
            print(end="\n")
            for room in range(i * self.__cols, (i + 1) * self.__cols):
                print(bottom[room], end="")
            print("\n")

    def set_player_traveled(self, key):
        room = self.__items.get(key)
        room.set_player_traveled()


    def print_dungeon(self, current_row=-1, current_col=-1):
        """
        Prints a simple visual representation of the Dungeon's maze.
        :return: None.
        """
        # Saves top strings of all rooms in dungeon
        top = []
        for row in range(self.__rows):
            for col in range(self.__cols):
                top.append(str(self.__maze[row][col])[0:3] + "     ")

        # saves mid string of all rooms in dungeon
        mid = []
        for row in range(self.__rows):
            for col in range(self.__cols):
                if row == current_row and col == current_col:
                    current = str(self.__maze[row][col])[4]
                    current += "@"
                    current += str(self.__maze[row][col])[6]  + "     "
                    mid.append(current)
                else:
                    if len(str(self.__maze[row][col])) == 10:
                        mid.append(str(self.__maze[row][col])[4:6] + "      ")
                    else:
                        mid.append(str(self.__maze[row][col])[4:7] + "     ")

        # Saves bottom strings of all rooms in dungeon
        bottom = []
        for row in range(self.__rows):
            for col in range(self.__cols):
                if len(str(self.__maze[row][col])) == 10:
                    bottom.append(str(self.__maze[row][col])[7:10] + "     ")
                else:
                    bottom.append(str(self.__maze[row][col])[8:11] + "     ")

        # prints dungeon according to the dimensons
        for i in range(0, self.__rows):
            print(end="\n")
            for room in range(i * self.__cols, (i + 1) * self.__cols):
                print(top[room], end="")
            print(end="\n")
            for room in range(i * self.__cols, (i + 1) * self.__cols):
                print(mid[room], end="")
            print(end="\n")
            for room in range(i * self.__cols, (i + 1) * self.__cols):
                print(bottom[room], end="")
            print("\n")

    # Internal methods

    def _create_maze(self, room, current_row, current_col):
        """
        Internal method that randomly generates a maze for the Dungeon.
        :param room: starting room
        :param current_row: current row coordinate
        :param current_col: current column coordinate
        :return: None
        """
        # Set the starting room to "visited"
        room.set_visited(True)

        # Shuffle a list of possible directions
        directions = ["N", "S", "E", "W"]
        random.shuffle(directions)

        # Loop through the shuffled directions
        for direction in directions:
            neighbor_row, neighbor_col = self._get_neighbor_coords(current_row, current_col, direction)
            if self.is_valid_room(neighbor_row, neighbor_col):
                neighbor_room = self.__maze[neighbor_row][neighbor_col]
                if not neighbor_room.get_visited():  # If the neighboring room hasn't been visited...
                    # Knock down the doors between them
                    self._knock_down_door(room, direction)
                    self._knock_down_door(neighbor_room, self._opposite_direction(direction))

                    # Recursively explore the neighbor Room
                    self._create_maze(neighbor_room, neighbor_row, neighbor_col)

    def _get_neighbor_coords(self, row, col, direction):
        """
        Internal method that returns the coordinates of the neighboring room in order to generate the maze.
        :param row: row coordinate, intended to be the current row
        :param col: column coordinate, intended to be the current column
        :param direction: the current direction that the maze is following during generation
        :return: the new row and column coordinates
        """
        d_row = {"N": -1, "S": 1, "E": 0, "W": 0}
        d_col = {"N": 0, "S": 0, "E": 1, "W": -1}

        new_row = row + d_row[direction]
        new_col = col + d_col[direction]
        return new_row, new_col

    def _opposite_direction(self, direction):
        """
        Internal method that returns the opposite direction of the provided direction.
        Raises ValueError if an invalid direction is given.
        :param direction: the given direction ("N," "S," "E," "W")
        :return: (Str) the opposite direction of the provided direction
        """
        if direction not in ("N," "S," "E," "W"):
            raise ValueError("INVALID DIRECTION PROVIDED")
        return {"N": "S", "S": "N", "E": "W", "W": "E"}[direction]

    def _knock_down_door(self, room, direction):
        """
        Internal method that "knocks down" a door in a particular direction ("N," "S," "E," "W") in relation
        to the provided Room.
        :param room: Room object whose doors need to be knocked down in _create_maze()
        :param direction: the direction of the door that will be knocked down ("N," "S," "E," "W")
        :return: None
        """
        if direction not in ("N," "S," "E," "W"):
            raise ValueError("INVALID DIRECTION PROVIDED")

        # Update the relevant door based on given direction
        if direction == "N":
            room.set_north_door()
        elif direction == "S":
            room.set_south_door()
        elif direction == "E":
            room.set_east_door()
        elif direction == "W":
            room.set_west_door()

    def _set_entrance_exit(self):
        """
        Internal method that sets the entrance and exit in the maze, sets them as passable, and sets them as empty.
        :return: None.
        """
        # Set the entrance and exit
        self.__maze[0][0].set_entrance(True)
        self.__maze[self.__rows - 1][self.__cols - 1].set_exit()

        # Set them as passable
        self.__maze[0][0].set_impasse(False)
        self.__maze[self.__rows - 1][self.__cols - 1].set_impasse(False)

        # Set them as empty
        self.__maze[0][0].set_empty_room(True)
        self.__maze[self.__rows - 1][self.__cols - 1].set_empty_room(True)

        # Set exterior doors
        self.__maze[0][0].set_west_door()
        self.__maze[self.__rows - 1][self.__cols - 1].set_east_door()

    def _make_impassable(self):
        """
        Internal method that randomly sets some Rooms as impassable.
        :return: None.
        """
        for row in range(self.__rows):
            for col in range(self.__cols):
                if random.randrange(1, 101) > 80:
                    self.__maze[row][col].set_impasse(True)

    def _is_traversable(self, start_row, start_col):
        """
        Internal method that returns a boolean reflecting whether the maze is passable or not.
        :param start_row: starting row coordinate (usually 0)
        :param start_col: starting column coordinate (usually 0)
        :return: boolean
        """
        return self._traverse_the_maze(start_row, start_col)

    def _traverse_the_maze(self, row, col):
        """
        :param row: starting row coordinate of the Room
        :param col: starting column coordinate of the Room
        :return: True if the maze is traversable, false if not.
        """
        target = self.__maze[self.__rows - 1][self.__cols - 1]  # Identify the coordinates of the exit

        if not self.is_valid_room(row, col):  # Check if the Room is valid
            return False

        if self.__maze[row][col] == target:  # Check if the Room is the exit
            return True

        self.__maze[row][col].set_visited(True)  # Set the starting Room as visited

        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]  # Check Rooms to the South, East, North, and West
        for d_row, d_col in directions:
            if self._traverse_the_maze(row + d_row, col + d_col):
                return True

        self.__maze[row][col].set_visited(True)  # If no exit is found in any direction, mark Room as unvisited
        return False

    def _place_items(self):
        """
        Internal method that randomly places healing potions, vision potions, and pits.
        :return:
        """
        for (row, col), room in self.__items.items():
            if room.get_entrance() or room.get_exit() or room.get_abstraction_pillar() \
                    or room.get_polymorphism_pillar() or room.get_inheritance_pillar() or room.get_encapsulation_pillar():
                continue
            else:
                item_list = ["V", "H", "M", "X"]
                choice = random.choice(item_list)
                possibility = random.randint(0, 100)
                # Place the healing potion
                if possibility <= 30:
                    # Place the vision potion
                    if choice == "V":
                        vision_potion = DungeonItemsFactory.create_item("V")
                        room.set_vision_potion(vision_potion)
                    # Place health potion
                    if choice == "H":
                        healing_potion = DungeonItemsFactory.create_item("H", 1, 10)
                        room.set_healing_potion(healing_potion)
                    # Place multi item
                    if choice == "M":
                        multiple_items = DungeonItemsFactory.create_multiple_items(1, 10)
                        for item in multiple_items:
                            room.set_multiple_items(item)
                    # Place the pit
                    if choice == "X":
                        pit = DungeonItemsFactory.create_item("X", 1, 10)
                        room.set_pit(pit)
                else:
                    room.set_empty_room(True)

    def _place_pillars(self):
        """
        Internal method that randomly places Pillars in eligible Rooms throughout the maze.
        :return: None
        """
        abstraction = False
        encapsulation = False
        inheritance = False
        polymorphism = False

        qualified_rooms = [room for (row, col), room in self.__items.items()
                           if not room.get_entrance() and not room.get_exit() and not room.get_impasse()
                           and not room.get_vision_potion() and not room.get_pit() and not room.get_healing_potion()]

        selected_rooms = random.sample(qualified_rooms, 4)

        for room in selected_rooms:
            if not abstraction:
                room.set_abstraction_pillar(True)
                abstraction = True
            elif not encapsulation:
                room.set_encapsulation_pillar(True)
                encapsulation = True
            elif not inheritance:
                room.set_inheritance_pillar(True)
                inheritance = True
            elif not polymorphism:
                room.set_polymorphism_pillar(True)
                polymorphism = True
            else:
                break

    def _get_object_symbols(self):
        """
        Internal method that overrides the Room class __str__() method by converting its symbols to shorter, more
        readable symbols in the Dungeon class dictionary.
        :return: the dictionary of symbols
        """
        symbols_dict = {}
        for (row, col), room in self.__items.items():
            symbols = ""
            if room.get_healing_potion():
                symbols += "H"
            elif room.get_vision_potion():
                symbols += "V"
            elif room.get_pit():
                symbols += "X"
            elif room.get_entrance():
                symbols += "i"
            elif room.get_exit():
                symbols += "O"
            elif room.get_multiple_items():
                symbols += "M"
            elif room.get_empty_room():
                symbols += " "
            elif room.get_abstraction_pillar():
                symbols += "A"
            elif room.get_polymorphism_pillar():
                symbols += "P"
            elif room.get_inheritance_pillar():
                symbols += "I"
            elif room.get_encapsulation_pillar():
                symbols += "E"
            symbols_dict[(row, col)] = symbols
        return symbols_dict
