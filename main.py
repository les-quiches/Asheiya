#-*- coding:utf-8 -*

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
import shootingent
import movingent
import livingent
import character
import boon
import files

#importation des IAs
import AI

#interaction clavier
oldSettings = termios.tcgetattr(sys.stdin)


#Globals

window= None #contete du jeu manche/menu
walls=None
allAssetGameZone = None
acutalAssetGameZone = None


timeStep = None
timeScreen = None
timeGravity = None

allEntity= {}

color={}

player = None
menu = None
manche = None #permet de gerer la manche et si c'est la premiere boucle de la manche




#______INIT________________________________________________________________________

def Init(): 	#initialisation des variables
	"""
    G{classtree}
    DESCRIPTION
    ===========
        Initialise les variables globales et la fenetre de jeu.

    PARAM
    =====
    	Sans parametre

    RETOUR
    ======
    	Sans retour
	"""
	global color, window, allAssetGameZone, timeStep, timeScreen, timeGravity, allEntity, player, menu, manche

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

	timeStep = 0.05 # en secondes -> 100 images par secondes
	timeScreen = time.time()
	timeGravity = time.time()

	allEntity["projectile"]=[] #gere les tirs de Asheiya et des ennemis
	allEntity["mobs"]=[] #gere Asheiya, les boss, et autres mobs avec des points de vies, qui se déplacent
	allEntity["stage"]=[] #gere les plateforme pieges et autres
	allEntity["boons"]=[] #gère les bonus et générateurs de bonus

	#start menu
	menu="start"
	manche = 10 #1 pour premiere manche, 0 pour le nb de fois qu'on est passe dans la boucle


	#asset background
	window=background.create_window("Windows.txt")
	allAssetGameZone={}
	for GameZone_doc in gameZone :
		allAssetGameZone[GameZone_doc]=background.create_window("GameZone/" + GameZone_doc + ".txt")
	allAssetGameZone["NumZone"]=1
	#interaction clavier
	tty.setcbreak(sys.stdin.fileno())

	#on concoit le joueur
	xPlayer = 0
	yPlayer = 0
	assetPlayer = {}
	assetPlayer["position"]=["Wait","Right",0] #correspond a sa representation : course/attente, orientation, position du bras
	for Asheiya_doc in asheiyaAsset :
		assetPlayer[Asheiya_doc]=entity.create_asset("Asheiya/Asset/" + Asheiya_doc + ".txt") #chargement Asset

	player = entity.create_entity("Asheiya Briceval",xPlayer,yPlayer,assetPlayer)

	vxPlayer = 0
	vyPlayer = 0
	speedPlayer = 0.07 #deplaxcement pas seconde
	player = movingent.create_moving_ent(player,vxPlayer,vyPlayer,speedPlayer)

	lifePlayer = 18
	armorPlayer =25
	player = livingent.create_living_ent(player,lifePlayer,armorPlayer)

	damage = 5
	assetShot = {}
	for Shot_doc in ["Gun_Horizontal","Gun_Slash","Gun_UnSlash","Gun_Vertical"] :
		assetShot[Shot_doc] =entity.create_asset("Asheiya/Projectile/"+Shot_doc+".txt")
	shotDelay = 3
	bulletSpeed = 0.05

	player = shootingent.create_shooting_ent(player,damage,bulletSpeed,assetShot,shotDelay)

	spowerSpeed = 1 #toutes les secondes on augmente de 1 la charge du super

	player = character.create_character(player , spowerSpeed)

	allEntity["mobs"].append(player)


	#definition de la fenetre de jeu

	#on efface la console
	sys.stdout.write("\033[1;1H")
	sys.stdout.write("\033[2J")
	return



def Init_manche():
	"""
    G{classtree}
    DESCRIPTION
    ===========
        Initialise chaque manche : placement du joueur, environnement, bonus, ennemies.

    PARAM
    =====
		Sans parametre

    RETOUR
    ======
	    Sans retour
	"""
	#-afaire
	global manche, menu, player, walls, allAssetGameZone, acutalAssetGameZone

	if manche == 10 :
		walls = background.create_window("GameZone/Zone_"+str(allAssetGameZone["NumZone"])+"_TraversantPleteforme.txt")
		acutalAssetGameZone= allAssetGameZone["Zone_"+str(allAssetGameZone["NumZone"])]
		
		player = movingent.tp_entity(player,20,37)

		#placement des bonus :  #-afair quand on les placera tous, automatiser le tout
		listeBonus = {"speedUp" : 0.02, "fireRateUp" : 1}
		xbonus = 80
		ybonus = 40
		assetBonus = {}
		assetBonus["boon1"] = entity.create_asset("Boon/boon1.txt") #-afair en sorte que les accès soient automatisé
		assetBonus["Actual"] = assetBonus["boon1"]
		boon1 = entity.create_entity("boon1", xbonus, ybonus, assetBonus) #-afair en sorte que leurs noms s'incrémente tout seul
		boon1 = boon.create_boon(boon1, listeBonus)

		allEntity["boons"].append(boon1)

		listeBonus = {"lifeUp" : 5, "armorMaxUp" : 2}
		xbonus = 80
		ybonus = 34
		assetBonus = {}
		assetBonus["boonGenerator"] = entity.create_asset("Boon/boonGenerator.txt")
		assetBonus["Actual"] = assetBonus["boonGenerator"]
		geneSpeed = 2
		boong = entity.create_entity("boong1", xbonus, ybonus, assetBonus)
		boong = boon.create_boon_generator(boong, listeBonus, geneSpeed)

		allEntity["boons"].append(boong)

		#/!\ juste un mob pour test, les valeurs sont débiles
		assetMob1 = {}
		assetMob1["boon1"] = entity.create_asset("Boon/boon1.txt")
		assetMob1["Actual"]= assetMob1["boon1"]
		mob1 = entity.create_entity("testmob",20,20,assetMob1, "AItest")
		mob1 = movingent.create_moving_ent(mob1,1,1,0.5)

		allEntity["mobs"].append(mob1)

		# manche initialisé
		manche = 11

	if manche == 20 :
		#initialiser la deuxieme manche
		manche = 21

	return


#______Game________________________________________________________________________
def Game():
	"""
    G{classtree}
    DESCRIPTION
    ===========
        Gere les evennements du jeu : prends des decisions en fonction des informations.
        Redirige vers differentes fonctions et change le contexte des autres fonctions.
        Gere la dynamique et l'adaptabilite des autres fonctions.

    PARAM
    =====
		Sans parametre.

    RETOUR
    ======
		Sans retour.
	"""
	global menu, player, manche, allEntity

	#gestion de debut de manche

	if menu=="start" :
		#animation de demarage + elements loristiques et tout
		menu = "manche" #a integrer dans la derniere fonction qui sera appele par startMenu -afair

	if menu == "manche" and (manche%10 == 0) : #on est dans une mancge non initialise
		Init_manche()

	#gestion des IAs : 
	for typeEnt in allEntity.keys() :
		for ent in allEntity[typeEnt] :
			if ent["AI"]!=None :
				log = AI.execute(ent, allEntity)
				ent = log[0]
				allEntity = log[1]
				

	#gestion des assets actuelles :
	for typeEnt in allEntity.keys() :
		for ent in allEntity[typeEnt] :
			if "character" in ent["Type"] :
				ent["Asset"]["Actual"] = character.get_asset(ent)
				pass #au cas ou on mette d'autre type ensuite, il faut pas que les assets actuels s'écrasent les uns les autres.


	#gestion de l'ultime
	if player["spowerDelay"]<=0 :
		player=character.power_off(player) #si le joueur n'a plus de temps d'ultime, il n'est pas entrain de l'utiliser
		player["spowerDelay"]=0

	#gestion des générateurs de boons -afair :
	for boong in allEntity["boons"] :
		if "boonGenerator" in boong["Type"] :
			# if il n'y a pas de bonus sur la case du générateur : -afair
			# boong = boon.set_free(boong)
			None



	#gestion des cadavres
	toRemove = []
	if menu == "manche" :
		for mob in allEntity["mobs"] :
			if "livingEnt" in mob["Type"]:
				if not(livingent.is_alive(mob)):
					toRemove.append(mob)
		for deadmob in toRemove :
			allEntity["mobs"].remove(deadmob)


		# #gestion des fins de manches

		# if not(livingent.is_alive(boss)) :
		# 	menu = "transition"
		# 	#-afair, gerer suivant la valeur de manche

		if not(livingent.is_alive(player)):
			menu = "youLose"
			# -afair

	if menu == "transition" :
		manche +=9 #on passe a la manche suivante
		if manche >= 40 :
			#-afair
			menu = "youWin"
		else :
			None
			#afficher les resultats de la manche precedente,
			#-afair, appeler les fonctions, puis derniere fonction appeler fait passer menu a manche

	elif menu == "youLose" :
		# -afair : afficher ecran de defaite attendre confirmation puis :
		Quit_game()



	return



#______Time_game________________________________________________________________________
def Time_game():
	"""
    G{classtree}
    DESCRIPTION
    ===========
        Gere toutes les actions a effectuer avec une certaine frequence.
        Effectue des protocoles en fonction de leur frequence.

    PARAM
    =====
		Sans parametre

    RETOUR
    ======
		Sans retour
	"""
	global window, timeStep, timeScreen, walls, allEntity, player, menu, timeGravity, acutalAssetGameZone
	if menu == "manche":
		#on est en jeu
		#gestion des tirs
		for bullet in allEntity["projectile"] :
			if time.time()>bullet["Speed"]+bullet["LastTime"] :
				bullet = movingent.move_entity(bullet,bullet["Vx"],bullet["Vy"])
				log = shootingent.hit(bullet,allEntity["mobs"],acutalAssetGameZone,walls)
				if log[1]:#une entite a etait touche
					log[2]=livingent.hurt(log[2],bullet["damageToInflict"])
				if log[0]:#il y a eu collision
					allEntity["projectile"].remove(bullet)

		#gestion de la gravite
		if time.time()>timeGravity + 0.08 :
			for mob in allEntity["mobs"] :
				onTheGround = entity.is_ground_beneath(entity.feet(mob),acutalAssetGameZone,walls) #-afair test s'il y a une plateforme en dessous
				mob = movingent.gravity(mob,onTheGround)
				if not(onTheGround) :
					movingent.move_entity(mob,0,1,True)
			timeGravity = time.time()

		#gestion des déplacements
		for mob in allEntity["mobs"] : # -afair modifier par movingent
			if (time.time()>mob["Speed"]+mob["LastTime"]) and (mob["Vx"]!=0 or mob["Vy"]!=0) :
				#inserer gestion de collision ici qui provient du module entity avec en param allEntity - afair
				#va etre la collision la plus complique a gerer  celle avec les entites et avec les walls -afair
				mob = movingent.move_entity(mob,mob["Vx"],mob["Vy"])
				willCollide = movingent.collision(mob,allEntity["mobs"],acutalAssetGameZone,walls)
				if willCollide :
					mob = movingent.move_entity(mob,-mob["Vx"],-mob["Vy"])

			#on fait tirer si le mob est un mob qui tir
			if (shootingent.is_shooting_ent(mob)) :
				if time.time()>mob["shotDelay"]+mob["lastShot"][0] :
					allEntity["projectile"].append(shootingent.shoot(mob))
					mob = shootingent.as_shot(mob)

		#gestion des générateurs de bonus
		for boonx in allEntity["boons"] :
			if "boonGenerator" in boonx["Type"] :
				if (boonx["GeneLastTime"][0]+boonx["GeneSpeed"] > time.time() and not(boonx["isGenerated"])) :
					allEntity["boons"].append(boon.generate(boonx))
					boonGene = boon.as_generate(boonx)

		#on gere les deplacements du joueur
		if time.time()>player["LastTime"]+player["Speed"]:
			Interact()

		if time.time()>player["LastTime"]+0.03 :
			player = character.switch_stand(player,"Wait")
			#on remet le joueur en position d'attente s'il fait rien

		#gestion de l'ultime
		if time.time()>player["spowerLastTime"]+player["spowerSpeed"] and player["spowerCharge"]<=60 :
			if (player["spowerOn"] and player["spowerDelay"]>0) :
				player = character.cooldown_ult(player)
			else :
				player = character.charge_ult(player)
				player["spowerLastTime"] = time.time()
	else : #on est dans un autre menu, -afair, disons pour le moment dans un menu textuelle
		Interact()


	if time.time()>timeScreen+timeStep:
		Show()


#______Show________________________________________________________________________

def Show() :
	"""
    G{classtree}
    DESCRIPTION
    ===========
        Gere l'affichage du jeu. Gere le retour utilisateur.

    PARAM
    =====
		Sans parametre

    RETOUR
    ======
		Sans retour
	"""
	global window, timeStep, timeScreen, allEntity, player, menu, allAssetGameZone, color


	#Show Frame

	#on efface tout
	background.show_pos(allAssetGameZone["Zone_"+str(allAssetGameZone["NumZone"])],0,0,color["background"]["Black"],color["txt"]["White"])

	#on affiche les entités
	for boonx in allEntity["boons"] :
		color_bg = color["background"]["Black"]
		color_txt = color["txt"]["Green"]
		if "boonGenerator" not in boonx["Type"] :
			entity.show_entity(boonx,color_bg,color_txt)

	for ent in allEntity["mobs"] :
		if "character" in ent["Type"]:
			color_bg = color["background"]["Black"] #noir
			color_txt = color["txt"]["Yellow"]#jaune
		else :
			#asset = entity.create_asset(ent["Asset"])
			color_bg = color["background"]["Black"]
			color_txt = color["txt"]["Yellow"]
		entity.show_entity(ent,color_bg,color_txt)

	for shot in allEntity["projectile"] :
		color_bg = color["background"]["Black"]
		color_txt = color["txt"]["Red"]
		entity.show_entity(shot,color_bg,color_txt)

	timeScreen = time.time()

	#restoration couleur
	sys.stdout.write("\033[37m")
	sys.stdout.write("\033[40m")
	#
	#deplacement curseur
	sys.stdout.write("\033[1;1H\n")
	return


#______INTERACT________________________________________________________________________
def Interact():
	"""
    G{classtree}
    DESCRIPTION
    ===========
        Gere les entrees claviers.
        Reagit en fonction des demandes de l'utilisateur.

    PARAM
    =====
		Sans parametre

    RETOUR
    ======
		Sans retour
	"""

	def isData():
		#recuperation evenement clavier
		return select.select([sys.stdin], [], [], 0) == ([sys.stdin], [], [])

	global player, menu, manche, walls, acutalAssetGameZone

	if isData() :
		c = sys.stdin.read(1)

		if c == '\x1b': # \x1b = esc
			Quit_game()

		if ((manche%10)==1 and menu=="manche") : #on est en jeu

			if (c == "\n" and player["spowerCharge"]>=60) : #-afair : si on appuie sur espace on balance l'ultime
				player["spowerCharge"]=0
				player["spowerDelay"]=4
				player["spowerOn"]=True


			if not(player["spowerOn"]):
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


				# /!\ dans toute cette zone, gerer les collisions avant les deplacements avec movingent.collision -afair
				elif c == "d":
					if not(player["Jump"]) : #-afair : si on est en saut on bouge pas les pieds, fonctionne pas actuellement
						player = character.switch_stand(player,"Run")
					player = movingent.move_entity(player,1,0)
					if movingent.collision(player, allEntity["mobs"], acutalAssetGameZone, walls) :
						player = movingent.move_entity(player,-1,0)

				elif c == "q":
					if not(player["Jump"]) :
						player = character.switch_stand(player,"Run")
					player = movingent.move_entity(player,-1,0)
					if movingent.collision(player, allEntity["mobs"], acutalAssetGameZone, walls) :
						player = movingent.move_entity(player,1,0)

				elif c == "z" and player["Jump"]==0 :
					player = character.switch_stand(player, "Wait")
					player = movingent.jump(player)
					player["Vy"]=-1

				# 	elif c == "s" and player_move == False:
				# 		Move.Player.stand("Wait")
				# 		player_move = True
				# -afair on fait descendre de la plateforme si c'est sur une plateforme
			else :
				None
				#-afair : gestion des interactions lorsque l'on est en ulti

		if menu in ["youLose", "youWin" , "transition"] : #-afair, si on est dans un menu textuel
		#deplacer le pointeur suivant l'endroit
		#passer a la suite si c'est une transitioin, quitte le jeu si c'est une fin de jeu
			if c=="z":
				None
			elif c=="s" :
				None
			elif c=="d" :
				None

	termios.tcflush(sys.stdin.fileno(),termios.TCIFLUSH) #on vide le buffer d'entree






#########Boucle de simulation#########__________________________________________________
def Run():
	"""
    G{classtree}
    DESCRIPTION
    ===========
        Protocol principal.
        Protocol lancee lors de l'execution du jeu.
        Redirige vers les autres protocol primordiaux.
        Contient la boucle de simulation.

    PARAM
    =====
		Sans parametre

    RETOUR
    ======
		Sans retour
	"""
	Init()
	#Infinite Loop
	while True:
		Game()
		Time_game()
	Quit_game()
	return




#______Quit_Game________________________________________________________________________

def Quit_game():
	"""
    G{classtree}
    DESCRIPTION
    ===========
        Quitte le jeu proprement.
        Apres une pause d'une seconde, remet en place le fonctionnement naturel du terminal.

    PARAM
    =====
		Sans param

    RETOUR
    ======
		Sans retour
	"""
	global oldSettings, allEntity

	sys.stdout.write("\033[1;1H")
	sys.stdout.write("\033[2J")

		#couleur white
	sys.stdout.write("\033[37m")
	sys.stdout.write("\033[40m")


	termios.tcsetattr(sys.stdin, termios.TCSADRAIN, oldSettings)

	time.sleep(1)
	print "Game exited successfully"

	sys.exit()









#____Jeux de Test________________________________________________________________
if (__name__=="__main__"):
	Run()
