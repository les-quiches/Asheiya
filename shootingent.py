#-*- coding:utf-8 -*

import entity
import time
import character
import movingent
import hitbox

void_collision ="0"
random_zone="O"
damage_Zone= "¤"
wall = "X"
Gostwall = "-"
take_damage = "."

#_____Create____________________________________________________________________
def create_shooting_ent(Entity, damage, bulletSpeed, assetShot, shotDelay, lastShot=[time.time(),0]) :

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
    bullet = entity.create_entity(bullet_name,x,y,asset)
    bullet = movingent.create_moving_ent(bullet, Vx, Vy, Entity["bulletSpeed"])
    bullet = create_bullet(bullet,Entity["damage"],Entity["Name"])

    return bullet


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
    @type walls: list

    RETOUR

    @return log  : contient trois informations comme suit : True si le projectile rentre en collision (False sinon), True si c'était une entité vivante(False sinon), l'identifiant de cette entité le cas échéant.
    @rtype log : tuple
    """
    None
    # -afair : les tests de collisions
    assetBullet = bullet["Asset"]["Asset"][bullet["Asset"]["FrameNb"]]
    Shadow_walls=hitbox.hit_box_complex(walls,Gostwall)
    Shadow_gameBorder=hitbox.hit_box_complex(gameBorder,wall)
    Shadow_backgound=hitbox.Add_Shadow(Shadow_walls,Shadow_gameBorder)
    Shadow_bullet=hitbox.hit_box_complex(assetBullet,damage_Zone)
    if not(hitbox.detect_collision_wall(assetBullet,Shadow_backgound,bullet["x"],bullet["y"])):
        Shadow_bullet_placed=hitbox.Add_Shadow(Shadow_bullet,Shadow_backgound,bullet["x"],bullet["y"])
        for entity in entities:
            if hitbox.detect_collision_entity(bullet,assetBullet,entity):#trouver asset général
                is_hit = True
                hit_entity=True  #test si la balle touche une entite ou pas
                log = (is_hit, hit_entity,entity)
                return(log)
            else:
                is_hit = False
                hit_entity=False  #test si la balle touche une entite ou pas
                entity = None
    else:
        is_hit = True
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
