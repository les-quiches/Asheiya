import entity
import time


#_____Create____________________________________________________________________
def create_moving_ent(Entity, Vx, Vy,Speed, LastTime):
    assert type(Entity) is dict
    assert "entity" in Entity["Type"]
    Entity["Vx"]= Vx
    Entity["Vy"]= Vy
    Entity["Speed"]=Speed
    Entity["LastTime"]=LastTime
    Entity["Jump"] = 0
    Entity["Type"].append("movingEnt")
    return Entity


#_____Move______________________________________________________________________
def move_entity(Entity,x,y,willCollide=False,isGravity=False):
    if not(willCollide):
        Entity["x"]+=2*x
        Entity["y"]+=y
        if not(isGravity) :
            Entity["LastTime"]=time.time()
    return(Entity)

def tp_entity(Entity,x,y):
    Entity["x"]=x
    Entity["y"]=y
    return(Entity)

def jump(Entity):
    Entity["Jump"] = 9
    return Entity

def gravity(Entity,onTheGround=False) :
    if Entity["Jump"]>=1 :
        Entity["Jump"]-=1
    elif(not(onTheGround)):
        Entity["Vy"]=1
    return (Entity)

#_____Collision______________________________________________________________________   
def collision(ent, allEntity, gameBorder, walls, x=None, y=None) : #x et y correspondent aux prochaines positions, utiles seulement pour le joueur sinon on recupere via entity
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
    #on regarde dans Walls/allentity/gameBorder si ia pas de collisions
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