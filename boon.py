#-*- coding:utf-8 -*

import entity

#_____Create____________________________________________________________________
def create_boon(Entity,Bonus) :
	"""
	G{classtree}
	DESCRIPTION
	===========
		Constructeur de bonus.
		Complemente une entite deja cree


	PARAM
	=====
	@param Entity : l'entite a laquelle rajouter le type boon
	@type Entity : dict

	@param Bonus : en clé : le type de bonus, en valeur : le taux d'augmentation fournit par le bonus
	@type Bonus : dict


	RETOUR
	======
	@return : nouvelle entité, contenant des bonus
	@rtype : dict
	"""
	assert type(Entity) is dict
	assert "entity" in Entity["Type"]

	Entity["Bonus"] = Bonus

	Entity["Type"].append("boon")

	return Entity



#_____Get______________________________________________________________________
def what_boon(boon) : 
	"""
	G{classtree}
	DESCRIPTION
	===========
		renvoi le type de bonus

	PARAM
	=====
	@param boon : le bonus dont on veut savoir la fonction
	@type boon : dict

	RETOUR
	======
	@return :  renvoi les fonction de boon, se qu'il fait
	@rtype : liste
	"""
	return boon.keys()

#_____Action______________________________________________________________________
def caught(boon, Entity) :
	"""
	G{classtree}
	DESCRIPTION
	===========
		Applique le bonus du boon ramassé sur l'entité qui l'a récupéré.

	PARAM
	=====
	@param boon : le bonus récupéré
	@type boon : dict

	@param Entity : l'entité qui récupère le bonus
	@type Entity : dict

	RETOUR
	======
	@return : l'entité avec le bonus récupéré par l'entité
	@rtype : dict
	"""
	assert type(Entity) is dict
	assert "entity" in Entity["Type"]
	assert "livingEnt" in Entity["Type"]

	#-afair pour chaque type de bonus
	allbonus = what_boon(boon)
	for bonus in allbonus :
		if bonus == "lifeUp" :
			Entity["Life"]+=boon[bonus]


	return Entity


