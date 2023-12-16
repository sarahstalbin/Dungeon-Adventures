"""
Name: Aqueno Nirasmi, Minna Chae, Sarah St. Albin
TCSS 501 and 502
Dungeon Adventure: dungeon adventure unit test
"""
import unittest
from unittest.mock import patch
from DungeonAdventure import DungeonAdventure


class DungeonAdventureTest(unittest.TestCase):

    @patch('builtins.input', side_effect=['easy', "Minna"])
    def test_set_play_mode_easy(self, prompt):
        """
        Testing easy play mode
        """
        expect_output = {"Name": "Minna", "HP": 100, "Healing Potion Count": 3,
                                "Vision Potion Count": 0, "Pillar Count": 0}

        da = DungeonAdventure()
        da.set_play_mode()
        self.assertEqual(da.adventurer.__get_name__(), expect_output["Name"], "Testing Easy for first set "
                                                                              "name failed")
        self.assertEqual(da.adventurer.__get_health_potion_count__(), expect_output["Healing Potion Count"],
                         "Testing Easy for health potion failed")
        self.assertTrue(1 <= da.adventurer.__get_vision_potion_count__() <= 3,
                         "Testing Easy for vision potion failed")
        self.assertEqual(da.adventurer.get_HP(), expect_output["HP"], "Testing Easy for HP failed")
        self.assertEqual(da.adventurer.get_pillar(), expect_output["Pillar Count"] , "Testing Easy for "
                                                                                    "Pillar count failed")
        self.assertEqual(da.dungeon.get_col_length(), 5, "Testing Easy for "
                                                                                 "collumn length failed")
        self.assertEqual(da.dungeon.get_row_length(), 5, "Testing Easy for "
                                                                                 "row length failed")

    @patch('builtins.input', side_effect=['medium', "Minna"])
    def test_set_play_mode_medium(self, prompt):
        """
        Testing medium play mode
        """
        expect_output = {"Name": "Minna", "HP": 100, "Healing Potion Count": 3,
                                "Vision Potion Count": 3, "Pillar Count": 0}

        da = DungeonAdventure()
        da.set_play_mode()
        self.assertEqual(da.adventurer.__get_name__(), expect_output["Name"], "Testing Easy for first set "
                                                                              "name failed")
        self.assertTrue(75 <= da.adventurer.get_HP() <= 100,
                         "Testing Med for HP failed")
        self.assertTrue(0 <= da.adventurer.__get_health_potion_count__() <= 2,
                         "Testing Med for health potion failed")
        self.assertTrue(0 <= da.adventurer.__get_vision_potion_count__() <= 1,
                         "Testing Easy for vision potion failed")
        self.assertEqual(da.adventurer.get_pillar(), expect_output["Pillar Count"] , "Testing Easy for "
                                                                                    "Pillar count failed")
        self.assertEqual(da.dungeon.get_col_length(), 10, "Testing Easy for "
                                                                                 "collumn length failed")
        self.assertEqual(da.dungeon.get_row_length(), 10, "Testing Easy for "
                                                                                 "row length failed")

    @patch('builtins.input', side_effect=['hard', "Minna"])
    def test_set_play_mode_hard(self, prompt):
        """
        Testing Hard play mode
        """
        expect_output = {"Name": "Minna", "HP": 100, "Healing Potion Count": 0,
                         "Vision Potion Count": 0, "Pillar Count": 0}

        da = DungeonAdventure()
        da.set_play_mode()
        self.assertEqual(da.adventurer.__get_name__(), expect_output["Name"], "Testing Easy for first set "
                                                                              "name failed")
        self.assertTrue(75 <= da.adventurer.get_HP() <= 90,"Testing hard for HP failed")
        self.assertEqual(da.adventurer.__get_health_potion_count__(), expect_output["Healing Potion Count"],
                         "Testing hard for health potion failed")

        self.assertEqual(da.adventurer.__get_vision_potion_count__(), expect_output["Vision Potion Count"],
                         "Testing hard for Vision Potion Count failed")
        self.assertEqual(da.adventurer.get_pillar(), expect_output["Pillar Count"], "Testing hard for "
                                                                                    "Pillar count failed")
        self.assertEqual(da.dungeon.get_col_length(), 15, "Testing Easy for "
                                                          "column length failed")
        self.assertEqual(da.dungeon.get_row_length(), 15, "Testing Easy for row length failed")

    @patch('builtins.input', side_effect=['c', 50, 20, 25, 20, 20, "Minna"])
    def test_set_play_mode_hard(self, prompt):
        """
        Testing User choice play mode
        """
        expect_output = {"Name": "Minna", "HP": 50, "Healing Potion Count": 20,
                         "Vision Potion Count": 25, "Pillar Count": 0}

        da = DungeonAdventure()
        da.set_play_mode()
        self.assertEqual(da.adventurer.__get_name__(), expect_output["Name"], "Testing Easy for first set "
                                                                              "name failed")
        self.assertEqual(da.adventurer.get_HP(), expect_output["HP"], "Testing hard for HP failed")
        self.assertEqual(da.adventurer.__get_health_potion_count__(), expect_output["Healing Potion Count"],
                         "Testing hard for health potion failed")

        self.assertEqual(da.adventurer.__get_vision_potion_count__(), expect_output["Vision Potion Count"],
                         "Testing hard for Vision Potion Count failed")
        self.assertEqual(da.adventurer.get_pillar(), expect_output["Pillar Count"], "Testing hard for "
                                                                                    "Pillar count failed")
        self.assertEqual(da.dungeon.get_col_length(), 20, "Testing Easy for "
                                                          "column length failed")
        self.assertEqual(da.dungeon.get_row_length(), 20, "Testing Easy for row length failed")

    def test_menu_str(self):
        """
        Tests the menu string to be printed
        """
        da = DungeonAdventure()
        menu = {"Action Menu": "m", "Go Up": "w", "Go Down": "s", "Go Left": "a", "Go Right": "d",
                "Use Health Potion": "h", "Use Vision": "v", "View current status": "stats", "Quit Game": "q"}

        formatted_list = ["    " + item + " : " + values for item, values in menu.items()]
        string_test = "\n".join(formatted_list) + "\n"
        actual_string = da.menu_str()
        self.assertEqual(actual_string, string_test, "Not equal")

    @patch('builtins.input', side_effect=['e', 'Minna', 'h', 'q'])
    def test_player_command_health(self, prompt):
        """
        Testing player using health command.
        """
        da = DungeonAdventure()
        da.set_play_mode() #sets default values - easy, name:"Minna", health potion: 3,
        da.player_command()
        health_potion_count = da.adventurer.__get_health_potion_count__()
        self.assertEqual(health_potion_count, 2, "Test player command h healing count failed")
        self.assertTrue(da.adventurer.get_HP() > 100, "Testing player command h HP failed")

    def test_move_adventurer_south(self):
        """
        Testing player input for south direction, check to see if that direction is possible and move that direction.
        If moving to next room is possible go to next room.
        """
        da = DungeonAdventure()
        da.move_adventurer("s")
        real_direction = "S"
        current_row = 0
        current_col = 0
        new_row, new_col = da.dungeon._get_neighbor_coords(current_row, current_col, real_direction)

        current_key = (current_row,current_col)
        new_key = (new_row, new_col)

        #test if there is a room
        if da.dungeon.is_valid_room(new_row, new_col):
            self.assertEqual(da.dungeon.is_valid_room(new_row, new_col), True, "Test move Adventurer next "
                                                                              "room failed")
            self.assertEqual(new_row, 1, "Test move Adventurer get row failed")
            self.assertEqual(new_col, 0, "Test move Adventurer get column failed")
        else:
            self.assertEqual(da.dungeon.is_valid_room(new_row, new_col), False, "Test move Adventurer next "
                                                                              "room fail failed")

        #test if you can go into the room
        if da.dungeon.get_doors(current_key, new_key, real_direction):
            self.assertEqual(da.dungeon.get_doors(current_key, new_key, real_direction), True, "Test move "
                                                                                              "adventurer door fail")
            self.assertEqual(da.player_loc_row, 1, "Test move Adventurer row failed")
            self.assertEqual(da.player_loc_col, 0, "Test move Adventurer row failed")
        else:
            self.assertEqual(da.dungeon.get_doors(current_key, new_key, real_direction), False, "Test move "
                                                                                        "adventurer room fail failed")

    def test_move_adventurer_north(self):
        """
        Testing player input for north direction, check to see if that direction is possible and move that direction.
        If moving to next room is possible go to next room.
        """
        da = DungeonAdventure()
        da.player_loc_col = 1
        da.player_loc_row = 1
        da.move_adventurer("w")
        real_direction = "N"
        current_row = da.player_loc_row
        current_col = da.player_loc_col
        new_row, new_col = da.dungeon._get_neighbor_coords(current_row, current_col, real_direction)

        current_key = (current_row, current_col)
        new_key = (new_row, new_col)

        # test if there is a room
        if da.dungeon.is_valid_room(new_row, new_col):
            self.assertEqual(da.dungeon.is_valid_room(new_row, new_col), True, "Test move Adventurer next "
                                                                               "room failed")
            self.assertEqual(new_row, 0, "Test move Adventurer get row failed")
            self.assertEqual(new_col, 1, "Test move Adventurer get column failed")
        else:
            self.assertEqual(da.dungeon.is_valid_room(new_row, new_col), False, "Test move Adventurer next "
                                                                               "room fail failed")

        # test if you can go into the room
        if da.dungeon.get_doors(current_key, new_key, real_direction):
            self.assertEqual(da.dungeon.get_doors(current_key, new_key, real_direction), True, "Test move "
                                                                                               "adventurer door fail")
            self.assertEqual(da.player_loc_row, 0, "Test move Adventurer row failed")
            self.assertEqual(da.player_loc_col, 1, "Test move Adventurer row failed")
        else:
            self.assertEqual(da.dungeon.get_doors(current_key, new_key, real_direction), False, "Test move "
                                                                                        "adventurer room fail failed")

    def test_move_adventurer_east(self):
        """
        Testing player input for east direction, check to see if that direction is possible and move that direction.
        If moving to next room is possible go to next room.
        """
        da = DungeonAdventure()
        da.move_adventurer("d")
        real_direction = "E"
        current_row = 0
        current_col = 0
        new_row, new_col = da.dungeon._get_neighbor_coords(current_row, current_col, real_direction)

        current_key = (current_row, current_col)
        new_key = (new_row, new_col)

        # test if there is a room
        if da.dungeon.is_valid_room(new_row, new_col):
            self.assertEqual(da.dungeon.is_valid_room(new_row, new_col), True, "Test move Adventurer next "
                                                                               "room failed")
            self.assertEqual(new_row, 0, "Test move Adventurer get row failed")
            self.assertEqual(new_col, 1, "Test move Adventurer get column failed")
        else:
            self.assertEqual(da.dungeon.is_valid_room(new_row, new_col), False, "Test move Adventurer next "
                                                                                "room fail failed")

        # test if you can go into the room
        if da.dungeon.get_doors(current_key, new_key, real_direction):
            self.assertEqual(da.dungeon.get_doors(current_key, new_key, real_direction), True, "Test move "
                                                                                               "adventurer door fail")
            self.assertEqual(da.player_loc_row, 0, "Test move Adventurer row failed")
            self.assertEqual(da.player_loc_col, 1, "Test move Adventurer row failed")
        else:
            self.assertEqual(da.dungeon.get_doors(current_key, new_key, real_direction), False, "Test move "
                                                                                                "room fail failed")

    def test_move_adventurer_west(self):
        """
        Testing player input for west direction, check to see if that direction is possible and move that direction.
        If moving to next room is possible go to next room.
        """
        da = DungeonAdventure()
        da.player_loc_col = 1
        da.player_loc_row = 1
        da.move_adventurer("a")
        real_direction = "W"
        current_row = da.player_loc_row
        current_col = da.player_loc_col
        new_row, new_col = da.dungeon._get_neighbor_coords(current_row, current_col, real_direction)

        current_key = (current_row, current_col)
        new_key = (new_row, new_col)

        # test if there is a room
        if da.dungeon.is_valid_room(new_row, new_col):
            self.assertEqual(da.dungeon.is_valid_room(new_row, new_col), True, "Test move Adventurer next "
                                                                               "room failed")
            self.assertEqual(new_row, 1, "Test move Adventurer get row failed")
            self.assertEqual(new_col, 0, "Test move Adventurer get column failed")
        else:
            self.assertEqual(da.dungeon.is_valid_room(new_row, new_col), False, "Test move Adventurer next "
                                                                                "room fail failed")

        # test if you can go into the room
        if da.dungeon.get_doors(current_key, new_key, real_direction):
            self.assertEqual(da.dungeon.get_doors(current_key, new_key, real_direction), True, "Test move "
                                                                                               "adventurer door fail")
            self.assertEqual(da.player_loc_row, 1, "Test move Adventurer row failed")
            self.assertEqual(da.player_loc_col, 0, "Test move Adventurer row failed")
        else:
            self.assertEqual(da.dungeon.get_doors(current_key, new_key, real_direction), False, "Test move "
                                                                                        "adventurer door fail failed")

    def test_collect_item_health(self):
        """
        Testing collect health item in room
        """
        # Collect Health potion
        da = DungeonAdventure()
        da.collect_item("H")
        health_potion_count = da.adventurer.__get_health_potion_count__()
        self.assertEqual(health_potion_count, 1, "Test healing count failed")

    def test_collect_item_vision(self):
        """
        Testing collect vision item in room
        """
        # Collect Health potion
        # pit_points = DungeonItemsFactory.create_item("X", 1, 15)
        da = DungeonAdventure()
        da.collect_item("V")
        # self.assertTrue(-15 <= da.item.create_item("X", 1,15).use_item() <= -1,"Testing item pit failed")
        self.assertEqual(da.adventurer.__get_vision_potion_count__(), 1, "Test vision count failed")

    def test_collect_item_pit(self):
        """
        Testing collect pit item in room
        """
        # Collect Health potion
        da = DungeonAdventure()
        da.collect_item("X")
        self.assertTrue(-15 <= da.item.create_item("X", 1,15).use_item() <= -1,"Testing item pit failed")


    def test_collect_item_exit(self):
        """
        Testing collect exit command in room
        """

        da = DungeonAdventure()
        item = da.collect_item("O")
        self.assertEqual("O", item, "Test exit failed")

    def test_collect_item_Multi(self):
        """
        Testing collect multi item in room
        """
        # Collect Health potion
        da = DungeonAdventure()
        da.collect_item("M")
        vision_potion_count = da.adventurer.__get_vision_potion_count__()
        health_potion_count = da.adventurer.__get_health_potion_count__()
        hp = da.adventurer.get_HP()
        self.assertTrue(0 <= health_potion_count <= 1,"Test multi item healing count failed")
        self.assertTrue(0 <= vision_potion_count <= 1, "Test multi item vision count failed")
        self.assertTrue(hp <= 0, "Test multi item pit failed")

    def test_collect_item_A(self):
        """
        Testing collect abstraction item in room
        """
        # Collect Health potion
        da = DungeonAdventure()
        da.collect_item("A")
        pillar_count = da.adventurer.get_pillar()
        self.assertEqual(pillar_count, 1)

    def test_collect_item_P(self):
        """
        Testing collect polymorphism item in room
        """
        # Collect Health potion
        da = DungeonAdventure()
        da.collect_item("P")
        pillar_count = da.adventurer.get_pillar()
        self.assertEqual(pillar_count, 1)

    def test_collect_item_I(self):
        """
        Testing collect inheritance item in room
        """
        # Collect Health potion
        da = DungeonAdventure()
        da.collect_item("I")
        pillar_count = da.adventurer.get_pillar()
        self.assertEqual(pillar_count, 1)

    def test_collect_item_E(self):
        """
        Testing collect encapsulation item in room
        """
        # Collect Health potion
        da = DungeonAdventure()
        da.collect_item("E")
        pillar_count = da.adventurer.get_pillar()
        self.assertEqual(pillar_count, 1)


if __name__ == "__main__":
    unittest.main()
