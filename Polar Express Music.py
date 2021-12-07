from threading import Thread
import pygame as pg 
import time 

PolarExpress_List1 = ['c4','g4','b3','g4',\
				'c4','e4','b3','g3',\
				]
PolarExpress_List2 = ['c4','c4','g4','g4','b3','b3','g4',\
				'c4','d4','e4','g3','b3','b3','g3',\
				]

pg.mixer.init()
pg.init()

pg.mixer.set_num_channels(len(PolarExpress_List2))

def play_notes(notePath,duration):
	time.sleep(duration) 
	pg.mixer.Sound(notePath).play()
	time.sleep(duration)
	print(notePath)

path  = 'Sounds/'

cnt =1

th = {}

for t in PolarExpress_List1:
	th[t] = Thread(target = play_notes,args = (path+'{}.ogg'.format(t),0.4))
	th[t].start()
	th[t].join()
	if cnt%4 == 0:
		print("---Long Pause---")
		time.sleep(0.5) # Let the sound play for the last note of each line
		
	cnt += 1

cnt2 =1

for t in PolarExpress_List2:
	th[t] = Thread(target = play_notes,args = (path+'{}.ogg'.format(t),0.2))
	th[t].start()
	th[t].join()
	if cnt2%7 == 0:
		print("---Long Pause---")
		time.sleep(1.5) # Let the sound play for the last note of each line
		
	cnt2 += 1
