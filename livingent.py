#-*- coding:utf-8 -*
import entity

#_____Create____________________________________________________________________
def create_living_ent(Entity,Life, Armor) :
    """
    G{classtree}
        DESCRIPTION
    ===========
        Permet d'ajouter les parametres de vie à une entité

    PARAM
    =====

    @param Entity: Entite que l'on veux déplacé
    @type Entity: dict

    @param Life: Vie max de l'entité
    @type  Life: int

    @param Armor: Armure max de l'entité
    @type  Armor: int


    RETOUR
    ======

    @return Entity : Entity de type vivante
    @rtype Entity :dict
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
        Permet de vérifier si l'entité est en vie

    PARAM
    =====

    @param Entity: Entity a tester
    @type Entity : dict


    RETOUR
    ======
    @return : Une information booléenne
    @rtype :bool
    """
    if Entity["Life"]<=0 :
        return False
    else :
        return True

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
