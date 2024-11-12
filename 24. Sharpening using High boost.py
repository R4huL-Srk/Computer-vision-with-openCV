import cv2
import numpy as np
from matplotlib import pyplot as plt

# Load the original image
image = cv2.imread('data1.jpg', cv2.IMREAD_GRAYSCALE)

# Define the boost factor
k = 1.5  # You can adjust this value to control the sharpness level

# Apply Gaussian blur to create a blurred version of the image
blurred_image = cv2.GaussianBlur(image, (9, 9), sigmaX=2)

# Create the high-pass mask by subtracting the blurred image from the original image
mask = cv2.subtract(image, blurred_image)

# Apply the high-boost formula: Original image + k * (mask)
high_boost_image = cv2.addWeighted(image, 1, mask, k, 0)

cv2.imshow("Original Image",image)
cv2.imshow("Sharpened image",high_boost_image)

cv2.waitKey(0)
cv2.destroyAllWindows()
