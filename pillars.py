from abc import ABC, abstractmethod


class Pillar(ABC):
    """ Pillar class implemented with abstractmethod"""

    def __init__(self, name):
        """ Initializing name
        param: name"""
        self.name = name

    def get_name(self):
        """ getter function for name"""
        return self.name

    @abstractmethod
    def use_pillar(self):
        """ abstract method of use_pillar"""
        pass


class AbstractionPillar(Pillar):
    def __init__(self, abstraction_pillar):
        super().__init__("A")
        self.abstraction_pillar = abstraction_pillar

    def use_pillar(self):
        """ Implementing use_pillar method for AbstractionPillar class"""
        return self.abstraction_pillar


class InheritancePillar(Pillar):
    def __init__(self, inheritance_pillar):
        super().__init__("I")
        self.inheritance_pillar = inheritance_pillar

    def use_pillar(self):
        """ Implementing use_pillar method for InheritancePillar class"""
        return self.inheritance_pillar


class PolymorphismPillar(Pillar):
    def __init__(self, polymorphism_pillar):
        super().__init__("P")
        self.polymorphism_pillar = polymorphism_pillar

    def use_pillar(self):
        """ Implementing use_pillar method for PolymorphismPillar class"""
        return self.polymorphism_pillar


class EncapsulationPillar(Pillar):
    def __init__(self, encapsulation_pillar):
        super().__init__("E")
        self.encapsulation_pillar = encapsulation_pillar

    def use_pillar(self):
        """ Implementing use_pillar method for EncapsulationPillar class"""
        return self.encapsulation_pillar
