import entity

#_____Create____________________________________________________________________
def create_living_ent(Entity,Life, Armor) :
	Entity["Life"]= Life
	Entity["LifeMax"]= Life
	Entity["Armor"]= Armor
	Entity["ArmorMax"]= Armor  
	return Entity

#_____Get______________________________________________________________________

def is_alive(Entity) :
    if Entity["Life"]<=0 :
        return False
    else :
        return True

#____Jeux de Test________________________________________________________________
if (__name__=="__main__"):
    Name = "Asheiya"
    Type = "Player"
    X = 20
    Y = 37
    Asset = {}
    Asset["position"]=["Wait","Right",0]
    for Asheiya_doc in ["Run_Right_0","Wait_Right_0","Run_Left_0","Wait_Left_0","Run_Right_45","Wait_Right_45"]:# a terme on utilisera "Asheiya_asset" ou un constructeur de txt
        Asset[Asheiya_doc]=entity.create_asset("Asheiya/Asset/" + Asheiya_doc + ".txt") #chargement Asset
    player = entity.create_entity(Name,Type,X,Y,Asset)