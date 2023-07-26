import cv2
 image = cv2.imread("C:/Users/student/Downloads/rgb.jfif")
image = cv2.imread("C:/Users/student/Downloads/birds.jfif")
 # converting BGR to RGB
image_rgbb= cv2.cvtColor(image, cv2.COLOR_RGB 2 BGR)
 image_rgbg = cv2.cvtColor(image, cv2.COLOR_RGB 2 GRAY)
image_rgbh = cv2.cvtColor(image, cv2.COLOR_RGB 2 HSV)
image_rgby = cv2.cvtColor(image, cv2.COLOR_RGB 2 YUV)
cv2.imshow('image', image_rgbb)
cv2.imshow('image', image_rgbg)
cv2.imshow('image', image_rgbh)
cv2.imshow('image', image_rgbr)
cv2.waitKey(0)
cv2.destroyAllWindows()
