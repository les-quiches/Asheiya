#-*- coding:utf-8 -*

import entity
import time

#_____Create____________________________________________________________________
def create_shooting_ent(Entity, damage, assetShot, shotDelay, lastShot=[time.time(),0]) :

    """
    G{classtree}
    DESCRIPTION
    ===========
        Ajoute à une entité la possibilité de tirer

    PARAM
    =====

    @param Entity: Entité a modifier
    @type Entity : dict

    @param damage: Dommages du projectile
    @type damage : int

    @param assetShot :Asset du projectile
    @type assetShot :list

    @param shotDelay : temps entre chaque tir
    @type shotDelay :int

    @param lastShot : représente le dernier tir (le moment du tir, et le numéro du tir)
    @type  : list

    RETOUR
    ======

    @return ca  : une Entiter de type projectile tiré
    @rtype ca :def
    """
    assert type(Entity) is dict
    assert "entity" in Entity["Type"]
    Entity["damage"] = damage
    Entity["assetShot"] = assetShot
    Entity["shotDelay"] = shotDelay
    Entity["lastShot"] = lastShot
    Entity["Type"].append("shootingEnt")
    return Entity

#-afair les entites de types bullet

#_____Accesseur____________________________________________________________________
def is_shooting_ent(Entity) :
    """
    G{classtree}
    DESCRIPTION
    ===========
        Permet de vérifier si l'entité est une entité capable de tirer

    PARAM
    =====

    @param Entité: Entité a tester
    @type Entité : dict


    RETOUR
    ======
    @return : True si l'entité est capable de tirer, False sinon.
    @rtype :bool
    """
    if "shootingEnt" in Entity["Type"] :
        return True
    else :
        return False


#_____Action____________________________________________________________________
def shoot(Entity) :
    """
    G{classtree}
    DESCRIPTION
    ===========
        Permet de faire tirer une entité

    PARAM
    =====

    @param Entity: l'entité qui va tirer
    @type Entity : dict


    RETOUR

    @return ca  : une Entité correspondant au projectile tiré
    @rtype ca : dict
    """
    assert type(Entity) is dict
    assert "shootingEnt" in Entity["Type"]
	#-afair
	# -> cre une entite de type bullet -> definir les carac d'une balle
    return

def hit(bullet, entities , gameBorder, walls ) :
    """
    G{classtree}
    DESCRIPTION
    ===========
        Permet de vérifier si un projectile rentre en collision avec quelquechose.
        Si c'est le cas, prends des décisions en fonction de la nature de l'objet touché.

    PARAM
    =====
    @param bullet: le projectile dont on chercher à savoir la collision
    @type bullet: dict

    @param entities: toute les entités du jeu
    @type entities : list


    @param gameBorder:  Zone de l'ecran ou le joueur peu se mouvoir
    @type gameBorder : list

    @param walls: tableau ou sont réparti tout les mur, plateformes
    @type wall: array

    RETOUR

    @return log  : contient trois informations comme suit : True si le projectile rentre en collision (False sinon), True si c'était une entité vivante(False sinon), l'identifiant de cette entité le cas échéant.
    @rtype log : tuple
    """
    None
    # -afair : les tests de collisions
    is_hit = False #test si la balle touche quelquechose
    hit_entity=False  #test si la balle touche une entite ou pas
    entity = None #l'entite touche (le nom) le cas echeant
    log = (is_hit, hit_entity,entity) #pour tout renvoyer
    return(log)





#____Jeux de Test________________________________________________________________
if (__name__=="__main__"):
    Name = "Asheiya"
    X = 20
    Y = 37
    Asset = {}
    Asset["position"]=["Wait","Right",0]
    for Asheiya_doc in ["Run_Right_0","Wait_Right_0","Run_Left_0","Wait_Left_0","Run_Right_45","Wait_Right_45"]:# a terme on utilisera "Asheiya_asset" ou un constructeur de txt
        Asset[Asheiya_doc]=entity.create_asset("Asheiya/Asset/" + Asheiya_doc + ".txt") #chargement Asset
    player = entity.create_entity(Name,X,Y,Asset)
