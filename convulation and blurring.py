# -*- coding: utf-8 -*-
"""
Created on Fri Dec 29 22:41:11 2017

@author: pentester
"""


## convolutions and Blurring
#convolutions is about make some thing in tow function and produce third function
# we use kernel to specifiy the size of over whichwe run our maniuplating  function over our image 
# we will use cv2.filter2D(image , -1  , kernel)  

import cv2
import numpy as np




image = cv2.imread('/anaconda/projects/opencv/amr.jpg')
cv2.imshow('amr ', image)
cv2.waitKey(0)


#create our 3*3 kernel

kernel_3x3 = np.ones((3,3) , np.float32)/9



#we use cv2.filter2D to convolove the kernel with image 
blurred = cv2.filter2D(image , -1 , kernel_3x3)
cv2.imshow('blurring' , blurred)
cv2.waitKey(0)







kernel_7x7 = np.ones((7,7) , np.float32)/49



#we use cv2.filter2D to convolove the kernel with image 
blurred2 = cv2.filter2D(image , -1 , kernel_7x7)
cv2.imshow('blurring2' , blurred2)
cv2.waitKey(0)


cv2.destroyAllWindows()






