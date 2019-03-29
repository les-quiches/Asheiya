import sys
import select

import tty

def isData():
	#recuperation evenement clavier
	return select.select([sys.stdin], [], [], 0) == ([sys.stdin], [], [])


def Init():
    tty.setcbreak(sys.stdin.fileno())

def Interact():
    if isData():
        print sys.stdin.read(1)

def Run():
    while True:
        Interact()

Init()
Run()
