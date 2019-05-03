import entity
import shootingmob

#____Position_Gun________________________
def position_gun(assetPosition):
    x=0
    y=0
    if(assetPosition[1]=="Left"):
        if(assetPosition[2]==0):
            x=0
            y=1
        elif(assetPosition[2]==45):
            x=0
            y=0
        elif(assetPosition[2]==90):
            x=0
            y=0
        elif(assetPosition[2]==-45):
            x=0
            y=2
        elif(assetPosition[2]==-90):
            x=1
            y=2

    elif(assetPosition[1]=="Right"):
        if(assetPosition[2]==0):
            x=6
            y=1
        elif(assetPosition[2]==45):
            x=5
            y=0
        elif(assetPosition[2]==90):
            x=5
            y=0
        elif(assetPosition[2]==-45):
            x=5
            y=2
        elif(assetPosition[2]==-90):
            x=3
            y=2
    postion = [x,y]
    return postion


#____Get________________________________________________

def get_asset_doc(player): #recupere le nom du fichier de l'asset correspondant a la position actuelle du joueur
	asset = "Asheiya/Asset/" + str(player["Asset"]["position"][0]+"_"+player["Asset"]["position"][1]+"_"+str(player["Asset"]["position"][2]))+".txt"
	return asset

#____Switch_____________________________________________________
def switch_orientation(player, orientation) :
	assert type(orientation) is str
	assert orientation in ["Right", "Left"]
	player["Asset"]["position"][1]=orientation
	return player

def switch_fire_angle(player, fireAngle) :
	assert type(fireAngle) is int
	assert fireAngle in [-45,45]
	angle = player["Asset"]["position"][2] + fireAngle
	if angle>=90 :
		angle = 90
	elif angle<=-90:
		angle = -90
	player["Asset"]["position"][2]=angle
	return player

def switch_stand(player, stand):
	assert stand in ["Wait","Run"]
	player["Asset"]["position"][0]=stand
	return player



#____Jeux de Test________________________________________________________________
if (__name__=="__main__"):
	Name = "Asheiya"
	Type = "Player"
	X = 0
	Y = 0
	Vx = 0
	Vy = 0
	Life = 50
	Armor = 18
	Speed = 5
	LastTime = 0
	Asset = {}
	Asset["position"]=["Run","Right",0]
	for Asheiya_doc in ["Run_Right_0","Wait_Right_0","Run_Left_0","Wait_Left_0","Run_Right_45","Wait_Right_45"]:# a terme on utilisera "Asheiya_asset" ou un constructeur de txt
		Asset[Asheiya_doc]=entity.create_asset("Asheiya/Asset/" + Asheiya_doc + ".txt") #chargement Asset
	player = entity.create_entity(Name,Type,X,Y,Vx,Vy,Life,Armor,Speed, LastTime, Asset)

	print get_asset_doc(player)
	# player = switch_stand(player, "Run")
	# print player
	# player = switch_orientation(player,"Left")
	# print player
	# player = switch_fire_angle(player, 45)
	# print player
