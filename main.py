import sys
import os
import select
import time
import termios

import pdb

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
gameBorder=[]
walls=None #-afair : grille representant le jeu

timeStep = None
timeIni = None
timeGravity = None

allEntity= {}

color={}

player = None
menu = None
manche = None #permet de gerer la manche et si c'est la premiere boucle de la manche




#______INIT________________________________________________________________________

def Init(): 	#initialisation des variables
	global color, window, assetGameZone, timeStep, timeIni, timeGravity, gameBorder, allEntity, player, menu, manche

	color["txt"]={"Black":30, "Red":31,"Green":32,"Yellow":33,"Blue":34,"Pink":35,"Cyan":36,"White":37}
	color["background"]={"Black":40, "Red":41,"Green":42,"Yellow":43,"Blue":44,"Pink":45,"Cyan":46,"White":47}

	asheiyaAsset=[
	"Run_Right_0", "Run_Right_45", "Run_Right_90",  "Run_Right_-45", "Run_Right_-90",
 	"Run_Left_0", "Run_Left_45", "Run_Left_90", "Run_Left_-45", "Run_Left_-90",
	"Wait_Right_0", "Wait_Right_45", "Wait_Right_90", "Wait_Right_-45", "Wait_Right_-90",
 	"Wait_Left_0", "Wait_Left_45", "Wait_Left_90", "Wait_Left_-45", "Wait_Left_-90",
	]

	gameZone=[
	"Zone_1",
	]
	projectileAsset=[
	"Gun_Horizontal","Gun_Slach","Gun_UnSlash","Gun_Vertical"
	]

	timeStep = 0.01 # en secondes -> 100 images par secondes
	timeIni = time.time()
	timeGravity = time.time()

	allEntity["projectile"]=[] #gere les tirs de Asheiya et des ennemis
	allEntity["mobs"]=[] #gere Asheiya, les boss, et autres mobs
	allEntity["stage"]=[] #gere les bonus, plateforme pieges et autres

	#start menu
	menu="startMenu"
	manche = 10 #1 pour premiere manche, 0 pour le nb de fois qu'on est passe dans la boucle


	#asset background
	window=background.create_window("Windows.txt")
	assetGameZone={}
	for GameZone_doc in gameZone :
		assetGameZone[GameZone_doc]=background.create_window("GameZone/" + GameZone_doc + ".txt")
	assetGameZone["NumZone"]=1
	#interaction clavier
	tty.setcbreak(sys.stdin.fileno())

	#on concoit le joueur
	xPlayer = 0
	yPlayer = 0
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
	player = shootingmob.create_shooting_mob(player,assetShot,shotDelay)

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
	return



def Init_manche(): #pour initialiser chaque manche
	#-afaire
	global manche, menu, player, walls

	if manche == 10 :
		player = entity.tp_entity(player,20,37)
		# walls =  -afair
		manche = 11

	return


#______Game________________________________________________________________________
def Game(): #gere les evennements du jeu, definit le contexte
	global menu, player, manche, allEntity
	if menu=="startMenu" :
		#animation de demarage + elements loristiques et tout
		menu = "menuManche1" #a integrer dans la derniere fonction qui sera appele par startMenu -afair
	if menu == "menuManche1" and manche == 10 :
		Init_manche()

	#gestion des fins de manches
	if not(entity.is_alive(player)):
		None
		# -afair

	#gestion des cadavres
	for mob in allEntity["mobs"] :
		if not(entity.is_alive(mob)):
			None
			# on le fait disparaitre du jeu -afair
	for bullet in allEntity["projectile"]:
		if not(entity.is_alive(bullet)):
			None
			# on le fait disparaitre du jeu -afair

	return



#______Time_game________________________________________________________________________
def Time_game(): #va rediriger sur les differentes fonctions selon leurs frequences
	global window, timeStep, timeIni, gameBorder,walls, allEntity, player, menu, timeGravity

	for bullet in allEntity["projectile"] :
		if time.time()>bullet["Speed"]+bullet["LastTime"] :
			bullet = entity.move_entity(bullet,bullet["Vx"],bullet["Vy"])
			log = shootingmob.hit(bullet,allEntity["mobs"],gameBorder,walls) #- afair walls est le tableau representant la map
			if log[1]:#une entite a etait touche
				None #blesser la dite entite
			if log[0]:#il y a eu collision
				None #detruire la balle
			#inserer gestion de collision ici qui provient du module entity avec en param allEntity - afair

	#gestion de la gravite
	if time.time()>timeGravity + 0.08 :
		for mob in allEntity["mobs"] :
			onTheGround = entity.is_ground_beneath(entity.feet(mob),gameBorder,walls) #-afair test s'il y a une plateforme en dessous
			mob = entity.gravity(mob,onTheGround)
			entity.move_entity(mob,0,1,onTheGround,True)
		timeGravity = time.time()

	for mob in allEntity["mobs"] :
		if (time.time()>mob["Speed"]+mob["LastTime"]) and (mob["Vx"]!=0 or mob["Vy"]!=0) :
			#inserer gestion de collision ici qui provient du module entity avec en param allEntity - afair
			#va etre la collision la plus complique a gerer  celle avec les entites et avec les walls -afair
			willCollide = entity.collision(mob,allEntity["mobs"],gameBorder,walls) # -afair
			mob = entity.move_entity(mob,mob["Vx"],mob["Vy"],willCollide)


		if (shootingmob.is_shooting_mob(mob)) :
			if time.time()>mob["shotDelay"]+mob["lastShot"] :
				#on fait tirer si le mob est un mob qui tir
				shootingmob.shoot(mob, len(allEntity["projectile"]))


	#on gere les deplacements du joueur
	if time.time()>player["LastTime"]+player["Speed"]:
		Interact()

	if time.time()>player["LastTime"]+0.03 :
		player = character.switch_stand(player,"Wait")
		#on remet le joueur en position d'attente s'il fait rien

	if time.time()>timeIni+timeStep:
		# gestion de la gravite, rajouter dans Entity dans MoveX/MoveY ? - afaire
		Show()


#______Show________________________________________________________________________

def Show() :
	global window, timeStep, timeIni, gameBorder, allEntity, player, menu, assetGameZone, color


	#Show Frame
	background.show_pos(assetGameZone["Zone_"+str(assetGameZone["NumZone"])],0,0,color["background"]["Black"],color["txt"]["White"])
	for shot in allEntity["projectile"] :
		asset = shot["Asset"]
		color_bg = color["background"]["Black"]#noir
		color_txt = color["txt"]["Red"] #rouge
		entity.show_entity(asset,shot,color_bg,color_txt)

	for ent in allEntity["mobs"] :
		if ent["Type"]=="player":
			asset = character.get_asset(player)
			color_bg = color["background"]["Black"] #noir
			color_txt = color["txt"]["Yellow"]#jaune
		else :
			asset = entity.create_asset(ent["Asset"])
			color_bg = color["background"]["Black"]
			color_txt = color["txt"]["Yellow"]
		entity.show_entity(asset,ent,color_bg,color_txt)
	timeIni = time.time()

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

	global player, menu, manche

	if isData() :
		c = sys.stdin.read(1)

		if c == '\x1b': # \x1b = esc
			Quit_game()

		if (manche%10) == 1 : #on est en jeu
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


			# /!\ dans toute cette zone, gerer les collisions avant les deplacements avec entity.collide -afair
			elif c == "d":
				player = character.switch_stand(player,"Run")
				player = entity.move_entity(player,1,0)

			elif c == "q":
				player = character.switch_stand(player,"Run")
				player = entity.move_entity(player,-1,0)

			elif c == "z" and player["Jump"]==0 :
				player = character.switch_stand(player, "Wait")
				player = entity.jump(player)
				player["Vy"]=-1

		# 	elif c == "s" and player_move == False:
		# 		Move.Player.stand("Wait")
		# 		player_move = True
		# -afaire on fait descendre de la plateforme si c'est sur une plateforme

	termios.tcflush(sys.stdin.fileno(),termios.TCIFLUSH) #on vide le buffer d'entree






#########Boucle de simulation#########__________________________________________________
def Run():
	Init()
	#Infinite Loop
	while True:
		Game()
		Time_game()
	return




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

	# -afaire : supprimer les fichiers compiler?

	sys.exit()









#____Jeux de Test________________________________________________________________
if (__name__=="__main__"):
	Run()
