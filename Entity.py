
def create_entity(Name, Type, X, Y, Life, Armor, Speed):
    Entity=dict()
    Entity["Name"]= Name
    Entity["x"]= X
    Entity["y"]= Y
    Entity["Type"]= type
    Entity["Life"]= Life
    Entity["Armor"]= Armor
    Entity["Speed"]=Speed


    return(Entity)

def move_entity(Entity,x,y):
    Entity["x"]=x
    Entity["y"]=y
    return(Entity)

def show_entity(doc, X, Y, color_bg, color_txt,open_doc ="0"):
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
