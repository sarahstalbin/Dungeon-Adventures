import unittest

from DungeonItems import HealingPotion, VisionPotion, Pit, EncapsulationPillar, PolymorphismPillar, InheritancePillar, \
    AbstractionPillar


class TestShapes(unittest.TestCase):
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


if __name__ == '__main__':
    unittest.main()
