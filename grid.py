#-*- coding:utf-8 -*
void_collision ="0"
_wall = "X"
Gostwall = "-"
EntityHitbox = "E"

import files

def Create_Grid(CG_filename):
	"""
    DESCRIPTION
    ===========
        créé une grille du jeux

    PARAM
    =====

    @param CG_filenamet: fichier a faire la grille
    @type CG_filename : str

    RETOUR
    ======

    @return SEG_grid: grille du jeu avec l'entité en moins
    @rtype SEG_grid: list
	"""
	ca=dict()
	myfile= files.OPEN_FILE_XML(CG_filename)
	mylist = myfile.split("\r\n")
	myGrid=[]
	for y in range(len(mylist)):
		myGrid.append([])
		for x in range(len(mylist[y])):
			myGrid[y].append([])
			myGrid[y][x]={}
			element = mylist[y][x]
			if element == " ":
				myGrid[y][x]["Backgound"]=void_collision
			elif element == "=":
				myGrid[y][x]["Backgound"]=Gostwall
			elif element in ["X","-","+"]:
				myGrid[y][x]["Backgound"]=_wall
			myGrid[y][x]["Entity"]={}

	files.SAVE_FILE_JSON(myGrid,"log_wtf")
	return
Create_Grid("GameZone/Windows.txt")

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
			if SEG_x != void_collision :
				SEG_grid[SEG_ent["y"]+SEG_y][SEG_ent["x"]+SEG_x].remove(SEG_ent)

	return SEG_grid
