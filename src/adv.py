import readline

from item import Item
from player import Player
from room import Room

# Declare all the rooms
room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
}

# Link rooms together
room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

# declare all items
item = {
    'item_1': Item('Item_1', 'an item of primary importance'),
    'item_2': Item('Item_2', 'an item of secondary importance')
}

# place all items
room['narrow'].items.append(item['item_1'])
room['foyer'].items.append(item['item_2'])

#
# Main
#

# Make a new player object that is currently in the 'outside' room.

player = Player('Player', room['outside'])

# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.

# initialze variables for procesing input
response = []
verb, obj = '', ''
words = {
    'stop': ['q', 'quit', 'x', 'exit', 'leave', 'done', 'bye'],
    'move': ['n', 'north', 's', 'south', 'e', 'east', 'w', 'west'],
    'get': ['g', 'get', 'take', 'grab'],
    'put': ['p', 'put', 'd', 'drop', 'lose'],
    'inventory': ['i', 'inventory', 'stuff', 'junk'],
    'examine': ['l', 'look', 'describe', 'examine', 'inspect'],
}

while verb.lower() not in words['stop']:
    # describe location
    print()
    print(player.current_room.name)
    print(player.current_room.description)    
    for item in player.current_room.items:
        print(' - ', item.name)
    if len(player.current_room.items) > 0:
        print()

    # get user input
    while True:
        response = input('> ').strip().split()
        try:
            verb = response[0]
            # have input, leave input loop
            break
        except IndexError:
            # no input, retry
            continue
    # parse additional input
    try:
        obj = response[1]
    except IndexError:
        obj = ''

    # process user input
    # movement
    if verb.lower() in words['move']:
        if not player.move(verb.lower()[0]):
            print(f'Unable to move {verb}')

    # get / take
    elif verb.lower() in words['get']:
        if not player.take(obj):
            print(f'Unable to take {obj}')

    # put / drop
    elif verb.lower() in words['put']:
        if not player.drop(obj):
            print(f'Unable to drop {obj}')

    # inventory
    elif verb.lower() in words['inventory']:
        print(player.inventory)

    # examine
    elif verb.lower() in words['examine']:
        found_it = False
        for item in player.items + player.current_room.items:
            if obj.lower() == item.name.lower():
                print(item)
                found_it = True
        if not found_it:
            print('Nothing to see.')

    # unknown
    elif verb.lower() not in words['stop']:
        print('Invalid action.')
