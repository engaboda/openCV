### other commenly used blurring methods in OPENCV
#low pass filter LPF and high pass filter HPF
#LPF help us to remove noise from image like blurring
# and HPF help us to find edges in image


#Image Blurring (Image Smoothing)



import cv2
import numpy as np



image = cv2.imread('/anaconda/projects/opencv/amr.jpg')
cv2.imshow('amr ', image)
cv2.waitKey(0)



#this take the bixels under the box and replace the centeral element
#box size need to add adn positive



blur = cv2.blur(image , (3,3))
cv2.imshow('blur' , blur)
cv2.waitKey(0)




#instead box filter using gaussian kernel


Gaussion  = cv2.GaussianBlur(image,(7,7) , 0)
cv2.imshow('gaussion' , Gaussion)
cv2.waitKey(0)



bilatera  = cv2.bilateralFilter(image , 9 ,75 , 75)
cv2.imshow('bilatera' , bilatera)
cv2.waitKey(0)






#fastNlMeansDenoising
#fastNlMeansDenoisingColored
#fastNlMeansDenoisingMulti
#fastNlMeansDenoisingColoredMulti
##image de noise  Non-Local Mean Denoiseing

non_local   = cv2.fastNlMeansDenoisingColored(image , None , 6 ,6 , 7 , 21)
cv2.imshow('non_local' , non_local)
cv2.waitKey(0)







median  = cv2.medianBlur(image,5)
cv2.imshow('median' , median)
cv2.waitKey(0)





