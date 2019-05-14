#-*- coding:utf-8 -*
void_collision ="0"
random_zone="O"
damage_Zone= "¤"
wall = "X"
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

        @return Shadow_backgound: Calque du background avec l'asset intéger
        @rtype Shadow_backgound :list
    """
    files.SAVE_FILE_JSON(Shadow_backgound,"Shadow_backgound")
    files.SAVE_FILE_JSON(Shadow_asset,"Shadow_asset")

    for i in range(0,len(Shadow_asset)):
        for j in range(0,len(Shadow_asset[i])):
            if Shadow_asset[i][j] != void_collision:
                Shadow_backgound[i+y][j+x] = Shadow_asset[i][j]

    return(Shadow_backgound)


def detect_collision_wall(Entity_Asset,Shadow_backgound,x,y):
    """
    G{classtree}
    DESCRIPTION
    ===========
        Permet de dectecter une collision entre une entité et unebordure du jeu

    PARAM
    =====
    @param Entity_Asset: entité que l'on test
    @type Entity_Asset : dict

    @param Shadow_backgound: Masque background
    @type Shadow_backgound: list

    RETOUR
    ======

    @return : True s'il y a une collision avec un mur, False sinon.
    @rtype :bool
    """
    Shadow_entity = hit_box_complex(Entity_Asset,random_zone)
    for i in range(0,len(Shadow_entity)):
        for j in range(0,len(Shadow_entity[i])):
            if Shadow_entity[i][j] != void_collision:    
                if Shadow_backgound[x+i][y+j] == wall: #detection collision wall
                    return True
    return False


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
    Shadow =[]
    x=[]
    for i in range(0,Xmax):
        x.append(void_collision)
    for j in range(0,Ymax):
        Shadow[j]=x
    return Shadow

def detect_collision_entity(Entity_1,asset_entity_1, Entity_2, asset_entity_2):
    """
    G{classtree}
    DESCRIPTION
    ===========
        Permet de dectecter une collision entre l'entité 1 et l'entité 2

    PARAM
    =====

    @param Entity_1: entité que l'on test
    @type Entity_1 : dict

    @param asset_entity_1: asset de l'entite
    @type asset_entity_1 :list

    @param asset_entity_2: asset de l'entite
    @type asset_entity_2: list

    @param  Entity_2: entité que l'on test
    @type Entity_2: dict

    RETOUR
    ======

    @return : Une information Si Vrais: il y a eu collision Sinon: il n'y a pas de collision
    @rtype :bool
    """
    x1=Entity_1["x"]
    y1=Entity_1["y"]
    x2=Entity_2["x"]
    y2=Entity_2["y"]
    Void_Shadow=create_void_shadow(x2+len(asset_entity_2[len(asset_entity_2)],len(asset_entity_2)))
    Shadow_asset_1 = hit_box_complex(asset_entity_1,random_zone)
    Shadow_asset_2 = hit_box_complex(asset_entity_2,random_zone)
    Shadow = Add_Shadow(Shadow_asset_2,Void_Shadow,x2,y2)
    for i in range(0,len(Shadow_asset_1)):
        for j in range(0,len(Shadow_asset_1[i])):
            if Shadow_asset_1[i][j] != void_collision:
                if Shadow[i+y1][j+x1] != void_collision:
                    return True
    return False



def hit_box_simple(asset,entity):  #####_____OBSOLETE______
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
        a.append(len(c)) # "a" représente la liste des longeurs de chaques lignes
    x = max(a) #on prend la plus grande ligne
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
