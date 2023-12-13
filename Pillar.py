from abc import ABC, abstractmethod


class Pillar(ABC):
    """
    An abstract base class representing a Pillar object. All subclasses should inherit from this class
    and implement the getter() and setter() methods to manage Pillars.

    Attributes: a name (str) for the Pillar type being instantiated.

    Contains three methods: a constructor to initialize a new Pillar object, an undefined getter() method, and an
    undefined setter() method to be used by all subclasses.
    """

    def __init__(self, pillar):
        """
        Initializes a new Pillar object.
        :param name (str): the name of the Pillar type.
        """
        self.__pillar = pillar

    @abstractmethod
    def get_pillar(self, pillar):
        """
        Undefined getter method for Pillar abstract base class.
        """
        pass

    @abstractmethod
    def set_pillar(self, pillar):
        """
        Undefined setter method for Pillar abstract base class.
        :param pillar: type of Pillar to be placed.
        """
        pass


class AbstractionPillar(Pillar):
    """
    Concrete class representing a Pillar of Abstraction.

    __init__(self, abstraction_pillar): Initializes an instance of a Pillar of Abstraction.
    get_pillar(abstraction): a getter method to retrieve a Pillar of Abstraction.
    set_pillar(abstraction): a setter method that sets a Pillar of Abstraction, such as in a room.
    """
    def __init__(self, abstraction_pillar):
        super().__init__("A")
        self.abstraction_pillar = abstraction_pillar

    def get_pillar(self, abstraction):
        return self.abstraction_pillar

    def set_pillar(self, abstraction):
        self.abstraction_pillar = abstraction


class EncapsulationPillar(Pillar):
    """
    Concrete class representing a Pillar of Encapsulation.

    __init__(self, encapsulation_pillar): Initializes an instance of a Pillar of Encapsulation.
    get_pillar(encapsulation): a getter method to retrieve a Pillar of Encapsulation.
    set_pillar(encapsulation): a setter method that sets a Pillar of Encapsulation, such as in a room.
    """
    def __init__(self, encapsulation_pillar):
        super().__init__("E")
        self.encapsulation_pillar = encapsulation_pillar

    def get_pillar(self, encapsulation):
        return self.encapsulation_pillar

    def set_pillar(self, encapsulation):
        self.encapsulation_pillar = encapsulation


class InheritancePillar(Pillar):
    """
    Concrete class representing a Pillar of Inheritance.

    __init__(self, inheritance_pillar): Initializes an instance of a Pillar of Inheritance.
    get_pillar(inheritance): a getter method to retrieve a Pillar of Inheritance.
    set_pillar(inheritance): a setter method that sets a Pillar of Inheritance, such as in a room.
    """
    def __init__(self, inheritance_pillar):
        super().__init__("I")
        self.inheritance_pillar = inheritance_pillar

    def get_pillar(self, inheritance):
        return self.inheritance_pillar

    def set_pillar(self, inheritance):
        self.inheritance_pillar = inheritance


class PolymorphismPillar(Pillar):
    """
    Concrete class representing a Pillar of Polymorphism.

    __init__(self, polymorphism_pillar): Initializes an instance of a Pillar of Polymorphism.
    get_pillar(polymorphism): a getter method to retrieve a Pillar of Polymorphism.
    set_pillar(polymorphism): a setter method that sets a Pillar of Polymorphism, such as in a room.
    """
    def __init__(self, polymorphism_pillar):
        super().__init__("P")
        self.polymorphism_pillar = polymorphism_pillar

    def get_pillar(self, polymorphism):
        return self.polymorphism_pillar

    def set_pillar(self, polymorphism):
        self.polymorphism_pillar = polymorphism

