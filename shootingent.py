import entity

#_____Create____________________________________________________________________
def create_shooting_ent(mobToBe, damage, assetShot, shotDelay, lastShot=0) :
    # -afair les degats de la balle tirer
    mobToBe["damage"] = damage
    mobToBe["assetShot"] = assetShot
    mobToBe["shotDelay"] = shotDelay
    mobToBe["lastShot"] = lastShot
    return mobToBe

#-afair les entites de types bullet

#_____Accesseur____________________________________________________________________
def is_shooting_ent(mob) :
	if "assetShot" in mob :
		return True
	else :
		return False


#_____Action____________________________________________________________________
def shoot(mob , nb) :
	#-afair
	#mob : le mob qui tir
	#nb : le "numero" du tir

	# -> cre une entite de type bullet -> definir les carac d'une balle
	return

def hit(bullet, entities , gameBorder, walls ) : 
    #entities c'est toutes les enttites qui peuvent bouffer la balle
    #gameBorder c'est les bords de la map pour tester si la balle sort
    #walls c'est le tableau double entree representant la map ou il y a toutes les plateformes "_" ""immuables""
    None
    # -afair : les tests de collisions
    is_hit = False #test si la balle touche quelquechose
    hit_entity=False  #test si la balle touche une entite ou pas
    entity = None #l'entite touche (le nom) le cas echeant
    log = (is_hit, hit_entity,entity) #pour tout renvoyer  
    return(log)





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