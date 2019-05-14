global liste

import test

mob = {"Name" : "player", "pv" : 10}
nomob = {"Name" : "notplayer", "pv" : 560}
liste = []
liste.append(nomob)
liste.append(mob)

print liste
liste = test.execute(liste)
print liste