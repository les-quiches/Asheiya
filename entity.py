import sys
import os
import time


import files
f=files

nFile = 0
#_____Create____________________________________________________________________
def create_entity(Name, Type, X, Y, Vx, Vy,Life, Armor, Speed, LastTime, Asset,AI = None):
    Entity=dict()
    Entity["Name"]= Name
    Entity["Type"]= Type
    Entity["x"]= X
    Entity["y"]= Y
    Entity["Vx"]= Vx
    Entity["Vy"]= Vy
    Entity["Life"]= Life
    Entity["Armor"]= Armor
    Entity["Speed"]=Speed
    Entity["LastTime"]=LastTime
    Entity["Asset"]= Asset
    Entity["AI"]=AI
    Entity["Jump"] = 0
    return(Entity)

def create_asset(filename):
    global nFile #sert a faire changer les assets, pas adaptable du tout, a modifier   - afair
                #faire un dictionnaire global nFile? et recuperer dans le filename la cle du dictionnaire
    ca=dict()
    ca["Asset"]= []
    myfile= f.OPEN_FILE_XML(filename)
    frame = myfile.split("frame\r\n")
    FrameMax=len(frame)
    for i in frame:
		ca["Asset"].append(i.split("\n"))

    nFile=(nFile+1)%FrameMax
    ca["FrameNb"]= nFile
    return(ca)

#_____Move______________________________________________________________________
def move_entity(Entity,x,y, isGravity=False):
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

def gravity(Entity) :  #-afair
    if Entity["Jump"]>=1 :
        Entity["Jump"]-=1
    else :
        Entity["Vy"]=1
    return (Entity)


#_____Get______________________________________________________________________

def is_alive(Entity) :
    if Entity["Life"]==0 :
        return False
    else :
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
    Vx = 0
    Vy = 0
    Life = 50
    Armor = 18
    Speed = 5
    LastTime = 0
    Asset = {}
    Asset["position"]=["Wait","Right",0]
    for Asheiya_doc in ["Run_Right_0","Wait_Right_0","Run_Left_0","Wait_Left_0","Run_Right_45","Wait_Right_45"]:# a terme on utilisera "Asheiya_asset" ou un constructeur de txt
        Asset[Asheiya_doc]=create_asset("Asheiya/Asset/" + Asheiya_doc + ".txt") #chargement Asset
    player = create_entity(Name,Type,X,Y,Vx,Vy,Life,Armor,Speed, LastTime, Asset)
    # print player.keys()

    # show_entity(create_asset("Asheiya/Asset/Run_Right_0.txt"),player,40,33)
    # print player["Asset"]["Run_Right_0"]
    # show_entity(create_asset("Asheiya/Asset/Run_Right_0.txt"),player,40,33)
    # print player["Asset"]["Run_Right_0"]
    print player["x"], player["y"]
    tp_entity(player, 10, 12)
    # pdb.set_trace()
    print player["x"], player["y"]



