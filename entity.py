#-*- coding:utf-8 -*

import sys
import os
import character
import grid
import hitbox


import files
f=files

void_collision ="0"
_wall = "X"
Gostwall = "-"
EntityHitbox = "E"


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

    @param Asset : grille représentant le jeu
    @type Asset : list

    @param grid : grille du jeu
    @type  grid : list

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

    return Entity

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
    ca["Shadow"]=hitbox.Create_Shadow(ca["Asset"])
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

def feet(FEET_entity) :#renvoi les "pieds" de l'entite
    """
    G{classtree}
    DESCRIPTION
    ===========
        Permet de donner la position des pieds d'un asset

    PARAM
    =====

    @param FEET_entity: Entite dont on veut obtenir la position des pieds
    @type FEET_entity: dict


    RETOUR
    ======

    @return FEET_feet : renvoi la position des pied de l'entité
    @rtype FEET_feet : list
    """
    FEET_x,FEET_y,FEET_xmax,FEET_ymax=hitbox.hit_box_simple(FEET_entity)
    FEET_feet=[FEET_x,FEET_xmax,FEET_ymax]
    return FEET_feet

def head(HEAD_entity) :
    """
    G{classtree}
    DESCRIPTION
    ===========
        Permet de donner la position de la tête d'un asset

    PARAM
    =====

    @param FEET_entity: Entite dont on veut obtenir la position de la tête
    @type FEET_entity: dict


    RETOUR
    ======

    @return FEET_feet : renvoi la position de la tête de l'entité
    @rtype FEET_feet : list
    """
    HEAD_x,HEAD_y,HEAD_xmax,HEAD_ymax=hitbox.hit_box_simple(HEAD_entity)
    HEAD_entity=[HEAD_x,HEAD_xmax,HEAD_y]
    return HEAD_entity

def is_ground_above(IGA_head) :
    """
    G{classtree}
    DESCRIPTION
    ===========
        Permet de savoir si il y a une plateforme solide au dessus de la position Pos

    PARAM
    =====

    @param pos : position de l'endroit où l'on veut savoir s'il y a un mur au dessus
    @type pos : list

    @param IGB_grid: grille représentant le jeu
    @type IGB_grid : dict


    RETOUR
    ======
    @return : True s'il y a bien un sol en dessous, False sinon.
    @rtype :bool
    """
    IGA_ground = IGA_head[2]-1 #position au dessus des pieds
    IGA_length_feet = IGA_feet[1]-IGA_feet[0]
    for a in range(IGA_length_feet):
        if IGA_grid[IGA_ground][IGA_feet[0]+a-1] == _wall :
            return True
    return False

def is_ground_beneath(IGB_feet, IGB_shadow) :
    """
    G{classtree}
    DESCRIPTION
    ===========
        Permet de savoir si il y a une plateforme solide sous la position Pos

    PARAM
    =====

    @param pos : position de l'endroit où l'on veut savoir s'il y a une plateforme en dessous
    @type pos : list

    @param IGB_grid: grille représentant le jeu
    @type IGB_grid : dict


    RETOUR
    ======
    @return : True s'il y a bien un sol en dessous, False sinon.
    @rtype :bool
    """
    IGB_ground = IGB_feet[2]+1 #position en dessous des pieds
    IGB_length_feet = IGB_feet[1]-IGB_feet[0]
    for a in range(IGB_length_feet):
        if IGB_shadow[IGB_ground][IGB_feet[0]+a-1] != void_collision :
            return True
    return False

def RightSide(RightSide_entity) :#renvoi les "pieds" de l'entite
    """
    G{classtree}
    DESCRIPTION
    ===========
        Permet de donner la position a droite d'un asset

    PARAM
    =====

    @param RightSide_entity: Entite dont on veut obtenir la position
    @type RightSide_entity: dict


    RETOUR
    ======

    @return FEET_feet : renvoi la position a droite de l'asset
    @rtype FEET_feet : list
    """
    RightSide_x,RightSide_y,RightSide_xmax,RightSide_ymax=hitbox.hit_box_simple(RightSide_entity)
    RightSide_right=[RightSide_y,RightSide_xmax,RightSide_ymax]
    return RightSide_right

def is_ground_right(IGR_pos) :
    """
    G{classtree}
    DESCRIPTION
    ===========
        Permet de savoir si il y a un mur a droite

    PARAM
    =====

    @param IGR_pos : position de l'endroit où l'on veut savoir s'il y a un mur a droite
    @type IGR_pos : list

    @param IGB_grid: grille représentant le jeu
    @type IGB_grid : dict


    RETOUR
    ======
    @return : True s'il y a bien un mur a droite, False sinon.
    @rtype :bool
    """
    IGR_wall = IGR_pos[1]+1 #position a droite
    IGR_length_right = IGR_pos[2]-IGR_pos[0]
    for a in range(IGR_length_right):
        if IGR_grid[IGR_pos[0]+a-1][IGR_wall] != void_collision :
            return True
    return False

def LeftSide(LeftSide_entity) :#renvoi les "pieds" de l'entite
    """
    G{classtree}
    DESCRIPTION
    ===========
        Permet de donner la position a gauche d'un asset

    PARAM
    =====

    @param LeftSide_entity: Entite dont on veut obtenir la position
    @type LeftSide_entity: dict


    RETOUR
    ======

    @return FEET_feet : renvoi la position a gauche de l'asset
    @rtype FEET_feet : list
    """
    LeftSide_x,LeftSide_y,LeftSide_xmax,LeftSide_ymax=hitbox.hit_box_simple(LeftSide_entity)
    LeftSide_Left=[LeftSide_x,LeftSide_y,LeftSide_ymax]
    return LeftSide_Left

def is_ground_left(IGL_pos) :
    """
    G{classtree}
    DESCRIPTION
    ===========
        Permet de savoir si il y a un mur a gauche

    PARAM
    =====

    @param IGR_pos : position de l'endroit où l'on veut savoir s'il y a un mur a gauche
    @type IGR_pos : list

    @param IGB_grid: grille représentant le jeu
    @type IGB_grid : dict


    RETOUR
    ======
    @return : True s'il y a bien un mur a gauche, False sinon.
    @rtype :bool
    """
    IGL_wall = IGL_pos[0]-1 #position a gauche
    IGL_length_left = IGL_pos[2]-IGL_pos[1]
    for a in range(IGL_length_left):
        if IGL_grid[IGL_pos[1]+a-1][IGL_wall]!= void_collision :
            return True
    return False

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

    @param color_bg : Couleur du background
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
    s=""
    #couleur fond
    s+="\033["+str(color_bg)+"m"
	#couleur texte
    s+="\033["+str(color_txt)+"m"

    Frame=asset["FrameNb"]
    if asset["FrameNb"]+1 < len(asset["Asset"]):
        asset["FrameNb"]+=1
    else:
        asset["FrameNb"]=0
    for j in range(0,len(asset["Asset"][Frame])):
        s+="\033["+str(Y+j)+";"+str(X)+"H"

        s+=asset["Asset"][Frame][j]
        s+="\n"
    sys.stdout.write(s)

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
