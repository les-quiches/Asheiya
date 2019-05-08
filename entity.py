#-*- coding:utf-8 -*
import sys
import os


import files
f=files

#_____Create____________________________________________________________________
def create_entity(Name, Type, X, Y, Asset, AI = None):
    """
    G{classtree}
    DESCRIPTION
    ===========
        Permet de créer une entitee basique.

    PARAM
    =====

    @param Name : Designation de l'entite, correspond au nom de l'entite dans l'Histoire (Lore)
    @type Name : string

    @param Type : represente le type de l'entite (player, boss, boonCreator, boon, bullet, [...])
    @type Type : string

    @param  X : position sur l'axe x de l'entite
    @type X : int

    @param  Y : position sur l'axe Y de l'entite
    @type Y : int

    @param Asset : variables contenant toutes les representations de l'entite
    @type Asset : dict

    @param IA : si l'entite est automatiquement controle, chemin d'acces vers le fichier qui la controle
    @type IA : string

    RETOUR
    ======

    @return Entity : Entiter créer
    @rtype : dict

    """
    Entity=dict()
    Entity["Name"]= Name
    Entity["Type"]= Type
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
		ca["Asset"].append(i.split("\n"))
    ca["FrameNb"]= 0
    return(ca)

#____collision___________________

def hit_box_simple(asset,entity):
    """
    G{classtree}
    DESCRIPTION
    ===========
        Permet de donné l'hitbox  d'un asset

    PARAM
    =====

    @param asset: Tableau représentant un asset
    @type asset : list

    @param entity:
    @type entity:


    RETOUR
    ======

    @return   : 
    @rtype : list
    """
    y=len(asset)
    a=0
    for i in asset:
        a+=len(asset[i])
    x= a/(i+1)
    hit_box_entity=[entity["x"], entity["y"], entity["x"]+x, entity["y"]+y]# plage de l'hitbox de l'asset (point en haut a gauche puit en bas a doite)
    return(hit_box_entity)

def feet(entity) :#renvoi les "pieds" de l'entite
    # feet = [hit_box_simple(entity["Asset"],entity)[2],hit_box_simple(entity["Asset"],entity)[3]] # -afair pas sur de mon coup pour le entity["Asset"]
    return

def is_ground_beneath(pos,gameBorder,walls) :
    # -afair : test si en dessous de pos il y a ou pas une plateforme et renvoie True or False en consequence
    return True


#_____Show______________________________________________________________________
def show_entity(doc,Entity, color_bg, color_txt):

    X=Entity["x"]+1
    Y=Entity["y"]+1
    #couleur fond
    sys.stdout.write("\033["+str(color_bg)+"m")
	#couleur texte
    sys.stdout.write("\033["+str(color_txt)+"m")

    Frame=doc["FrameNb"]
    if doc["FrameNb"]+1 < len(doc["Asset"]):
        doc["FrameNb"]+=1
    else:
        doc["FrameNb"]=0
    for j in range(0,len(doc["Asset"][Frame])):
        s="\033["+str(Y+j)+";"+str(X)+"H"
        sys.stdout.write(s)
        sys.stdout.write(doc["Asset"][Frame][j])
        sys.stdout.write("\n")

    return


#____Jeux de Test________________________________________________________________
if (__name__=="__main__"):
    Name = "Asheiya"
    Type = "Player"
    X = 20
    Y = 37
    Asset = {}
    Asset["position"]=["Wait","Right",0]
    for Asheiya_doc in ["Run_Right_0","Wait_Right_0","Run_Left_0","Wait_Left_0","Run_Right_45","Wait_Right_45"]:# a terme on utilisera "Asheiya_asset" ou un constructeur de txt
        Asset[Asheiya_doc]=create_asset("Asheiya/Asset/" + Asheiya_doc + ".txt") #chargement Asset
    player = create_entity(Name,Type,X,Y,Asset)

    print player
