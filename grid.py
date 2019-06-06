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
				myGrid[y][x]["Backgound"]=void_collision
			else:
				Gostelement =myGostlist[y][x]
				if Gostelement!=void_collision
					myGrid[y][x]["Backgound"]=Gostwall
				else:
					myGrid[y][x]["Backgound"]=_wall
			myGrid[y][x]["Entity"]={}
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
	for SEG_y in SEG_ent["Asset"][ActualAsset]["Shadow"] :
		for SEG_x in SEG_y :
			if SEG_x != void_collision and (SEG_ent in SEG_grid[SEG_ent["y"]+SEG_y][SEG_ent["x"]+SEG_x]["Entity"]) :
				SEG_grid[SEG_ent["x"]+SEG_x][SEG_ent["y"]+SEG_y]["Entity"].remove(SEG_ent)

	return SEG_grid


def Add_Ent_Grid(SEG_ent, SEG_grid, SEG_collision=False) :
	"""
    DESCRIPTION
    ===========
        Supprime une entité de la grille de jeu

    PARAM
    =====

    @param SEG_ent: entité à ajouter à la grille
    @type SEG_ent : dict

    @param SEG_grid: grille du jeu
    @type SEG_grid: str

    @param SEG_collision: liste des entités présents sur les cases ou l'entité a été ajouté
    @type SEG_collision: list

    RETOUR
    ======

    @return SEG_grid: tuple composé de la grille avec l'entité en plus et si demandé, les entités déjà présentent sur les cases où a été ajouté l'entité
    @rtype SEG_grid: tuple
"""
	SEG_collided_ent=[]

	for SEG_y in SEG_ent["Asset"][ActualAsset]["Shadow"] :
		for SEG_x in SEG_y :
			if SEG_x != void_collision :
				if SEG_collision :
					for SEG_what_ent in SEG_grid[SEG_ent["y"]+SEG_y][SEG_ent["x"]+SEG_x]["Entity"] :
						SEG_collided_ent.append(SEG_what_ent)
				SEG_grid[SEG_ent["x"]+SEG_x][SEG_ent["y"]+SEG_y]["Entity"].append(SEG_ent)


	return (SEG_grid, SEG_collided_ent)
