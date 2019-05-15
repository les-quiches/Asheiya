#-*- coding:utf-8 -*

import entity
import time


#_____Create____________________________________________________________________
def create_moving_ent(Entity, Vx, Vy,Speed, LastTime=time.time()):
    """
    G{classtree}
        DESCRIPTION
    ===========
        Permet d'ajouter les parametres de déplacement à une entité

    PARAM
    =====

    @param Entity: Entité que l'on veux déplacé
    @type Entity: dict

    @param vx: déplacement sur x que l'on veux appliquer à l'entité
    @type  vx: int

    @param vy: déplacement sur y que l'on veux appliquer à l'entité
    @type  vy: int

    @param Speed: vitesse du joueur
    @type Speed: : int

    @param LastTime: dernière fois que l'entité c'est déplacé
    @type LastTime :int

    RETOUR
    ======

    @return Entity : Entity de type déplaçable
    @rtype Entity :dict
    """
    assert type(Entity) is dict
    assert "entity" in Entity["Type"]
    Entity["Vx"]= Vx
    Entity["Vy"]= Vy
    Entity["Speed"]=Speed
    Entity["LastTime"]=LastTime
    Entity["Jump"] = 0
    Entity["Type"].append("movingEnt")
    return Entity


#_____Modificateur______________________________________________________________________
def speedUp(Entity, amount) :
    """
    G{classtree}
    DESCRIPTION
    ===========
        Augmente la vitesse d'une entité

    PARAM
    =====

    @param Entity: Entité dont on veut augmenter la vitesse
    @type Entity : dict

    @param amount: quantité d'augmentation de la vitesse
    @type amount : float

    RETOUR
    ======
    @return : L'Entité avec sa vitesse augmenté
    @rtype : dict
    """
    assert type(Entity) is dict
    assert "moovingEnt" in Entity["Type"]

    if Entity["Speed"]+amount >=0.01 : #tant qu'on va pas plus vite que la boucle de simulation
        Entity["Speed"]+=amount

    return Entity


#_____Move______________________________________________________________________
def move_entity(Entity,x,y,willCollide=False,isGravity=False):

    """
    G{classtree}
        DESCRIPTION
    ===========
        Permet de déplacer une entité

    PARAM
    =====

    @param Entity: Entite que l'on veux déplacer
    @type Entity: dict

    @param x: déplacement sur x que l'on veux appliquer à l'entité
    @type  x: int

    @param y: déplacement sur y que l'on veux appliquer à l'entité
    @type  y: int

    @param willCollide: True si le déplacement va engendrer une collision, False sinon
    @type willCollide : bool

    @param isGravity: True si le déplacement est dû à la gravité
    @type isGravity : bool

    RETOUR
    ======

    @return Entity : Entité déplacé
    @rtype Entity :dict
    """
    if not(willCollide):
        Entity["x"]+=2*x
        Entity["y"]+=y
        if not(isGravity) :
            Entity["LastTime"]=time.time()
    return(Entity)

def tp_entity(Entity,x,y):
    """
    G{classtree}
        DESCRIPTION
    ===========
        Permet de déplacer une entité à une position précise

    PARAM
    =====

    @param Entity: Entite que l'on veux déplacer
    @type Entity: dict

    @param x: postion sur x où on veut déplacer l'entité
    @type  x: int

    @param y: postion sur y où on veut déplacer l'entité
    @type  y: int

    RETOUR
    ======

    @return Entity : Entité déplacé
    @rtype Entity :dict
    """
    Entity["x"]=x
    Entity["y"]=y
    return(Entity)

def jump(Entity):
    """
    G{classtree}
    DESCRIPTION
    ===========
        Permet de démarer un saut d'une entité

    PARAM
    =====

    @param Entity: Entité que l'on veut faire sauter
    @type Entity: dict

    RETOUR
    ======

    @return Entity : Entité entrain de sauter
    @rtype Entity :dict
    """
    Entity["Jump"] = 9
    return Entity

def gravity(Entity,onTheGround=False) :
    """
    G{classtree}
    DESCRIPTION
    ===========
        Permet d'aplique une gravité a une Entitée

    PARAM
    =====
    @param Entity: Entite à qui l'on veut appliquer notre gravitée
    @type Entity: dict

    @param onTheGround: True si l'entité est déjà au sol, False sinon
    @type  onTheGround: bool

    RETOUR
    ======

    @return Entity : Entité soumise à une force gravitationelle
    @rtype Entity :dict
    """
    if Entity["Jump"]>=1 :
        Entity["Jump"]-=1
    elif(not(onTheGround)):
        Entity["Vy"]=1
    if onTheGround==True :
        Entity["Jump"]=0
    return (Entity)


#_____Collision______________________________________________________________________
def collision(ent, allEntity, Asset_Game_Zone, walls, x=None, y=None) : #x et y correspondent aux prochaines positions, utiles seulement pour le joueur sinon on recupere via entity
    """
    G{classtree}
    DESCRIPTION
    ===========
        Permet de détecter une collision

    PARAM
    =====
    @param ent: entité dont l'on veux tester si il y a une collision
    @type ent:dict

    @param allEntity: toutes les entités qui pourrais etre en collision
    @type allEntity: dict

    @param Asset_Game_Zone:  Asset de l'ecran ou le joueur peu se mouvoir
    @type Asset_Game_Zone : list

    @param walls: dictionnaire ou sont réparti tout les mur, plateformes
    @type wall: dict

    @param x: coordonnés x
    @type x: int

    @param y: coordonnés y
    @type y: int

    RETOUR
    ======

    @return collision : Renvoie True s'il y a une collision, False sinon.
    @rtype collision :bool
    """
    # -afair : reperer tout d'abord si ia pas de collisions avec les murs, puis ensuite les collisions possibles
    #           avec les entites proches, en recuperant les hit_box des entites PROCHES SEULEMENT

    #pos["x"] et pos["y"] les FUTURS positions de l'entite
    if (x != None or y!=None):
        None
        #ca veut dire quon gere le deplacement du joueur, donc la position en prendre en compte c'est ent[x]+x
    else :
        None
        #on gere une entite programme, donc on prend en compte ent[x]+ent[Vx]
    #on recupere pos -> avec X Y les positions a tester
    #on regarde dans Walls/allentity/Asset_Game_Zone si ia pas de collisions
    return False




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
