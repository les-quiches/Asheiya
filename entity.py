#-*- coding:utf-8 -*

import sys
import os
import character


import files
f=files

#_____Create____________________________________________________________________
def create_entity(Name, X, Y, Asset, AI = None):
    """
    G{classtree}
    DESCRIPTION
    ===========
        Permet de créer une entitee basique.

    PARAM
    =====

    @param Name : Designation de l'entite, correspond au nom de l'entite dans l'Histoire (Lore)
    @type Name : str

    @param  X : position sur l'axe x de l'entite
    @type X : int

    @param  Y : position sur l'axe Y de l'entite
    @type Y : int

    @param Asset : variables contenant toutes les representations de l'entite
    @type Asset : dict

    @param AI : si l'entite est automatiquement controle, chemin d'acces vers le fichier qui la controle
    @type AI : str

    RETOUR
    ======

    @return Entity : Entité créée
    @rtype : dict

    """
    Entity=dict()
    Entity["Name"]= Name
    Entity["Type"]= []
    Entity["Type"].append("entity")
    Entity["x"]= X
    Entity["y"]= Y
    Entity["Asset"]= Asset
    Entity["AI"]=AI

    return(Entity)

def create_asset(filename):
    """
    G{classtree}
    DESCRIPTION
    ===========
        Permet de créer un asset

    PARAM
    =====

    @param filename: Chemin d'acces du fichier
    @type filename : str


    RETOUR
    ======

    @return ca  : Tableau représentant un asset
    @rtype ca : list
    """
    ca=dict()
    ca["Asset"]= []
    myfile= f.OPEN_FILE_XML(filename)
    frame = myfile.split("frame\r\n")
    FrameMax=len(frame)
    for i in frame:
        a=i.split("\r\n")
        del a[-1]
        ca["Asset"].append(a)
    ca["FrameNb"]= 0
    return(ca)

#____getter___________________________________________________
def get_actual_asset(entity) :
    """
    G{classtree}
    DESCRIPTION
    ===========
        Permet de donner l'asset actuelle d'une entité.

    PARAM
    =====

    @param entity: Entite dont on veut obtenir l'asset
    @type entity: dict


    RETOUR
    ======

    @return : renvoi l'asset actuelle de l'entité sous forme [nbFrame, Asset]
    @rtype : list
    """
    assert type(entity) is dict

    return entity["Asset"]["Actual"]


#____collision___________________________________________________

def feet(entity) :#renvoi les "pieds" de l'entite
    """
    G{classtree}
    DESCRIPTION
    ===========
        Permet de donner la position des pieds d'un asset

    PARAM
    =====

    @param entity: Entite dont on veut obtenir la position des pieds
    @type entity: dict


    RETOUR
    ======

    @return : renvoi la position des pied de l'entité
    @rtype : list
    """

    return

def is_ground_beneath(pos,Asset_Game_Zone,walls) :
    """
    G{classtree}
    DESCRIPTION
    ===========
        Permet de savoir si il y a une plateforme solide sous la position Pos

    PARAM
    =====

    @param pos : position de l'endroit où l'on veut savoir s'il y a une plateforme en dessous
    @type pos : list

    @param Asset_Game_Zone:  Asset de l'ecran ou le joueur peut se mouvoir
    @type Asset_Game_Zone : list

    @param walls : Ensemble des plateformes du jeu
    @type walls : array

    RETOUR
    ======
    @return : True s'il y a bien un sol solide en dessous, False sinon.
    @rtype :bool
    """
    # -afair : test si en dessous de pos il y a ou pas une plateforme et renvoie True or False en consequence
    return True


#_____Show______________________________________________________________________
def show_entity(Entity, color_bg, color_txt):
    """
    G{classtree}
    DESCRIPTION
    ===========
        Permet d'afficher l'asset d'un entité

    PARAM
    =====

    @param Entity : Entitée
    @type Entity :dict

    @param color_bg : Couleur du backgound
    @type color_bg :int

    @param color_txt : Couleur de l'asset
    @type color_txt :int

    RETOUR
    ======
		Sans retour
    """
    assert type(Entity) is dict
    assert "entity" in Entity["Type"]

    asset  = Entity["Asset"]["Actual"]
    X=Entity["x"]+1
    Y=Entity["y"]+1
    #couleur fond
    sys.stdout.write("\033["+str(color_bg)+"m")
	#couleur texte
    sys.stdout.write("\033["+str(color_txt)+"m")

    Frame=asset["FrameNb"]
    if asset["FrameNb"]+1 < len(asset["Asset"]):
        asset["FrameNb"]+=1
    else:
        asset["FrameNb"]=0
    for j in range(0,len(asset["Asset"][Frame])):
        s="\033["+str(Y+j)+";"+str(X)+"H"
        sys.stdout.write(s)
        sys.stdout.write(asset["Asset"][Frame][j])
        sys.stdout.write("\n")

    return


#____Jeux de Test________________________________________________________________
if (__name__=="__main__"):
    Name = "Asheiya"
    X = 20
    Y = 37
    Asset = {}
    Asset["position"]=["Wait","Right",0]
    for Asheiya_doc in ["Run_Right_0","Wait_Right_0","Run_Left_0","Wait_Left_0","Run_Right_45","Wait_Right_45"]:# a terme on utilisera "Asheiya_asset" ou un constructeur de txt
        Asset[Asheiya_doc]=create_asset("Asheiya/Asset/" + Asheiya_doc + ".txt") #chargement Asset
    player = create_entity(Name,X,Y,Asset)

    print player
