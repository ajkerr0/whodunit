# -*- coding: utf-8 -*-
"""

"""
import random
import sys

from build import Menu, Option

class Story:
    """The story structure of the game.
    
    Arguments:
        persons (list): List of Person objects that are characters in the game.  This list is shuffled when the story is instantiated.
        
    Parameters:
        persons: Now shuffled, each index corresponds to a story role:
            0): Mansion host
            1): Friend 1
            2): Grand Louge Murder Victim
            etc...
            
        We have to change this if we want the possibility of characters 'double dipping' their roles, i.e the host can also be the killer sometimes, etc."""
    
    def __init__(self, rooms, persons, items):
        random.shuffle(persons)
        self.persons = persons
        #assign roles
        self.host = self.persons[0]
        self.friend1 = self.persons[1]
        self.glmv = self.persons[2]  # grand lounge murder victim
        self.killer_index = 3
        self.killer = self.persons[self.killer_index]
        #assign rooms
        self.rooms = rooms
        self.kitchen = self.rooms[6]
        self.main_entrance = self.rooms[1]
        self.kitchen.event_func = self.kitchen_scene
        self.kitchen.event = True
        
    def name(self, index):
        return self.persons[index].name
        
    def prologue(self):
        print("You, a lowly graduate student, have been invited to the annual Physics Social at Minkowski Manor. \
        The social is regularly frequented by some of the largest names in physics and astronomy.  \
        Minkowski Manor is a large two story mansion with a basement.  A heavy storm is brewing and in fact a downpour has already begun.  \
        However, the Physics Social is one of the largest events of the year and the host {0} regularly brags about the safety of the residence.\n \
        Upon entering you shed your rain soaked coat and are quickly greeted by {1} and Werner Heisenberg.  \
        They offer you a drink and you move into the Grand Lounge with your two comrades. \
        The ***REMOVED***hts festivities begin but you have a feeling to***REMOVED***ht's Physics Social will be very different from any other..."\
        .format(self.host.name, self.friend1.name))
        
    def start(self):
        print("You have drunk {0} drinks and are swaying to the soft music playing in the background.  \
        The guests have all taken it upon themselves to move freely about the manor nosing their way through the host’s possessions.\
        You lean in to tell Heisenberg a dirty joke when lightning strikes just outside the Dining Room window shaking the whole house with the deafening thunder.\
        The power goes out and several screams are heard throughout the house along with various other noises you can't identify.\n \
        You assume that some people must have fallen when the power went out. \
        The power comes back on and everyone in the Grand Lounge is shocked to see {1} lying on the floor motionless with a small arrow in their back. \
        You are stunned and the {2} quickly yells to the butler to call for an ambulance and the police for a murder has occurred.  \
        {3} starts to tell everyone to remain calm as panic slowly starts to creep in among the party guests. \n \
        Just as everyone starts to calm down, to the extent they are capable of anyways after all a murder had just happened right in front of them, \
        the butler returns to relay the news that the phones are down.  \
        The valet then drives the final nail in the coffin by telling everyone in the Grand Lounge that the road to the manor has been blocked by trees \
        and that the small bridge has collapsed due to the raging waters caused by the downpour. \n \
        Slowly the eerie truth that they are stuck in the mansion at least until morning starts to sink into the minds of the party goers including yourself. \
        After finishing the rest of your drink, you decide that you will use the knowledge you have obtained so far in \
        your physics career to solve this murder so that no one else comes to harm.\n"\
        .format(random.randint(1,10), self.glmv.name, self.host.name, self.host.name))
        
    def kitchen_scene(self):
        print("As you walk into the kitchen you notice a bullet hole on the western wall!  \
        You deduce that the perpetrator must be {} cm tall.".format(self.killer.height))
        self.kitchen.event = False
        self.main_entrance.event_func = self.entrance_scene
        self.main_entrance.event = True
        
    def entrance_scene(self):
        print("Everyone has gathered in the mansion entrance.  It's time for you to identify the killer!")
        win_options = [Option("{0} at {1}".format(person.name, person.height), lose_screen) for person in self.persons]
        win_options[self.killer_index].function = win_screen
        random.shuffle(win_options)
        win_menu = Menu(win_options, "Who is the killer?")
        win_menu.display()
        
def win_screen():
    sys.exit("You've won! :D")
    
def lose_screen():
    sys.exit("You've lost! :O")
    
        
    