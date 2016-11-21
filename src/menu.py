"""


@author: Alex Kerr
"""

bar = "X"*50

class Option:
    """An option in a menu.
    
    Arguments:
        name (str): The name of the menus; string that is displayed in the menu.
        function (function): The function that is called when the option is selected."""
        
    def __init__(self, name, function):
        self.name = name
        self.function = function
        
    def do(self, *args):
        self.function(*args)

class Menu:
    """A collection of options that can be displayed, one of which can be chosen.
    
    Arguments:
        options (list): List of option objects that are the choices in the menu.
        message (str): String that is displayed above the options."""
    
    def __init__(self, options, message):
        self.options = options
        self.message = message
        
    def display(self):
        ans = True
        while ans:
            print(bar)
            print(self.message)
            for counter, option in enumerate(self.options):
                print(str(counter+1) + ": " + option.name)
            print(bar)
            try:
#                try: 
#                    input = raw_input
#                except NameError: 
#                    pass
                ans = int(input("What will you do?  "))
            except ValueError:
                print("Please input an integer")
                continue
            for counter, option in enumerate(self.options):
                if ans == counter+1:
                    option.function()
                else:
                    pass
#            print("Try again")
            self.display()
        
class Item:
    """An item in the game.
    
    Arguments:
        name (str): Name of the item.
        desc (str): Descripton of the item available to the player."""
        
    def __init__(self, name, desc):
        self.name = name
        self.desc = desc


        