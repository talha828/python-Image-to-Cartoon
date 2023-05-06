import cv2           
import numpy as np

# load image
image = cv2.imread("talha.jpg")

# convert to grey image
grey = cv2.cvtColor(image ,cv2.COLOR_BGR2GRAY)

# blur effect
grey = cv2.medianBlur(grey, 5)

# performs adaptive thresholding on an input image (grey image to binary image)
edge = cv2.adaptiveThreshold(grey,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,9,9)

# performs a bilateral filter on an input image
color = cv2.bilateralFilter(image,9,250,250)

# performs the bitwise AND operation on two input images
cartoon = cv2.bitwise_and(color,color,mask=edge)

# compare reesults
cv2.imshow("Image",image)
cv2.imshow("Edge",edge)
cv2.imshow("Cartoon",cartoon)
cv2.waitKey(0)
cv2.destoryAllWindows()