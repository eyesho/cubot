#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Filename      : colordetection.py
# Author        : Kim K
# Created       : Tue, 26 Jan 2016
# Last Modified : Sun, 31 Jan 2016


from sys import exit as Die
try:
    import sys
except ImportError as err:
    Die(err)

class ColorDetection:

    def get_color_name(self, hsv):
        """ Get the name of the color based on the hue.

        :returns: string
        """
        (h,s,v) = hsv
        print((h,s,v))
        if h>170 and s>170 and v>170:
			return 'white'  
        if v < 100 :
			if s<130:
				return 'blue'
			else:
				return 'green'
        if s < 110 :
			return 'red'	
        if s>175 :			
			return 'yellow'
        if s<175 :
			
			return  'orange'
	
        return 'white'

    def name_to_rgb(self, name):
        """
        Get the main RGB color for a name.
		
		
		
		if h>170 and s>170 and v>170:
			return 'white'  
        if v < 100 :
			if s<130:
				return 'blue'
			else:
				return 'green'
        if s < 110 :
			return 'red'	
        if s>175 :			
			return 'yellow'
        if s<175 :
			
			return  'orange'
			
			
			
			
			
		
		
		
        :param name: the color name that is requested
        :returns: tuple
        """
        color = {
            'red'    : (0,0,255),
            'orange' : (0,165,255),
            'blue'   : (255,0,0),
            'green'  : (0,255,0),
            'white'  : (255,255,255),
            'yellow' : (0,255,255)
        }
        return color[name]

    def average_hsv(self, roi):
        """ Average the HSV colors in a region of interest.

        :param roi: the image array
        :returns: tuple
        """
        h   = 0
        s   = 0
        v   = 0
        num = 0
        for y in range(len(roi)):
            if y % 10 == 0:
                for x in range(len(roi[y])):
                    if x % 10 == 0:
                        chunk = roi[y][x]
                        num += 1
                        h += chunk[0]
                        s += chunk[1]
                        v += chunk[2]
        h /= num
        s /= num
        v /= num
        return (int(h), int(s), int(v))

ColorDetector = ColorDetection()
