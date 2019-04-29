import sys
import os

import files
f=files
#_____Create____________________________________________________________________
def create_entity(Name, Type, X, Y, Vx, Vy, Life, Armor, Speed, AI = None):
    Entity=dict()
    Entity["Name"]= Name
    Entity["Type"]= type
    Entity["x"]= X
    Entity["y"]= Y
    Entity["Vx"]= Vy
    Entity["Vy"]= Vy
    Entity["Life"]= Life
    Entity["Armor"]= Armor
    Entity["Speed"]=Speed
    Entity["AI"]=AI
    Entity["Asset"]= None
    return(Entity)

def create_asset(filename):
    ca=dict()
    ca["Asset"]= []
    myfile= f.OPEN_FILE_XML(filename)
    frame = myfile.split("frame\r\n")
    for i in frame:
		ca["Asset"].append(i.split("\n"))
    ca["FramesNb"]=0
    print "\n"
    print ca["Asset"]
    return(ca)

#_____Move______________________________________________________________________
def move_entity(Entity,x,y):
    Entity["x"]+=x
    Entity["y"]+=y
    return(Entity)

def tp_entity(Entity,x,y):
    Entity["x"]=x
    Entity["y"]=y
    return(Entity)

#_____Show______________________________________________________________________
def show_entity(doc,Entity, color_bg, color_txt):
    X=Entity["x"]+1
    Y=Entity["y"]+1
    #couleur fond
    sys.stdout.write("\033["+str(color_bg)+"m")
	#couleur white
    sys.stdout.write("\033["+str(color_txt)+"m")

    Frame=doc["FramesNb"]
    if int(doc["FramesNb"])+1 < int(len(doc["Asset"])):
        doc["FramesNb"]+=1
    else:
        doc["FramesNb"]=0

    for j in range(0,len(doc["Asset"][Frame])):
        s="\033["+str(Y+j)+";"+str(X)+"H"
        sys.stdout.write(s)
        sys.stdout.write(doc["Asset"][Frame][j])
        sys.stdout.write("\n")
    return
