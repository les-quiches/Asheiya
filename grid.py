#-*- coding:utf-8 -*
void_collision ="0"
_wall = "X"
Gostwall = "-"
EntityHitbox = "E"

import files

def Create_Grid(CG_filenum):
	"""
    DESCRIPTION
    ===========
        créé une grille du jeux

    PARAM
    =====

    @param CG_filenum: Numéro de la liste a ouvrir
    @type CG_filenum : int

    RETOUR
    ======

    @return SEG_grid: grille du jeu
    @rtype SEG_grid: list

	"""
	ca=dict()
	Background= files.OPEN_FILE_XML("GameZone/Zone_"+str(CG_filenum)+".txt")
	BackgroundGost= files.OPEN_FILE_XML("GameZone/Zone_"+str(CG_filenum)+"_GostWall.txt")
	mylist = Background.split("\r\n")
	myGostlist = BackgroundGost.split("\r\n")
	myGrid=[]
	for y in range(len(mylist)):
		myGrid.append([])
		for x in range(len(mylist[y])):
			myGrid[y].append([])
			myGrid[y][x]={}
			element = mylist[y][x]
			if element == " ":
				myGrid[y][x]["Background"]=void_collision
			else:
				Gostelement =myGostlist[y][x]
				if Gostelement!=void_collision :
					myGrid[y][x]["Background"]=Gostwall
				else:
					myGrid[y][x]["Background"]=_wall
			myGrid[y][x]["Entity"]=[]
	return myGrid


def Supr_Ent_Grid(SEG_ent, SEG_grid) :
	"""
    DESCRIPTION
    ===========
        Supprime une entité de la grille de jeu

    PARAM
    =====

    @param SEG_ent: entité à supprimer de la grille
    @type SEG_ent : dict

    @param SEG_grid: grille du jeu
    @type SEG_grid: str

    RETOUR
    ======

    @return SEG_grid: grille du jeu avec l'entité en moins
    @rtype SEG_grid: list
"""
	SEG_shadowEnt = SEG_ent["Asset"]["Actual"]["Shadow"][SEG_ent["Asset"]["Actual"]["FrameNb"]]
	for y in range(len(SEG_shadowEnt)-1):
		for x in range(len(SEG_shadowEnt[y])-1) :
			if SEG_grid[SEG_ent["y"]+y][SEG_ent["x"]+x]["Background"] != void_collision and not(SEG_ent in SEG_grid[SEG_ent["y"]+y][SEG_ent["x"]+x]["Entity"]) :
				SEG_grid[SEG_ent["y"]+y][SEG_ent["x"]+x]["Entity"].remove(SEG_ent)

	return SEG_grid


def Add_Ent_Grid(AEG_ent, AEG_grid, AEG_collision=False) :
	"""
    DESCRIPTION
    ===========
        Supprime une entité de la grille de jeu

    PARAM
    =====

    @param AEG_ent: entité à ajouter à la grille
    @type AEG_ent : dict

    @param AEG_grid: grille du jeu
    @type AEG_grid: str

    @param AEG_collision: liste des entités présents sur les cases ou l'entité a été ajouté
    @type AEG_collision: list

    RETOUR
    ======

    @return AEG_grid: tuple composé de la grille avec l'entité en plus et si demandé, les entités déjà présentent sur les cases où a été ajouté l'entité
    @rtype AEG_grid: tuple
"""
	AEG_collided_ent=[]

	AEG_shadowEnt = AEG_ent["Asset"]["Actual"]["Shadow"][AEG_ent["Asset"]["Actual"]["FrameNb"]]
	for y in range(len(AEG_shadowEnt)-1):
		for x in range(len(AEG_shadowEnt[y])-1) :
			if AEG_grid[AEG_ent["y"]+y][AEG_ent["x"]+x]["Background"] != void_collision and not(AEG_ent in AEG_grid[AEG_ent["y"]+y][AEG_ent["x"]+x]["Entity"]) :
				if (AEG_collision):
					for AEG_what_ent in AEG_grid[AEG_ent["y"]+y][AEG_ent["x"]+x]["Entity"] :
						AEG_collided_ent.append(AEG_what_ent)
				AEG_grid[AEG_ent["y"]+y][AEG_ent["x"]+x]["Entity"].append(AEG_ent)


	return (AEG_grid, AEG_collided_ent)
