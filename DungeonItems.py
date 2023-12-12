import random
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
