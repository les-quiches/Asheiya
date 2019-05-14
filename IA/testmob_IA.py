#-*- coding:utf-8 -*

def execute (mymob, allEntity, walls) :
	
	if mymob["x"]>80 :
		mymob["Vx"] = -1
	elif mymob["x"]<10 :
		mymob["Vx"] = 1
	if mymob["y"]>38 :
		mymob["Vy"] = -1
	elif mymob["y"]<5 :
		mymob["Vy"] = 1s