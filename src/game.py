# -*- coding: utf-8 -*-

"""

The start up script.

@author: Alex
"""

import sys

from story import Story
from menu import Option, Menu
import build

TITLE = "WHODUNIT"
ROOMS = build.buildRooms()
PERSONS = build.buildPeople()
ITEMS = build.buildItems()

story = Story(ROOMS, PERSONS, ITEMS)

def main():
    """Main program execution."""
    
    story.prologue()
    
    main_menu = Menu([Option("Start", start), Option("Quit", exit_program)], TITLE)
    
    main_menu.display()
    
def start():
    
    story.start()
    ROOMS[2].menu.display()

def exit_program():
    sys.exit("You've exited {}!".format(TITLE))
    
if __name__ == "__main__":
    main()

