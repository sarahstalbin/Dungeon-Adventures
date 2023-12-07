import random


class Room:
    """ Room class sets all the items necessary for the dungeon adventure and
    prints the layout of the room """

    def __init__(self, healing_potion=False,
                 vision_potion=False, pit=False):
        """ Initializing the items and setting it to False  """

        self.__healing_potion = False
        self.__vision_potion = False
        self.__pit = False
        self.__entrance = False
        self.__exit = False
        self.__impasse = False
        self.__visited = False
        self.__multiple_items = False
        self.__north_door = False
        self.__south_door = False
        self.__east_door = False
        self.__west_door = False
        self.__abstraction_pillar = False
        self.__encapsulation_pillar = False
        self.__inheritance_pillar = False
        self.__polymorphism_pillar = False
        self.__empty_room = False

    # getter methods
    def get_north_door(self):
        """ gets north_door boolean value """
        return self.__north_door

    def get_south_door(self):
        """ gets south_door boolean value """
        return self.__south_door

    def get_east_door(self):
        """ gets east_door boolean value """
        return self.__east_door

    def get_west_door(self):
        """ gets west_door boolean value """
        return self.__west_door

    def get_impasse(self):
        """ gets impasse boolean value """
        return self.__impasse

    def get_visited(self):
        """ gets visited boolean value """
        return self.__visited

    def get_empty_room(self):
        """ gets empty_room boolean value """
        return self.__empty_room

    def get_entrance(self):
        """ gets entrance boolean value """
        return self.__entrance

    def get_exit(self):
        """ gets exit boolean value """
        return self.__exit

    # setter methods

    def set_healing_potion(self, add_potion):
        """ setting healing potion
         param: add_potion"""
        self.__healing_potion = add_potion

    def set_vision_potion(self, vision_potion):
        """ setting vision potion
                 param: vision_potion"""
        self.__vision_potion = vision_potion

    def set_pit(self, reduce_potion):
        """ setting pit
        param: reduce_potion"""
        self.__pit = reduce_potion

    def set_north_door(self):
        """ setting north_door """
        self.__north_door = True

    def set_south_door(self):
        """ setting south_door """
        self.__south_door = True

    def set_east_door(self):
        """ setting east_door """
        self.__east_door = True

    def set_west_door(self):
        """ setting west_door """
        self.__west_door = True

    def set_abstraction_pillar(self):
        """ setting abstraction_pillar """
        self.__abstraction_pillar = True

    def set_encapsulation_pillar(self):
        """ setting encapsulation_pillar """
        self.__encapsulation_pillar = True

    def set_inheritance_pillar(self):
        """ setting inheritance_pillar """
        self.__inheritance_pillar = True

    def set_polymorphism_pillar(self):
        """ setting polymorphism_pillar """
        self.__polymorphism_pillar = True

    def set_empty_room(self):
        """ setting empty_room """
        self.__empty_room = True

    def set_entrance(self):
        """ setting entrance """
        self.__entrance = True

    def set_exit(self):
        """ setting exit """
        self.__exit = True

    def set_impasse(self, impasse):
        """ setting impasse """
        self.__impasse = impasse

    def set_visited(self, visited):
        """ setting visited """
        self.__visited = visited

    def multiple_items(self):
        """ This method is for one or more items in a room """
        count = 0
        if self.__healing_potion:
            count += 1
        if self.__vision_potion:
            count += 1

        if count > 1:
            self.__multiple_items = True

    def can_enter(self):
        """ This method can be called if there is no impasse and if it is not visited """
        return not self.__impasse and not self.__visited

    def __str__(self):
        """ str method prints the layout of the room class with its abbreviated names and symbols"""
        layout = ""
        if self.__north_door:
            layout += "*_*"
        else:
            layout += "***"
        layout += "\n"
        if self.__west_door:
            layout += "|"
        else:
            layout += "*"
        if self.__healing_potion:
            layout += "H"
        elif self.__vision_potion:
            layout += "V"
        elif self.__pit:
            layout += "X"
        elif self.__entrance:
            layout += "i"
        elif self.__exit:
            layout += "O"
        elif self.__multiple_items:
            layout += "M"
        elif self.__empty_room:
            layout += " "
        elif self.__abstraction_pillar:
            layout += "A"
        elif self.__polymorphism_pillar:
            layout += "P"
        elif self.__inheritance_pillar:
            layout += "I"
        elif self.__encapsulation_pillar:
            layout += "E"
        if self.__east_door:
            layout += "|"
        else:
            layout += "*"
        layout += "\n"
        if self.__south_door:
            layout += "*_*"
        else:
            layout += "***"
        return layout


class RoomFactory:
    @classmethod
    def create_room(cls, has_healing_potion=False, has_vision_potion=False, has_pit=False):
        return Room(has_healing_potion, has_vision_potion,
                    has_pit)


has_healing_potion = random.randint(0, 100) <= 10
has_vision_potion = random.randint(0, 100) <= 10
has_pit = random.randint(0, 100) <= 10
