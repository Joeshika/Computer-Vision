#24 Bit to 1 Bit
import cv2
input = cv2.imread('C:/Users/student/Downloads/image.jfif')
#Get input size
height, width = input.shape[:2]
c, d = (2, 2)
temp2 = cv2.resize(input, (c, d), cv2.INTER_LINEAR) 
output2 = cv2.resize(temp2, (width, height), cv2.INTER_NEAREST) 
cv2.imshow("1bit.jpg",output2)
cv2.imshow("24bit.jpg",input)
