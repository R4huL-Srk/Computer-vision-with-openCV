import cv2
import numpy as np

img = cv2.imread("data1.jpg")
image = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
if image is None:
    print("Error loading image.")
    exit()

sobel_y = cv2.Sobel(image, cv2.CV_64F, dx=0, dy=1, ksize=3)
sobel_y = cv2.convertScaleAbs(sobel_y) 
cv2.imshow("Original image ", img)

cv2.imshow("Sobel Y Edge Detection", sobel_y)

cv2.waitKey(0)
cv2.destroyAllWindows()
