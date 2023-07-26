#24 Bit to 4 Bit
import cv2
#Input image
input = cv2.imread('C:/Users/student/Downloads/image.jfif')
#Get input size
height, width = input.shape[:2]
a, b = (16, 16)
temp1 = cv2.resize(input, (a, b), cv2.INTER_LINEAR) 
output1 = cv2.resize(temp1, (width, height), cv2.INTER_NEAREST) 
cv2.imshow("4bit.jpg",output1)
cv2.imshow("24bit.jpg",input)
