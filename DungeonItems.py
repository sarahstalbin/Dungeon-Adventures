"""
Name: Aqueno Nirasmi, Minna Chae, Sarah St. Albin
TCSS 501 and 502
Dungeon Adventure
"""

import random, copy
from abc import ABC, abstractmethod


class DungeonItems(ABC):
    """ DungeonItems class implemented with abstractmethod"""

    def __init__(self, name):
        """ Initializing name
        param: name"""
        self.name = name

    def get_name(self):
        """ getter function for name"""
        return self.name

    @abstractmethod
    def use_item(self):
        """ abstract method of use_item"""
        pass


class HealingPotion(DungeonItems):
    def __init__(self, minimum, maximum):
        """ Inheriting DungeonItems class initializing name as "H" and passing a minimum amd maximum parameters
        param: minimum, maximum"""
        super().__init__("H")
        self.health_points = random.randint(minimum, maximum)

    def use_item(self):
        """ Implementing use_item method for HealingPotion class"""
        return self.health_points


class VisionPotion(DungeonItems):
    def __init__(self):
        """ Inheriting DungeonItems class initializing name as "H" """
        super().__init__("V")

    def use_item(self):
        pass

    def use_vision(self, current_row, current_col, dungeon_max_row, dungeon_max_col, dungeon):
        """
        Prints a view of the surrounding rooms at current location. Used for Vision Potion
        :return: None
        """
        vision_rooms = []
        current_room = copy.deepcopy(dungeon.get_room_str((current_row, current_col)))
        dungeon.set_current_room(current_room)
        row = 3
        col = 3
        if current_row == 0 or current_row == dungeon_max_col - 1:
            if 0 < current_col < dungeon_max_row - 1:
                row = 2
                col = 3
            elif current_col == 0 or current_col == dungeon_max_row - 1:
                row = 2
                col = 2

        elif current_col == 0 or current_col == dungeon_max_row - 1:
            if 0 < current_row < dungeon_max_col - 1:
                row = 3
                col = 2
        # NW
        vision_rooms.append(self.get_vision_rm_corner(current_row, current_col, "N", "W", dungeon))
        # N
        vision_rooms.append(self.get_vision_rm_one(current_row, current_col, "N", dungeon))
        # NE
        vision_rooms.append(self.get_vision_rm_corner(current_row, current_col, "N", "E", dungeon))
        # new line
        # W
        vision_rooms.append(self.get_vision_rm_one(current_row, current_col, "W", dungeon))
        # self
        vision_rooms.append(current_room)
        # E
        vision_rooms.append(self.get_vision_rm_one(current_row, current_col, "E", dungeon))
        # /n
        # SW
        vision_rooms.append(self.get_vision_rm_corner(current_row, current_col, "S", "W", dungeon))
        #S
        vision_rooms.append(self.get_vision_rm_one(current_row, current_col, "S", dungeon))
        # SE
        vision_rooms.append(self.get_vision_rm_corner(current_row, current_col, "S", "E", dungeon))

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

        # Printing View
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
        Retrieves and returns string room for corner rooms
        :return: str
        """

        # Grab new column
        temp, north_col = dungeon._get_neighbor_coords(current_row, current_col,
                                                       col_direction)
        # Grab new row
        west_row, temp = dungeon._get_neighbor_coords(current_row, current_col,
                                                      row_direction)
        # If it is a true room, return the room
        if dungeon.is_valid_room(west_row, north_col):
            return dungeon.get_room_str((west_row, north_col))
        return ""

    def get_vision_rm_one(self, current_row, current_col, direction, dungeon):
        """
        Retrieves and returns string room for directly touching rooms
        :return: str
        """
        row, col = dungeon._get_neighbor_coords(current_row, current_col, direction)
        if dungeon.is_valid_room(row, col):
            return dungeon.get_room_str((row, col))
        return ""


class Pit(DungeonItems):
    def __init__(self, minimum, maximum):
        """ Inheriting DungeonItems class initializing name as "X" and passing a minimum amd maximum parameters
        param: minimum, maximum"""
        super().__init__("X")
        self.pit = -random.randint(minimum, maximum)

    def use_item(self):
        """ Implementing use_item method for Pit class"""
        return self.pit


class AbstractionPillar(DungeonItems):
    def __init__(self, abstraction_pillar):
        super().__init__("A")
        self.abstraction_pillar = abstraction_pillar

    def use_item(self):
        """ Implementing use_item method for AbstractionPillar class"""
        return self.abstraction_pillar


class InheritancePillar(DungeonItems):
    def __init__(self, inheritance_pillar):
        super().__init__("I")
        self.inheritance_pillar = inheritance_pillar

    def use_item(self):
        """ Implementing use_item method for InheritancePillar class"""
        return self.inheritance_pillar


class PolymorphismPillar(DungeonItems):
    def __init__(self, polymorphism_pillar):
        super().__init__("P")
        self.polymorphism_pillar = polymorphism_pillar

    def use_item(self):
        """ Implementing use_item method for PolymorphismPillar class"""
        return self.polymorphism_pillar


class EncapsulationPillar(DungeonItems):
    def __init__(self, encapsulation_pillar):
        super().__init__("E")
        self.encapsulation_pillar = encapsulation_pillar

    def use_item(self):
        """ Implementing use_item method for EncapsulationPillar class"""
        return self.encapsulation_pillar
