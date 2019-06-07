#-*- coding:utf-8 -*
import files

def execute(mob, allEntity) :
	if mob["AI"] == "AItest" :
		log = AItest(mob, allEntity)
		return log # dans l'ordre : mob, tout les mobs


#######################################
"""
MY AI
"""
########################################


def AItest(mymob, allEntity) :

#on tourne dans un carré
	if mymob["x"]>80 :
		mymob["Vx"] = -1
	elif mymob["x"]<10 :
		mymob["Vx"] = 1
	if mymob["y"]>38 :
		mymob["Vy"] = -1
	elif mymob["y"]<5 :
		mymob["Vy"] = 1

	log =  [mymob, allEntity]
	return log

#######################################
"""
MY FUNCTION
"""
######################################
def get_player(allEntity) : 
	for mob in allEntity["mobs"] :
		if mob["Name"] == "Asheiya Briceval":
			return mob
	return None