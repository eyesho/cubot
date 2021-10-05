from sys import exit as Die
try:
    import sys
    import json
    import mover as mv 
    from time import sleep
    import random
except ImportError as err:
    Die(err)

def RandScramble():

	for i in range(1,12):
		notation=random.randint(1,18)
		print (notation)
	
		if notation==1:
			mv.U()
		if notation==2:
			mv.D()
		if notation==3:
			mv.L()
		if notation==4:
			mv.R()
		if notation==5:
			mv.F()
		if notation==6:
			mv.B()
		
		if notation==7:
			mv.UA()
		if notation==8:
			mv.DA()
		if notation==9:
			mv.LA()
		if notation==10:
			mv.RA()
		if notation==10:
			mv.FA()
		if notation==12:
			mv.BA()
		
		if notation==13:
			mv.UU()
		if notation==14:
			mv.DD()
		if notation==15:
			mv.LL()
		if notation==16:
			mv.RR()
		if notation==17:
			mv.FF()
		if notation==18:
			mv.BB()	
					
