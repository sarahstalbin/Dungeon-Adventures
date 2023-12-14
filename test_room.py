import unittest
from room import Room


class TestRoom(unittest.TestCase):
    """ Testing Room class getter, setter and str functions"""

    def test_room_getter_setter(self):
        """ This method tests the getter and setter of some items of Room class"""
        room = Room()
        room.set_south_door()
        self.assertEqual(True, room.get_south_door())
        room.set_inheritance_pillar(True)
        self.assertEqual(True, room.get_inheritance_pillar())
        room.set_healing_potion(True)
        self.assertEqual(True, room.get_healing_potion())
        room.set_current_room(True)
        self.assertEqual(True, room.get_current_room())

    def test_room_str(self):
        """ This method tests the str(layout) of the Room class"""
        room = Room()
        room.set_empty_room(True)
        self.assertEqual("***\n* *\n***", room.__str__())
        room.set_entrance(True)
        self.assertEqual("***\n*i*\n***", room.__str__())
        room.set_west_door()
        self.assertEqual("***\n|i*\n***", room.__str__())


if __name__ == '__main__':
    unittest.main()
