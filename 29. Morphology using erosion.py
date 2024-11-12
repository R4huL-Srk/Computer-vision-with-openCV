import cv2
import numpy as np

# Load the grayscale or binary image
image = cv2.imread('data1.jpg', cv2.IMREAD_GRAYSCALE)

# Thresholding to create a binary image (optional, if input is not already binary)
_, binary_image = cv2.threshold(image, 127, 255, cv2.THRESH_BINARY)

# Define the structuring element (kernel)
kernel = np.ones((5, 5), np.uint8)  # 5x5 square kernel

# Apply the erosion operation
eroded_image = cv2.erode(binary_image, kernel, iterations=1)  # 1 iteration

cv2.imshow("Binary image",binary_image)
cv2.imshow("Eroded image",eroded_image)

cv2.waitKey(0)
cv2.destroyAllWindows()
