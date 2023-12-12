import random
from abc import ABC, abstractmethod


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
        " Implementing use_potion method for HealingPotion class"
        return self.health_points


class VisionPotion(Potion):
    def __init__(self):
        """ Inheriting Potion class initializing name as "H" """
        super().__init__("V")

    def use_potion(self):
        pass
