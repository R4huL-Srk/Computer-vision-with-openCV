import cv2
import numpy as np
from matplotlib import pyplot as plt

# Load the original image
image = cv2.imread('data1.jpg', cv2.IMREAD_GRAYSCALE)

# Apply Gaussian blur to create a blurred version of the image
blurred_image = cv2.GaussianBlur(image, (9, 9), sigmaX=2)

# Create the mask by subtracting the blurred image from the original image
mask = cv2.subtract(image, blurred_image)

# Sharpen the image by adding the mask to the original image
sharpened_image = cv2.addWeighted(image, 1.5, mask, -0.5, 0)

cv2.imshow("Original Image", image)
cv2.imshow("Sharpened image",sharpened_image)

cv2.waitKey(0)
cv2.destroyAllWindows()
