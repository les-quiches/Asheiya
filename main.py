import sys
import os
import select
import time
import termios

import tty

#My module
import background
import entity
import shootingmob
import character

#interaction clavier
oldSettings = termios.tcgetattr(sys.stdin)


#Globals

window= None
timeStep = None
timeIni = None
gameBorder=[]
allEntity= {}

player = None
menu = None





#______INIT________________________________________________________________________

def Init(): 	#initialisation des variables
	global window, timeStep, timeIni, gameBorder, allEntity, player, menu

	asheiyaAsset=[
	"Run_Right_0", "Run_Right_45", "Run_Right_90",  "Run_Right_-45", "Run_Right_-90",
 	"Run_Left_0", "Run_Left_45", "Run_Left_90", "Run_Left_-45", "Run_Left_-90",
	"Wait_Right_0", "Wait_Right_45", "Wait_Right_90", "Wait_Right_-45", "Wait_Right_-90",
 	"Wait_Left_0", "Wait_Left_45", "Wait_Left_90", "Wait_Left_-45", "Wait_Left_-90",
	]

	projectileAsset=[
	"Gun_Horizontal","Gun_Slach","Gun_UnSlash","Gun_Vertical"
	]

	timeStep = 0.01 # en secondes -> 10 images par secondes
	timeIni = time.time()

	allEntity["projectile"]=[] #gere les tirs de Asheiya et des ennemis
	allEntity["mobs"]=[] #gere Asheiya, les boss, et autres mobs
	allEntity["stage"]=[] #gere les bonus, plateforme pieges et autres

	#start menu
	menu="quiche"


	#asset background
	window=background.create_window("Windows.txt")

	#interaction clavier
	tty.setcbreak(sys.stdin.fileno())

	#on concoit le joueur
	xPlayer = 20
	yPlayer = 37
	vxPlayer = 0
	vyPlayer = 0
	lifePlayer = 18
	armorPlayer =25
	speedPlayer = 0.07 #deplaxcement pas seconde
	lastTime = time.time() #moment d'apparition, permettra de gerer l'affichage
	assetPlayer = {}
	assetPlayer["position"]=["Wait","Right",0] #correspond a sa representation : course/attente, orientation, position du bras
	for Asheiya_doc in asheiyaAsset :
		assetPlayer[Asheiya_doc]=entity.create_asset("Asheiya/Asset/" + Asheiya_doc + ".txt") #chargement Asset
	player = entity.create_entity(
		"Asheiya Briceval",
		"player",
		xPlayer,yPlayer,vxPlayer,vyPlayer,lifePlayer,armorPlayer,speedPlayer,lastTime,assetPlayer
		)
	assetShot = {}
	for Shot_doc in ["Gun_Horizontal","Gun_Slash","Gun_UnSlash","Gun_Vertical"] :
		assetShot[Shot_doc] =entity.create_asset("Projectile/"+Shot_doc+".txt")
	shotDelay = 3
	shootingmob.create_shooting_mob(player,assetShot,shotDelay)

	allEntity["mobs"].append(player)
	#definition de la fenetre de jeu
	x=0
	y=0
	xmax=90
	ymax=42
	gameBorder=[x,y,xmax,ymax]

	#on efface la console
	sys.stdout.write("\033[1;1H")
	sys.stdout.write("\033[2J")
	return()


#______Show________________________________________________________________________

def Show() :
	global window, timeStep, timeIni, gameBorder, allEntity, player, menu


	#Show Frame
	background.show_window(window)

	for shot in allEntity["projectile"] :
		asset = shot["Asset"]
		color_bg = 40 #noir
		color_txt = 33 #jaune
		entity.show_entity(asset,shot,color_bg,color_txt)

	for ent in allEntity["mobs"] :
		if ent["Type"]=="player":
			asset =entity.create_asset(character.get_asset_doc(ent))
			color_bg = 40 #noir
			color_txt = 31 #rouge
		else :
			asset = entity.create_asset(ent["Asset"])
			color_bg = 40
			color_txt = 33
		entity.show_entity(asset,ent,color_bg,color_txt)
	timeIni = time.time()

	#restoration couleur
	sys.stdout.write("\033[37m")
	sys.stdout.write("\033[40m")
	#
	#deplacement curseur
	sys.stdout.write("\033[1;1H\n")
	return

#______Time_game________________________________________________________________________


def Time_game(): #va rediriger sur les differentes fonctions selon leurs frequences
	global window, timeStep, timeIni, gameBorder, allEntity, player, menu

	for bullet in allEntity["projectile"] :
		if time.time()>bullet["Speed"]+bullet["LastTime"] :
			bullet = entity.move_entity(bullet,bullet["Vx"],bullet["Vy"])
			#inserer gestion de collision ici qui provient du module entity avec en param allEntity



	for mob in allEntity["mobs"] :
		if (time.time()>mob["Speed"]+mob["LastTime"]) and (mob["Vx"]!=0 or mob["Vy"]!=0) :
			mob = entity.move_entity(mob,mob["Vx"],mob["Vy"])

			#inserer gestion de collision ici qui provient du module entity avec en param allEntity

		if (shootingmob.is_shooting_mob(mob)) :
			if time.time()>mob["shotDelay"]+mob["lastShot"] :
				#on fait tirer si le mob est un mob qui tir
				shootingmob.shoot(mob, len(allEntity["projectile"]))

	if time.time()>player["LastTime"]+player["Speed"]:
		Interact()

	if time.time()>player["LastTime"]+0.3 :
		player = character.switch_stand(player,"Wait")
		#on remet le joueur en position d'attente s'il fait rien

	if time.time()>timeIni+timeStep:
		Show()


#______INTERACT________________________________________________________________________
def Interact():

	def isData():
		#recuperation evenement clavier
		return select.select([sys.stdin], [], [], 0) == ([sys.stdin], [], [])

	global player, menu
	if isData() :
		c = sys.stdin.read(1)

		if c == '\x1b': # \x1b = esc
			Quit_game()

		if c == "l":
			player = character.switch_orientation(player,"Right")
			player = character.switch_stand(player,"Wait")

		elif c == "j":
			player = character.switch_orientation(player,"Left")
			player = character.switch_stand(player,"Wait")

		elif c == "i":
			player = character.switch_fire_angle(player,45)
			player = character.switch_stand(player,"Wait")

		elif c == "k":
			player = character.switch_fire_angle(player,-45)
			player = character.switch_stand(player,"Wait")


		elif c == "d":
			player = character.switch_stand(player,"Run")
			player = entity.move_entity(player,1,0)

		elif c == "q":
			player = character.switch_stand(player,"Run")
			player = entity.move_entity(player,-1,0)

	# 	elif c == "z" and player_move == False and Player["Vy"] == 0:#_________________________Vy______ bug possible multi jump si utilisateur rapuit sur le bouton de saut a l'apoger de sont saut
	# 		Move.Player.stand("Wait")
	# 		Player["Vy"]-=5
	# 		player_move = True
	# 	elif c == "s" and player_move == False:
	# 		Move.Player.stand("Wait")
	# 		player_move = True

	termios.tcflush(sys.stdin.fileno(),termios.TCIFLUSH) #on vide le buffer d'entree





#########Boucle de simulation#########__________________________________________________
def Run():
	Init()
	#Infinite Loop
	while True:
		Time_game()
		#Game()
	return()


#______Quit_Game________________________________________________________________________

def Quit_game():
	#restoration parametres terminal
	global oldSettings

	sys.stdout.write("\033[1;1H")
	sys.stdout.write("\033[2J")

		#couleur white
	sys.stdout.write("\033[37m")
	sys.stdout.write("\033[40m")


	termios.tcsetattr(sys.stdin, termios.TCSADRAIN, oldSettings)

	A = time.time()
	while time.time()<A+1 :
		None
	print "Game exited successfully"

	sys.exit()









#____Jeux de Test________________________________________________________________
if (__name__=="__main__"):
	Run()
