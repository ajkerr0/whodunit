"""


@author: Alex Kerr
"""

class Option:
    """An object that has a printed name and a function associated with it."""
    
    def __init__(self, name, function):
        self.name = name
        self.function = function
        
    def do(self, *args):
        self.function(*args)
            
class Menu:
    """A collection of options that can be displayed."""
    
    def __init__(self, optionsList, message):
        self.options = optionsList
        self.message = message
        
    def display(self):
        ans = True
        while ans:
            print self.message
            for counter, option in enumerate(self.options):
                print str(counter+1) + ": " + option.name
            try:
                ans = int(raw_input(prompt))
            except ValueError:
                print "Please input an integer"
                continue
            for counter, option in enumerate(self.options):
                if ans == counter+1:
                    option.function()
                else:
                    pass
            print "Try again"
            self.display()