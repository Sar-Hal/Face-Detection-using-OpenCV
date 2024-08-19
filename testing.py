import cv2

#Reading color image as grayscale
gray = cv2.imread("image.png",0)

#Showing grayscale image
cv2.imshow("Grayscale image",gray)

cv2.waitKey(0)  #time is in milliseconds 1000 = 1 second , 0 = infinite
cv2.destroyAllWindows()