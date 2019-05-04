import entity

def create_shooting_mob(mobToBe, assetShot, shotDelay, lastShot=0) :
	mobToBe["assetShot"] = assetShot
	mobToBe["shotDelay"] = shotDelay
	mobToBe["lastShot"] = lastShot
	return mobToBe

def is_shooting_mob(mob) :
	if "assetShot" in mob :
		return True
	else :
		return False

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




#___Jeux de test_______________________________________________
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
    for Asheiya_doc in ["Run_Right_0","Wait_Right_0","Run_Left_0","Wait_Left_0","Run_Right_45","Wait_Right_45"]:# a terme on utilisera "Asheiya_asset" ou un constructeur de txt
        Asset[Asheiya_doc]=entity.create_asset("Asheiya/Asset/" + Asheiya_doc + ".txt") #chargement Asset
    player = entity.create_entity(Name,Type,X,Y,Vx,Vy,Life,Armor,Speed, LastTime, Asset)

    print is_shooting_mob(player)


    assetShot = {}
    for Shot_doc in ["Gun_Horizontal","Gun_Slash","Gun_UnSlash","Gun_Vertical"] :
    	assetShot[Shot_doc] =entity.create_asset("Projectile/"+Shot_doc+".txt") 
    fireDelay = 3
    player = create_shooting_mob(player,assetShot,fireDelay)

    print player.keys()
    print is_shooting_mob(player)