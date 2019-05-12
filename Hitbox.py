#-*- coding:utf-8 -*
void_collision ="0"
random_zone="O"
damage_Zone= "%"
wall = "X"
take_damage = "1"


def Add_Shadow(Shadow_asset,Shadow_backgound):
    """
        G{classtree}
        DESCRIPTION
        ===========
            Ajoute
        PARAM
        =====

        @param Shadow_asset:
        @type Shadow_asset :list

        @param Shadow_backgound:
        @type Shadow_backgound :list

        RETOUR
        ======

        @return Shadow_backgound:
        @rtype Shadow_backgound :list
    """
    for i in range(0,len(Shadow_asset)):
        for j in range(0,len(Shadow_asset[i])):
            if Shadow_asset[i][j] != void_collision:
                Shadow_backgound[i][j] = Shadow_asset[i][j]
    return(Shadow_backgound)
def detect_collision_wall(Entity,Shadow_backgound):
    """
    G{classtree}
    DESCRIPTION
    ===========
        Permet de dectecter une collision entre une entité et bordure du jeu

    PARAM
    =====
    @param Entity_1: entité que l'on test
    @type Entity_1 : dict

    @param Shadow_backgound: Masque background
    @type Shadow_backgound: list

    RETOUR
    ======

    @return :
    @rtype :
    """
    x=Entity["x"]
    y=Entity["y"]
    asset= Entity["Asset"]
    Shadow_entity = hit_box_complex(asset,random_zone)
    for i in range(0,len(Shadow_entity)):
        for j in range(0,len(Shadow_entity[i])):
            if Shadow_entity[i][j] != void_collision:    #detection collision wall
                if Shadow_backgound[x+i][y+j] == wall:
                    return True
    return False


def detect_collision_entity(Entity_1, Entity_2):
    """
    G{classtree}
    DESCRIPTION
    ===========
        Permet de dectecter une collision entre l'entité 1 et l'entité 2

    PARAM
    =====

    @param Entity_1: entité que l'on test
    @type Entity_1 : dict

    @param  Entity_2: entité que l'on test
    @type Entity_2: dict

    RETOUR
    ======

    @return :
    @rtype :
    """
    x=Entity_bullet["x"]
    y=Entity_bullet["y"]
    asset_entity_1= Entity_1["Asset"]
    asset_entity_1= Entity_1["Asset"]
    Shadow_asset_1 = hit_box_complex(asset_entity_1,random_zone)
    Shadow_asset_2 = hit_box_complex(asset_entity_2,random_zone)
    for i in range(0,len(Shadow_asset_1)):
        for j in range(0,len(Shadow_asset_1[i])):
            if Shadow_asset_1[i][j] != void_collision:
                if Shadow_asset_2 != void_collision:
                    return True
    return False



def hit_box_simple(asset,entity):
    """
    G{classtree}
    DESCRIPTION
    ===========
        Permet de donner l'hitbox simplifiée d'un asset

    PARAM
    =====

    @param asset: Tableau représentant un asset
    @type asset : list

    @param entity: Entite dont on veut obtenir l'asset
    @type entity: dict


    RETOUR
    ======

    @return : quatre positions correspondants aux valeurs extremes des contours de l'entite. Permet de positionner les quatre coins.
    @rtype : list
    """
    y=len(asset)
    a=0
    for i in asset:
        a+=len(asset[i])
    x= a/(i+1)
    hit_box_entity=[entity["x"], entity["y"], entity["x"]+x, entity["y"]+y]# plage de l'hitbox de l'asset (point en haut a gauche puit en bas a doite)
    return(hit_box_entity)

def hit_box_complex(asset,type_hitbox):
    """
    G{classtree}
    DESCRIPTION
    ===========
        Permet de donner un calque d'un asset

    PARAM
    =====

    @param asset: Tableau représentant un asset
    @type asset : list

    @param type_hitbox: type de l'hitbox
    @type type_hitbox: str

    RETOUR
    ======

    @return : renvois un calque de l'asset
    @rtype : list
"""
    y=len(asset)
    c=0
    a=[]
    for c in asset:
        a.append(len(c))
    x = max(a)
    bloc = [[void_collision] * x for _ in range(y)]
    #maintenant que j'ai la taille de l'asset max je vais ramplacer les valeur interieur du bloc
    for i in range(0,len(asset)):
        for j in range(0,len(asset[i])):
            if asset[i][j] != " ":
                bloc[i][j] = type_hitbox
            else:
                bloc[i][j] = void_collision
    return(bloc)


if (__name__=="__main__"):
    import background
    import time
    #init
    gameZone=[
    "Zone_1",
    ]
    a = time.time()
    window=background.create_window("Windows.txt")
    assetGameZone={}
    assetb=background.create_window("GameZone/Zone_1_TraversantPleteforme.txt")
    for GameZone_doc in gameZone :
        assetGameZone[GameZone_doc]=background.create_window("GameZone/" + GameZone_doc + ".txt")
    assetGameZone["NumZone"]=1
    asset =assetGameZone["Zone_"+str(assetGameZone["NumZone"])]
    background.show_window(asset)

    while a > time.time()-3:
        None
    asset=hit_box_complex(asset,"X")
    background.show_window(asset)

    a = time.time()
    while a > time.time()-3:
        None
    assetb=hit_box_complex(assetb,"=")
    asset=Add_Shadow(assetb,asset)
    background.show_window(asset)
