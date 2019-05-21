global liste

import test

def move(ent) :
    mob["pv"]+=1
    return mob

mob = {"Name" : "player", "pv" : 10}
nomob = {"Name" : "notplayer", "pv" : 560}

liste = []
liste.append(mob)
liste.append(nomob)

print "liste debut", liste
print len(liste)

for poulet in liste :
    print "debut" , poulet
    poulet = move(poulet)
##    poulet = poulet2
#    print "poulet2",  poulet2
    print "poulet fin", poulet


print "liste fin",  liste
