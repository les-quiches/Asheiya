import sys
import os
import select
import time
import termios

import tty

#My module
import background
B=background
import entity
E=entity

#interaction clavier
old_settings = termios.tcgetattr(sys.stdin)

#My var
window= None
TimeStep = None
lastTime = {}

#asset
entity_asset = {}
entity_asset["Player"]={}
Ea_p = None # Ea_p = entity_asset["Player"]["position"]

window= None

#entity type
Player = None
Mob = None
Boon = None

Menu = None
#asset Asheiya
#on le metra dans Init
Asheiya_asset=[
"Run_Right_0", "Run_Right_45", "Run_Right_90",  "Run_Right_-45", "Run_Right_-90",
 "Run_Left_0", "Run_Left_45", "Run_Left_90", "Run_Left_-45", "Run_Left_-90",
"Wait_Right_0", "Wait_Right_45", "Wait_Right_90", "Wait_Right_-45", "Wait_Right_-90",
 "Wait_Left_0", "Wait_Left_45", "Wait_Left_90", "Wait_Left_-45", "Wait_Left_-90",
]

#______INIT________________________________________________________________________
def Init():
	global window, TimeStep, lastTime, Menu, Player, entity_asset, Ea_p
	lastTime["dt"] = time.time()
	lastTime["2s"] = time.time()
	Menu = "Quiche"
	TimeStep = 0.05 #seconde (0.05 equivaux a 20 img seconde)
	#asset bg
	window = B.create_wd("Windows.txt")

	B.show_wd(window)
	# interaction clavier
	tty.setcbreak(sys.stdin.fileno())

	#Player
	entity_asset["Player"]["position"] = ["Wait","Right","0"]
	Ea_p = entity_asset["Player"]["position"]
	X_player = 20
	Y_player = 37
	life_player = 18
	armor_player =25
	speed_player = 5
	Player = E.create_entity("Asheiya Briceval", "Player", X_player, Y_player, life_player, armor_player, speed_player)
	for Asheiya_doc in ["Run_Right_0","Wait_Right_0","Run_Left_0","Wait_Left_0"]:# a terme on utilisera "Asheiya_asset" ou un constructeur de txt
		entity_asset["Player"][Asheiya_doc]=E.create_asset("Asheiya/Asset/" + Asheiya_doc + ".txt") #chargement Asset
	entity_asset["Player"]["FramesNb"]=0
	print entity_asset
	#effacer la console
	sys.stdout.write("\033[1;1H")
	sys.stdout.write("\033[2J")
	return()

#______SHOW________________________________________________________________________
def show():
	global window, TimeStep, lastTime, Menu,Player, entity_asset, Ea_p
	#
	#Show Frame
	if time.time() >= lastTime["dt"] + TimeStep:
		B.show_wd(window)
		#if Menu == "Quiche" :
		print Ea_p[0]+"_"+Ea_p[1]+"_"+Ea_p[2]
		E.show_entity(entity_asset["Player"][str(Ea_p[0]+"_"+Ea_p[1]+"_"+Ea_p[2])], Player, 40, 33)
		lastTime["dt"] = time.time()
	#end loop
	if time.time() >= lastTime["2s"] + 2:
		lastTime["2s"]=time.time()
	#
	#restoration couleur
	sys.stdout.write("\033[37m")
	sys.stdout.write("\033[40m")
	#
	#deplacement curseur
	#sys.stdout.write("\033[1;1H\n")
	return

#______INTERACT________________________________________________________________________
def Interact():
	def isData():
		#recuperation evenement clavier
		return select.select([sys.stdin], [], [], 0) == ([sys.stdin], [], [])

	global Menu, Player, Ea_p
	if isData() :
		c = sys.stdin.read(1)
		if c == '\x1b': # \x1b = esp
			quitGame()
		elif c == "l":
			Ea_p=[Ea_p[0],"Right",Ea_p[2]]
		elif c == "j":
			Ea_p=[Ea_p[0],"Left",Ea_p[2]]
	else:
		Ea_p = ["Wait",Ea_p[1],Ea_p[2]]
#_____HIT BOX_________________________________________________________________________
def Hit_box():
	return
#_____MOVE_________________________________________________________________________
def move():
	global Player
	return()

#_____RUN_________________________________________________________________________
def Run():
	Init()
	#Loop
	while True:
		Interact()
		show()
	return()

#____Start___________________________________________________________________________
Run()
quitGame()
#____END___________________________________________________________________________
def quitGame():

	#restoration parametres terminal
	global old_settings

	#couleur white
	sys.stdout.write("\033[37m")
	sys.stdout.write("\033[40m")

	termios.tcsetattr(sys.stdin, termios.TCSADRAIN, old_settings)
	sys.exit()
