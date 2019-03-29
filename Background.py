import sys
import os

import Files
f =Files

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
