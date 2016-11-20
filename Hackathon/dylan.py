import Room
import Person

def  buildRooms():

 MainEntrance = Room.Room(["Bat","Picture"],
		[2,6,10,12],
		"Main Entrance",
		"This is the main entrance of the building. In front of you is a grand staircase. There is a door to your left, one to the right, and also a door under the stairs.")
 GrandeLounge = Room.Room([],
		 [1,3],
		 "Grande Lounge",
		 "This is a large social area complete with a wet bar.")
 DiningRoom = Room.Room([],
		 [2,6],
		 "Dining Room",
		 "This is a large dining room complete with a long dinner table set with food.")
 Storage = Room.Room([],
		 [5],
		 "Storage",
		 "Storage pantry with plenty of food.")
 ServantsQuarters = Room.Room([],
		 [4,6],
		 "Servant's Quarters",
		 "A small cot and a few magazines are surrounded by dirty clothes" )
 Kitchen = Room.Room([],
		 [3,5,7,1],
		 "Kitchen",
		 " Large kitchen complete with an island and all appliances.")
 Freezer = Room.Room([],
		 [6],
		 "Freezer",
		 "Walk in freezer. Relatively empty")
 BallRoom = Room.Room([],
		 [6,9],
		 "Ball Room",
		 "Large ball room that has been decorated for some event. There is a stage in the corner, and an open ceiling that looks up to a balcony.")
 Restroom = Room.Room([],
		 [8,10],
		 "Restroom",
		 "Large fancy restroom with marble floors and a couch. Contains two entrances.")
 SideRoom = Room.Room([],
		 [1,9,11],
		 "Side Room",
		 "Large room that has recently been used for storage. There appears to be another small closet in the corner.")
 Nook = Room.Room([],
		 [10],
		 "Nook",
		 "A small closet which contains a large table with physics experiments on top")
 LargeHallway = Room.Room([],
		 [13,14,15,16,17,18],
		 "Large Hallway",
		 "A large hallway at the top of the stairs")
 BallRoomOverLook = Room.Room([],
		 [12,23],
		 "Ball Room OverLook",
		 "An open balcony the looks down on the ballroom")
 GuestBath1 = Room.Room([],
		 [12],
		 "Guest Bath 1",
		 "Small bathroom with a sink and tub")
 GuestBath2 = Room.Room([],
		 [12],
		 "Guest Bath 2",
		 "Small bathroom with a sink and tub")
 GuestRoom1 = Room.Room([],
		 [18],
		 "Guest Room 1",
		 "Guest bedroom one of 4 identical")
 GuestRoom2 = Room.Room([],
		 [18],
		 "Guest Room 2",
		 "Guest bedroom one of 4 identical")
 GuestRoom3 = Room.Room([],
		 [18],
		 "Guest Room 3",
		 "Guest bedroom one of 4 identical")
 GuestRoom4 = Room.Room([],
		 [18],
		 "Guest Room 4",
		 "Guest bedroom one of 4 identical")
 MasterBath = Room.Room([],
		 [17],
		 "Master Bath",
		 "Master Bathroom. Two sinks and a shower with water that falls from the ceiling")
 MasterBedRoom = Room.Room([],
		 [12,16,24],
		 "Master BedRoom",
		 "Master bedroom. King size bed. There appears to be a double door that opens to a balcony")
 Hallway = Room.Room([],
		 [12,19,20,21,22],
		 "Hallway",
		 "Narrow hallway")
 Library = Room.Room([],
		 [13],
		 "Library",
		 "A very interesting library. There are four rows of books, mostly math and science.")
 MasterBalcony = Room.Room(["Dagger" ],
		 [17],
		 "Master Balcony",
		 "A small balcony that overlooks a fountain in the garden")
 Building = Room.Room(description=" A large mansion that holds many secrets")

 roomList = [Building,MainEntrance,GrandeLounge,DiningRoom,Storage,ServantsQuarters,Kitchen,Freezer,BallRoom,Restroom,SideRoom,Nook,LargeHallway,BallRoomOverLook,GuestBath1,GuestBath2,MasterBath,MasterBedRoom,Hallway,GuestRoom1,GuestRoom2,GuestRoom3,GuestRoom4,Library,MasterBalcony]
 return roomList

def buildPeople():
	AlbertEinstein = Person.Person(height=172.2,
			weight=712,
			name="Albert Einstein",
			watch=True,
			glasses=False,
			testimony="Drinking heavily. Off putting and angry about being stuck with here.  In slurring words tells you to leave them alone")
	MarieCurie = Person.Person(160,
			600,
			"Marie Curie",
			False,
			False,
			testimony="Saw the silhouette of a person in the doorway of the dining room but lightning blinded him then the person was gone")
	NielsBohr = Person.Person(182,
			900,
			"Niels Bohr",
			True,
			False,
			testimony="Standing near the right side of the entrance to the dining room. Heard a snap from his right hand side near the book shelf")
	IsaacNewton = Person.Person(158,
			650,
			"Isaac Newton",
			False,
			False,
			testimony="Breathing heavily. Seems nervous or frightened. Heard a scream in the entrance area.")
	StephenHawking = Person.Person(110,
			300,
			"Stephen Hawking",
			True,
			True,
			testimony="Appears oddly untroubled by the murder but does appear flustered by something. Will excuse himself to the kitchen to check on food for his guests so that hopefully it will help calm them")
            
	peopleList = [AlbertEinstein,MarieCurie,NielsBohr,IsaacNewton,StephenHawking]
	
	return peopleList

def printLayout():
 print("First Floor")
 print("          ---------------                 ")
 print("          |    |        |                 ")
 print("          | 4  |   5    |                 ")
 print("          |    |        |                 ")
 print("          |    \        |                 ")
 print("---------------------___------------------   1. Main Entrance")
 print("|         \             |                |   2. Grande Lounge")
 print("|         |             |                |   3. Dining Room")
 print("|         |             |                |   4. Storage")
 print("|         |       6     |                |   5. Servant's Quarters")
 print("|   3     |             \        8       |   6. Kitchen")
 print("|         |--           |-----           |   7. Freezer")
 print("|         |7 |          |    \           |   8. Ball Room")
 print("|         |  |          | 9  |           |   9. Restroom")
 print("|--__-----|---------__--|    |-----------|  10. Side Room")
 print("|         |             |    \           |  11. Nook")
 print("|         |    =====    |----|           |")
 print("|         |     ===     \                |")
 print("|         |     ===     |                |")
 print("|         |             |  10      |-----|")
 print("|         |             |          |     |")
 print("|         |             |          |  11 |")
 print("|  2      |      1      |          |     |")
 print("|         \             |          \     |")
 print("----------------___-----------------------")
 print(" ")
 print("Second Floor")
 print(" ")
 print("----------                                ")
 print("|  24    |                                ")
 print("|   -__----------------------------------------  12. Large Hallway ")
 print("|   |         \     |     |     |             |  13. BallRoom Overlook")
 print("----|   17    | 16  | 15  | 14  |    13       |  14. Guest Bath 1 ")
 print("    |         |-----|---__|---__|             |  15. Guest Bath 2 ")
 print("    |-------__|                               |  16. Master Bath")
 print("    |                    12                   |  17. Master Bedroom")
 print("    -------__------|------====---------__-----|  18. Hallway")
 print("    |     |  |     |      ====     |          |  19. Guest Room 1")
 print("    | 19  |18| 21  |               |          |  20. Guest Room 2")
 print("    |     \  \     |               |          |  21. Guest Room 3")
 print("    |-----|  |-----|               |    23    |  22. Guest Room 4")
 print("    |     \  \     |               |          |  23. Library")
 print("    | 20  |  |  22 |               |          |  24. Master Balcony")
 print("    |     |  |     |               |          |")
 print("    -------------------------------------------")



