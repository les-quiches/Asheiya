import entity

void_collision = "0"
take_damage_collision = "1"

def hit_box_simple(asset,entity):
    y=len(asset)
    a=0
    for i in asset:
        a+=len(asset[i])
    x= a/(i+1)
    hit_box_entity=[entity["x"], entity["y"], entity["x"]+x, entity["y"]+y]# plage de l'hitbox de l'asset (point en haut a gauche puit en bas a doite)
    return(hit_box_entity)

def hit_box_complex_entity_can_take_damage(asset):
	"""
	recupere 
	"""
	y=len(asset)-1
	c=0
	a=[]
	for c in asset:
		a.append(len(c)-1)
	x = max(a)
	bloc = [[void_collision] * x for _ in range(y)]
	#maintenant que j'ai la taille de l'asset max je vais ramplacer les valeur interieur du bloc
	for i in range(0,len(asset)-1):
		for j in range(0,len(asset[i])-1):
			if asset[i][j] != " ":
				bloc[i][j] = take_damage_collision
			else:
				bloc[i][j] = void_collision
	return(bloc)

if (__name__=="__main__"):
	asset_test=entity.create_asset("Asheiya/Asset/Run_Right_0.txt")
	print asset_test
	print asset_test["Asset"][0]
	d=  hit_box_complex_entity_can_take_damage(asset_test["Asset"][0])
	print d







"""
	G{classtree}
	DESCRIPTION
	===========
		BLablabblublou

	PARAM
	=====
	@param var : poulet
	@type var : type(var)

	RETOUR
	======
	@return :  un bon repas
	@rtype : type(return)
	"""