#-*- coding:utf-8 -*

void_collision ="0"
random_zone="O"
damage_Zone= "¤"
_wall = "X"
Gostwall = "-"
take_damage = "."


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