import cv2
import numpy as np

img = cv2.imread("data1.jpg")
image = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
if image is None:
    print("Error loading image.")
    exit()

sobel_x = cv2.Sobel(image, cv2.CV_64F, dx=1, dy=0, ksize=3)
sobel_x = cv2.convertScaleAbs(sobel_x)
cv2.imshow("Original image ", img)

cv2.imshow("Sobel X Edge Detection", sobel_x)

cv2.waitKey(0)
cv2.destroyAllWindows()
