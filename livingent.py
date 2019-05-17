#-*- coding:utf-8 -*

import entity

#_____Create____________________________________________________________________
def create_living_ent(Entity,Life, Armor) :
    """
    G{classtree}
    DESCRIPTION
    ===========
        Complète une entité pour qu'elle puisse recevoir des dégâts.
        Les living_entity sont détruitent et éliminé lorsqu'elles n'ont plus de vie.

    PARAM
    =====
    @param Entity : L'entité auquel rajouter le type "vivant"
    @type Entity : dict

    @param Life : le nombre de point de vie maximum et initial de l'entité
    @type Life : int

    @param Armor : le nombre de points d'armure maximum et initial de l'entité
    @type Armor : int

    RETOUR
    ======
    @return : l'entité donné en entré, avec le type vivant en plus.
    @rtype : dict
    """
    assert type(Entity) is dict
    assert "entity" in Entity["Type"]

    Entity["Life"]= Life
    Entity["LifeMax"]= Life
    Entity["Armor"]= Armor
    Entity["ArmorMax"]= Armor
    Entity["Type"].append("livingEnt")
    return Entity

#_____Get______________________________________________________________________

def is_alive(Entity) :
    """
    G{classtree}
    DESCRIPTION
    ===========
        Determine si une living_entity possède encore des points de vie ou non

    PARAM
    =====
    @param Entity : l'entité à tester
    @type Entity : dict

    RETOUR
    ======
    @return :  True si elle est encore en vie, False sinon
    @rtype : bool
    """
    assert type(Entity) is dict
    assert "livingEnt" in Entity["Type"]

    if Entity["Life"]<=0 :
        return False
    else :
        return True


#_____Accesseur______________________________________________________________________

def hurt(Entity,damage) :
    """
    G{classtree}
    DESCRIPTION
    ===========
        Blesse une entité

    PARAM
    =====
    @param Entity : l'entité à blesser
    @type Entity : dict

    @param damage : le nombre de dégâts à lui infliger
    @type damage : int

    RETOUR
    ======
    @return :  l'entité blessé
    @rtype : dict
    """
    assert type(Entity) is dict
    assert "livingEnt" in Entity["Type"]

    Entity["Life"]-=damage
    return Entity

def heal(Entity,amount) :
    """
    G{classtree}
    DESCRIPTION
    ===========
        Soigne une entité

    PARAM
    =====
    @param Entity : l'entité à soigner
    @type Entity : dict

    @param amount : le nombre de dégâts à lui réstaurer
    @type amount : int

    RETOUR
    ======
    @return :  l'entité soigné
    @rtype : dict
    """
    assert type(Entity) is dict
    assert "livingEnt" in Entity["Type"]

    if Entity["Life"] + amount <= Entity["LifeMax"] :
        Entity["Life"]+=amount
    return Entity

def armorUp(Entity,amount) :
    """
    G{classtree}
    DESCRIPTION
    ===========
        Restaure l'armure d'une entité

    PARAM
    =====
    @param Entity : l'entité dont on veut restaurer l'armure
    @type Entity : dict

    @param amount : le nombre de points d'armures à lui réstaurer
    @type amount : int

    RETOUR
    ======
    @return :  l'entité réparé
    @rtype : dict
    """
    assert type(Entity) is dict
    assert "livingEnt" in Entity["Type"]

    if Entity["Armor"]+amount <= Entity["ArmorMax"] :
        Entity["Armor"]+=amount

    return Entity

def armorMaxUp(Entity,amount) :
    """
    G{classtree}
    DESCRIPTION
    ===========
        Améliore l'armure d'une entité

    PARAM
    =====
    @param Entity : l'entité dont on veut améliorer l'armure
    @type Entity : dict

    @param amount : le nombre de points d'armures à lui améliorer
    @type amount : int

    RETOUR
    ======
    @return :  l'entité avec une meilleur armure
    @rtype : dict
    """
    assert type(Entity) is dict
    assert "livingEnt" in Entity["Type"]

    Entity["ArmorMax"]+=amount
    return Entity

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
