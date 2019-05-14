#-*- coding:utf-8 -*

def get_player(allEntity) : 
	for mob in allEntity["mobs"] :
		if mob["Name"] == "Asheiya Briceval":
			return mob
	return None