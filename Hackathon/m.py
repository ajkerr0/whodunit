
















def hallway():
	print "You enter the main hallway."
	print "There are three rooms, A closet to your left, a dining room to your right, and a living room ahead."
	move = raw_input("Where would you like to go? (1,2,3)")
	if (move=="1"):
		frontCloset()

def frontCloset():
	print "You open the closet"
	move = raw_input("Leave ? ")




hallway()
