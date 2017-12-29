import cv2
import numpy as np

import sqlite3


db = sqlite3.connect('image.db')
cur = db.cursor()
all_image = cur.execute('select image_url from image_info')

amr = cv2.imread('/anaconda/projects/opencv/amr.jpg')
for x in all_image.fetchall():
	d =  x[0].split('\n')[0]
	line = cv2.imread(d)


	try:
		sub = cv2.subtract(amr,line)
	except Exception as e :
		print "YEs"
		
		black = np.ones((600,600,3),np.uint8)*255
		cv2.putText(black , "I FInd It " , (75,290) , cv2.FONT_HERSHEY_COMPLEX , 2 , (100,170,0) , 3)
		cv2.imshow("THat WHat YU NeEd" , black)
		cv2.waitKey(0)
		cv2.destroyAllWindows()
		break
	is_true = not np.any(sub)#Fasle if sub is zeros


	if is_true is True:
	    cv2.imshow('amr',amr)
	    cv2.waitKey(0)
	    cv2.imshow('line',line)
	    cv2.waitKey(0)
	    cv2.destroyAllWindows()
	    break
else:
    black = np.zeros((600,600,3),np.uint8)
    cv2.putText(black , "Not The same " , (75,290) , cv2.FONT_HERSHEY_COMPLEX , 2 , (100,170,0) , 3)
    cv2.imshow("Not  The Same" , black)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
