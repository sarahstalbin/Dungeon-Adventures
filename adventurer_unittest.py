"""
Name: Aqueno Nirasmi, Minna Chae, Sarah St. Albin
TCSS 501 and 502
Dungeon Adventure: Adventure Unit Test
"""


from Adventurer import Adventurer
import unittest


class adventurer_test(unittest.TestCase):

    def test_set_name(self):
        """
        Testing set name
        """
        adventurer = Adventurer("Minna",100, 2,1)
        dict_test = {"Name": "Minna", "HP" : 100, "Healing Potion Count": 2, "Vision Potion Count": 1,"Pillar Count": 0}

        formatted_list = ["   " +str(item) + " : " + str(values) for item, values in dict_test.items()]
        final_formatted_list = "\n" + "\n".join(formatted_list) + "\n"
        self.assertEqual(adventurer.__str__(), final_formatted_list, "Testing for str failed")

    def test_set_name_diff(self):
        """
        Testing update set name
        """
        adventurer = Adventurer("Minna",100, 2,1)
        dict_test = {"Name": "Minna", "HP" : 100, "Healing Potion Count": 2, "Vision Potion Count": 1,"Pillar Count": 0}

        self.assertEqual(adventurer.get_name__(), dict_test["Name"], "Testing for first set name failed")

        adventurer.set_name("Johnny")
        dict_test["Name"] = "Johnny"

        self.assertEqual(adventurer.get_name__(), dict_test["Name"], "Testing for second set_name failed")

    def test_get_name(self):
        """
        Testing get name
        """
        adventurer = Adventurer("Minna", 100, 2, 1)
        test_name = "Minna"
        self.assertEqual(adventurer.get_name__(), test_name, "Testing for get name failed")

    def test_get_health_potion_count__(self):
        """
        Testing get health potion count
        """
        adventurer = Adventurer("Minna", 100, 2, 1)
        self.assertEqual(adventurer.get_health_potion_count__(), 2, "Testing for get name failed")

    def test__get_vision_potion_count__(self):
        """
        Testing get vision potion count
        """
        adventurer = Adventurer("Minna", 100, 2, 1)
        self.assertEqual(adventurer.get_vision_potion_count__(), 1, "Testing for get name failed")

    def test_get_HP(self):
        """
        Testing get health point (HP) value
        """
        adventurer = Adventurer("Minna", 100, 2, 1)
        self.assertEqual(adventurer.get_HP(), 100, "Testing for get name failed")

    def test_get_pillar(self):
        """
        Testing get pillar count
        """
        adventurer = Adventurer("Minna", 100, 2, 1)
        adventurer.inc_pillar()
        self.assertEqual(adventurer.get_pillar(), 1, "Testing for get name failed")

    def test_increase_healing_potion_count(self):
        """
        Testing increase healing potion count
        """
        adventurer = Adventurer("Minna", 100, 2, 1)
        adventurer.inc_healing_potion_count()
        self.assertEqual(adventurer.get_health_potion_count__(), 3, "Testing for increase vision potion count failed")

    def test_increase_vision_potion_count(self):
        """
        Testing vision potion count
        """
        adventurer = Adventurer("Minna", 100, 2, 1)
        adventurer.inc_vision_potion_count()
        self.assertEqual(adventurer.get_vision_potion_count__(), 2, "Testing for increase vision potion count failed")

    def test_set_HP(self):
        """
        Testing set healing point (hp) count
        """
        adventurer = Adventurer("Minna", 100, 2, 1)
        adventurer.set_HP(20)
        self.assertEqual(adventurer.get_HP(), 120, "Testing for increase HP failed")

    def test_inc_pillar(self):
        """
        Testing increase pillar count
        """
        adventurer = Adventurer("Minna", 100, 2, 1)
        adventurer.inc_pillar()
        self.assertEqual(adventurer.get_pillar(), 1, "Testing for increase HP failed")

    def test_dec_vision_potion(self):
        """
        Testing decrease vision potion count
        """
        adventurer = Adventurer("Minna", 100, 2, 1)
        adventurer.dec_vision_potion()
        self.assertEqual(adventurer.get_pillar(), 0, "Testing for decrease vision potion failed")


if __name__ == "__main__":
    unittest.main()
