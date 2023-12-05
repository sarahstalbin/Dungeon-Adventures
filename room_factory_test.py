import random
from room_factory import RoomFactory, has_healing_potion, has_vision_potion, has_pit


def test_room_factory():
    """ this method tests Room and RoomFactory class """
    room = RoomFactory.create_room(has_healing_potion, has_vision_potion, has_pit)
    room.set_north_door()
    room.set_east_door()
    room.set_empty_room()
    print(room)
    room = RoomFactory.create_room(has_healing_potion, has_vision_potion, has_pit)
    room.set_south_door()
    room.set_north_door()
    room.set_exit()
    print(room)


test_room_factory()
