from potion import HealingPotion, VisionPotion

class PotionFactory:
    """
    Creates and returns Potion objects for DungeonAdventure. All potions should be created via the PotionFactory.

    Contains one method: create_potion(), which creates a Potion object of a specified type along with the relevant
    data for creating that Potion.
    """

    @staticmethod
    def create_potion(potion_type, *args):
        """
        Creates a Potion object of a specified type using the relevant data for building that Potion. Returns
        the Potion.
        :param potion_type: name of the Potion object to be created.
        :param *args: variable Potion data required based on the type of Potion to be created.
        :return: a Vision Potion or a Healing Potion.
        """
        if potion_type == "vision":
            return VisionPotion()
        elif potion_type == "healing":
            return HealingPotion(*args)
        else:
            raise ValueError("Potion type is not valid")

