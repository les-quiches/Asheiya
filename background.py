#-*- coding:utf-8 -*
import sys
import os

import files
f =files

def create_window(filename):

    """
    G{classtree}
    DESCRIPTION
    ===========
        Permet de créer une fenetre

    PARAM
    =====

    @param filename: Chemin d'acces du fichier
    @type filename : str


    RETOUR
    ======

    @return ca  : Tableau représentant la fenetre
    @rtype ca : list
    """

    wd = dict()
    wd["window"]=[]
    myfile=f.OPEN_FILE_XML(filename)
    doc =myfile.splitlines() # axe y
    for x in doc:# axe x
        y = list(x)
        wd["window"].append(y)
    return(wd)

def show_window(doc):
    """
    G{classtree}
    DESCRIPTION
    ===========
        Permet d'afficher la fenetre principal

    PARAM
    =====

    @param doc : Tableau représentant la fennetre principal
    @type doc : list

    RETOUR
    ======
		Sans retour
    """
	#couleur fond
	sys.stdout.write("\033[40m")
	#couleur white
	sys.stdout.write("\033[37m")
	#goto
	for y in range(0,len(doc["window"])):
		for x in range(0,len(doc["window"][y])):
			s="\033["+str(y+1)+";"+str(x+1)+"H"
			sys.stdout.write(s)
			#affiche
			sys.stdout.write(doc["window"][y][x])

def show_pos(doc, X, Y, color_bg, color_txt):
    """
    G{classtree}
    DESCRIPTION
    ===========
        Permet d'afficher un fenetre a des coordonnés précise

    PARAM
    =====

    @param doc : Tableau représentant la fenetre
    @type doc : list

    @param X: coordonnés x où installer la fenetre
    @type X: int

    @param Y: coordonnés y où installer la fenetre
    @type Y: int

    @param color_bg : Couleur du backgound
    @type color_bg :int

    @param color_txt : Couleur des characters
    @type color_txt :int

    RETOUR
    ======
		Sans retour
    """
    #couleur fond
    sys.stdout.write("\033["+str(color_bg)+"m")
	#couleur white
    sys.stdout.write("\033["+str(color_txt)+"m")
    for y in range(0,len(doc["window"])):
		for x in range(0,len(doc["window"][y])):
			s="\033["+str(Y+y+1)+";"+str(X+x+1)+"H"
			sys.stdout.write(s)
			#affiche
			sys.stdout.write(doc["window"][y][x])




""" txt  bg
    30, 40 : noir ;
    31, 41 : rouge ;
    32, 42 : vert ;
    33, 43 : jaune ;
    34, 44 : bleu ;
    35, 45 : rose ;
    36, 46 : cyan ;
    37, 47 : gris.

"""

#____Jeux de Test________________________________________________________________
if (__name__=="__main__"):
    window = create_window("Windows.txt")
    show_window(window)
