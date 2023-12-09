from DungeonAdventure import DungeonAdventure

class Play_DungeonAdventure:
    play_game = DungeonAdventure()
    play_game.print_introduction()
    play_game.set_play_mode()
    # print(play_game.menu_str())
    play_game.set_up_player()
    play_game.get_input_player()
    play_game.player_results()
    play_game.print_end()
