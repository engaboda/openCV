
# coding: utf-8

# In[10]:


import cv2
import numpy as np
from matplotlib import pyplot as plt


image = cv2.imread('./amr.jpg')



#علشان تعمل calchist دي داله بتاخد مجموعه من المتغيرات وهي )([list of images] , channel [0] for grayscale , mask None for make histogram to take full image , histsize , [256] , range for color [0,256])
#[0] to show blue only
histogram = cv2.calcHist([image] , [0] ,  None , [256] , [0,256])




#دي طريقه تانيه علشان تعرض histogram, image.ravel() دي بتحويل الصوره لا array  , 256 دا حجم ال hist , [0,256]دا كل احتمالات الالوان 
# ravel() convert 2 dianmentianal array to 1 --> image.ravel()
plt.hist(image.ravel() , 256  , [0,256]);plt.show()



color = ('b' ,'g', 'r')




# هنا بنعمل فصل لكل لون ونعرضه لوحده 
for i , col in enumerate(color):
    histogram2 = cv2.calcHist([image] , [i] ,None , [256] , [0,256] )
    plt.plot(histogram2 , color=col)
    plt.xlim([0,256])

    
plt.show()


# In[11]:


import cv2
import numpy as np


image = np.zeros((512,512,3) , np.uint8)


gray_image = np.zeros((512,512 ) , np.uint8)


cv2.imshow('image  from numpy' , image)
cv2.imshow('image numpy gray' ,  gray_image)
cv2.waitKey(0)
cv2.destroyAllWindows()


# In[6]:


#cv2.line(image , start cordinates , end cordinates , color , thickness)


import cv2
import numpy as np


#image = np.zeros((512,512,3) , np.uint8)
image = cv2.imread('./amr.jpg')


#علشان ترسم خط نستخدم cv2.line()
#first argyment is the image that u will drow line inside it , and second coordinate for first spot , end coordinate  , colors   , thickness ل




cv2.line(image , (0,0) , (612,612) , (255,120,0) , 5)
cv2.line(image ,(612,0) , (0,612) , (255,120,0)  , 5)
cv2.line(image ,(306,0) , (306,612) , (255,120,0)  , 5)
cv2.line(image ,(0,306) , (612,306) , (255,120,0)  , 5)

cv2.imwrite('line.jpg' , image)
cv2.imshow('image with line ' , image)
cv2.waitKey(0)
cv2.destroyAllWindows()


# In[1]:


#cv2.rectangel(image , starting vertex , opposite vertex , color ,  thickness)
import cv2
import numpy as np
image = np.zeros((512,512,3) , np.uint8)


#-1 علشان تخالي اللون يملي التجويف الداخلي
cv2.rectangle(image , (100,100), (300,250) , (255,120,0) , -1)
cv2.imshow('image with rectangle ' , image)
cv2.waitKey(0)
cv2.destroyAllWindows()



# In[1]:


#cv2.circle(image , center , radius , color , fill)

import cv2 
import numpy as np


image =  cv2.imread('./amr.jpg')

cv2.circle(image , (350, 350) , 100 , (15,75,50) , -1 )

cv2.imshow('circle ' , image)

cv2.waitKey(0)
cv2.destroyAllWindows()






# In[2]:


import cv2 
import numpy as np

image = cv2.imread('./amr.jpg')


pts = np.array([[10,50],[400,50],[90,200],[50,500]], np.int32)

pts = pts.reshape((1,-1,2))


cv2.polylines(image , [pts] , True , (0,0,255 )  , 3)
cv2.imshow('polylines  ' , image)
cv2.waitKey(0)
cv2.destroyAllWindows()




# In[2]:


#cv2.putText(image , "textto display " , bottom left start point , font , font size ,   color , thickness)

import cv2 
import numpy as np

image = cv2.imread('./amr.jpg')

image2 = np.zeros((512,512,3) , np.uint8)
#np.zeros((hieght , width,3))
image3 = np.zeros((512,512,3) , np.uint8)

cv2.putText(image2 , "hello world " , (75,290) , cv2.FONT_HERSHEY_COMPLEX , 2 , (100,170,0) , 3)

cv2.imshow("text inside image " , image3)
cv2.waitKey(0)
cv2.destroyAllWindows()



