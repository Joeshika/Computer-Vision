#24 Bit to 8 Bit
import cv2
#Input image
input = cv2.imread('C:/Users/student/Downloads/image.jfif')
#Get input size
height, width = input.shape[:2]
w, h = (256, 256)
temp = cv2.resize(input, (w, h), cv2.INTER_LINEAR) 
output = cv2.resize(temp, (width, height), cv2.INTER_NEAREST) 
cv2.imshow("8bit.jpg",output)
cv2.imshow("24bit.jpg",input)
