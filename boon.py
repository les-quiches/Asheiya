import entity

#_____Create____________________________________________________________________
def create_boon(Entity,Bonus,Value) : #Bonus rpz le type de boon (damageUp, SpeedUp etc), Value le montant d'augmentation
	Entity["Bonus"] = Bonus
	Entity["Value"] = Value
	return Entity



#_____Get______________________________________________________________________
def what_boon(boon) : 
	return boon["Bonus"]