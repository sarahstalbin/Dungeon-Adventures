"""
Name: Aqueno Nirasmi, Minna Chae, Sarah St. Albin
TCSS 501 and 502
Dungeon Adventure
"""
# from Pillar import AbstractionPillar, EncapsulationPillar, InheritancePillar, PolymorphismPillar
from DungeonItems import HealingPotion, VisionPotion, Pit


class DungeonItemsFactory:
    """
    Creates and returns Item objects for the Dungeon Adventure Game.
    All Items should be created via the DungeonItemsFactory.

    Contains one method: create_item(), which creates an Item object of a specified type along with the relevant
    data for creating that Item.

    """

    @staticmethod
    def create_item(item_type, *args):
        """
        Static method that returns Items for the Dungeon.
        :param item_type (Str): The type of Item to be instantiated.
        :param args: Variable arguments based on the Item to be instantiated.
        :return: an Item object for the Dungeon Adventure Game.
        """
        if item_type == "V":
            return VisionPotion()
        elif item_type == "H":
            return HealingPotion(*args)
        elif item_type == "X":
            return Pit(*args)
        # elif item_type == "A":
        #     return AbstractionPillar("A")
        # elif item_type == "E":
        #     return EncapsulationPillar("E")
        # elif item_type == "I":
        #     return InheritancePillar("I")
        # elif item_type == "P":
        #     return PolymorphismPillar("P")
        else:
            raise ValueError("Invalid item type")


# Example usage
# vision_potion = DungeonItemsFactory.create_item("V")
# healing_potion = DungeonItemsFactory.create_item("H", 2, 4)
# pit = DungeonItemsFactory.create_item("X", 2, 5)
# # abstraction = DungeonItemsFactory.create_item("A")
# # encapsulation = DungeonItemsFactory.create_item("E")
# # inheritance = DungeonItemsFactory.create_item("I")
# # polymorphism = DungeonItemsFactory.create_item("P")
# print(healing_potion.use_item())