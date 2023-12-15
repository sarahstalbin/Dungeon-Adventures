"""
Name: Aqueno Nirasmi, Minna Chae, Sarah St. Albin
Assignment: Dungeon Adventure Game
Class: TCSS 502
"""

import unittest
from unittest.mock import patch
from room import Room
from DungeonTest import Dungeon
from DungeonItemsFactoryTest import DungeonItemsFactory
import random


class DungeonTests(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        random.seed(5)

    def test_init(self):
        rows, cols = 5, 5
        dungeon = Dungeon(rows, cols)

        self.assertEqual(dungeon.get_row_length(), rows)
        self.assertEqual(dungeon.get_col_length(), cols)

        self.assertEqual(len(dungeon.get_maze_array()), rows)
        self.assertEqual(len(dungeon.get_maze_array()), cols)

        for row in dungeon.get_maze_array():
            self.assertEqual(len(row), 5)
            for room in row:
                self.assertIsInstance(room, Room)

        self.assertNotEqual(len(dungeon.get_maze_dictionary()), 0)

    # def test_build_dungeon(self):
    #     rows, cols = 5, 5
    #     dungeon = Dungeon(rows, cols)
    #
    #     with patch.object(dungeon, '_create_maze') as mock_create_maze, \
    #             patch.object(dungeon, '_set_entrance_exit'), \
    #             patch.object(dungeon, '_make_impassable'), \
    #             patch.object(dungeon, '_is_traversable', return_value=True), \
    #             patch.object(dungeon, '_place_pillars'), \
    #             patch.object(dungeon, '_place_items'):
    #         dungeon.build_dungeon()
    #
    #         # Add assertions to check the interactions with internal methods???
    #         mock_create_maze.assert_called_once_with(
    #             dungeon.get_maze_array()[1][2], 1, 2
    #         )
    #
    #         # Add more assertions???
    #
    #         # Add assertions for the final state of the Dungeon instance
    #         self.assertNotEqual(len(dungeon.get_maze_dictionary()), 0)

    def test_get_entrance(self):
        rows, cols = 5, 5
        dungeon = Dungeon(rows, cols)

        result = dungeon.get_entrance()
        self.assertEqual(result, dungeon.get_maze_array()[0][0])



    def test_get_maze_array(self):
        rows, cols = 5, 5
        dungeon = Dungeon(rows, cols)

        result = dungeon.get_maze_array()
        self.assertEqual(result, dungeon.get_maze_array())

    def test_get_room_str(self):
        rows, cols = 5, 5
        dungeon = Dungeon(rows, cols)

        key = (1, 0)
        result = dungeon.get_room_str(key)
        self.assertEqual(result, dungeon.get_maze_dictionary().get(key))

    def test_get_col_length(self):
        rows, cols = 5, 5
        dungeon = Dungeon(rows, cols)

        result = dungeon.get_col_length()
        self.assertEqual(result, cols)

    def test_get_row_length(self):
        rows, cols = 5, 5
        dungeon = Dungeon(rows, cols)

        result = dungeon.get_row_length()
        self.assertEqual(result, rows)

    # @patch('room.Room')
    # def test_get_doors(self, mock_room):
    #     rows, cols = 5, 5
    #     dungeon = Dungeon(rows, cols)
    #
    #     mock_attributes_current = mock_room.return_value
    #     mock_attributes_new = mock_room.return_value
    #
    #     mock_attributes_current.get_north_door.return_value = True
    #     mock_attributes_new.get_south_door.return_value = True
    #
    #     curr_key = (1, 0)
    #     new_key = (1, 1)
    #
    #     with patch.object(dungeon, 'get_maze_dictionary', {(1, 0): mock_attributes_current, (1, 1): mock_attributes_new}):
    #         direction = "N"
    #         result = dungeon.get_doors(curr_key, new_key, direction)
    #         self.assertTrue(result)

    def test_set_current_room(self):
        rows, cols = 5, 5
        dungeon = Dungeon(rows, cols)

        room = dungeon.get_maze_array()[1][0]
        result = dungeon.set_current_room(room)
        self.assertEqual(result, room.set_current_room(True))

    def test_set_room_empty(self):
        rows, cols = 5, 5
        dungeon = Dungeon(rows, cols)

        room = dungeon.get_maze_array()[1][0]
        result = dungeon.set_room_empty((1, 0), pit=False)
        self.assertEqual(result, room.set_empty_room(True))

    def test_get_room_contents(self):
        rows, cols = 5, 5
        dungeon = Dungeon(rows, cols)

        mock_items = {(1, 0): {'healing_potion': True, 'vision_potion': False, 'pit': False,
                               'entrance': False, 'exit': False, 'multiple_items': False,
                               'empty_room': False, 'abstraction_pillar': False,
                               'polymorphism_pillar': False, 'inheritance_pillar': False,
                               'encapsulation_pillar': False}}

        with patch.object(dungeon, 'get_maze_dictionary', mock_items):
            result = dungeon.get_room_contents((1, 0))

        self.assertEqual(result, "I")

    def test_print_dictionary(self):
        rows, cols = 5, 5
        dungeon = Dungeon(rows, cols)

        mock_items = {(1, 0): {'healing_potion': True, 'vision_potion': False, 'pit': False,
                               'entrance': False, 'exit': False, 'multiple_items': False,
                               'empty_room': False, 'abstraction_pillar': False,
                               'polymorphism_pillar': False, 'inheritance_pillar': False,
                               'encapsulation_pillar': False}}

        with patch.object(dungeon, 'get_maze_dictionary', return_value=" "):
            result = dungeon.print_dictionary()

        self.assertEqual(result, None)

    def test_is_valid_room(self):
        rows, cols = 5, 5
        dungeon = Dungeon(rows, cols)

        row = 1
        col = 0

        result = dungeon.is_valid_room(row, col)
        self.assertEqual(result, True)


    # def test_str_(self):
    #     rows, cols = 5, 5
    #     dungeon = Dungeon(rows, cols)
    #
    #     dungeon_item_string =


    #
    # def test_print_play_dungeon(self):
    #     pass
    #

    @patch.object(Room, 'set_player_traveled')
    @patch.object(Dungeon, 'get_maze_dictionary')
    def test_set_player_traveled(self, mock_get_maze_dictionary, mock_set_player_traveled):
        rows, cols = 5, 5
        dungeon = Dungeon(rows, cols)

        key = (1, 0)

        mock_items = {(1, 0): {'healing_potion': True, 'vision_potion': False, 'pit': False,
                               'entrance': False, 'exit': False, 'multiple_items': False,
                               'empty_room': False, 'abstraction_pillar': False,
                               'polymorphism_pillar': False, 'inheritance_pillar': False,
                               'encapsulation_pillar': False}}

        mock_get_maze_dictionary.return_value = mock_items

        result = dungeon.set_player_traveled(key)

        mock_set_player_traveled.assert_called_once()

    #
    # def test_print_dungeon(self):
    #     pass
    #
    # def test_create_maze(self):
    #     pass


    def test_get_neighbor_coords(self):
        row, col = 5, 5
        dungeon = Dungeon(row, col)

        row = 2
        col = 1
        direction = "N"

        new_row, new_col = dungeon._get_neighbor_coords(row, col, direction)
        self.assertEqual((new_row, new_col), (1, 1))

    def test_opposite_direction(self):
        row, col = 5, 5
        dungeon = Dungeon(row, col)

        direction = "N"

        result = dungeon._opposite_direction(direction)
        self.assertEqual(result, {"N": "S", "S": "N", "E": "W", "W": "E"}[direction])

    @patch.object(Room, 'set_north_door')
    def test_knock_down_door_north(self, mock_set_north_door):
        rows, cols = 5, 5
        dungeon = Dungeon(rows, cols)
        room = Room()

        dungeon._knock_down_door(room, "N")

        mock_set_north_door.assert_called()

    @patch.object(Room, 'set_south_door')
    def test_knock_down_door_south(self, mock_set_south_door):
        rows, cols = 5, 5
        dungeon = Dungeon(rows, cols)
        room = Room()

        dungeon._knock_down_door(room, "S")

        mock_set_south_door.assert_called()

    @patch.object(Room, 'set_east_door')
    def test_knock_down_door_east(self, mock_set_east_door):
        rows, cols = 5, 5
        dungeon = Dungeon(rows, cols)
        room = Room()

        dungeon._knock_down_door(room, "E")

        mock_set_east_door.assert_called()

    @patch.object(Room, 'set_west_door')
    def test_knock_down_door_west(self, mock_set_west_door):
        rows, cols = 5, 5
        dungeon = Dungeon(rows, cols)
        room = Room()

        dungeon._knock_down_door(room, "W")

        mock_set_west_door.assert_called()

    # @patch.object(Room, 'set_entrance', 'set_exit', 'set_impasse')
    # @patch.object(Room, 'set_west_door', 'set_east_door', 'set_empty_room')
    # def test_set_entrance_exit(self, mock_set_entrance, mock_set_exit, mock_set_impasse, mock_set_west_door,
    #                            mock_set_east_door, mock_set_empty_room):
    #     rows, cols = 5, 5
    #     dungeon = Dungeon(rows, cols)
    #
    #     mock_entrance = dungeon.get_maze_array()[0][0]
    #     mock_exit = dungeon.get_maze_array()[rows - 1][cols - 1]
    #
    #     result = dungeon._set_entrance_exit()





        # @patch.object(Room, 'set_player_traveled')
        # @patch.object(Dungeon, 'get_maze_dictionary')
        # def test_set_player_traveled(self, mock_get_maze_dictionary, mock_set_player_traveled):
        #     rows, cols = 5, 5
        #     dungeon = Dungeon(rows, cols)
        #
        #     key = (1, 0)
        #
        #     mock_items = {(1, 0): {'healing_potion': True, 'vision_potion': False, 'pit': False,
        #                            'entrance': False, 'exit': False, 'multiple_items': False,
        #                            'empty_room': False, 'abstraction_pillar': False,
        #                            'polymorphism_pillar': False, 'inheritance_pillar': False,
        #                            'encapsulation_pillar': False}}
        #
        #     mock_get_maze_dictionary.return_value = mock_items
        #
        #     result = dungeon.set_player_traveled(key)
        #
        #     mock_set_player_traveled.assert_called_once()


    # def test_make_impassable(self):
    #     pass
    #
    # def test_is_traversable(self):
    #     pass
    #
    # def traverse_the_maze(self):
    #     pass
    #
    # def test_place_items(self):
    #     pass
    #
    # def test_place_pillars(self):
    #     pass
    #
    # def test_get_maze_dictionary(self):
    #     pass
    #
    # def test_get_object_symbols(self):
    #     pass


if __name__ == '__main__':
    unittest.main()
