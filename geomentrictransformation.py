import numpy as np
import cv2 as cv
#getting input image 
Img = cv.imread('joker.jpg',1)
#for portrait
#img = cv.resize(im,(480,720))

#tilt the image into slanting
def tilt(img):
    rows,cols,ch = img.shape[:3]
    pts1 = np.float32([[50,50],[200,50],[50,200]])
    pts2 = np.float32([[10,100],[200,50],[100,200]])
    M = cv.getAffineTransform(pts1,pts2)
    res = cv.warpAffine(img,M,(cols,rows))
    return res
#it magnify the image and get the image focused
def zoom(img):
    rows,cols,ch = img.shape[:3]
    pts1 = np.float32([[46,65],[300,65],[46,300],[300,300]])
    pts2 = np.float32([[10,10],[350,10],[10,350],[350,350]])
    M = cv.getPerspectiveTransform(pts1,pts2)
    res = cv.warpPerspective(img,M,(cols,rows))
    return res
cv.imshow('Tilted Image',tilt(img))
cv.waitKey()
cv.imshow('Focused Image',zoom(img))
cv.waitKey()
cv.destroyAllWindows()
