#-*- coding:utf-8 -*

import entity
import time
import hitbox
import files

void_collision ="0"
random_zone="O"
damage_Zone= "¤"
_wall = "X"
Gostwall = "-"
take_damage = "."

#_____Create____________________________________________________________________
def create_moving_ent(CME_Entity, CME_Vx, CME_Vy,CME_Speed, CME_Gravity=True, CME_LastTime=time.time()):
    """
    G{classtree}
        DESCRIPTION
    ===========
        Permet d'ajouter les parametres de déplacement à une entité

    PARAM
    =====

    @param CME_Entity: Entité que l'on veux déplacé
    @type CME_Entity: dict

    @param CME_Vx: déplacement sur x que l'on veux appliquer à l'entité
    @type  CME_Vx: int

    @param CME_Vy: déplacement sur y que l'on veux appliquer à l'entité
    @type  CME_Vy: int

    @param CME_Speed: vitesse du joueur
    @type CME_Speed: : int

    @param CME_Speed: Si l'entité subit la gravité ou pas
    @type CME_Speed: : bool

    @param LastTime: dernière fois que l'entité c'est déplacé
    @type LastTime :int

    RETOUR
    ======

    @return CME_Entity : entité de type déplaçable
    @rtype CME_Entity :dict
    """
    assert type(CME_Entity) is dict
    assert "entity" in CME_Entity["Type"]
    CME_Entity["Vx"]= CME_Vx
    CME_Entity["Vy"]= CME_Vy
    CME_Entity["Speed"]=CME_Speed
    CME_Entity["LastTime"]=CME_LastTime
    CME_Entity["Jump"] = 0
    CME_Entity["Type"].append("movingEnt")
    CME_Entity["Gravity"]=CME_Gravity
    return CME_Entity


#_____Modificateur______________________________________________________________________
def speedUp(SU_Entity, SU_amount) :
    """
    G{classtree}
    DESCRIPTION
    ===========
        Augmente la vitesse d'une entité

    PARAM
    =====

    @param SU_Entity: Entité dont on veut augmenter la vitesse
    @type SU_Entity : dict

    @param SU_amount: quantité d'augmentation de la vitesse
    @type SU_amount : float

    RETOUR
    ======
    @return SU_Entity : L'Entité avec sa vitesse augmenté
    @rtype SU_Entity: dict
    """
    assert type(SU_Entity) is dict
    assert "moovingEnt" in SU_Entity["Type"]

    if SU_Entity["Speed"]+SU_amount >=0.01 : #tant qu'on va pas plus vite que la boucle de simulation
        SU_Entity["Speed"]+=SU_amount

    return SU_Entity


#_____Move______________________________________________________________________
def move_entity(ME_Entity,ME_x,ME_y,ME_isGravity=False):

    """
    G{classtree}
        DESCRIPTION
    ===========
        Permet de déplacer une entité

    PARAM
    =====

    @param ME_Entity: Entite que l'on veux déplacer
    @type ME_Entity: dict

    @param ME_x: déplacement sur x que l'on veux appliquer à l'entité
    @type  ME_x: int

    @param ME_y: déplacement sur y que l'on veux appliquer à l'entité
    @type  ME_y: int

    @param ME_willCollide: True si le déplacement va engendrer une collision, False sinon
    @type ME_willCollide : bool

    @param ME_isGravity: True si le déplacement est dû à la gravité
    @type ME_isGravity : bool

    RETOUR
    ======

    @return ME_Entity : Entité déplacé
    @rtype ME_Entity :dict
    """
    ME_Entity["x"]+=2*ME_x
    ME_Entity["y"]+=ME_y
    if not(ME_isGravity):
        ME_Entity["LastTime"]=time.time()
    return(ME_Entity)

def tp_entity(TPE_Entity,TPE_x,TPE_y):
    """
    G{classtree}
        DESCRIPTION
    ===========
        Permet de déplacer une entité à une position précise

    PARAM
    =====

    @param TPE_Entity: Entite que l'on veux déplacer
    @type TPE_Entity: dict

    @param TPE_x: postion sur x où on veut déplacer l'entité
    @type  TPE_x: int

    @param TPE_y: postion sur y où on veut déplacer l'entité
    @type  TPE_y: int

    RETOUR
    ======

    @return TPE_Entity : Entité déplacé
    @rtype TPE_Entity :dict
    """
    TPE_Entity["x"]=TPE_x
    TPE_Entity["y"]=TPE_y
    return(TPE_Entity)

def jump(JUMP_Entity):
    """
    G{classtree}
    DESCRIPTION
    ===========
        Permet de démarer un saut d'une entité

    PARAM
    =====

    @param JUMP_Entity: Entité que l'on veut faire sauter
    @type JUMP_Entity: dict

    RETOUR
    ======

    @return JUMP_Entity : Entité entrain de sauter
    @rtype JUMP_Entity :dict
    """
    JUMP_Entity["Jump"] = 9
    return JUMP_Entity

def gravity(GRAVITY_Entity,GRAVITY_onTheGround) :
    """
    G{classtree}
    DESCRIPTION
    ===========
        Permet d'aplique une gravité a une Entitée

    PARAM
    =====
    @param GRAVITY_Entity: Entite à qui l'on veut appliquer notre gravitée
    @type GRAVITY_Entity: dict

    @param GRAVITY_onTheGround: True si l'entité est déjà au sol, False sinon
    @type  GRAVITY_onTheGround: bool

    RETOUR
    ======

    @return GRAVITY_Entity : Entité soumise à une force gravitationelle
    @rtype GRAVITY_Entity :dict
    """
    if GRAVITY_Entity["Jump"]>=1 :
        GRAVITY_Entity["Jump"]-=1
    else : 
        GRAVITY_Entity["Vy"]=1

    if GRAVITY_onTheGround==True :
        GRAVITY_Entity["Jump"]=0
        GRAVITY_Entity["Vy"]=0
    return GRAVITY_Entity

#_____Collision______________________________________________________________________
def Zone_Collision(ZC_ent,ZC_Asset_Game_Zone,ZC_walls):
    """
    G{classtree}
    DESCRIPTION
    ===========
        Permet de détecter la collision entre une entité et le backgound

    PARAM
    =====
    @param ZC_ent:entité a tester
    @type ZC_ent:dict

    @param ZC_Asset_Game_Zone: asset de la zone de jeu
    @type  ZC_Asset_Game_Zone:list

    @param ZC_walls: asset des plateformes de jeu
    @type  ZC_walls:list

    RETOUR
    ======

    @return ZC_hitentwall : renvois ce qui a été détecter
    @rtype ZC_hitentwall :str
    """
    ZC_Shadow_walls=hitbox.hit_box_complex(ZC_walls,Gostwall)
    ZC_Shadow_gameBorder=hitbox.hit_box_complex(ZC_Asset_Game_Zone,_wall)
    ZC_Shadow_backgound=hitbox.Add_Shadow(ZC_Shadow_walls,ZC_Shadow_gameBorder)
    ZC_hitentwall=hitbox.detect_collision_wall(ZC_ent,ZC_Shadow_backgound)
    return ZC_hitentwall



def collision(COLLI_ent, COLLI_allEntityTest, COLLI_Asset_Game_Zone, COLLI_walls) : #x et y correspondent aux prochaines positions, utiles seulement pour le joueur sinon on recupere via entity
    """
    G{classtree}
    DESCRIPTION
    ===========
        Permet de détecter une collision

    PARAM
    =====
    @param COLLI_ent: entité dont l'on veux tester si il y a une collision
    @type COLLI_ent:dict

    @param COLLI_allEntityTest: toutes les entités qui pourrais etre en collision
    @type COLLI_allEntityTest: dict

    @param COLLI_Asset_Game_Zone:  Asset de l'ecran ou le joueur peu se mouvoir
    @type COLLI_Asset_Game_Zone : list

    @param COLLI_walls: dictionnaire ou sont réparti tout les mur, plateformes
    @type COLLI_wall: dict

    @param COLLI_x: coordonnés x
    @type COLLI_x: int

    @param COLLI_y: coordonnés y
    @type COLLI_y: int

    RETOUR
    ======

    @return COLLI_log : Renvoie une liste d'information : s'il y a eu une collision dur, 
    @rtype COLLI_log :bool
    """
    COLLI_hitentwall=Zone_Collision(COLLI_ent, COLLI_Asset_Game_Zone, COLLI_walls)

    COLLI_log=[]
    COLLI_log.append(False)

    if COLLI_hitentwall == _wall:
        #detect un mur
        COLLI_log[0]=True
    elif COLLI_hitentwall == void_collision:
        for COLLI_Entity in COLLI_allEntityTest:
            if COLLI_Entity != COLLI_ent :
                if hitbox.detect_collision_entity(COLLI_ent,COLLI_Entity):
                   COLLI_log[0]=True
                    #collision entre les deux entiter
    else:
        files.SAVE_FILE_JSON(COLLI_ent,"log_wtf")
        # si on est ici c'est un BUG

    return COLLI_log




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
