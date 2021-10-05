#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Filename      : video.py
# Author        : Kim K
# Created       : Fri, 29 Jan 2016
# Last Modified : Sun, 31 Jan 2016


from sys import exit as Die
try:
    import sys
    import cv2
    from colordetection import ColorDetector
    import picamera
    import picamera.array
    import numpy
    

    import os
    import os.path
    from fractions import Fraction
    from mover import RT,FRT,FFRT,BACK
    from rand import RandScramble
except ImportError as err:
    Die(err)






class Webcam:
	
    def __init__(self):
       #self.cam              = cv2.VideoCapture(0)
        self.stickers         = self.get_sticker_coordinates('main')
        self.current_stickers = self.get_sticker_coordinates('current')
        self.preview_stickers = self.get_sticker_coordinates('preview')
        self.sca=0

		
    def get_sticker_coordinates(self, name):
        """
        Every array has 2 values: x and y.
        Grouped per 3 since on the cam will be
        3 rows of 3 stickers.

        :param name: the requested color type
        :returns: list
        """
        stickers = {
            'main': [
                [80, 20], [250, 20], [460, 20],
                [100,230], [250, 190], [470, 230],
                [110, 370], [250, 385], [450, 370]
            ],
            'current': [
                [20, 20], [54, 20], [88, 20],
                [20, 54], [54, 54], [88, 54],
                [20, 88], [54, 88], [88, 88]
            ],
            'preview': [
                [20, 130], [54, 130], [88, 130],
                [20, 164], [54, 164], [88, 164],
                [20, 198], [54, 198], [88, 198]
            ]
        }
        return stickers[name]


    def draw_main_stickers(self, frame):
        """Draws the 9 stickers in the frame."""
        for x,y in self.stickers:
            cv2.rectangle(frame, (x,y), (x+64, y+64), (255,255,255), 2)

    def draw_current_stickers(self, frame, state):
        """Draws the 9 current stickers in the frame."""
        for index,(x,y) in enumerate(self.current_stickers):
            cv2.rectangle(frame, (x,y), (x+32, y+32), ColorDetector.name_to_rgb(state[index]), -1)

    def draw_preview_stickers(self, frame, state):
        """Draws the 9 preview stickers in the frame."""
        for index,(x,y) in enumerate(self.preview_stickers):
            cv2.rectangle(frame, (x,y), (x+32, y+32), ColorDetector.name_to_rgb(state[index]), -1)

    def color_to_notation(self, color):
        """
        Return the notation from a specific color.
        We want a user to have green in front, white on top,
        which is the usual.

        :param color: the requested color
        """
        notation = {
            'green'  : 'F',
            'white'  : 'U',
            'blue'   : 'B',
            'red'    : 'R',
            'orange' : 'L',
            'yellow' : 'D'
        }
        return notation[color]
    def draw_circle(self,event,x,y,flags,param):
        print(x,y)
       
        if event == cv2.EVENT_LBUTTONDBLCLK:
			if x>300 and x<500:
				if y<240:
					if y<126:
						print('clicked' )
						
						self.sca=1
					else:
						RandScramble()	
						
    def scan(self):
        """
        Open up the webcam and scans the 9 regions in the center
        and show a preview in the left upper corner.

        After hitting the space bar to confirm, the block below the
        current stickers shows the current state that you have.
        This is show every user can see what the computer toke as input.

        :returns: dictionary
        """

        sides   = {}
        preview = ['white','white','white',
                   'white','white','white',
                   'white','white','white']
        state   = [0,0,0,
                   0,0,0,
                   0,0,0]
        
        with picamera.PiCamera() as camera:
			camera.resolution = (640,480)
			  
				
				 
		
			#camera.framerate=Fraction(1, 6)
			camera.exposure_mode = 'off'    # 137/128 8 
			camera.awb_mode = 'off'
			camera.awb_gains=(Fraction(85, 64), Fraction(49, 32))

			#camera.meter_mode= 'spotlit' 
			#camera.shutter_speed = 6000000000
			#camera.digital_gain = 800
			#camera.framerate_delta = 6/1

			#camera.iso = 800
			#camera.exposure_speed=camera.shutter_speed
			#camera.exposure_speed=camera.shutter_speed
			
			
			
			#camera.awb_gains =89 /64
			cv2.namedWindow('default')
			cv2.setMouseCallback('default',self.draw_circle)
			
			while True:
				#_, frame = self.cam.read()
            
				with picamera.array.PiRGBArray(camera) as stream:
					camera.capture(stream, format='bgr')
					frame = stream.array

					#frame = cv2.resize(frame,(640,480),interpolation=cv2.INTER_AREA)
					
				
				hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
				key = cv2.waitKey(10) & 0xff

            # init certain stickers.
				self.draw_main_stickers(frame)
				self.draw_preview_stickers(frame, preview)

				for index,(x,y) in enumerate(self.stickers):
					roi          = frame[y:y+64, x:x+64]
					
					avg_hsv      = ColorDetector.average_hsv(roi)
				
					color_name   = ColorDetector.get_color_name(avg_hsv)
					
					print(index+1)
					print(avg_hsv)
					#color_histogram_feature_extraction.color_histogram_of_test_image(roi)
		
					#color_name = knn_classifier.main('training.data', 'test.data')
					state[index] = color_name
					
					#cv2.imwrite(str(index+1)+'.jpg',roi)

                # update when space bar is pressed.
                #print(key)
                
				cv2.putText(frame,'Solve',(350,77), cv2.FONT_HERSHEY_SIMPLEX, 1,(255,255,255),2)
				
				cv2.putText(frame,'Scramble',(350,176), cv2.FONT_HERSHEY_SIMPLEX, 1,(255,255,255),2)
				
				if key == 32:					
					self.sca=True
					print(key)
				if key == 10:
					RandScramble()	
						#cv2.imwrite(state[4]+'.jpg',frame)
				if self.sca:
					preview = list(state)
					self.draw_preview_stickers(frame, state)
					face = self.color_to_notation(state[4])
					notation = [self.color_to_notation(color) for color in state]
					sides[face] = notation
					
				#move robot
					if len(sides)<4:
						RT()
					elif len(sides)==4:
						FRT()
					elif len(sides)==5:
						FFRT()	
					#elif len(sides)==6:
						#BACK()	
				# show the new stickers	
				self.draw_current_stickers(frame, state)

            # append amount of scanned sides
				text = 'scanned sides: {}/6'.format(len(sides))
				cv2.putText(frame, text, (20, 460), cv2.FONT_HERSHEY_TRIPLEX, 0.5, (255,255,255), 1)

            # quit on escape.
				if len(sides)==6:
					break

            # show result
				cv2.imshow("default", frame)

			#self.cam.release()
			cv2.destroyAllWindows()
			return sides if len(sides) == 6 else False

webcam = Webcam()
