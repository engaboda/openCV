
# coding: utf-8

# In[ ]:


import cv2

# علشان تعمل تحميل لصوره في متغير اسمه imahe 
image = cv2.imread('./amr.jpg')

#علشان تعمل عرض لصوره بعنوان
cv2.imshow('hello' , image)

#غلشان تخالي البرنامج يستني لحد ما تدخل متغير 
ch  = cv2.waitKey()
if ch==27:
    #علشان تخالي البرنامج يقفل كل الشاشات
    cv2.destroyAllWindows()
print "bye!!"


# In[ ]:







import cv2 

image = cv2.imread('./amr.jpg')


print image.shape
print "height in pixles" , image.shape[0] , "___" , "width in pixles"  , image.shape[1] , "___" , "depth in color GBR"  , image.shape[2]


# In[ ]:


import cv2 

image = cv2.imread('./amr.jpg' , 0 )

cv2.imshow('hello gray' , image)
ch = cv2.waitKey()
print image.shape
if ch==27:
    cv2.destroyAllWindows()
    
    


# In[ ]:


import cv2

image = cv2.imread('./amr.jpg')

B ,G , R = image[10][0]
print B , G , R



gray_image = cv2.cvtColor(image , cv2.COLOR_BGR2GRAY)
print gray_image.shape
print gray_image[0][0]


