#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Filename      : normalizer.py
# Author        : Kim K
# Created       : Sat, 30 Jan 2016
# Last Modified : Mon, 01 Feb 2016


from sys import exit as Die
try:
    import sys
    import json
    import mover as mv 
    from time import sleep
except ImportError as err:
    Die(err)


class Normalizer:

    def algorithm(self, alg, language):
        """ Noramlize an algorithm from the
        json-written manual.

        :param alg: The algorithm itself
        :returns: list
        """
        with open('solve-manual.json') as f:
            manual = json.load(f)

        solution = []
        
        for notation in alg.split(' '):
			print(notation)
			
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
			
			
			solution.append(manual[language][notation])
        return solution

normalize = Normalizer()
