import entity

#_____Create____________________________________________________________________
def create_shooting_ent(Entity, damage, assetShot, shotDelay, lastShot=0) :

    """
    G{classtree}
    DESCRIPTION
    ===========
        Permet d'ajouter les parametres de projectile tiré a une entite

    PARAM
    =====

    @param Entity: Entiter a modifier
    @type Entity : dict

    @param damage: Damage du projectile
    @type damage : int

    @param assetShot :Asset du projectile
    @type assetShot :list

    @param shotDelay : temps entre chaque projectile
    @type shotDelay :int

    @param lastShot : représdente le dernier tire
    @type  :int

    RETOUR
    ======

    @return ca  : une Entiter de type projectile tiré
    @rtype ca :def
    """
    assert type(Entity) is dict
    assert "entity" in Entity["Type"]
    Entity["damage"] = damage
    Entity["assetShot"] = assetShot
    Entity["shotDelay"] = shotDelay
    Entity["lastShot"] = lastShot
    Entity["Type"].append("shootingEnt")
    return Entity

#-afair les entites de types bullet

#_____Accesseur____________________________________________________________________
def is_shooting_ent(mob) :
    """
    G{classtree}
    DESCRIPTION
    ===========
        Permet de vérifier si il possède un asset

    PARAM
    =====

    @param mob:
    @type mob : dict


    RETOUR
    ======
        Sans retour
    """
	if "assetShot" in mob :
		return True
	else :
		return False


#_____Action____________________________________________________________________
def shoot(mob , nb) :
    """
    G{classtree}
    DESCRIPTION
    ===========
        Permet de vérifier si il possède un asset

    PARAM
    =====

    @param mob:
    @type mob : dict

    @param nb: numéro du tire
    @type nb: long

    RETOUR

    @return ca  : une Entiter de type projectile tiré
    @rtype ca :def
    """
	#-afair
	#mob : le mob qui tir
	#nb : le "numero" du tir
	# -> cre une entite de type bullet -> definir les carac d'une balle
	return

def hit(bullet, entities , gameBorder, walls ) :
    """
    G{classtree}
    DESCRIPTION
    ===========
        Permet de vérifier si il possède un asset

    PARAM
    =====

    @param entities:
    @type entities : dict

    @param bullet:
    @type lullet:

    @param gameBorder:  Zone de l'ecran ou le joueur peu se mouvoir
    @type gameBorder : list

    @param walls: dictionnaire ou sont réparti tout les mur, plateformes
    @type wall: dict

    RETOUR

    @return log  : donné renvoyer si la balle touche quelquechose, si la balle touche une entite ou pas et l'entité si toucher
    @rtype log : tuple
    """
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
    X = 20
    Y = 37
    Asset = {}
    Asset["position"]=["Wait","Right",0]
    for Asheiya_doc in ["Run_Right_0","Wait_Right_0","Run_Left_0","Wait_Left_0","Run_Right_45","Wait_Right_45"]:# a terme on utilisera "Asheiya_asset" ou un constructeur de txt
        Asset[Asheiya_doc]=entity.create_asset("Asheiya/Asset/" + Asheiya_doc + ".txt") #chargement Asset
    player = entity.create_entity(Name,X,Y,Asset)
