
from sys import exit as Die
try:

    import kociemba
    import argparse

    from combiner import combine
    from tkinter import *
    from video import webcam
    from normalizer import normalize
    from fractions import Fraction
    import sys
	
except ImportError as err:
    Die(err)


class Qbr:

    def __init__(self, normalize, language):
        self.humanize = 1
        self.language = (language[0]) if isinstance(language, list) else language

    def run(self):
        state         = webcam.scan()
        if not state:
            print('\033[0;33m[QBR SCAN ERROR] Ops, you did not scan in all 6 sides.')
            print('Please try again.\033[0m')
            Die(1)

        unsolvedState = combine.sides(state)
        print (unsolvedState)
        try:
            algorithm     = kociemba.solve(unsolvedState)
            length        = len(algorithm.split(' '))
        except Exception as err:
            print('\033[0;33m[QBR SOLVE ERROR] Ops, you did not scan in all 6 sides correctly.')
            print('Please try again.\033[0m')
            Die(1)

        print('-- SOLUTION --')
        print('Starting position:\n    front: green\n    top: white\n')
        print(algorithm, '({0} moves)'.format(length), '\n')

        if self.humanize:
            manual = normalize.algorithm(algorithm, self.language)
            for index, text in enumerate(manual):
                print('{}. {}'.format(index+1, text))
        Die(0)



def clicked():
 
	res = "Welcome to " + txt.get()
 
	lbl.configure(text= res)
	Qbr(1,'en').run()
	
def rands():
 
	res = "Welcome to " + txt.get()
	
			if notation=='U':
				mv.U()
			if notation=='D':
				mv.D()
			if notation=='R':   #Exchange coordinate after scaned
				mv.L()
			if notation=='L':
				mv.R()
			if notation=='B':
				mv.F()				
			if notation=='F':
				mv.B()
				
			if notation=="U'" :
				mv.UA()
			if notation=="D'" :
				mv.DA()
			if notation=="R'" :
				mv.LA()
			if notation=="L'" :
				mv.RA()
			if notation=="B'" :
				mv.FA()				
			if notation=="F'" :
				mv.BA()						
			
			
			if notation=="U2" :
				mv.UU()
			if notation=="D2" :
				mv.DD()
			if notation=="R2" :
				mv.LL()
			if notation=="L2" :
				mv.RR()
			if notation=="B2" :
				mv.FF()				
			if notation=="F2" :
				mv.BB()		

if __name__ == '__main__':
 
	window = Tk()
 
	window.title("Welcome to cubic app")
 
	window.geometry('100x200')
 
	lbl = Label(window, text="Formula")
 
	lbl.grid(column=5, row=5)
 
	txt = Entry(window,width=10)
 
	txt.grid(column=5, row=6)
 
 
 

 
	btn = Button(window, text="Scramble", command=rands)
	
	btn.grid(column=5, row=7)
	
	
	btn1 = Button(window, text="Solve", command=clicked)
	
	btn1.grid(column=6, row=6)
	
	
	
	window.mainloop()



