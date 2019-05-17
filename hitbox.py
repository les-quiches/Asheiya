#-*- coding:utf-8 -*
void_collision ="0"
random_zone="O"
damage_Zone= "¤"
_wall = "X"
Gostwall = "-"
take_damage = "."

import files

def Add_Shadow(Shadow_asset,Shadow_backgound,x=0,y=0):
    """
        G{classtree}
        DESCRIPTION
        ===========
            Ajoute un claque d'asset sur un calque de backgound
        PARAM
        =====

        @param Shadow_asset: Calque de l'asset
        @type Shadow_asset :list

        @param Shadow_backgound: Calque du backgound
        @type Shadow_backgound :list

        @param x: position x du calque de l'asset
        @type x :int

        @param y: position y du calque de l'asset
        @type y :int
        RETOUR
        ======

        @return Shadow_backgound: Calque du background avec l'asset intégrer
        @rtype Shadow_backgound :list
    """
    for i in range(0,len(Shadow_asset)-1):
        for j in range(0,len(Shadow_asset[i])-1):
            if Shadow_asset[i][j] != void_collision:
                Shadow_backgound[i+y][j+x] = Shadow_asset[i][j]

    return(Shadow_backgound)


def detect_collision_wall(Entity,Shadow_backgound):
    """
    G{classtree}
    DESCRIPTION
    ===========
        Permet de dectecter une collision entre une entité et une bordure du jeu

    PARAM
    =====
    @param Entity: entité que l'on test
    @type Entity : dict

    @param Shadow_backgound: Masque background
    @type Shadow_backgound: list

    RETOUR
    ======

    @return detect: True s'il y a une collision avec un mur, False sinon.
    @rtype detect: str
    """
    asset = Entity["Asset"]["Actual"]["Asset"][Entity["Asset"]["Actual"]["FrameNb"]]
    x = Entity["x"]
    y = Entity["y"]
    Shadow_entity = hit_box_complex(asset,random_zone)
    detect = void_collision
    for i in range(0,len(Shadow_entity)):
        for j in range(0,len(Shadow_entity[i])):
            if Shadow_entity[i][j] != void_collision:
                if Shadow_backgound[y+i][x+j] == _wall:
                     #detection collision wall
                     detect = _wall
                     return detect
                elif Shadow_backgound[i+y][j+x] == Gostwall:
                    detect = Gostwall
    return detect


def create_void_shadow(Xmax,Ymax):
    """
    G{classtree}
    DESCRIPTION
    ===========
        Permet de créer un calque vide de taille Xmax / Ymax

    PARAM
    =====
    @param Xmax: taille du calque, sur l'axe x que l'on veut créer
    @type Xmax: int

    @param Ymax: taille du calque, sur l'axe y que l'on veut créer
    @type Ymax: int

    RETOUR
    ======
    @return Shadow: Calque de dimmantion Xmax, Ymax
    @rtype Shadow:list
    """
    Shadow = [[void_collision] * Xmax for _ in range(Ymax)]
    return Shadow

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

    @return : Une information Si Vrais: il y a eu collision Sinon: il n'y a pas de collision
    @rtype :bool
    """
    files.SAVE_FILE_JSON((Entity_1["Name"],Entity_2["Name"]),"logname")
    x1=Entity_1["x"]
    y1=Entity_1["y"]
    x2=Entity_2["x"]
    y2=Entity_2["y"]
    asset_entity_1 = Entity_1["Asset"]["Actual"]["Asset"][Entity_1["Asset"]["Actual"]["FrameNb"]]
    asset_entity_2 = Entity_2["Asset"]["Actual"]["Asset"][Entity_2["Asset"]["Actual"]["FrameNb"]]
    a2,b2,x_2,y_2=hit_box_simple(Entity_2)
    a1,b1,x_1,y_1=hit_box_simple(Entity_2)
    x = max(x_1,x_2)
    y = max(y_1,y_2)
    Void_Shadow=create_void_shadow(x,y)
    Shadow_asset_1 = hit_box_complex(asset_entity_1,random_zone)
    Shadow_asset_2 = hit_box_complex(asset_entity_2,random_zone)
    Shadow = Add_Shadow(Shadow_asset_2,Void_Shadow,x2,y2)

    files.SAVE_FILE_JSON(Shadow_asset_1,"logasset1")
    files.SAVE_FILE_JSON(Shadow_asset_2,"logasset2")
    files.SAVE_FILE_JSON(Shadow,"logshadow")

    for i in range(0,len(Shadow_asset_1)-1):
        for j in range(0,len(Shadow_asset_1[i])-1):
            if Shadow_asset_1[i][j] != void_collision:
                files.SAVE_FILE_JSON((i+y1,j+x1),"log")
                if Shadow[i+y1][j+x1] != void_collision:
                    return True
    return False



def hit_box_simple(entity):  #####_____OBSOLETE______
    """
    G{classtree}
    DESCRIPTION
    ===========
        Permet de donner l'hitbox simplifiée d'un asset

    PARAM
    =====

    @param entity: Entite dont on veut obtenir l'asset
    @type entity: dict


    RETOUR
    ======

    @return : quatre positions correspondants aux valeurs extremes des contours de l'entite. Permet de positionner les quatre coins.
    @rtype : list
    """
    asset= entity["Asset"]["Actual"]["Asset"][entity["Asset"]["Actual"]["FrameNb"]]
    y=len(asset)
    a=[]
    for i in asset:
        a.append(len(i))

    # x = max(a) -afair , la fonction bug for no reason, elle vide la liste a
    amax=0
    for b in a :
        if b>amax :
            amax = b
    x = amax

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
        a.append(len(c)) # "a" représente la liste des longeurs de chaques lignes

    # x = max(a)
    # -afair , la fonction bug for no reason, elle vide la liste a
    amax = 0
    for b in a : #on prend la plus grande ligne
        if b>amax :
            amax = b
    x = amax

    bloc=[]
    bloc= [[void_collision] * x for _ in range(y)] #créé un tableau de x par y remplie de 0
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

    assetBullet = bullet["Asset"]["Actual"]["Asset"]
    Shadow_bullet=hitbox.hit_box_complex(assetBullet,damage_Zone)
