#-*- coding:utf-8 -*
void_collision ="0"
_wall = "X"
Gostwall = "-"
EntityHitbox = "E"

import files
import sys

def Create_Shadow(CS_asset):#fonctionne
    """
    G{classtree}
    DESCRIPTION
    ===========
        Permet de donner un calque d'un asset

    PARAM
    =====

    @param CS_asset: Liste de tableau représentant un asset
    @type CS_asset : list

    RETOUR
    ======

    @return CS_Claque: renvois un calque de l'asset
    @rtype CS_Claque: list
"""
    CS_Claque=[]
    for frame in range(0,len(CS_asset)):
        c=0
        a=[]
        y=len(CS_asset[frame])
        CS_Claque.append([])
        for c in CS_asset[frame]:
            a.append(len(c)) # "a" représente la liste des longeurs de chaques lignes
        amax = 0
        for b in a : #on prend la plus grande ligne
            if b>amax :
                amax = b
                x = amax
        CS_Claque[frame]= [[void_collision] * x for _ in range(y)] #créé un tableau de x par y remplie de 0
                #maintenant que j'ai la taille de l'asset max je vais ramplacer les valeur interieur du CS_Claque
        for i in range(0,len(CS_asset[frame])):
            for j in range(0,len(CS_asset[frame][i])):
                if CS_asset[frame][i][j] != " ":
                    CS_Claque[frame][i][j] = EntityHitbox
                else:
                    CS_Claque[frame][i][j] = void_collision
    return(CS_Claque)

def Create_ShadowBackgrond(CG_filenum):
    """
    DESCRIPTION
    ===========
        créé une grille du jeux

    PARAM
    =====

    @param CG_filenum: Numéro de la liste a ouvrir
    @type CG_filenum : int

    RETOUR
    ======

    @return SEG_grid: grille du jeu
    @rtype SEG_grid: list

    """
    ca=dict()
    Background= files.OPEN_FILE_XML("GameZone/Zone_"+str(CG_filenum)+".txt")
    BackgroundGost= files.OPEN_FILE_XML("GameZone/Zone_"+str(CG_filenum)+"_GostWall.txt")
    mylist = Background.split("\r\n")
    myGostlist = BackgroundGost.split("\r\n")
    myGrid=[]
    for y in range(len(mylist)):
        myGrid.append([])
        for x in range(len(mylist[y])):
            element = mylist[y][x]
            myGrid[y].append([])
            if element == " ":
                myGrid[y][x]=void_collision
            else:
                Gostelement =myGostlist[y][x]
                if Gostelement != " " :
                    myGrid[y][x]=Gostwall
                else:
                    myGrid[y][x]= _wall
    return myGrid

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
    for i in range(0,len(Shadow_asset)):
        for j in range(0,len(Shadow_asset[i])):
            if Shadow_asset[i][j][0] != void_collision:
                Shadow_backgound[i+y][j+x] = Shadow_asset[i][j]

    return(Shadow_backgound)

def hit(bullet, entities , Shadow_backgound ) :#non tester
    """
    G{classtree}
    DESCRIPTION
    ===========
        Permet de vérifier si un projectile rentre en collision avec quelquechose.
        Si c'est le cas, prends des décisions en fonction de la nature de l'objet touché.

    PARAM
    =====
    @param bullet: le projectile dont on chercher à savoir la collision
    @type bullet: dict

    @param entities: toute les entités du jeu
    @type entities : list


    @param gameBorder:  Zone de l'ecran ou le joueur peu se mouvoir
    @type gameBorder : list

    @param walls: tableau ou sont réparti tout les mur, plateformes
    @type walls: list

    RETOUR

    @return log  : contient trois informations comme suit : True si le projectile rentre en collision (False sinon), True si c'était une entité vivante(False sinon), l'identifiant de cette entité le cas échéant.
    @rtype log : tuple
    """
    HIT_log = {}
    HIT_log["is_hit"] = False
    HIT_log["hit_entity"]=False
    HIT_log["entity"] = None

    HIT_collision_wall = detect_collision_wall(bullet,Shadow_backgound)

    if HIT_collision_wall != void_collision :
        if HIT_collision_wall != _wall:
            for HIT_entity in entities:
            HIT_collision_entity = detect_collision_entity(bullet,HIT_entity)
            if HIT_collision_entity :
                if bullet["origine"] == HIT_entity["Name"]:
                    HIT_log["is_hit"] = False
                    HIT_log["hit_entity"]=False
                    HIT_log["entity"] = None
                    pass
                if "livingEnt" in HIT_entity["Type"] :
                    HIT_log["is_hit"] = True
                    HIT_log["hit_entity"]=True  #test si la balle touche une entite ou pas
                    HIT_log["entity"] = HIT_entity
                    pass
        else:
            HIT_log["is_hit"] = True
            HIT_log["hit_entity"]=False  #test si la balle touche une entite ou pas
            HIT_log["entity"] = None

    return(HIT_log)

#_____Collision______________________________________________________________________
def Zone_Collision(ZC_Asset_Game_Zone,ZC_walls):#non tester
    """
    G{classtree}
    DESCRIPTION
    ===========
        Permet de détecter la collision entre une entité et le background

    PARAM
    =====
    @param ZC_ent:entité a tester
    @type ZC_ent:dict

    @param ZC_Asset_Game_Zone: asset de la zone de jeu
    @type  ZC_Asset_Game_Zone:list

    @param ZC_walls: asset des plateformes de jeu
    @type  ZC_walls:list

    RETOUR
    ======

    @return ZC_hitentwall : renvois ce qui a été détecter
    @rtype ZC_hitentwall :str
    """
    ZC_Shadow_walls=Create_Shadow(ZC_walls,Gostwall)
    ZC_Shadow_gameBorder=Create_Shadow(ZC_Asset_Game_Zone,_wall)
    ZC_Shadow_background=Add_Shadow(ZC_Shadow_walls,ZC_Shadow_gameBorder)
    return ZC_Shadow_background

#_____Collision______________________________________________________________________
def collision(COLLI_ent, COLLI_allEntityTest, COLLI_Shadow_background) : #non tester
    #x et y correspondent aux prochaines positions, utiles seulement pour le joueur sinon on recupere via entity
    """
    G{classtree}
    DESCRIPTION
    ===========
        Permet de détecter une collision

    PARAM
    =====
    @param COLLI_ent: entité dont l'on veux tester si il y a une collision
    @type COLLI_ent:dict

    @param COLLI_allEntityTest: toutes les entités qui pourrais etre en collision
    @type COLLI_allEntityTest: dict

    @param COLLI_Shadow_background: calque du backgound
    @type COLLI_Shadow_background : list

    @param COLLI_x: coordonnés x
    @type COLLI_x: int

    @param COLLI_y: coordonnés y
    @type COLLI_y: int

    RETOUR
    ======

    @return COLLI_log : Renvoie une liste d'information : s'il y a eu une collision dur,
    @rtype COLLI_log :bool
    """

    COLLI_hitentwall=detect_collision_wall(COLLI_ent,COLLI_Shadow_background)

    COLLI_log=[False,None,None]
    if COLLI_hitentwall == _wall:
        #detect un mur
        COLLI_log=[True,_wall,None]
    elif COLLI_hitentwall == Gostwall:
        COLLI_log=[True,Gostwall,None]

    elif COLLI_hitentwall == void_collision:
        COLLI_detect =[]
        for COLLI_Entity in COLLI_allEntityTest:
            if COLLI_Entity != COLLI_ent :
                COLLI_detect = detect_collision_entity(COLLI_ent,COLLI_Entity)
                if COLLI_detect != void_collision:
                    COLLI_log=[True,COLLI_detect,COLLI_Entity]
                    #collision entre les deux entiter
                    return COLLI_log
    else:
        files.SAVE_FILE_JSON(COLLI_ent,"log_wtf")
        # si on est ici c'est un BUG

    return COLLI_log



def detect_collision_wall(Entity,Shadow_background):#ne fonctionne pas
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
    x = Entity["x"]
    y = Entity["y"]
    Shadow_entity=[]
    Shadow_entity = Entity["ShadowAsset"]["Actual"]["Asset"][Entity["ShadowAsset"]["Actual"]["FrameNb"]]
    detect = void_collision
    for i in range(0,len(Shadow_entity)):
        for j in range(0,len(Shadow_entity[i])):
            if Shadow_entity[i][j] != void_collision:
                if Shadow_background[y+i][x+j][0] == _wall:
                     #detection collision wall
                     detect = _wall
                     return detect
                elif Shadow_background[i+y][j+x][0] == Gostwall:
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

def detect_collision_entity(DCE_Entity_1, DCE_Entity_2):#non tester
    """
    G{classtree}
    DESCRIPTION
    ===========
        Permet de dectecter une collision entre l'entité 1 et l'entité 2

    PARAM
    =====

    @param DCE_Entity_1: entité que l'on test
    @type DCE_Entity_1 : dict

    @param DCE_Entity_2: entité que l'on test
    @type DCE_Entity_2: dict

    RETOUR
    ======

    @return : Une information Si Vrais: il y a eu collision Sinon: il n'y a pas de collision
    @rtype :bool
    """
    DCE_x1=DCE_Entity_1["x"]
    DCE_y1=DCE_Entity_1["y"]
    DCE_x2=DCE_Entity_2["x"]
    DCE_y2=DCE_Entity_2["y"]
    DCE_Void_Shadow=create_void_shadow(140,42) #genere un fond vierge pour eviter de le calculer a chaque boucle
    DCE_Shadow_asset_1 = DCE_Entity_1["ShadowAsset"]["Actual"]["Asset"][DCE_Entity_1["ShadowAsset"]["Actual"]["FrameNb"]]
    DCE_Shadow_asset_2 = DCE_Entity_2["ShadowAsset"]["Actual"]["Asset"][DCE_Entity_2["ShadowAsset"]["Actual"]["FrameNb"]]
    DCE_Shadow = Add_Shadow(DCE_Shadow_asset_2,DCE_Void_Shadow,DCE_x2,DCE_y2)
    for i in range(0,len(DCE_Shadow_asset_1)):
        for j in range(0,len(DCE_Shadow_asset_1[i])):
            if DCE_Shadow_asset_1[i][j][0] != void_collision:
                if DCE_Shadow[i+DCE_y1][j+DCE_x1][0] != void_collision:
                    return DCE_Shadow[i+DCE_y1][j+DCE_x1][0]
    return void_collision


#ancien code mais toujours utiles
def hit_box_simple(entity):
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
    y=len(asset)-1
    a=[]
    for i in asset:
        a.append(len(i))

    amax=0
    for b in a :
        if b>amax :
            amax = b
    x = amax

    hit_box_entity=[entity["x"], entity["y"], entity["x"]+x, entity["y"]+y]# plage de l'hitbox de l'asset (point en haut a gauche puit en bas a doite)
    return hit_box_entity

#pour les tests
def show_Shadow(ss_Shadow):
    """
    G{classtree}
    DESCRIPTION
    ===========
        Permet d'afficher la fenetre principal

    PARAM
    =====

    @param doc : Tableau représentant la fennetre principal
    @type doc : list

    RETOUR
    ======
        Sans retour
    """
    s=""
    #couleur fond
    s+="\033[40m"
    #couleur white
    s+="\033[37m"
    #goto
    for y in range(0,len(ss_Shadow)):
        for x in range(0,len(ss_Shadow[y])):
          s+="\033["+str(y+1)+";"+str(x+1)+"H"
          #affiche
          s+=ss_Shadow[y][x][0]
    sys.stdout.write(s)


if (__name__=="__main__"):
    import background
    import time
    #init

    Shadow = Create_ShadowBackgrond(1)
    background.show_window(Shadow)
"""
    gameZone=[
    "Zone_1",
    ]
    a = time.time()
    assetGameZone={}
    for GameZone_doc in gameZone :
        assetGameZone[GameZone_doc]=background.create_window("GameZone/" + GameZone_doc + ".txt")
    assetGameZone["NumZone"]=1
    asset =assetGameZone["Zone_"+str(assetGameZone["NumZone"])]
    background.show_window(asset)


    while a > time.time()-3:
        None
    shadow=Create_Shadow(asset,"X")
    files.SAVE_FILE_JSON(shadow,"log_shadow")
    show_Shadow(shadow)


    a = time.time()
    while a > time.time()-3:
        None
    a = time.time()
    assetb= background.create_window("GameZone/Zone_1_TraversantPlateforme.txt")
    files.SAVE_FILE_JSON(assetb,"logGamentPlateforme.txt")


    while a > time.time()-3:
        None
    assetc=Create_Shadow(assetb,"=")
    show_Shadow(assetc)


    a = time.time()
    while a > time.time()-3:
        None
    shadow=Add_Shadow(assetc,shadow)
    show_Shadow(shadow)
"""
