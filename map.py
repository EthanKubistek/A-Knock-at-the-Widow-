
import rooms



class Map(object):

    room_names = {
        'intro': rooms.Introduction(),
        'bedroom': rooms.bedroom(),
        'bathroom': rooms.bathroom(),
        'kitchen': rooms.kitchen(),
        'office': rooms.office(),
        'basement': rooms.basement(),
        'living_room': rooms.living_room(),
        'death': rooms.Death(),
        'win': rooms.Win()
        }

    def __init__(self, start_room):
        self.start_room = start_room
    def next_room(self, room_name):
        val = Map.room_names.get(room_name)
        return val
    def opening_room(self):
        return self.next_room(self.start_room)
