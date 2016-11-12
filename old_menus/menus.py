# -*- coding: utf-8 -*-
"""
Created on Thu Nov 12 15:27:17 2015

@author: alex
"""

import os
import sys
import importlib

import nm

mainMenuRef = ["create system", "combine systems", "calculate normal modes", "list created systems", "list potentials", "quit"]

def main():
    
    print "Initializing the program..."
    
    mainMenu, createSysMenu, combineSysMenu, calcNMMenu, listSysMenu, listPotMenu = initialize_menus
    
    print "Welcome to KerrNM!"    
    
    mainMenu.display()
    
        
def initialize_menus():
    """Return the initialized menu objects"""
    
    #CREATE SYSTEMS
    createOpList = []
    for key in nm.systemsDic:
        value = nm.systemsDic[key]
        option = nm.Option(key, create_option(value))
        createOpList.append(option)
    createOpList.append(nm.Option("GO BACK", dum))
    createSysMenu = nm.Menu(createOpList, "Which system to create?")
    
    #COMBINE SYSTEMS
    #needs work
    combineSysMenu = nm.Menu(nm.Option("dum", dum), "Unfinished menu...")
    
    #CALCULATE NORMAL MODES
    #needs work
    calcNMMenu = nm.Menu(nm.Option("dum", dum), "Unfinished menu...")
    
    #LIST SYSTEMS
    sysFileNames = os.listdir("../systems")
    sysOpList = []
    for fileName in sysFileNames:
        sysOpList.append(nm.Option(fileName, dum))
    sysOpList.append(nm.Option("GO BACK", dum))
    listSysMenu = nm.Menu(sysOpList, "Here are your created systems, use GO BACK to go back")
    
    #LIST POTENTIALS
    potOpList = []
    for potential in nm.potInitials:
        potOpList.append(nm.Option(potential, dum))
    potOpList.append(nm.Option("GO BACK", dum))
    listPotMenu = nm.Menu(potOpList, "Here are your potentials (force fields), use GO BACK to go back.")
    
    #MAIN
    createSysOp = nm.Option("Create a system", createSysMenu.display)
    combineSysOp = nm.Option("Combine two systems", combineSysMenu.display)
    calcNMOp = nm.Option("Calculate normal modes", calcNMMenu.display)
    listSysOp = nm.Option("List created systems", listSysMenu.display)
    listPotOp = nm.Option("List potentials (force fields)", listPotMenu.display)
    quitOp = nm.Option("QUIT", exit_program)
    mainMenu = nm.Menu([createSysOp, combineSysOp, calcNMOp, listSysOp, listPotOp, quitOp], "What will you do?")
    
    #give GO BACK option
    tier1MenuList = [createSysMenu, combineSysMenu, calcNMMenu, listSysMenu, listPotMenu]
    for menu in tier1MenuList:
        menu.options[-1].function = mainMenu.display
    
    return mainMenu, createSysMenu, combineSysMenu, calcNMMenu, listSysMenu, listPotMenu
    
def create_option(moduleName):
    i = importlib.import_module("create." + moduleName)
    return getattr(i, 'main')
    
def dum():
    print "Follow the instructions"
    pass

def exit_program():
    sys.exit("You've exited KerrNM!")

if __name__ == "__main__":
    main()
