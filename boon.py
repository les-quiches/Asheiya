#-*- coding:utf-8 -*

import entity
import livingent
import shootingent
import movingent

import time

# Liste des bonus possibles : (speedUp, armorUp, damageUp, lifeUp, armorMaxUp, fireRateUp)


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

def create_boon_generator(Entity,Bonus, GeneSpeed, GeneLastTime=[time.time(),0]) :
	"""
	G{classtree}
	DESCRIPTION
	===========
		Constructeur de générateur de bonus.
		Complemente une entite deja cree


	PARAM
	=====
	@param Entity : l'entite a laquelle rajouter le type boon
	@type Entity : dict

	@param Bonus : en clé : le type de bonus, en valeur : le taux d'augmentation fournit par le bonus
	@type Bonus : dict


	RETOUR
	======
	@return : nouvelle entité, créant des bonus
	@rtype : dict
	"""

	assert type(Entity) is dict
	assert "entity" in Entity["Type"]

	Entity["Bonus"] = Bonus
	Entity["GeneSpeed"] = GeneSpeed
	Entity["GeneLastTime"] = GeneLastTime

	Entity["Type"].append("boonGenerator")

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
	assert type(boon) is dict
	assert "entity" in Entity["Type"]
	assert "livingEnt" in Entity["Type"]
	assert "boon" in boon["Type"]


	allbonus = what_boon(boon)
	for bonus in allbonus :
		if bonus == "lifeUp" :
			Entity = livingent.heal(Entity,boon["bonus"])
		elif bonus == "damageUp" :
			Entity = shootingent.damageUp(Entity, bonus["bonus"])
		elif bonus == "armorUp" :
			Entity = livingent.armorUp(Entity, bonus["bonus"])
		elif bonus =="speedUp" :
			Entity = movingent.speedUp(Entity, bonus["bonus"])
		elif bonus == "armorMaxUp" :
			Entity = livingent.armorMaxUp(Entity, bonus["bonus"])
		elif bonus == "fireRateUp" :
			Entity = shootingent.fireRateUp(Entity, bonus["bonus"])


	return Entity


def generate(boonG) :
	"""
	G{classtree}
	DESCRIPTION
	===========
		Génère un bonus à partir d'un générateur de bonus

	PARAM
	=====
	@param boonG : le générateur de bonus qui va générer
	@type boonG : dict

	RETOUR
	======
	@return : le bonus généré
	@rtype : dict
	"""
	assert type(boonG) is dict
	assert "boonGenerator" in boonG["Type"]

	x = boonG["X"]
	y = boonG["Y"]
	asset = "Boon/boon1.txt"
	name = "boon" +"_"+ boonG["Name"] +"_"+ str(boonG["GeneLastTime"][1])

	boon = entity.create_entity(name,x,y,asset)
	boon = create_boon(boonG["Bonus"])

	return boon

def as_generate(boonG) :
	"""
	G{classtree}
	DESCRIPTION
	===========
		Confirme la création d'un bonus

	PARAM
	=====
	@param boonG : le générateur de bonus qui a généré
	@type boonG : dict

	RETOUR
	======
	@return : le générateur avec les délais mis à jour
	@rtype : dict
	"""
	assert type(boonG) is dict
	assert "boonGenerator" in boonG["Type"]

	boonG["GeneLastTime"][0] = time.time()
	boonG["GeneLastTime"][1]+=1
	return boonG


#____Jeux de Test________________________________________________________________
if (__name__=="__main__"):
	None

