#-*- coding:utf-8 -*

import files

def create_story(cs_storyFile, cs_maxLigne,cs_LastTime):
    """
    G{classtree}
    DESCRIPTION
    ===========
        Permet de passé à la ligne suivante

    PARAM
    =====

    @param SNL_Story : histoire a changer de ligne
    @type SNL_Story :dict

    RETOUR
    ======
    @return cs_Story : Histoire Créer
    @rtype cs_Story :dict
    """
    cs_Story = {}
    cs_Story["Name"]=files.READ_FILELIGNE_XML(cs_storyFile,1)
    cs_Story["File"]=cs_storyFile
    cs_Story["MaxLigne"]=cs_maxLigne
    cs_Story["Ligne"]=5
    cs_Story["LastTime"]=cs_LastTime
    cs_Story["Speed"]=8
    i=1
    cs_txt=[]
    while i <= 5:
        cs_file=files.READ_FILELIGNE_XML(cs_storyFile,i)
        cs_txt.append(cs_file)
        i+=1
    cs_Story["Txt"]=cs_txt
    return cs_Story

def Story_Next_Ligne(SNL_Story):
    """
    G{classtree}
    DESCRIPTION
    ===========
        Permet de passé à la ligne suivante

    PARAM
    =====

    @param SNL_Story : histoire a changer de ligne
    @type SNL_Story :dict

    RETOUR
    ======

    """
    del SNL_Story["Txt"][0]
    SNL_Story["Ligne"]+=1
    if SNL_Story["Ligne"] <= SNL_Story["MaxLigne"]:
         SNL_Story["Txt"].append(files.READ_FILELIGNE_XML(SNL_Story["File"],SNL_Story["Ligne"]))
    else:
        SNL_Story["Txt"].append([" "])
        SNL_Story["Ligne"]=0
