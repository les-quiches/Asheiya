#-*- coding:utf-8 -*

import entity

#_____Create____________________________________________________________________
def create_boon(Entity,Bonus,Value) :
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

	@param Bonus : le type de bonus (lifeUp, armorUp, damageUp, speedUp, [...])
	@type Bonus : str

	@param Value : la puissance du bonus, la quantite modifié lorsqu'on le recupère
	@type Value : int/float

	RETOUR
	======
	@return : la nouvelle entite créée, correspondant a l'ancienne mais avec le type boon en plus
	@rtype : dict
	"""
	assert type(Entity) is dict
	assert "entity" in Entity["Type"]
	Entity["Bonus"] = Bonus
	Entity["Value"] = Value
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
	@type boon : str

	RETOUR
	======
	@return :  renvoi la fonction de boon, se qu'il fait
	@rtype : str
	"""
	return boon["Bonus"]