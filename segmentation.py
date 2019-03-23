import cv2
import numpy as np
import matplotlib.pyplot as plt

image=cv2.imread('E:\hello.jpg',0)
plt.imshow(image,cmap='gray')
plt.show()

gray=cv2.adaptiveThreshold(image,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,\
            cv2.THRESH_BINARY,11,15)
#plt.imshow(gray)
#plt.show()
#ret,thresh=cv2.threshold(gray,125,255,cv2.THRESH_BINARY_INV)
#im_gray = cv2.GaussianBlur(gray, (5, 5), 0)


ret, thresh = cv2.threshold(gray, 90, 255, cv2.THRESH_BINARY_INV)
plt.imshow(thresh,cmap='gray')
plt.show()

kernel=np.ones((5,10),np.uint8)
img_dilation=cv2.dilate(thresh,kernel,iterations=1)
#plt.imshow(img_dilation)
#plt.show()

im2,ctrs,hier=cv2.findContours(img_dilation.copy(),cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
sorted_ctrs = sorted(ctrs, key=lambda ctr: cv2.boundingRect(ctr)[1])
print(len(ctrs))
for i, ctr in enumerate(sorted_ctrs):
    x, y, w, h = cv2.boundingRect(ctr)
    roi = image[y:y+h, x:x+w]
    cv2.imshow('segment no:'+str(i),roi)
    cv2.waitKey(0)
    #cv2.rectangle(image,(x,y),( x + w, y + h ),(90,0,255),2)
    #cv2.waitKey(0)
    cv2.destroyAllWindows()
    print("functions")
cv2.imshow('marked areas',image)
cv2.waitKey(0)
cv2.destroyAllWindows()
print ("Number of Contours %d ->",len(ctrs))
