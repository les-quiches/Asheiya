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
import AI
#interaction clavier
old_settings = termios.tcgetattr(sys.stdin)

#My var
window= None
TimeStep = None
lastTime = {}
player_move =False
game_border=[]
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
Projectile_Asset=[
"Gun_Horizontal","Gun_Slach","Gun_UnSlash","Gun_Vertical"
]

#______INIT________________________________________________________________________
def Init():
	global window, TimeStep, lastTime, Menu, Player, entity_asset, Ea_p, game_border, Entity
#time
	TimeStep = 0.05 #seconde (0.05 equivaux a 20 img seconde)

	lastTime["dt"] = time.time()
	lastTime["2s"] = time.time()
	lastTime["Player"] = time.time()

	#start menu
	Menu = "Quiche"

	#asset bg
	window = B.create_wd("Windows.txt")

	B.show_wd(window)
	# interaction clavier
	tty.setcbreak(sys.stdin.fileno())

	#Player
	entity_asset["Player"]["position"] = ["Wait","Right",0]
	Ea_p = entity_asset["Player"]["position"]
	X_player = 20
	Y_player = 37
	Vx_player = 0
	Vy_player = 0
	life_player = 18
	armor_player =25
	speed_player = 0.1 #deplaxcement pas seconde
	Player = E.create_entity("Asheiya Briceval", "Player", X_player, Y_player,Vy_player,Vy_player, life_player, armor_player, speed_player)
	for Asheiya_doc in ["Run_Right_0","Wait_Right_0","Run_Left_0","Wait_Left_0","Run_Right_45","Wait_Right_45"]:# a terme on utilisera "Asheiya_asset" ou un constructeur de txt
		entity_asset["Player"][Asheiya_doc]=E.create_asset("Asheiya/Asset/" + Asheiya_doc + ".txt") #chargement Asset
	print entity_asset

	#Projectile
	for Projectile_doc in ["Gun_Horizontal","Gun_Slach","Gun_UnSlash","Gun_Vertical"]:
		entity_asset["Projectile"][Projectile_doc]=E.create_asset("Projectile" + Projectile_doc + ".txt")

	#windows
	x=0
	y=0
	xmax=90
	ymax=42
	game_border=[x,y,xmax,ymax]
	#effacer la console
	sys.stdout.write("\033[1;1H")
	sys.stdout.write("\033[2J")
	return()

def Time_game():
	global TimeStep, lastTime, player_move, entity_asset, Ea_p,Entity
	if time.time() >= lastTime["dt"] + TimeStep:
		Show()
	if time.time() >= lastTime["2s"] + 2:
		lastTime["2s"]=time.time()
	if time.time() >= lastTime["Gun"]:
		#X_projectile, Y_projectile,Vx_projectile = truc chian a faire pour determiner ou est l'arme pour faire partir le projectile depuit l'arme
		Entity["Projectile"]["Player"]=E.create_entity("", "Projectile", X_projectile, Y_projectile,Vx_projectile,Vy_projectile=0, life_projectile=1, armor_projectile=0, speed_projectile=0.1)
	if time.time() >= lastTime["Player"] + Player["Speed"]:
		player_move = False
		lastTime["Player"]=time.time()

def Windows():
    #sa sera des fonction pour afficher dans les fenetres a droite (le texte)
def Randoms_Entity():
	global Entity
    #creation entity de facon aleatoire genre les pics qui tombe du plafon ou montre random et des fonctoin autour de l'allea et des entiter
#______SHOW________________________________________________________________________
def Show():
	global window, TimeStep, lastTime, Menu, Player, entity_asset, Ea_p

	#Show Frame
	B.show_wd(window)
	print Ea_p[0]+"_"+Ea_p[1]+"_"+str(Ea_p[2])#--------------------------------------------------------------print
	E.show_entity(entity_asset["Player"][str(Ea_p[0]+"_"+Ea_p[1]+"_"+str(Ea_p[2]))], Player, 40, 33)
	lastTime["dt"] = time.time()

	#restoration couleur
	sys.stdout.write("\033[37m")
	sys.stdout.write("\033[40m")
	#
	#deplacement curseur
	sys.stdout.write("\033[1;1H\n")
	return

#______INTERACT________________________________________________________________________
def Interact():
	def isData():
		#recuperation evenement clavier
		return select.select([sys.stdin], [], [], 0) == ([sys.stdin], [], [])

	global Menu, Player, Ea_p, player_move
	if isData() :
		c = sys.stdin.read(1)
		if c == '\x1b': # \x1b = esp
			quitGame()
		if c == "l":
			Ea_p=[Ea_p[0],"Right",Ea_p[2]]
		elif c == "j":
			Ea_p=[Ea_p[0],"Left",Ea_p[2]]
		elif c == "i" and Ea_p[2] != +90:
			Ea_p=[Ea_p[0],Ea_p[1],Ea_p[2]+45]
		elif c == "k" and Ea_p[2] != -90:
			Ea_p=[Ea_p[0],Ea_p[1],Ea_p[2]-45]
		if c == "d" and player_move == False:
			Ea_p=["Run",Ea_p[1],Ea_p[2]]
			Player["x"]+=1
			player_move = True
		elif c == "q" and player_move == False:
			Ea_p=["Run",Ea_p[1],Ea_p[2]]
			Player["x"]+=(-1)
			player_move = True
		elif c == "z" and player_move == False and Player["Vy"] == 0:#_________________________Vy______ bug possible multi jump si utilisateur rapuit sur le bouton de saut a l'apoger de sont saut
			Ea_p=["Wait",Ea_p[1],Ea_p[2]]
			Player["Vy"]+=25
			player_move = True
		elif c == "s" and player_move == False:
			player_move = True
	else:
		if player_move == False:
			Ea_p=["Wait",Ea_p[1],Ea_p[2]]

#_____MOVE_________________________________________________________________________
def Move():
	global Player,Entity, game_border,entity_asset, Ea_p
	#_____HIT BOX__________________________________________________________________
	def hit_box_simple(asset,entity):
		y=len(asset)
		a=0
		for i in asset:
			a+=len(asset[i])
		x= a/(i+1)
		hit_box_entity=[entity["x"],entity["x"]+x,entity["y"], entity["x"]+y]# plage de l'hitbox de l'asset
		return(hit_box_entity)

	return()

#_____RUN_________________________________________________________________________
def Run():
	Init()
	#Loop
	while True:
		Interact()
		Time_game()
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
