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
window= None

#entity type
Player = None
Mob = None
Boon = None

Menu = None


#______INIT________________________________________________________________________
def Init():
	global window, TimeStep, lastTime, Menu, Player, entity_asset
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
	X_player = 20
	Y_player = 37
	life_player = 18
	armor_player =25
	speed_player = 5
	Player = E.create_entity("Asheiya Briceval", "Player", X_player, Y_player, life_player, armor_player, speed_player)
	entity_asset["Player"] = E.create_asset("Player.txt")

	#effacer la console
	sys.stdout.write("\033[1;1H")
	sys.stdout.write("\033[2J")
	return()

#______SHOW________________________________________________________________________
def show():
	global window, TimeStep, lastTime, Menu,Player, entity_asset
	#
	#Show Frame
	if time.time() >= lastTime["dt"] + TimeStep:
		B.show_wd(window)
		#if Menu == "Quiche" :
		E.show_entity(entity_asset["Player"],Player, 40, 33)
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
	global Menu, Player
	if isData() :
		c = sys.stdin.read(1)
		if c == '\x1b': # \x1b = esp
			quitGame()

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
