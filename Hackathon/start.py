# -*- coding: utf-8 -*-

"""

The start up script.

@author: Alex
"""

import sys

from story import Story
from menu import Option, Menu

TITLE = "Jerky McJerk Game"
HOST = "Muh ***REMOVED***"
FRIEND1 = "Rick Sanchez"
GLMV = "Jerry Smith"

story = Story(HOST, FRIEND1, GLMV)

def exit_program():
    sys.exit("You've exited {}!".format(TITLE))

story.prologue()
#first menu
main_menu = Menu([Option("Start", story.start), Option("Quit", exit_program)], "Jerky McJerk Game")

main_menu.display()

