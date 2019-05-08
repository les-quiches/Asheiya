#-*- coding:utf-8 -*
import entity
import time


#_____Create____________________________________________________________________
def create_character(Entity, spowerSpeed):
    """
    G{classtree}
        DESCRIPTION
    ===========
        Permet d'ajouter une capacite ultime a un entité

    PARAM
    =====

    @param Entity: Entite que l'on veux ajouté une capacite ultime
    @type Entity: dict

    @param spowerSpeed: vitesse de chargement de l'ultim
    @type  spowerSpeed: int

    RETOUR
    ======

    @return Entity : Entity possédent une attaque ultime
    @rtype Entity :dict
    """
	assert type(Entity) is dict
	assert "entity" in Entity["Type"]

	Entity["spowerCharge"] = 0 #la barre de chargement de l'ultime
	Entity["spowerOn"]=False #est-ce que le pouvoir est actif
	Entity["spowerDelay"] = 0 #pendant combien de temps on est encore en ult
	Entity["spowerLastTime"] = time.time() #derniere fois qu'on a charge l'ultime
	Entity["spowerSpeed"] = spowerSpeed #vitesse de chargement de l'ultime
	Entity["Type"].append("character")
	return Entity



#____Ultime______________________________
def charge_ult(player) :
    """
    G{classtree}
        DESCRIPTION
    ===========
        Permet de charger la capacité ultime de l'entité

    PARAM
    =====

    @param player: Entite que l'on veux charger la capacite ultime
    @type player dict

    RETOUR
    ======

    @return Entity : Entity avec la capacité charger
    @rtype Entity :dict
    """
	player["spowerCharge"]+=1
	return player

def cooldown_ult(player) :
    """
    G{classtree}
        DESCRIPTION
    ===========
        Permet de d'enlever du temps sur la recharge de la capacité ultime

    PARAM
    =====

    @param player: Entite que l'on veux charger la capacite ultime
    @type player dict

    RETOUR
    ======

    @return Entity : Entity avec du temps enlever sur la recharge de la capacité ultime
    @rtype Entity :dict
    """
	player["spowerDelay"]-=1
	return player

def powerOff(player) :
    """
    G{classtree}
        DESCRIPTION
    ===========
        Permet de desactiver la capacité ultime

    PARAM
    =====

    @param player: Entite que l'on veux desactiver la capacité ultime
    @type player dict

    RETOUR
    ======

    @return Entity : Entity avec la capacité ultime desactiver
    @rtype Entity :dict
    """
	player["spowerOn"]=False
	return player

#____Position_Gun________________________
def position_gun(assetPosition):
    """
    G{classtree}
        DESCRIPTION
    ===========
        Permet donnée la position de l'arme du joueur en fonction de sont asset

    PARAM
    =====

    @param assetPosition: asset du joueur
    @type assetPosition:list

    RETOUR
    ======

    @return position: coordonnés position arme sur l'asset
    @rtype position: list
    """
    x=0
    y=0
    if(assetPosition[1]=="Left"):
        if(assetPosition[2]==0):
            x=0
            y=1
        elif(assetPosition[2]==45):
            x=0
            y=0
        elif(assetPosition[2]==90):
            x=0
            y=0
        elif(assetPosition[2]==-45):
            x=0
            y=2
        elif(assetPosition[2]==-90):
            x=1
            y=2

    elif(assetPosition[1]=="Right"):
        if(assetPosition[2]==0):
            x=6
            y=1
        elif(assetPosition[2]==45):
            x=5
            y=0
        elif(assetPosition[2]==90):
            x=5
            y=0
        elif(assetPosition[2]==-45):
            x=5
            y=2
        elif(assetPosition[2]==-90):
            x=3
            y=2
    postion = [x,y]
    return postion


#____Get________________________________________________

def get_asset_doc(player): #recupere le nom du fichier de l'asset correspondant a la position actuelle du joueur
    """
    G{classtree}
        DESCRIPTION
    ===========
        Permet donnée l'asset du joueur

    PARAM
    =====

    @param player: entite du joueur
    @type player:dict

    RETOUR
    ======

    @return asset: Chemin d'acces de l'asset du joueur
    @rtype asset: str
    """
    asset = "Asheiya/Asset/" + str(player["Asset"]["position"][0]+"_"+player["Asset"]["position"][1]+"_"+str(player["Asset"]["position"][2]))+".txt"
    return asset

#____Switch_____________________________________________________
def switch_orientation(player, orientation) :
    """
    G{classtree}
        DESCRIPTION
    ===========
        Permet changer de sens l'asset du joueur

    PARAM
    =====

    @param player: entite du joueur
    @type player:dict

    @param orientation: orientation choisi
    @type orientation:str

    RETOUR
    ======

    @return player: joueur avec un orientation differentes
    @rtype player: dict
    """
	assert type(orientation) is str
	assert orientation in ["Right", "Left"]
	player["Asset"]["position"][1]=orientation
	return player

def switch_fire_angle(player, fireAngle) :
    """
    G{classtree}
        DESCRIPTION
    ===========
        Permet changer l'angle de tire de l'asset du joueur

    PARAM
    =====

    @param player: entite du joueur
    @type player:dict

    @param fireAngle: modification de l'angle de tire
    @type fireAngle: int

    RETOUR
    ======

    @return player: joueur avec angle de tire differentes
    @rtype player: dict
    """
	assert type(fireAngle) is int
	assert fireAngle in [-45,45]
	angle = player["Asset"]["position"][2] + fireAngle
	if angle>=90 :
		angle = 90
	elif angle<=-90:
		angle = -90
	player["Asset"]["position"][2]=angle
	return player

def switch_stand(player, stand):
    """
    G{classtree}
        DESCRIPTION
    ===========
        Permet changer l'action de l'asset du joueur

    PARAM
    =====

    @param player: entite du joueur
    @type player:dict

    @param stand: modification de la position
    @type stand: int

    RETOUR
    ======

    @return player: joueur avec une action differentes
    @rtype player: dict
    """
	assert stand in ["Wait","Run"]
	player["Asset"]["position"][0]=stand
	return player

def get_asset(entity_to_get_asset):
    """
    G{classtree}
        DESCRIPTION
    ===========
        Permet donnée l'asset du joueur

    PARAM
    =====

    @param entity_to_get_asset): entite que l'on veux recupere l'asset
    @type entity_to_get_asset):dict

    RETOUR
    ======

    @return asset: Nom de fichier de l'asset de l'entité
    @rtype asset: str
    """
	asset = entity_to_get_asset["Asset"][entity_to_get_asset["Asset"]["position"][0]+"_"+entity_to_get_asset["Asset"]["position"][1]+"_"+str(entity_to_get_asset["Asset"]["position"][2])]
	return(asset)

#____Jeux de Test________________________________________________________________
if (__name__=="__main__"):
	Name = "Asheiya"
	X = 0
	Y = 0
	Vx = 0
	Vy = 0
	Life = 50
	Armor = 18
	Speed = 5
	LastTime = 0
	Asset = {}
	Asset["position"]=["Run","Right",0]
	for Asheiya_doc in ["Run_Right_0","Wait_Right_0","Run_Left_0","Wait_Left_0","Run_Right_45","Wait_Right_45"]:# a terme on utilisera "Asheiya_asset" ou un constructeur de txt
		Asset[Asheiya_doc]=entity.create_asset("Asheiya/Asset/" + Asheiya_doc + ".txt") #chargement Asset
	player = entity.create_entity(Name,X,Y, Asset)
	player = create_character(player, 3)

	# print get_asset_doc(player)
	# player = switch_stand(player, "Run")
	# print player
	# player = switch_orientation(player,"Left")
	# print player
	# player = switch_fire_angle(player, 45)
	# print player
