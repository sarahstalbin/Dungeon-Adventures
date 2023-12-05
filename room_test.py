from room import Room


def test_room():
    """ method to test the room class"""
    r = Room()
    r.set_north_door()
    r.set_south_door()
    r.set_east_door()
    r.set_polymorphism_pillar()
    print(r)
    r = Room()
    r.set_east_door()
    r.set_south_door()
    r.set_west_door()
    r.set_entrance()
    print(r)


test_room()
