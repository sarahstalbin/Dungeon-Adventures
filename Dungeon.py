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

    def build_dungeon(self):
        """
        Generates a maze for the Dungeon.
        :return: none
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


    def _create_maze(self, room, current_row, current_col):
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

                    # Recursively explore the neighbor cell
                    self._create_maze(neighbor_room, neighbor_row, neighbor_col)

    def _get_neighbor_coords(self, row, col, direction):
        dx = {"N": 0, "S": 0, "E": 1, "W": -1}
        dy = {"N": -1, "S": 1, "E": 0, "W": 0}

        new_row = row + dx[direction]
        new_col = col + dy[direction]
        return new_row, new_col

    def is_valid_room(self, row, col):
        return 0 <= row < self.__rows and 0 <= col < self.__cols

    def _opposite_direction(self, direction):
        return {"N": "S", "S": "N", "E": "W", "W": "E"}[direction]

    def _knock_down_door(self, room, direction):
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
        Sets the entrance and exit in the maze, sets them as passable, and sets them as empty.
        :return: None.
        """
        # Set the entrance and exit
        self.__maze[0][0].set_entrance()
        self.__maze[self.__rows - 1][self.__cols - 1].set_exit()

        # Set them as passable
        self.__maze[0][0].set_impasse(False)
        self.__maze[self.__rows - 1][self.__cols - 1].set_impasse(False)

        # Set them as empty
        self.__maze[0][0].set_empty_room()
        self.__maze[self.__rows - 1][self.__cols - 1].set_empty_room()

    def _make_impassable(self):
        """
        Randomly sets some Rooms as impassable.
        :return: None.
        """
        for row in range(self.__rows):
            for col in range(self.__cols):
                if random.randrange(1, 101) > 80:
                    self.__maze[row][col].set_impasse(True)

    def _is_traversable(self, start_row, start_col):
        return self._traverse_the_maze(start_row, start_col)

    def _traverse_the_maze(self, row, col):
        """
        Traverses the dungeon from entrance to exit to verify that it is passable.
        :param row: starting row, usually 0.
        :param col: starting column, usually 0.
        :return: boolean.
        """
        # Check that the starting room is valid

        found_exit = False
        if self.is_valid_room(row, col):
            self.__maze[row][col].set_visited(True)
            # check for exit
            if self.__maze[row][col].get_exit():
                return True
            # not at exit so try another room: south, east, north, west
            found_exit = self._traverse_the_maze(row + 1, col)  # south
            if not found_exit:
                found_exit = self._traverse_the_maze(row, col + 1)  # east
            if not found_exit:
                found_exit = self._traverse_the_maze(row - 1, col)  # north
            if not found_exit:
                found_exit = self._traverse_the_maze(row, col - 1)  # west

            # if we did not reach the exit from this room we need mark it as visited to
            # avoid going into the room again
            if not found_exit:
                self.__maze[row][col].set_visited(True)

        else:  # tried to move into a room that is not valid
            return False
        return found_exit

    def _place_items(self):
        for (row, col), room in self.__items.items():
            if room.get_impasse() or room.get_entrance() or room.get_exit():
                continue

            else:

                pillars = {
                    "abstraction": 0,
                    "encapsulation": 0,
                    "polymorphism": 0,
                    "inheritance": 0
                }

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
                room.set_pit(True)

    def _get_maze_dictionary(self):
        return self.__items

    def _get_object_symbols(self):
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

    def print_dictionary(self):
        symbols_dict = dungeon._get_object_symbols()
        for key, value in symbols_dict.items():
            print(f"Room at ({key[0]}, {key[1]}): {value}")

    def print_details(self):
        """
        Prints the details of the maze by accessing the __str__() method in Room
        :return: None.
        """
        for row in range(0, self.__rows):
            print("row ", row)
            for col in range(0, self.__cols):
                print("col", col)
                print(self.__maze[row][col].__str__())
            print()

    def print_dungeon(self):
        """
        Prints a simple visual representation of the Dungeon's maze.
        :return: None.
        """
        print("+", end="")
        for _ in range(self.__rows * 2):
            print("-", end="")
        print("+")

        # Print each row of cells
        for col in range(self.__cols):
            # Print left wall
            print("|", end="")

            # Print each cell's doors
            for row in range(self.__rows):
                room = self.__maze[col][row]
                if room.get_entrance():
                    print(" E", end="")
                elif room.get_exit():
                    print(" X", end="")
                elif room.get_impasse():
                    print(" #", end="")
                else:
                    print(" " if room.get_west_door() else " |", end="")
                    print(" " if room.get_south_door() else "-", end="")
            print("|")

        # Print bottom border
        print("+", end="")
        for _ in range(self.__rows * 2):
            print("-", end="")
        print("+")

# Example usage
dungeon = Dungeon(20, 20)
dungeon.print_dungeon()

dungeon.print_dictionary()