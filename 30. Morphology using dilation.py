import cv2
import numpy as np
import matplotlib.pyplot as plt

# Load the image in grayscale
image = cv2.imread("data1.jpg", 0)

# Apply a binary threshold to get a binary image
_, binary_image = cv2.threshold(image, 127, 255, cv2.THRESH_BINARY)

# Define the kernel for dilation (you can adjust the kernel size for different effects)
kernel = np.ones((5, 5), np.uint8)  # 5x5 kernel of 1s

# Apply the dilation operation
dilated_image = cv2.dilate(binary_image, kernel, iterations=1)

cv2.imshow("Original Image",image)
cv2.imshow("Binary Image",binary_image)
cv2.imshow("Dilated image",dilated_image)

cv2.waitKey(0)
cv2.destroyAllWindows()
