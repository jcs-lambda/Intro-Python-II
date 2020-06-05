# Implement a class to hold room information. This should have name and
# description attributes.

from item import Item

class Room(object):
    def __init__(self, name:str, description:str):
        self.name = name.strip()
        self.description = description.strip()
        self.items:[Item] = []

    def add_item(self, item:Item):
        try:
            self.items.append(item)
            return True
        except:
            return False

    def remove_item(self, item:Item):
        try:
            self.items.remove(item)
            return True
        except ValueError:
            return False
