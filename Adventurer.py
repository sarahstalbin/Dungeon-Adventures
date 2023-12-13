"""
Minna Chae
TCSS 501 and 502
Dungeon Adventure
"""


class Adventurer:
    def __init__(self, name="", HP=0, healing_potion_count =0, vision_potion_count=0):
        self.adventurer_dict = {"Name": name, "HP": HP, "Healing Potion Count": healing_potion_count,
                                "Vision Potion Count": vision_potion_count, "Pillar Count": 0}

    def set_name(self, name):
        """
        Setting name
        """
        self.adventurer_dict["Name"] = name

    def __get_name__(self):
        """
        Getting name
        """
        return self.adventurer_dict["Name"]

    def __get_health_potion_count__(self):
        """
        :returns: health potion count
        """
        return self.adventurer_dict["Healing Potion Count"]

    def __get_vision_potion_count__(self):
        """
        :returns: vision potion count
        """
        return self.adventurer_dict["Vision Potion Count"]

    def get_HP(self):
        """
        :Returns: health points
        """
        return self.adventurer_dict["HP"]

    def get_pillar(self):
        """
        :returns: pillar count
        """
        return self.adventurer_dict["Pillar Count"]

    def inc_healing_potion_count(self):
        """
        Increasing Healing Potion count
        """
        self.adventurer_dict["Healing Potion Count"] +=1
    #
    def inc_vision_potion_count(self):
        """
        Increasing Vision Potion count
        """
        self.adventurer_dict["Vision Potion Count"] += 1

    def set_HP(self, change_amount):
        """
        Reduces Healing potion count
        """
        self.adventurer_dict["HP"] += change_amount
        if change_amount > 0:
            self.adventurer_dict["Healing Potion Count"] -= 1


    def inc_pillar(self):
        """
        Increases pillar count
        """
        self.adventurer_dict["Pillar Count"] += 1

    def dec_vision_potion(self):
        """
        Decreases vision potion count
        """
        self.adventurer_dict["Vision Potion Count"] -= 1

    def __str__(self):
        """
        Printing Adventurer's statistics
        """
        formatted_list = [str(item) + " : " + str(values) for item, values in self.adventurer_dict.items()]
        return "\n" + "\n".join(formatted_list) + "\n"
