"""
Name: Aqueno Nirasmi, Minna Chae, Sarah St. Albin
TCSS 501 and 502
Dungeon Adventure
"""

from DungeonItems import HealingPotion, VisionPotion, Pit
import random


class DungeonItemsFactory:
    """
    Creates and returns Item objects for the Dungeon Adventure Game.
    All Items should be created via the DungeonItemsFactory.

    Contains two methods: create_item(), which creates an Item object of a specified type using relevant data for
    creating that Item, and create_multiple_items(), which creates multiple Item objects.

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
        else:
            raise ValueError("Invalid item type")

    @staticmethod
    def create_multiple_items(*args):
        """
        Creates multiple Item objects using relevant data for instantiating that object.
        :param args: necessary data for instantiating an object. Some objects require no parameters.
        :return: an array of Item objects.
        """
        items = ["V", "H", "X"]
        results = random.sample(items, 3)
        created_items = []

        for value in results:
            if value == "V":
                created_items.append(VisionPotion())
            elif value == "H":
                created_items.append(HealingPotion(*args))
            elif value == "X":
                created_items.append(Pit(*args))
            else:
                raise ValueError("Invalid item type")
        return created_items



