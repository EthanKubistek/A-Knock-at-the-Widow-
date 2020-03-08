
#map is going to give a dict of all the rooms
from textwrap import dedent
import rooms


class Map(object):



    room_names = {
    'bedroom': rooms.bedroom(),
    'bathroom': rooms.bathroom(),
    'kitchen': rooms.kitchen(),
    'office': rooms.office(),
    'basement': rooms.basement(),
    'living_room': rooms.living_room()
    }


    def room (self):

        room = input()
        Map.room_names.get(room).event()
