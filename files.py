#-*- coding:utf-8 -*

import json
import sys
import os

#Gestion document

#json
#utilisation dictionnaire


def OPEN_FILE_JSON(filename):
    #Lit le fichier selectionner (filename)
    #renvois le contenue (en dictionnaire ou liste) du fichier lu
    with open(filename,"r") as file:
        file_open = json.load(file)
    return(file_open)


def SAVE_FILE_JSON(save,filename):
    #ecrase le fichier "filename" pour le remplacer par "save"
    with open(filename, 'w') as file:
        json.dump(save, file)
    return()

#XML
#utilisation str str
def SAVE_FILE_XML(save,filename):
    #ecrase le fichier "filename" pour le remplacer par "save"
    myFile=open(filename,"w")
    myFile.write(save)
    myFile.close()
    return()

def OPEN_FILE_XML(filename):
    #Lit le fichier selectionner "filename" et le renvois
    myFile=open(filename,"r")
    txt=myFile.read()
    myFile.close()
    return(txt)

def SPLIT(doc,spliter):
    #permet de coupee un txt pour le transformer en liste
    #doc = srt a split
    #spliter type str est le mots/ simbole / phrase ou le txt doit etre coupe
    doc_split=doc.split(spliter)
    return(doc_split)

def SPLIT_LINES(doc):
    doc_split=doc.splitlines()
    return(doc_split)
