#-*- coding:utf-8 -*

import entity
import time
import character
import movingent
import livingent
import hitbox

import files

void_collision ="0"
random_zone="O"
damage_Zone= "¤"
_wall = "X"
Gostwall = "-"
take_damage = "."

import files
#_____Create____________________________________________________________________
def create_shooting_ent(Entity, damage, bulletSpeed, assetShot, shotDelay,color, lastShot=[time.time(),0]) :

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

    @param bulletSpeed : vitesse des projectiles
    @type bulletSpeed : int

    @param assetShot :Asset du projectile
    @type assetShot :list

    @param shotDelay : temps entre chaque tir
    @type shotDelay :int

    @param lastShot : représente le dernier tir (le moment du tir, et le numéro du tir)
    @type  : list

    RETOUR
    ======

    @return Entity  : une entité capable de tirer
    @rtype Entity : dict
    """
    assert type(Entity) is dict
    assert "entity" in Entity["Type"]

    Entity["damage"] = damage
    Entity["bulletSpeed"] = bulletSpeed
    Entity["assetShot"] = assetShot
    Entity["shotDelay"] = shotDelay
    Entity["baseShotDelay"] = shotDelay
    Entity["lastShot"] = lastShot
    Entity["Type"].append("shootingEnt")
    Entity["bulletColor"]=color
    return Entity

def create_bullet(Entity, damage, origine) :
    """
    G{classtree}
    DESCRIPTION
    ===========
        Ajoute à une entité le type bullet

    PARAM
    =====

    @param Entity: Entité a modifier
    @type Entity : dict

    @param Entity: le nom de l'entité qui a produite ce projectile
    @type Entity : str

    @param damage: Dommages du projectile
    @type damage : int

    RETOUR
    ======

    @return ca  : une Entiter de type bullet
    @rtype ca :def
    """
    assert type(Entity) is dict
    assert "entity" in Entity["Type"]

    Entity["origine"] = origine
    Entity["damageToInflict"] = damage
    Entity["Type"].append("bullet")
    return Entity

#_____Accesseur____________________________________________________________________
def nb_shot(Entity) :
    """
    G{classtree}
    DESCRIPTION
    ===========
        Permet de savoir le numéro de la prochaine balle à tirer

    PARAM
    =====

    @param Entity: Entité dont on veut récupérer l'information
    @type Entity : dict


    RETOUR
    ======
    @return : Le numéro de la prochaine balle qui sera tiré
    @rtype : int
    """
    assert type(Entity) is dict
    assert "shootingEnt" in Entity["Type"]

    return Entity["lastShot"][1]

#_____Modificateur____________________________________________________________________

def as_shot(Entity):
    """
    G{classtree}
    DESCRIPTION
    ===========
        Permet d'incrémenter le numéro de la prochaine balle tiré.
        A utiliser juste après un tir.

    PARAM
    =====

    @param Entity: Entité dont on veut incrémenter le numéro de la balle
    @type Entity : dict


    RETOUR
    ======
    @return : L'Entité avec sa prochaine balle incrémentée
    @rtype : dict
    """
    assert type(Entity) is dict
    assert "shootingEnt" in Entity["Type"]

    Entity["lastShot"][1] += 1
    Entity["lastShot"][0] = time.time()
    return Entity

def damageUp(Entity, amount):
    """
    G{classtree}
    DESCRIPTION
    ===========
        Augmente les dégats d'une entité

    PARAM
    =====

    @param Entity: Entité dont on veut augmenter les dégats
    @type Entity : dict

    @param amount: le nombre de dégâts infligés en plus
    @type amount : int

    RETOUR
    ======
    @return : L'Entité avec ses dégats augmentés
    @rtype : dict
    """
    assert type(Entity) is dict
    assert "shootingEnt" in Entity["Type"]

    Entity["damage"]+=amount
    return Entity


def fireRateUp(Entity, amount) :
    """
    G{classtree}
    DESCRIPTION
    ===========
        Augmente la cadence de tir d'une entité

    PARAM
    =====

    @param Entity: Entité dont on veut augmenter la cadence de tir
    @type Entity : dict

    @param amount: le nombre de dégâts infligés en plus
    @type amount : int

    RETOUR
    ======
    @return : L'Entité avec sa cadence de tir augmentée
    @rtype : dict
    """
    assert type(Entity) is dict
    assert "shootingEnt" in Entity["Type"]

    if Entity["shotDelay"] - amount >= 0.01 : #tant qu'on tir pas plus vite que la boucle de simulation
        Entity["shotDelay"]-=amount

    return Entity

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

    bullet_name = "bullet"+"_"+Entity["Name"]+"_"+str(nb_shot(Entity))

    if "character" in Entity["Type"] :
        posture = character.get_posture(Entity)
        pos_gun = character.position_gun(posture)
        x = pos_gun[0]+Entity["x"]
        y = pos_gun[1]+Entity["y"]

    if posture[2] in [90,-90] :
        Vx = 0
        name_asset = "Gun_Vertical"

    elif posture[1] == "Right" :
        Vx = 1
        if posture[2]>0 :
            name_asset="Gun_Slash"
        elif posture[2]<0 :
            name_asset="Gun_UnSlash"
    else :
        Vx = -1
        if posture[2]>0 :
            name_asset="Gun_UnSlash"
        elif posture[2]<0 :
            name_asset="Gun_Slash"

    if posture[2]>0 :
        Vy = -1
    elif posture[2]<0:
        Vy = 1
    else :
        Vy = 0
        name_asset = "Gun_Horizontal"

    asset = {}
    asset[name_asset] = Entity["assetShot"][name_asset]
    asset["Actual"] = Entity["assetShot"][name_asset]
    bullet = entity.create_entity(bullet_name,x,y,asset,Entity["bulletColor"])
    bullet = movingent.create_moving_ent(bullet, Vx, Vy, Entity["bulletSpeed"])
    bullet = create_bullet(bullet,Entity["damage"],Entity["Name"])

    return bullet


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
