#-*- coding:utf-8 -*
import test2

liste=[230,816,899,105,879]
print liste



def execute(liste) :
	for a in liste :
		if a>300 :
			liste.remove(a)
		print a
	return liste

execute(liste)
print liste


"""
	G{classtree}
	DESCRIPTION
	===========
		BLablabblublou

	PARAM
	=====
	@param var : poulet
	@type var : type(var)

	RETOUR
	======
	@return :  un bon repas
	@rtype : type(return)
	"""
