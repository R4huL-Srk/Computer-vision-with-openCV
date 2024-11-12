import cv2
import numpy as np

image = cv2.imread('data1.jpg', 0)

kernel = np.ones((15, 15), np.uint8)

black_hat = cv2.morphologyEx(image, cv2.MORPH_BLACKHAT, kernel)

cv2.imshow("Black Top Hat",black_hat)

cv2.waitKey(0)
cv2.destroyAllWindows()
