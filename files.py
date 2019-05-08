#-*- coding:utf-8 -*
import json
import sys
import os

#Gestion document

#json
#utilisation dictionnaire


def OPEN_FILE_JSON(filename):
def is_ground_beneath(pos,gameBorder,walls) :
    """
    G{classtree}
    DESCRIPTION
    ===========
        Permet de récuperer un fichier

    PARAM
    =====

    @param filename : Chemin d'acces du fichier à ouvrir
    @type filename :str

    RETOUR
    ======
    @return file_open : renvoi le contenue du fichier
    @rtype file_open :dict
    """
    #Lit le fichier selectionner (filename)
    #renvois le contenue (en dictionnaire ou liste) du fichier lu
    with open(filename,"r") as file:
        file_open = json.load(file)
    return(file_open)


def SAVE_FILE_JSON(save,filename):
    """
    G{classtree}
    DESCRIPTION
    ===========
        Permet de sauvegarder un fichier

    PARAM
    =====

    @param save: donnée a sauvegarder
    @type save: dict

    @param filename : Chemin d'acces du fichier à sauvegarder
    @type filename :str

    RETOUR
    ======
        Sans retour
    """
    #ecrase le fichier "filename" pour le remplacer par "save"
    with open(filename, 'w') as file:
        json.dump(save, file)
    return()

#XML
#utilisation str str
def SAVE_FILE_XML(save,filename):
    """
    G{classtree}
    DESCRIPTION
    ===========
        Permet de sauvegarder un fichier

    PARAM
    =====

    @param save: donnée a sauvegarder
    @type save: str

    @param filename : Chemin d'acces du fichier à sauvegarder
    @type filename :str

    RETOUR
    ======
        Sans retour
    """
    #ecrase le fichier "filename" pour le remplacer par "save"
    myFile=open(filename,"w")
    myFile.write(save)
    myFile.close()
    return()

def OPEN_FILE_XML(filename):
    """
    G{classtree}
    DESCRIPTION
    ===========
        Permet de récuperer un fichier

    PARAM
    =====

    @param filename : Chemin d'acces du fichier à ouvrir
    @type filename :str

    RETOUR
    ======
    @return file_open : renvoi le contenue du fichier
    @rtype file_open :str
    """
    #Lit le fichier selectionner "filename" et le renvois
    myFile=open(filename,"r")
    txt=myFile.read()
    myFile.close()
    return(txt)
