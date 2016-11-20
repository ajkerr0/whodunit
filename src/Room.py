"""

"""

from menu import Option, Menu

class Room(object):
    des = "You are unsure what this room is."
    def __init__(self,itemList=[],roomList=[],name="unknown",description=des):
        self.items = itemList
        self.adjacentRooms = roomList
        self.name = name
        self.description = description
        self.menu = Menu([], "dummy menu")
        
    def listAdjacentRooms(self):
        print("The nearby rooms are: ")
        print(" ")
        for i in range(0,len(self.adjacentRooms)):
            print(self.adjacentRooms[i])
    
    def listItems(self):
        print("After surveying the room you notice a few items out of place: ")
        print(" ")
        for i in range(0,len(self.items)):
            print(self.items[i])
    
    def addItem(self,item):
        self.item.append(str(item))
        
    def display(self):
        self.menu.display()


    

