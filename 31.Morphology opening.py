import cv2
import numpy as np

image = cv2.imread('data1.jpg', 0)

_, binary_image = cv2.threshold(image, 127, 255, cv2.THRESH_BINARY)

kernel = np.ones((5, 5), np.uint8)

opening = cv2.morphologyEx(binary_image, cv2.MORPH_OPEN, kernel)

cv2.imshow("Original Image", image)
cv2.imshow("Opening Technique Image", opening)

cv2.waitKey(0)
cv2.destroyAllWindows()
