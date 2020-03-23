class Engine(object):
    def __init__(self, room_map):
        self.room_map = room_map

    def play(self):
        current_room = self.room_map.opening_room()
        last_room = self.room_map.next_room('finished')

        while current_room != last_room:
            next_room_name = current_room.event()
            current_room = self.room_map.next_room(next_room_name)

        current_room.event()
