#Sharpening is opposite of blurring
#strength the edge in images

#           |-1 -1 -1 |
#   kernel =|-1  9 -1 |
#           |-1 -1 -1 |
#
import cv2
import numpy as np

image = cv2.imread('/anaconda/projects/opencv/amr.jpg')
    
kernel_sharpening = np.array([
                                [-1,-1,-1],
                                [-1,9,-1],
                                [-1,-1,-1]
                                ]) 
sherpened = cv2.filter2D(image , -1 , kernel_sharpening)

cv2.imshow('sharpened' , sherpened)
cv2.waitKey(0)
cv2.destroyAllWindows()
