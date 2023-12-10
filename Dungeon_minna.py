from room import Room
import random


class Dungeon:
    """
    Creates a Dungeon for the DungeonAdventure Game.
    """
    def __init__(self, rows, cols):
        self.__rows = rows
        self.__cols = cols
        self.__items = {}
        self.__maze = [[Room() for _ in range(rows)] for _ in range(cols)]
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
        start_room = self.__maze[start_col][start_row]

        # Generate the maze
        self._create_maze(start_room, start_row, start_col)

        # Set entrance and exit
        self._set_entrance_exit()

        # Make some Rooms impassable
        self._make_impassable()

        # Verify that the maze is still traversable from entrance to exit
        if self._is_traversable(0, 0):  # If it's traversable
            self.__items = {(row, col): self.__maze[col][row] for col in range(self.__cols) for row
                            in range(self.__rows)}
            self._place_items()  # Randomly add pillars, potions, and other objects to it
        else:
            self._create_maze(start_room, start_row, start_col)  # Otherwise generate a new maze if not passable

    def get_entrance(self):
        """
        Gets the entrance Room coordinates of the Dungeon's maze.
        :return: Room
        """
        return self.__maze[0][0]

    def get_room_str(self, key):
        """
        Gets the entrance Room coordinates of the Dungeon's maze.
        :return: Room
        """
        return self.__items.get(key)

    def get_room_contents(self, key):
        """
       Gets the contents of a Room in the dungeon.
       :param key: a tuple representation of the row, column Room coordinates (0, 0)
       :return: the contents of the specified Room, in the format specified in the __str__() method in Room class.
       """
        # symbols_dict = self._get_object_symbols()
        # return symbols_dict.items(key)
        item = self.__items.get(key)
        # print(f"self.__items.get(key): \n {self.__items.get(key)}")
        # print(f"this is item \n {item}")
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

        # symbols_dict[(row, col)] = symbols
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
        for col in range(self.__cols):
            for row in range(self.__rows):
                room = self.__maze[col][row]
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
                dungeon_info += f"\n  - Abstraction Pillar: {room.set_abstraction_pillar()}"
                dungeon_info += f"\n  - Encapsulation Pillar: {room.set_encapsulation_pillar()}"
                dungeon_info += f"\n  - Inheritance Pillar: {room.set_inheritance_pillar()}"
                dungeon_info += f"\n  - Polymorphism Pillar: {room.set_polymorphism_pillar()}"
                dungeon_info += f"\n  - Healing Potion: {room.set_healing_potion(True)}"
                dungeon_info += f"\n  - Vision Potion: {room.set_vision_potion(True)}"
                dungeon_info += f"\n  - Pit: {room.set_pit(True)}"
                dungeon_info += "\n\n"

        return dungeon_info

    def print_dungeon(self):
        """
        Prints a simple visual representation of the Dungeon's maze.
        :return: None.
        """
        # Saves top strings of all rooms in dungeon
        top = []
        for row in range(self.__rows):
            for col in range(self.__cols):
                top.append(str(self.__maze[col][row])[0:3] + "  ")

        # saves mid string of all rooms in dungeon
        mid = []
        for row in range(self.__rows):
            for col in range(self.__cols):
                if len(str(self.__maze[col][row])) == 10:
                    mid.append(str(self.__maze[col][row])[4:6]+ "   ")
                else:
                    mid.append(str(self.__maze[col][row])[4:7] + "  ")

        # Saves bottom strings of all rooms in dungeon
        bottom = []
        for row in range(self.__rows):
            for col in range(self.__cols):
                if len(str(self.__maze[col][row])) == 10:
                    bottom.append(str(self.__maze[col][row])[7:10] + "  ")
                else:
                    bottom.append(str(self.__maze[col][row])[8:11] + "  ")

        #prints dungeon according to the dimensons
        for i in range(0, self.__rows):
            print(end="\n")
            for room in range(i*self.__cols, (i+1)*self.__cols):
                print(top[room], end="")
            print(end="\n")
            for room in range(i*self.__cols, (i+1)*self.__cols):
                print(mid[room], end="")
            print(end="\n")
            for room in range(i * self.__cols, (i+1) * self.__cols):
                print(bottom[room], end="")
        print("\n")


        """------------------------------------------------------------------"""

        # print("+", end="")
        # for _ in range(self.__rows * 2):
        #     print("-", end="")
        # print("+")
        #
        # # Print each row of Rooms
        # for col in range(self.__cols):
        #     # Print left wall
        #     print("|", end="")
        #
        #     # Print each Room's doors
        #     for row in range(self.__rows):
        #         room = self.__maze[col][row]
        #         if room.get_entrance():
        #             print(" E", end="")
        #         elif room.get_exit():
        #             print(" X", end="")
        #         elif room.get_impasse():
        #             print(" #", end="")
        #         else:
        #             print(" " if room.get_west_door() else " |", end="")
        #             print(" " if room.get_south_door() else "-", end="")
        #     print("|")
        #
        # # Print bottom border
        # print("+", end="")
        # for _ in range(self.__rows * 2):
        #     print("-", end="")
        # print("+")

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
                neighbor_room = self.__maze[neighbor_col][neighbor_row]
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
        d_row = {"N": 0, "S": 0, "E": 1, "W": -1}
        d_col = {"N": -1, "S": 1, "E": 0, "W": 0}

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
        self.__maze[0][0].set_entrance()
        # print(f"This is row {len(self.__maze[self.__rows])}")
        # print(f"This is col {len(self.__maze)}")
        self.__maze[self.__rows - 1][self.__cols - 1].set_exit()

        # Set them as passable
        self.__maze[0][0].set_impasse(False)
        self.__maze[self.__rows - 1][self.__cols - 1].set_impasse(False)

        # Set them as empty
        self.__maze[0][0].set_empty_room()
        self.__maze[self.__rows - 1][self.__cols - 1].set_empty_room()

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
        Internal method that traverses the Dungeon from entrance to exit to verify that it is passable.
        :param row: starting row, usually 0.
        :param col: starting column, usually 0.
        :return: boolean.
        """
        # Check that the starting room is valid

        found_exit = False
        if self.is_valid_room(row, col):
            self.__maze[row][col].set_visited(True)
            # Check if the Room is the exit
            if self.__maze[row][col].get_exit():
                return True
            # If it isn't the exit, try another Room to the South, East, North, and West
            found_exit = self._traverse_the_maze(row + 1, col)  # South
            if not found_exit:
                found_exit = self._traverse_the_maze(row, col + 1)  # East
            if not found_exit:
                found_exit = self._traverse_the_maze(row - 1, col)  # North
            if not found_exit:
                found_exit = self._traverse_the_maze(row, col - 1)  # West

            # If the exit was not found in this Room, mark it as visited
            if not found_exit:
                self.__maze[row][col].set_visited(True)

        else:  # If the Room is not valid
            return False
        return found_exit

    def _place_items(self):
        """
        Internal method that randomly places items in the Dungeon.
        :return: None
        """

        pillars = {
            "abstraction": 0,
            "encapsulation": 0,
            "polymorphism": 0,
            "inheritance": 0
        }

        for (row, col), room in self.__items.items():
            if room.get_impasse() or room.get_entrance() or room.get_exit():
                continue

            else:

                if random.random() <= 0.04 and pillars["abstraction"] < 1:
                    room.set_abstraction_pillar()
                    pillars["abstraction"] += 1
                elif random.random() <= 0.04 and pillars["encapsulation"] < 1:
                    room.set_encapsulation_pillar()
                    pillars["encapsulation"] += 1
                elif random.random() <= 0.04 and pillars["polymorphism"] < 1:
                    room.set_polymorphism_pillar()
                    pillars["polymorphism"] += 1
                elif random.random() <= 0.04 and pillars["inheritance"] < 1:
                    room.set_inheritance_pillar()
                    pillars["inheritance"] += 1

            possibility = random.randint(0, 100)
            if possibility <= 10:
                room.set_healing_potion(True)
            if possibility <= 12:
                room.set_pit(True)
            if possibility <= 20:
                room.set_vision_potion(True)

    def _get_maze_dictionary(self):
        """
        Internal getter method that returns the dictionary.
        :return: the dictionary instantiated in the class constructor.
        """
        return self.__items

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






# Example usage
dungeon = Dungeon(10, 10)
dungeon.print_dungeon()
# dungeon.print_dictionary()
# print(dungeon.get_room_contents((0, 1)))
