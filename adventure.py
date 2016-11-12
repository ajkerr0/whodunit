"""


@author: Alex Kerr
"""

class Room:
    """A location in the game world.
    
    Arguments:
        name (str): Unique name of the room.
        msg (str): The message that appears to the player when he enters the room."""
    
    def __init__(self, name, msg):
        self.name = name
        self.msg = msg
        self.items = []
        
    def print_(self):
        print(self.msg)
        
class Item:
    """An item in the game.
    
    Arguments:
        name (str): Name of the item.
        desc (str): Descripton of the item available to the player."""
        
    def __init__(self, name, desc):
        self.name = name
        self.desc = desc

        