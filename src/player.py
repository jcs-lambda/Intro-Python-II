# Write a class to hold player information, e.g. what room they are in
# currently.

from room import Room
from item import Item

class Player(object):
    def __init__(self, name:str, room:Room):
        self.name = name.strip()
        self.current_room = room
        self.items:[Item] = []

    def move(self, direction:str):
        try:
            self.current_room = getattr(self.current_room, f'{direction}_to')
            return True
        except AttributeError:
            # no room in that direction
            return False

    def take(self, obj:str):
        for item in self.current_room.items:
            if obj.lower() == item.name.lower():
                self.current_room.remove_item(item)
                self.items.append(item)
                item.on_take()
                return True
        return False
    
    def drop(self, obj:str):
        for item in self.items:
            if obj.lower() == item.name.lower():
                self.items.remove(item)
                self.current_room.add_item(item)
                item.on_drop()
                return True
        return False

    @property
    def inventory(self):
        message = ['You are carrying:'] + \
            [f' - {item.name}' for item in self.items]
        return '\n'.join(message)