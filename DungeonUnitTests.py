"""
Name: Aqueno Nirasmi, Minna Chae, Sarah St. Albin
Assignment: Dungeon Adventure Game
Class: TCSS 502
"""

import unittest
from unittest.mock import patch, call, Mock, MagicMock
from io import StringIO
from room import Room
from DungeonTest import Dungeon
from DungeonItemsFactoryTest import DungeonItemsFactory
import random


class DungeonTests(unittest.TestCase):

    class MockRoom:
        def __init__(self, **kwargs):
            for key, value in kwargs.items():
                setattr(self, key, value)

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

    @patch.object(Dungeon, '_create_maze')
    def test_build_dungeon(self, mock_create_maze):
        rows, cols = 5, 5
        dungeon = Dungeon(rows, cols)

        # Create mock Room for start_room
        start_row = 2
        start_col = 3
        start_room = dungeon.get_maze_array()[start_row][start_col]

        dungeon.build_dungeon()

        # # Call _create_maze
        # mock_create_maze.assert_called_with()
        # expected_calls = 2
        # self.assertGreaterEqual(mock_create_maze.call_count, 1)




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

    def test_get_doors_north(self):
        rows, cols = 5, 5
        dungeon = Dungeon(rows, cols)

        current = (1,0)
        next = (0,0)
        direction = "N"
        is_current_room_north_door = dungeon.get_room_str(current).get_north_door()
        is_next_room_north_door = dungeon.get_room_str(next).get_south_door()
        results = dungeon.get_doors(current, next, direction)

        if is_current_room_north_door and is_next_room_north_door:
            self.assertTrue(results, "Test get doors north true failed")
        else:
            self.assertFalse(results, "Test get doors north false failed")

    def test_get_doors_south(self):
        rows, cols = 5, 5
        dungeon = Dungeon(rows, cols)

        current = (1,1)
        next = (2,1)
        direction = "S"
        is_current_room_north_door = dungeon.get_room_str(current).get_south_door()
        is_next_room_north_door = dungeon.get_room_str(next).get_north_door()
        results = dungeon.get_doors(current, next, direction)

        if is_current_room_north_door and is_next_room_north_door:
            self.assertTrue(results, "Test get doors south true failed")
        else:
            self.assertFalse(results, "Test get doors south false failed")

    def test_get_doors_east(self):
        rows, cols = 5, 5
        dungeon = Dungeon(rows, cols)

        current = (1,1)
        next = (1,2)
        direction = "E"
        is_current_room_north_door = dungeon.get_room_str(current).get_east_door()
        is_next_room_north_door = dungeon.get_room_str(next).get_west_door()
        results = dungeon.get_doors(current, next, direction)

        if is_current_room_north_door and is_next_room_north_door:
            self.assertTrue(results, "Test get doors east true failed")
        else:
            self.assertFalse(results, "Test get doors east false failed")

    def test_get_doors_west(self):
        rows, cols = 5, 5
        dungeon = Dungeon(rows, cols)

        current = (1,1)
        next = (1,0)
        direction = "W"
        is_current_room_north_door = dungeon.get_room_str(current).get_west_door()
        is_next_room_north_door = dungeon.get_room_str(next).get_east_door()
        results = dungeon.get_doors(current, next, direction)

        if is_current_room_north_door and is_next_room_north_door:
            self.assertTrue(results, "Test get doors west true failed")
        else:
            self.assertFalse(results, "Test get doors west false failed")

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

    # def test_get_room_contents(self):
    #     rows, cols = 5, 5
    #     dungeon = Dungeon(rows, cols)
    #
    #     mock_items = {(1, 0): {'healing_potion': True, 'vision_potion': False, 'pit': False,
    #                            'entrance': False, 'exit': False, 'multiple_items': False,
    #                            'empty_room': False, 'abstraction_pillar': False,
    #                            'polymorphism_pillar': False, 'inheritance_pillar': False,
    #                            'encapsulation_pillar': False}}
    #
    #     with patch.object(dungeon, 'get_maze_dictionary', mock_items):
    #         result = dungeon.get_room_contents((1, 0))
    #
    #     self.assertEqual(result, "V")

    def test_print_dictionary(self):
        rows, cols = 5, 5
        dungeon = Dungeon(rows, cols)

        mock_items = {(1, 0): {'healing_potion': True, 'vision_potion': False, 'pit': False,
                               'entrance': False, 'exit': False, 'multiple_items': False,
                               'empty_room': False, 'abstraction_pillar': False,
                               'polymorphism_pillar': False, 'inheritance_pillar': False,
                               'encapsulation_pillar': False}}

        with patch.object(dungeon, 'get_maze_dictionary', return_value=mock_items):
            result = dungeon.print_dictionary()

        self.assertEqual(result, None)

    def test_is_valid_room(self):
        rows, cols = 5, 5
        dungeon = Dungeon(rows, cols)

        row = 1
        col = 0

        result = dungeon.is_valid_room(row, col)
        self.assertEqual(result, True)
    #
    # # def test_str_(self):
    # #     pass
    #
    #
    # #
    # # def test_print_play_dungeon(self):
    # #     pass
    # #
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
    # #
    # # def test_print_dungeon(self):
    # #     pass

    @patch('random.shuffle')
    @patch('random.choice')
    def test_create_maze(self, mock_shuffle, mock_choice):
        mock_shuffle.side_effect = lambda x: x[0]
        mock_choice.side_effect = lambda x: x

        rows, cols = 5, 5
        dungeon = Dungeon(rows, cols)

        # Mock the _get_neighbor_coords method to return specific coordinates
        with patch.object(dungeon, '_get_neighbor_coords', side_effect=[(1, 0), (2, 0), (1, 1), (0, 1)]):
            # Mock the is_valid_room method to always return True
            with patch.object(dungeon, 'is_valid_room', return_value=True):
                # Mock the _opposite_direction method to return the opposite direction
                with patch.object(dungeon, '_opposite_direction', side_effect=lambda x: {"N": "S", "S": "N", "E": "W",
                                                                                         "W": "E"}[x]):
                    # Mock the _knock_down_door method to do nothing during the test
                    with patch.object(dungeon, '_knock_down_door', Mock()):
                        # Call the _create_maze method
                        dungeon._create_maze(dungeon.get_maze_array()[0][0], 0, 0)

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
    #
    # # def test_set_entrance_exit(self):
    # #     pass
    #
    # # def test_make_impassable(self):
    # #     pass
    # #
    #
    # # def test_is_traversable(self):
    # #     pass
    #
    # #
    # # def traverse_the_maze(self):
    # #     pass
    # #
    # # def test_place_items(self):
    # #     pass
    # #
    # # def test_place_pillars(self):
    # #     pass
    # #
    #
    # def test_get_maze_dictionary(self):
    #     rows = 3
    #     cols = 3
    #     dungeon = Dungeon(rows, cols)
    #
    #     mock_items = {
    #         (0, 0): Mock(spec=Room),
    #         (0, 1): Mock(spec=Room),
    #         (0, 2): Mock(spec=Room),
    #         (1, 0): Mock(spec=Room),
    #         (1, 1): Mock(spec=Room),
    #         (1, 2): Mock(spec=Room),
    #         (2, 0): Mock(spec=Room),
    #         (2, 1): Mock(spec=Room),
    #         (2, 2): Mock(spec=Room),
    #     }
    #
    #     with patch.object(dungeon, '_Dungeon__items', mock_items):
    #         result = dungeon.get_maze_dictionary()
    #
    #     self.assertEqual(result, mock_items)
    #
    # def test_get_object_symbols(self):
    #     pass
    #





if __name__ == '__main__':
    unittest.main()
