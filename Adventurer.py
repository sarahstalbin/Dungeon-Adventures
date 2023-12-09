"""
Minna Chae
TCSS 501 and 502
Dungeon Adventure
"""
import random

class Adventurer:
    def __init__(self, name="", HP=0, healing_potion_count =0, vision_potion_count=0):
        #super().__init__() = name
        self.adventurer_dict = {"Name": name, "HP": HP, "Healing Potion Count": healing_potion_count,
                                "Vision Potion Count": vision_potion_count, "Pillar Count": 0}
        # self.HP = #random.randint(75, 100)
        # self.healing_potion_count = 0 - can change
        # self.vision_Potion_count = 0
        # self.pillar_count = 0

    # @abstractmethod
    def set_name(self, name):
        """getting name from Dungeon Adventure, setting, and passing name if needed"""
        self.adventurer_dict["Name"] = name

    def __get_name__(self):
        """Setting name"""
        return self.adventurer_dict["Name"]

    def __get_health_potion_count__(self):
        """returns health potion count"""
        return self.adventurer_dict["Healing Potion Count"]

    def __get_vision_potion_count__(self):
        """returns health potion count"""
        return self.adventurer_dict["Vision Potion Count"]

    def get_HP(self):
        return self.adventurer_dict["HP"]

    def get_pillar(self):
        return self.adventurer_dict["Pillar Count"]

    def inc_healing_potion_count(self):
        """Increasing healing Potion count passed from Dungeon"""
        self.adventurer_dict["Healing Potion Count"] +=1
    #
    def inc_vision_potion_count(self):
        """Increasing Vision Potion count passed from Dungeon"""
        self.adventurer_dict["Vision Potion Count"] += 1

    def inc_HP(self):
        """Increase health point requested via Dungeon"""
        self.adventurer_dict["HP"] += random.randint(1, 10)
        self.adventurer_dict["Healing Potion Count"] -= 1

    def inc_pillar(self):
        self.adventurer_dict["Pillar Count"] += 1
    def dec_HP(self):
        """Decrease HP if falling in pit"""
        # self.adventurer_dict["HP"] -= random.randint(1, 10)
        self.adventurer_dict["HP"] -= 100

    def dec_vision_potion(self):
        self.adventurer_dict["Vision Potion Count"] -= 1

    def __str__(self):
        """Printing in string form"""
        # string_value = ""
        # for item, values in self.adventurer_dict.items():
        #     string_value += str(item) + " " + str(values) + " "
        # return string_value
        formatted_list = [str(item) + " : " + str(values) for item, values in self.adventurer_dict.items()]
        return "\n" + "\n".join(formatted_list) + "\n"
