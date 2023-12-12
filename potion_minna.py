import random
from abc import ABC, abstractmethod
from Dungeon_minna import Dungeon
import copy


class Potion(ABC):
    """ Potion class implemented with abstractmethod"""
    def __init__(self, name):
        """ Initializing name
        param: name"""
        self.name = name

    def get_name(self):
        """ getter function for name"""
        return self.name

    @abstractmethod
    def use_potion(self):
        """ abstract method of use_potion"""
        pass


class HealingPotion(Potion):
    def __init__(self, minimum, maximum):
        """ Inheriting Potion class initializing name as "H" and passing a minimum amd maximum parameters
        param: minimum, maximum"""
        super().__init__("H")
        self.health_points = random.randint(minimum, maximum)

    def use_potion(self):
        """ Implementing use_potion method for HealingPotion class"""
        return self.health_points


class VisionPotion(Potion):
    def __init__(self):
        """ Inheriting Potion class initializing name as "H" """
        super().__init__("V")
        self.vision_count = 1

    def use_potion(self):
        return self.vision_count

    def use_vision(self, current_row, current_col, dungeon_max_row, dungeon_max_col, dungeon):
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
        current_room = copy.deepcopy(dungeon.get_room_str((current_row, current_col)))
        dungeon.set_current_room(current_room)
        row = 3
        col = 3
        if current_row == 0 or current_row == dungeon_max_col-1:
            if 0 < current_col < dungeon_max_row-1:
                row = 2
                col = 3
            elif current_col == 0 or current_col == dungeon_max_row-1:
                row = 2
                col = 2

        elif current_col == 0 or current_col == dungeon_max_row-1:
            if 0 < current_row < dungeon_max_col-1:
                row = 3
                col = 2
        #NW - W/N
        vision_rooms.append(self.get_vision_rm_corner(current_row, current_col, "W", "N", dungeon))
        #N - W
        vision_rooms.append(self.get_vision_rm_one(current_row, current_col,"W", dungeon))
        #NE - WS
        vision_rooms.append(self.get_vision_rm_corner(current_row, current_col,"W", "S", dungeon))
        #new line
        #W = N
        vision_rooms.append(self.get_vision_rm_one(current_row, current_col,"N", dungeon))
        #self
        vision_rooms.append(current_room)
        #E - S
        vision_rooms.append(self.get_vision_rm_one(current_row, current_col,"S", dungeon))
        #/n
        #SW - E/N
        vision_rooms.append(self.get_vision_rm_corner(current_row, current_col,"E", "N", dungeon))
        vision_rooms.append(self.get_vision_rm_one(current_row, current_col,"E", dungeon))
        #SE - ES
        vision_rooms.append(self.get_vision_rm_corner(current_row, current_col,"E", "S", dungeon))

        # Splitting room view by top, middle, bottom
        # top string
        top = []
        for rooms in vision_rooms:
            if str(rooms) != "":
                top.append(str(rooms)[0:3] + "    ")
        # mid
        mid = []
        for rooms in vision_rooms:
            if str(rooms) != "":
                if len(str(rooms)) == 10:
                    mid.append(str(rooms)[4:6] + "     ")
                else:
                    mid.append(str(rooms)[4:7] + "    ")

        # bottom
        bottom = []
        for rooms in vision_rooms:
            if str(rooms) != "":
                if len(str(rooms)) == 10:
                    bottom.append(str(rooms)[7:10] + "    ")
                else:
                    bottom.append(str(rooms)[8:11] + "    ")

        #Printing View
        print("\n")
        for i in range(0, row):
            for room in range(i * col, (i + 1) * col):
                print(top[room], end="")
            print(end="\n")
            for room in range(i * col, (i + 1) * col):
                print(mid[room], end="")
            print(end="\n")
            for room in range(i * col, (i + 1) * col):
                print(bottom[room], end="")
            print("\n")

    def get_vision_rm_corner(self, current_row, current_col, row_direction, col_direction, dungeon):
        """
        Retrieves and returns column and row for corner rooms
        :return: New column and row
        """

        #Grab new column
        temp, north_col = dungeon._get_neighbor_coords(current_row, current_col,
                                                            col_direction)
        # Grab new row
        west_row, temp = dungeon._get_neighbor_coords(current_row, current_col,
                                                           row_direction)
        #If it is a true room, return the
        if dungeon.is_valid_room(west_row, north_col):
            return dungeon.get_room_str((west_row, north_col))
        return ""

    def get_vision_rm_one(self, current_row, current_col, direction, dungeon):
        """
        Retrieves and returns column and row for directly touching rooms
        :return: New column and row
        """

        row, col = dungeon._get_neighbor_coords(current_row, current_col, direction)

        # print(f"valid? {self.dungeon.is_valid_room(row, col)}")
        if dungeon.is_valid_room(row, col):
            # print("I am printing?")
            return dungeon.get_room_str((row, col))
        return ""

