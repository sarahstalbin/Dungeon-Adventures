import unittest

from DungeonItems import HealingPotion, VisionPotion, Pit, EncapsulationPillar, PolymorphismPillar, InheritancePillar, \
    AbstractionPillar
from DungeonAdventure import DungeonAdventure

"""
Dungeon Adventure Unit Test. Must delete at end of DungeonAdventure.py 
game_play = DungeonAdventure()
game_play.play_whole_game()

for unit test to run properly.
"""

class TestItems(unittest.TestCase):
    """ Test cases for the child classes of DungeonItems """
    def test_healing_potion(self):
        """ Tests HealingPotion class get_name and the abstract method use_item"""
        healing_potion = HealingPotion(1, 10)
        self.assertEqual("H", healing_potion.get_name())
        self.assertGreaterEqual(healing_potion.use_item(), 1)
        self.assertLessEqual(healing_potion.use_item(), 10)

    def test_pit(self):
        """ Tests Pit class get_name and the abstract method use_item"""
        pit = Pit(1, 10)
        self.assertEqual("X", pit.get_name())
        self.assertGreaterEqual(pit.use_item(), -10)
        self.assertLessEqual(pit.use_item(), -1)

    def test_pillar(self):
        """ Tests one if the pillar class get_name and the abstract method use_item"""
        pillar = EncapsulationPillar(True)
        self.assertEqual("E", pillar.get_name())
        self.assertEqual(pillar.use_item(), True)

        def test_vision_rm_corner_no_cornerNW(self):
        """
        Tests NW corner of an area without a NW corner (coordinates are 0,0).
        """
        da = DungeonAdventure()
        vision = VisionPotion()
        current_row = 0
        current_col = 0
        coords = vision.get_vision_rm_corner(current_row, current_col, "N", "W", da.dungeon)
        self.assertEqual("", coords, "Test corner no corner coordinates failed")

    def test_vision_rm_corner_cornerNW(self):
        """
        Tests NW corner of an area with a NW corner (coordinates are 1,1).
        """
        da = DungeonAdventure()
        vision = VisionPotion()
        current_row = 1
        current_col = 1
        coords = vision.get_vision_rm_corner(current_row, current_col, "N", "W", da.dungeon)
        self.assertEqual(da.dungeon.get_room_str((0, 0)), coords, "Test corner coordinates failed")

    def test_vision_rm_corner_cornerSE(self):
        """
        Tests SE corner of an area with a SE corner (coordinates are 1,1).
        """
        da = DungeonAdventure()
        vision = VisionPotion()
        current_row = 1
        current_col = 1
        coords = vision.get_vision_rm_corner(current_row, current_col, "S", "E", da.dungeon)
        self.assertEqual(da.dungeon.get_room_str((2, 2)), coords, "Test corner coordinates failed")

    def test_vision_rm_corner_no_cornerSE(self):
        """
        Tests SE corner of an area without a SE corner (coordinates are 4,4).
        """
        da = DungeonAdventure()
        vision = VisionPotion()
        current_row = 4
        current_col = 4
        coords = vision.get_vision_rm_corner(current_row, current_col, "S", "E", da.dungeon)
        self.assertEqual("", coords, "Test corner no corner coordinates failed")

    def test_vision_rm_oneN(self):
        """
        Tests N corner of an area with a N corner (coordinates are 1,1).
        """
        da = DungeonAdventure()
        vision = VisionPotion()
        current_row = 1
        current_col = 1
        coords = vision.get_vision_rm_one(current_row, current_col, "N", da.dungeon)
        self.assertEqual(da.dungeon.get_room_str((0, 1)), coords, "Test corner coordinates failed")

    def test_vision_rm_oneS(self):
        """
        Tests S corner of an area with a S corner (coordinates are 1,1).
        """
        da = DungeonAdventure()
        vision = VisionPotion()
        current_row = 1
        current_col = 1
        coords = vision.get_vision_rm_one(current_row, current_col, "S", da.dungeon)
        self.assertEqual(da.dungeon.get_room_str((2, 1)), coords, "Test corner coordinates failed")

    def test_vision_rm_one_no_room(self):
        """
        Tests N corner of an area without a N corner (coordinates are 0,0).
        """
        da = DungeonAdventure()
        vision = VisionPotion()
        current_row = 0
        current_col = 0
        coords = vision.get_vision_rm_one(current_row, current_col, "N", da.dungeon)
        self.assertEqual("", coords, "Test corner coordinates failed")

if __name__ == '__main__':
    unittest.main()
