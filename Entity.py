
def create_entity(Name, Type, X, Y, Life, Shild, Speed):
    Entity=dict()
    Entity["Name"]= Name
    Entity["x"]= X
    Entity["y"]= Y
    Entity["Type"]= type
    Entity["Life"]= Life
    Entity["Shild"]= Shild
    Entity["Speed"]=Speed


    return(Entity)

def move_entity(Entity,x,y):
    Entity["x"]=x
    Entity["y"]=y
    return(Entity)
