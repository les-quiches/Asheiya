import sys
import os

import files
f =files

def create_wd(filename):
    wd = dict()
    wd["window"]=[]
    myfile=f.OPEN_FILE_XML(filename)
    doc = f.SPLIT_LINES(myfile) # axe y
    for x in doc:# axe x
        y = list(x)
        wd["window"].append(y)
    return(wd)

def show_wd(doc):
	#couleur fond
	sys.stdout.write("\033[40m")
	#couleur white
	sys.stdout.write("\033[37m")
	#goto
	for y in range(0,len(doc["window"])):
		for x in range(0,len(doc["window"][y])):
			s="\033["+str(y+1)+";"+str(x+1)+"H"
			sys.stdout.write(s)
			#affiche
			sys.stdout.write(doc["window"][y][x])

def show(doc, X, Y, color_bg, color_txt,open_doc ="0"):
    #couleur fond
    sys.stdout.write("\033["+str(color_bg)+"m")
	#couleur white
    sys.stdout.write("\033["+str(color_txt)+"m")
    if open_doc != "0":
        doc= create(open_doc)
    for y in range(0,len(doc["window"])):
		for x in range(0,len(doc["window"][y])):
			s="\033["+str(Y+y+1)+";"+str(X+x+1)+"H"
			sys.stdout.write(s)
			#affiche
			sys.stdout.write(doc["window"][y][x])


""" txt  bg
    30, 40 : noir ;
    31, 41 : rouge ;
    32, 42 : vert ;
    33, 43 : jaune ;
    34, 44 : bleu ;
    35, 45 : rose ;
    36, 46 : cyan ;
    37, 47 : gris.

"""
