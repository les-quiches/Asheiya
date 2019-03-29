import sys
import os
import select
import time
import termios

import tty

#My module
import Background

#interaction clavier
old_settings = termios.tcgetattr(sys.stdin)

#My var
window= None
TimeStep = None
lastTime = None

#entity type
Player = None
Mob = None
Boon = None
#______INIT________________________________________________________________________

def Init():
	global window, TimeStep, lastTime, Player
	lastTime = time.time()
	TimeStep = 0.05 #seconde (0.05 equivaux a 20 img seconde)
	window = Background.create_wd("Windows.txt")

	# interaction clavier
	tty.setcbreak(sys.stdin.fileno())

	#effacer la console
	sys.stdout.write("\033[1;1H")
	sys.stdout.write("\033[2J")
	return()

#______SHOW________________________________________________________________________

def show():
	global window, TimeStep, lastTime
	#Show Frame
	if time.time() >= lastTime + TimeStep:
		Background.show_wd(window)
		print "AHHHHHHH"
		print time.time()
		lastTime = time.time()
	#end loop

	#restoration couleur
	sys.stdout.write("\033[37m")
	sys.stdout.write("\033[40m")

	#deplacement curseur
	sys.stdout.write("\033[1;1H\n")

#______INTERACT________________________________________________________________________
def Interact():
    if isData():
		c = sys.stdin.read(1)
		if c == '\x1b': # \x1b = esp
			quitGame()

def isData():
	#recuperation evenement clavier
	return select.select([sys.stdin], [], [], 0) == ([sys.stdin], [], [])

def quitGame():

	#restoration parametres terminal
	global old_settings

	#couleur white
	sys.stdout.write("\033[37m")
	sys.stdout.write("\033[40m")

	termios.tcsetattr(sys.stdin, termios.TCSADRAIN, old_settings)
	sys.exit()
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
