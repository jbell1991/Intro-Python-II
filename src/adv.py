from room import Room
from item import Item
from player import Player
import textwrap

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

room['outside'].move["n"] = room['foyer']
room['foyer'].move["s"] = room['outside']
room['foyer'].move["n"] = room['overlook']
room['foyer'].move["e"] = room['narrow']
room['overlook'].move["s"] = room['foyer']
room['narrow'].move["w"] = room['foyer']
room['narrow'].move["n"] = room['treasure']
room['treasure'].move["s"] = room['narrow']

#
# Main
#

# Make a new player object that is currently in the 'outside' room.
new_player = Player("Joe", room['outside'])

# Make item objects 
bow = Item("Bow", "A longbow made from a yew tree.")
arrows = Item("Arrows", "Put these in your quiver.")

# Assign items to a room
room['foyer'].assign_item(bow)
room['overlook'].assign_item(arrows)

# Welcome message
print("Welcome to the Adventure Game!")
print("Please choose a direction to move.")

game_running = True

# Write a loop that:
while game_running:
    # * Prints the current room name
    print("Current room:", new_player.current_room.name)
    # * Prints the current description (the textwrap module might be useful here).
    print("Description:", new_player.current_room.description)
    # * Waits for user input and decides what to do.
    # Print Item
    for item in new_player.current_room.items:
        print("Found Item:", item.name, item.description)
    print("Current Inventory", new_player.inventory)
    user = input("""[n] north [s] south [e] east [w] west 
    [p] pickup [d] drop [q] quit\n""")
    # If the user enters a cardinal direction, attempt to move to the room there.
    if user in ["n", "s", "e", "w"]:
        new_player.move(user)
    elif user == "q":
        print("Game Over!")
        break
    elif user == "p":
        new_player.pickup_item(item)
    elif user == "d":
        new_player.drop_item(item)
    else:
        print("Not a valid input!")
